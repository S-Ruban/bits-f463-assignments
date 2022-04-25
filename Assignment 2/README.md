<h1>Fake Product Identification System Using Blockchain Technology</h1>

<h2>Introduction to Blockchain</h2>

A blockchain is a digital and distributed ledger of transactions, recorded and replicated in real-time across a network of computers or nodes. Every transaction must be cryptographically validated via a consensus mechanism executed by the nodes before being permanently added as a new “block” at the end of the “chain.” There is no need for a central authority to approve the transaction, which is why blockchain is sometimes referred to as a peer-to-peer trustless mechanism.

Blockchain can be thought of as a linked list with each node containing multiple transactions. Each transaction has a hash that depends on the previous transactions hash as well. So we can see that the order of transactions is important. If we were to change one transaction somewhere, it would have a ripple effect and change the hash of all subsequent transactions. This is one of the reasons why blockchain is a powerful medium for storing transactions.

The placing of a transaction in a block is called a successful conclusion to a proof of work challenge, and is carried out by special nodes called miners. Proof of Work is a system that requires some work from the service requester, usually meaning processing time by a computer. Producing a proof of work is a random process with low probability, so normally a lot of trial and error is required for a valid proof of work to be generated. When it comes to Bitcoins, hash is what serves as a proof of work. Miners on a Blockchain are nodes that produce blocks by solving proof of work problems. If a miner produces a block that is approved by an electronic consensus of nodes then the miner is rewarded with coins. This essentially is the crux of blockchain. Proof of Work is what is keeping all transactions on the blockchain secure and protecting it from malicious attempts to alter these transactions.

<h2>Problem Statement</h2>

Every popular brand has fake manufacturers selling a counterfeit item with misleading and invalid labels, which are sold at cheaper rates. Even the company experts may not be able to distinguish between counterfeit and original items.

Suppose we come across a counterfeit item - we need to be able to identify that it is indeed fake through its QR code.

<h2>Our Solution to the Problem</h2>

- Each product has a blockchain and each block in the blockchain will have a set of transactions that are associated with the product.
- Each block will consist of -
  - an unique index (to differentiate between transactions)
  - timestamp (when the block was created)
  - verification code
  - proof
  - set of transactions

Suppose a person wants to buy a specific product. They must:

- Verify the QR code of the product with the blockchain to verify the product's validity,
- Insert the transaction data into a block while checking against it with the proof/nonce,
- Wait for the block to be verified across all the decentralized database so it can be inserted into the blockchain.
- Additionally, the blockchain must be resilient to attacks and modifications to the product list by unknown sources.
