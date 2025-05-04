import datetime
import hashlib
import json
from python.src.main.app.services.proof_of_work import ProofOfWork

proof_of_work = ProofOfWork()

class Blockchain:

    def __init__(self):
        #array of blocks
        self.chain = []
        #Start with Genisis Block with initial proof as 1 and previous Hash as 0 
        self.create_block(proof = 1, previous_hash = '0')

    #we should call it after block is mined. It will create and append block to blockchain
    def create_block(self, proof, previous_hash):
        block = {'index': len(self.chain) + 1,
                 'timestamp': str(datetime.datetime.now()),
                 'proof': proof,
                 'previous_hash': previous_hash}
        self.chain.append(block)
        return block

    def get_previous_block(self):
        return self.chain[-1]

    #it will start from genesis block (means from 1st block).
    #it will check if:
    # 1. for the current block's Previous hash key is same as Previous block hash
    # 2. and hash is starting with 4 leading zeros
    def is_chain_valid(self, chain):
        previous_block = chain[0]
        block_index = 1
        while block_index < len(chain):
            block = chain[block_index]
            if block['previous_hash'] != self.hash(previous_block):
                return False
            previous_proof = previous_block['proof']
            proof = block['proof']
            hash_operation = proof_of_work.hash_operation(proof, previous_proof)
            if proof_of_work.check_proof(hash_operation) is False:
                return False
            previous_block = block
            block_index += 1
        return True
    
    def hash(self, block):
        encoded_block = json.dumps(block, sort_keys = True).encode()
        return hashlib.sha256(encoded_block).hexdigest()