import hashlib
import time
import json

class Block:
    def __init__(self, index, transactions, proof, previous_hash):
        """
        Khởi tạo một Block
        :param index: Vị trí của block trong chain
        :param transactions: Danh sách các giao dịch
        :param proof: Proof of work
        :param previous_hash: Hash của block trước đó
        """
        self.index = index
        self.timestamp = time.time()
        self.transactions = transactions
        self.proof = proof
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()
    
    def calculate_hash(self):
        """
        Tính hash của block một cách nhất quán.
        Sử dụng json.dumps để đảm bảo thứ tự của dictionary.
        """
        block_dict = {
            'index': self.index,
            'timestamp': self.timestamp,
            'transactions': self.transactions,
            'proof': self.proof,
            'previous_hash': self.previous_hash
        }
        block_string = json.dumps(block_dict, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()
    
    def __repr__(self):
        return f"""
Block #{self.index}
Index: {self.index}
Timestamp: {self.timestamp}
Transactions: {self.transactions}
Proof: {self.proof}
Previous Hash: {self.previous_hash}
Hash: {self.hash}
"""