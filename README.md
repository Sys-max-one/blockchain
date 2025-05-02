### 📦 Blockchain Implementation Overview

This project provides a simplified yet functional implementation of a basic **Blockchain system**, including mining support and a minimal set of RESTful APIs for interaction and validation. 
It is designed for educational purposes and offers insight into how blockchain technology operates at a foundational level.

#### 🚀 Key Features

* Creation and mining of new blocks
* Maintenance and retrieval of the full blockchain
* Validation of blockchain integrity

#### 🔗 Available API Endpoints

1. **`/mine_block`**
   Initiates the mining of a new block by solving the proof-of-work algorithm and appending the block to the chain. The response includes details of the newly mined block.

2. **`/get_chain`**
   Returns the full blockchain, including all blocks in the current chain along with their associated metadata (index, timestamp, proof, previous hash, etc.).

3. **`/is_valid`**
   Validates the integrity and consistency of the blockchain by checking the proof of work and hash references for each block.

#### 📚 Use Cases

* Learn how blockchain data structures and consensus algorithms work.
* Experiment with basic cryptographic hashing and proof-of-work.
* Extend or integrate with additional features such as peer-to-peer networking or smart contract simulations.
