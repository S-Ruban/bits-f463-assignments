import hashlib
import json
from os import stat
import string
import random
from urllib import response
import qrcode

from datetime import datetime
from time import time
from uuid import uuid4
from flask import Flask, jsonify, request

product_ids = set()
product_codes = {}
users = {}
transactions = {}
suspicious_users = {}

g = 5274534567267895415184019624415280449825390351329186092
p = 907109773182311179103178812521309427516175444259645304222389

def generate_product_id():
    while True:
        product_id = random.randint(0, 1000000000000000)
        if product_id not in product_ids:
            product_ids.add(product_id)
            return product_id

def generate_product_code(product_id, product_name):
    while True:
        product_code = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(32))
        if product_code not in product_codes:
            product_codes[product_code] = (product_id, product_name)
            return product_code

def generate_user_id(name):
    user_id = str(uuid4()).replace('-', '')
    users[user_id] = name
    transactions[user_id] = []
    return user_id

class Product():
    def __init__(self, product_name):
        self.product_id = generate_product_id()
        self.product_code = generate_product_code(self.product_id, product_name)
        self.product_name = product_name
        self.qrcode = qrcode.make(self.product_code)

class Blockchain():
    def __init__(self):
        # blockchain consists of a list of blocks
        self.chain = []

        # each block stores a list of transactions
        self.current_transactions = []

        # create the genesis block
        self.new_block(previous_hash=1, proof=100)

    @staticmethod
    def zero_knowledge_proof(x):
        y = pow(g, x, p)
        r = random.randint(0, p - 2)
        h = pow(g, r, p)
        b = random.randint(0, 1)
        s = (r + b * x) % (p - 1)
        return (pow(g, s, p) == h * pow(y, b, p) % p)

    def verify_transaction(self, transaction):
        product_id = transaction['product']['product_code']
        product_code = product_codes[product_id][0]
        for _ in range(500):
            if self.zero_knowledge_proof(product_code) == False:
                print("Invalid Transaction")
                user_id = transaction['sender']['sender_id']
                user_name = users[user_id]
                suspicious_users[user_id] = user_name
                return -1

        self.current_transactions.append(transaction)
    
    def new_block(self, proof, previous_hash=None):
        """
        Creates a new block in the blockchain

        proof parameter is the proof obtained by the Proof of Work algorithm
        previous_hash parameter is the hash of the previous block in the chain

        function returns the new block created
        """

        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transactions': self.current_transactions,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1])
        }

        # add the new block created to the chain
        self.chain.append(block)

        # once the mined block is inserted onto the blockchain,
        # transactions need to be cleared for the next block that will be mined
        self.current_transactions = []

        return block

    def new_transaction(self, sender_id, recipient_id, product_code, price):
        """
        Creates a new transaction to go into the next mined block

        sender parameter is the address of the sender
        recipient parameter is the address of the receiver

        function returns the index of the block to which the transaction was added
        """

        if sender_id not in users or recipient_id not in users:
            print("Invalid sender or/and receipient")
            return -1

        transaction = {}
        if product_code in product_codes:
            transaction = {
                'sender': {
                    'sender_id': sender_id,
                    'sender_name': users[sender_id]
                },
                'recipient': {
                    'recipient_id': recipient_id,
                    'recipient_name': users[recipient_id]
                },
                'time': datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
                # 'product_name': product_codes[product_code][1],
                'product': {
                    'product_code': product_code,
                    'product_name': product_codes[product_code][1]
                },
                'price': price
            }

            # add the new transaction to the block which will be mined
            if self.verify_transaction(transaction) == -1:
                return -1
            
            transactions[sender_id].append(transaction)
            transactions[recipient_id].append(transaction)

            # self.current_transactions.append(transaction)
            return self.last_block['index'] + 1
        else:
            suspicious_users[sender_id] = users[sender_id]

    @staticmethod
    def hash(block):
        # json.dumps gives us the json equivalent for a python dictionary
        # we also need to sort the keys in the dictionary, else we would get incorrect hashes
        # string.encode() encodes the string to utf-8 (converts the string into bytes, so that it can be passed to sha256)
        block_string = json.dumps(block, sort_keys=True).encode()

        # SHA stands for Secure Hash Algorithm
        # .sha256() is a constructor that is used to create a SHA256 hash
        # hexdigest converts the hashed data into hexadecimal format
        return hashlib.sha256(block_string).hexdigest()

    @property
    def last_block(self):
        return self.chain[-1]

    def proof_of_work(self, last_proof):
        proof = 0
        while self.valid_proof(last_proof, proof) is False:
            proof += 1

        return proof

    @staticmethod
    def valid_proof(last_proof, proof):
        guess = f'{last_proof}{proof}'.encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:4] == ("0"*4)

