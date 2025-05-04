import hashlib

class ProofOfWork:
    
    def proof_of_work_sha256(self, previous_proof):
        #it is nonce, we need to find this value to show proof of work to mine new block
        new_proof = 1
        check_proof = False
        while check_proof is False:
            # sha256 operation of asymmetrical value between previous and new proof cannot be easily guessed
            # (symmetric like: a+b is same as b+a and asymmetric means a-b is not equals to b-a)
            hash_operation = self.hash_operation(new_proof, previous_proof)
            if self.check_proof(hash_operation):
                check_proof = True
            else:
                new_proof += 1
        return new_proof

    def hash_operation(self, new_proof, previous_proof):
        return hashlib.sha256(str(new_proof**2 - previous_proof**2).encode()).hexdigest()

    def check_proof(self, hash_operation):
        if hash_operation[:4] == '0000':
            return True
        else:
            return False