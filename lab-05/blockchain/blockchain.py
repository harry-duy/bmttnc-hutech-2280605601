from block import Block
import hashlib

class Blockchain:
    def __init__(self):
        """Khởi tạo blockchain với genesis block"""
        self.chain = []
        self.current_transactions = []
        
        # Tạo genesis block
        genesis_block = Block(0, [], 1, "0")
        self.chain.append(genesis_block)
    
    def create_block(self, proof):
        """
        Tạo block mới
        :param proof: Proof of work
        :return: Block mới
        """
        block = Block(
            index=len(self.chain),
            transactions=self.current_transactions,
            proof=proof,
            previous_hash=self.chain[-1].hash
        )
        
        self.current_transactions = []
        self.chain.append(block)
        return block
    
    def add_transaction(self, sender, recipient, amount):
        """
        Thêm giao dịch mới
        :param sender: Người gửi
        :param recipient: Người nhận
        :param amount: Số tiền
        """
        self.current_transactions.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount
        })
    
    def proof_of_work(self, last_proof):
        """
        Thuật toán Proof of Work
        Tìm số p sao cho hash(p*last_p) có 4 số 0 đầu tiên
        :param last_proof: Proof trước đó
        :return: Proof mới
        """
        proof = 0
        while not self.valid_proof(last_proof, proof):
            proof += 1
        return proof
    
    def valid_proof(self, last_proof, proof):
        """
        Kiểm tra proof có hợp lệ không
        :param last_proof: Proof trước đó
        :param proof: Proof hiện tại
        :return: True nếu đúng, False nếu sai
        """
        guess = f'{last_proof}{proof}'.encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:4] == "0000"
    
    def is_chain_valid(self):
        """
        Kiểm tra tính hợp lệ của blockchain
        :return: True nếu hợp lệ, False nếu không
        """
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i-1]
            
            # Kiểm tra hash
            if current_block.previous_hash != previous_block.hash:
                return False
            
            # Kiểm tra proof of work
            if not self.valid_proof(previous_block.proof, current_block.proof):
                return False
        
        return True
    
    def get_last_block(self):
        """Lấy block cuối cùng"""
        return self.chain[-1]