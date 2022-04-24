import hashlib
import json
from textwrap import dedent
from time import time
from uuid import uuid4

from flask import Flask, jsonify, request

class Blockchain():
    def __init__(self):
        # blockchain consists of a list of blocks
        self.chain = []

        # each block stores a list of transactions
        self.current_transactions = []

        # create the genesis block
        self.new_block(previous_hash=1, proof=100)
    
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

        # when a new block is created, it should have no transactions in it
        self.current_transactions = []

        # add the new block created to the chain
        self.chain.append(block)
        return block

    def new_transaction(self, sender, recipient, amount):
        """
        Creates a new transaction to go into the next mined block

        sender parameter is the address of the sender
        recipient parameter is the address of the receiver
        amount paramter

        function returns the index of the block to which the transaction was added
        """

        transaction = {
            'sender': sender,
            'recipient': recipient,
            'amount': amount
        }

        # add the new transaction to the block which will be mined
        self.current_transactions.append(transaction)

        return self.last_block['index'] + 1

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
    
    def new_transaction(self, sender, recipient, amount):
        self.current_transactions.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount
        })

        return self.last_block['index'] + 1

    def new_block(self, proof, previous_hash):
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transactions': self.current_transactions,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1])
        }

        self.current_transactions = []
        self.chain.append(block)
        return block

    def proof_of_work(self, last_proof):
        proof = 0
        while self.valid_proof(last_proof, proof) is False:
            proof += 1

        return proof

    @staticmethod
    def valid_proof(last_proof, proof):
        guess = f'{last_proof}{proof}'.encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:4] == "0000"

# Instantiate Node
app = Flask(__name__)

# Generate a globally unique address for this node
node_identifier = str(uuid4()).replace('-', '')

# Instantiate blockchain
blockchain = Blockchain()

@app.route('/mine', methods=['GET'])
def mine():
    # run the proof of work algorithm to get the next proof
    last_block = blockchain.last_block
    last_proof = last_block['proof']
    proof = blockchain.proof_of_work(last_proof)

    # We must receive a reward for finding the proof.
    # The sender is "0" to signify that this node has mined a new coin.
    blockchain.new_transaction(
        sender="0",
        recipient=node_identifier,
        amount=1,
    )

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
    required = ['sender', 'recipient', 'amount']
    if not all(k in values for k in required):
        return 'Missing values', 400

    # Create a new transaction
    index = blockchain.new_transaction(values['sender'], values['recipient'], values['amount'])

    response = {'message': f'Transaction will be added to Block {index}'}
    return jsonify(response), 201

@app.route('/chain', methods=['GET'])
def full_chain():
    response = {
        'chain': blockchain.chain,
        'length': len(blockchain.chain)
    }
    return jsonify(response), 200

if __name__ == '__main__':
    app.run(host='localhost', port=5000)
