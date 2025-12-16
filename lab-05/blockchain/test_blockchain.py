from blockchain import Blockchain

def test_blockchain():
    # Tạo blockchain
    blockchain = Blockchain()
    
    print("=== BLOCKCHAIN DEMO ===\n")
    print(blockchain.get_last_block())
    
    # Thêm các giao dịch
    blockchain.add_transaction("Alice", "Bob", 10)
    blockchain.add_transaction("Bob", "Charlie", 5)
    blockchain.add_transaction("Charlie", "Alice", 3)
    
    # Mining: Tìm proof of work
    print("Đang mining block mới...")
    last_block = blockchain.get_last_block()
    proof = blockchain.proof_of_work(last_block.proof)
    
    # Thêm phần thưởng cho miner
    blockchain.add_transaction("Genesis", "Miner", 1)
    
    # Tạo block mới
    new_block = blockchain.create_block(proof)
    print(new_block)
    
    # Kiểm tra tính hợp lệ
    print(f"Is Blockchain Valid: {blockchain.is_chain_valid()}")

if __name__ == "__main__":
    test_blockchain()