# Instantiate Node
app = Flask(__name__)

blockchain = Blockchain()

@app.route('/add_node', methods=['POST'])
def add_node():
    values = request.get_json()
    required = ['name']
    if not all (k in values for k in required):
        return 'Missing values', 400
    name = values['name']
    user_id = generate_user_id(name)
    
    response = {'message': f"Added a new node for {name}. Your node ID is {user_id}"}
    return jsonify(response), 201

@app.route('/add_product', methods=['POST'])
def add_product():
    values = request.get_json()
    required = ['product_name']
    if not all(k in values for k in required):
        return 'Missing values', 400
    else:
        product_name = values['product_name']
        product = Product(product_name)
        
        response = {'message': f"Added a new product {product_name}. The code for this product is {product.product_code}. Keep a note of this."}
        return jsonify(response), 201

@app.route('/mine', methods=['GET'])
def mine():
    # run the proof of work algorithm to get the next proof
    last_block = blockchain.last_block
    last_proof = last_block['proof']
    proof = blockchain.proof_of_work(last_proof)

    # Forge the new Block by adding it to the chain
    previous_hash = blockchain.hash(last_block)
    block = blockchain.new_block(proof, previous_hash)

    response = {
        'message': "New Block Forged",
        'index': block['index'],
        'transactions': block['transactions'],
        'proof': block['proof'],
        'previous_hash': block['previous_hash'],
    }
    return jsonify(response), 200

@app.route('/transactions/new', methods=['POST'])
def new_transaction():
    values = request.get_json()
    required = ['sender_id', 'recipient_id', 'product_code', 'price']
    if not all(k in values for k in required):
        return 'Missing values', 400

    # Create a new transaction
    index = blockchain.new_transaction(values['sender_id'], values['recipient_id'], values['product_code'], values['price'])
    if index == -1:
        response = {'error': f'Invalid details given'}
        return jsonify(response), 400

    response = {'message': f'Transaction will be added to Block {index}'}
    return jsonify(response), 201

@app.route('/get_transactions', methods=['POST'])
def get_transactions():
    values = request.get_json()
    required = ['user_id']
    if not all(k in values for k in required):
        return 'Missing values', 400

    transaction_list = transactions[values['user_id']]
    user_transaction_list = []
    for transaction in transaction_list:
        user_transaction_list.append(transaction)

    response = { "transactions": user_transaction_list}
    return jsonify(response), 201

@app.route('/chain', methods=['GET'])
def full_chain():
    response = {
        'chain': blockchain.chain,
        'length': len(blockchain.chain)
    }
    return jsonify(response), 200

@app.route('/users', methods=['GET'])
def get_all_users():
    users_list = []
    for user in users:
        user_info = {
            'ID': user,
            'Name': users[user]
        }
        users_list.append(user_info)
    
    response = {'users': users_list}
    return jsonify(response), 200

@app.route('/suspicious_users', methods=['GET'])
def get_suspicious_users():
    suspicious_users_list = []
    for suspicious_user in suspicious_users:
        suspicious_user_info = {
            'ID': suspicious_user,
            'Name': suspicious_users[suspicious_user]
        }
        suspicious_users_list.append(suspicious_user_info)
    
    response = {'suspicious_users': suspicious_users_list}
    return jsonify(response), 200

@app.route('/products', methods=['GET'])
def get_products():
    products_list = []
    for product in product_codes:
        product_info = {
            'product_code': product,
            'product_name': product_codes[product][1]
        }
        products_list.append(product_info)

    response = {'products': products_list}
    return jsonify(response), 200

if __name__ == '__main__':
    app.run(host='localhost', port=5000)
