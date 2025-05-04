from flask import jsonify, Flask
from python.src.main.app.services.blockchain import Blockchain
from python.src.main.app.services.proof_of_work import ProofOfWork

# Creating a Blockchain
blockchain = Blockchain()
proof_of_work = ProofOfWork()

def setup_mining_routes(app: Flask):
    @app.route('/mine_block', methods = ['GET'])
    def mine_block():
        previous_block = blockchain.get_previous_block()
        previous_proof = previous_block['proof']
        proof = proof_of_work.proof_of_work_sha256(previous_proof)
        previous_hash = blockchain.hash(previous_block)
        block = blockchain.create_block(proof, previous_hash)
        response = {'message': 'Congratulations, you just mined a block!',
                    'index': block['index'],
                    'timestamp': block['timestamp'],
                    'proof': block['proof'],
                    'previous_hash': block['previous_hash']}
        return jsonify(response), 200

    # Getting the full Blockchain
    @app.route('/get_chain', methods = ['GET'])
    def get_chain():
        response = {'chain': blockchain.chain,
                    'length': len(blockchain.chain)}
        return jsonify(response), 200

    # Checking if the Blockchain is valid
    @app.route('/is_valid', methods = ['GET'])
    def is_valid():
        is_valid = blockchain.is_chain_valid(blockchain.chain)
        if is_valid:
            response = {'message': 'The Blockchain is valid.'}
        else:
            response = {'message': 'The Blockchain is not valid.'}
        return jsonify(response), 200