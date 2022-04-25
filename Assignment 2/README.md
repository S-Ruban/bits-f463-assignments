<h1>Fake Product Identification System Using Blockchain Technology</h1>

<h2>Introduction to Blockchain</h2>

A blockchain is a digital and distributed ledger of transactions, recorded and replicated in real-time across a network of computers or nodes. Every transaction must be cryptographically validated via a consensus mechanism executed by the nodes before being permanently added as a new “block” at the end of the “chain.” There is no need for a central authority to approve the transaction, which is why blockchain is sometimes referred to as a peer-to-peer trustless mechanism.

Blockchain can be thought of as a linked list with each node containing multiple transactions. Each transaction has a hash that depends on the previous transactions hash as well. So we can see that the order of transactions is important. If we were to change one transaction somewhere, it would have a ripple effect and change the hash of all subsequent transactions. This is one of the reasons why blockchain is a powerful medium for storing transactions.

The placing of a transaction in a block is called a successful conclusion to a proof of work challenge, and is carried out by special nodes called miners. Proof of Work is a system that requires some work from the service requester, usually meaning processing time by a computer. Producing a proof of work is a random process with low probability, so normally a lot of trial and error is required for a valid proof of work to be generated. When it comes to Bitcoins, hash is what serves as a proof of work. Miners on a Blockchain are nodes that produce blocks by solving proof of work problems. If a miner produces a block that is approved by an electronic consensus of nodes then the miner is rewarded with coins. This essentially is the crux of blockchain. Proof of Work is what is keeping all transactions on the blockchain secure and protecting it from malicious attempts to alter these transactions.

<h2>Problem Statement</h2>

Every popular brand has fake manufacturers selling a counterfeit item with misleading and invalid labels, which are sold at cheaper rates. Even the company experts may not be able to distinguish between counterfeit and original items.

Suppose we come across a counterfeit item - we need to be able to identify that it is indeed fake through its QR code.

<h2>Our Solution to the Problem</h2>

We can add users and nodes into the network at any time. There is a single blockchain that stores the transactions. Each blockchain has several blocks and each transaction has several transactions. Each transaction consists of the following details:

<ul>
<li> Date and time
<li> Sender/Seller name and ID
<li> Recipient name and ID
<li> Product name and ID
<li> Price
</ul>

In case the seller enters a wrong product code (i.e., a counterfeit item), the transaction is verified using the [Zero Knowledge Proof](#zkp) by verifying whether the item is original or not. If the transaction is found to be invalid, the seller is added to the list of suspicious users and the transaction is not added to the blockchain.

<h2 id="zkp">Zero-Knowledge Proof</h2>

In cryptography, a zero-knowledge proof or zero-knowledge protocol is a method by which one party (the prover) can prove to another party (the verifier) that a given statement is true while the prover avoids conveying any additional information apart from the fact that the statement is indeed true. The essence of zero-knowledge proofs is that it is trivial to prove that one possesses knowledge of certain information by simply revealing it; the challenge is to prove such possession without revealing the information itself or any additional information.

If proving a statement requires that the prover possess some secret information, then the verifier will not be able to prove the statement to anyone else without possessing the secret information. The statement being proved must include the assertion that the prover has such knowledge, but without including or transmitting the knowledge itself in the assertion. Otherwise, the statement would not be proved in zero-knowledge because it provides the verifier with additional information about the statement by the end of the protocol. A zero-knowledge proof of knowledge is a special case when the statement consists only of the fact that the prover possesses the secret information.

<h3>Zero-Knowledge Proof Algorithm</h3>

Alice has sensitive data $x$ for which she chooses two numbers $p$ and $g$. $p$ can be a large prime and $g$ is a generator for $p$. She calculates $y$ as $y = g^x \mod p$. Now she performs the following steps to create a zero knowledge proof for $x$.

1. Alice chooses a random number $r < p-1$ and sends it to Bob as $h = g^r \mod p$
2. Bob receives $h$ and sends back a random bit $b$ ($0/1$).
3. Alice sends $s = (r+bx) \mod (p-1)$ to Bob.
4. Bob computes $g^s \mod p$ which should equal $hy^b \mod p$

Here Bob acts as a verifier and checks if Alice knows the value of $x$ without actually getting to know what $x$ is.

<h3>Implementation of Zero-Knowledge Proof</h3>

We have used Python's default `pow()` for modular exponentiation, and the `random` library to generate the random bit.

<br><br><br><br><br><br><br><br><br>

<h2>Flowchart depicting the control flow of the Blockchain</h2>

<img align="center" src="Fake Product Identification System Flowchart.jpeg">

<br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>

<h2>UML Diagram of classes used</h2>

<img align="center" src="UML Diagram for Fake Product Identification System.jpeg">

<h2>Screenshots of the working Application</h2>

<h3>Add Node (User) to the Blockchain</h3>

<img align="center" src="Add Node (User).png">

<br><br><br>

<h3>Add a Product to a Blockchain</h3>

<img align="center" src="Add Product.png">

<h3>Show all users of the Blockchain</h3>

<img align="center" src="Get All Nodes (Users).png">

<br><br><br><br><br><br><br><br><br><br><br><br><br>

<h3>Show all products in the Blockchain</h3>

<img align="center" src="Get All Products.png">

<h3>Create a Transaction</h3>

<img align="center" src="Create Transaction.png">

<br><br><br><br><br><br><br><br><br><br><br><br><br>

<h3>Mine a block</h3>

<img align="center" src="Mine Block.png">
<br><br><br>
<img align="center" src="Mine Block (output).png">

<br><br><br><br><br><br><br><br><br><br><br><br>

<h3>Show Blockchain</h3>

<img align="center" src="Get Blockchain.png">
<br>
<img align="center" src="Get Blockchain (output).png">

<br><br><br><br><br><br><br><br><br><br><br><br><br><br>

<h3>Incorrect Product Code</h3>

<img align="center" src="Incorrect Product Code.png">

<h3>List of Suspicious Users</h3>

<img align="center" src="Suspicious Users.png">

<script type="text/javascript" src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML"></script>

<script type="text/x-mathjax-config">MathJax.Hub.Config({ tex2jax: {inlineMath: [['$', '$']]}, messageStyle: "none" });</script>
