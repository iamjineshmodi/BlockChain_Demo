import hashlib
import time

# Block structure
class Block:
    def __init__(self, index, transactions, previous_hash):
        self.index = index
        self.timestamp = time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime())
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.nonce = 0
        self.current_hash = self.calculate_hash()

    # Calculate the hash of the block
    def calculate_hash(self):
        block_string = str(self.index) + self.timestamp + str(self.transactions) + self.previous_hash + str(self.nonce)
        return hashlib.sha256(block_string.encode()).hexdigest()

    # Mine block using a simple proof-of-work algorithm (start with '00')
    def mine_block(self, difficulty):
        target = '0' * difficulty  # Target with '0's based on difficulty
        while self.current_hash[:difficulty] != target:
            self.nonce += 1
            self.current_hash = self.calculate_hash()
        print(f"Block mined: {self.current_hash}")

# Blockchain class
class Blockchain:
    def __init__(self, initial_difficulty, target_block_time=1):
        self.chain = [self.create_genesis_block()]
        self.difficulty = initial_difficulty
        self.target_block_time = target_block_time  # Target time in seconds
        self.time_taken_for_last_block = None  # To store time taken for the previous block

    # Create the genesis block
    def create_genesis_block(self):
        return Block(0, ["Genesis Block"], "0")

    # Get the latest block in the chain
    def get_latest_block(self):
        return self.chain[-1]

    # Adjust difficulty based on mining time
    def adjust_difficulty(self):
        if self.time_taken_for_last_block is None:
            return  # No need to adjust difficulty for the first block
        if self.time_taken_for_last_block < self.target_block_time:
            self.difficulty += 1
            print(f"Block mined too fast, increasing difficulty to {self.difficulty}")
        elif self.time_taken_for_last_block > self.target_block_time:
            self.difficulty = max(1, self.difficulty - 1)  # Difficulty should not go below 1
            print(f"Block mined too slow, decreasing difficulty to {self.difficulty}")

    # Add a new block to the chain
    def add_block(self, transactions):
        start_time = time.time()  # Track the start time
        new_block = Block(len(self.chain), transactions, self.get_latest_block().current_hash)
        new_block.mine_block(self.difficulty)
        self.chain.append(new_block)
        self.time_taken_for_last_block = time.time() - start_time  # Calculate time taken to mine the block
        print(f"Time taken to mine block: {self.time_taken_for_last_block} seconds")
        self.adjust_difficulty()  # Adjust difficulty based on time taken

    # Print the blockchain
    def print_chain(self):
        for block in self.chain:
            print(f"Block {block.index} [Time: {block.timestamp}]")
            print(f"Transactions: {block.transactions}")
            print(f"Previous Hash: {block.previous_hash}")
            print(f"Hash: {block.current_hash}")
            print(f"Nonce: {block.nonce}\n")

    # Validate the blockchain
    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            # Check if current block's hash is correct
            if current_block.current_hash != current_block.calculate_hash():
                return False

            # Check if previous hash is correct
            if current_block.previous_hash != previous_block.current_hash:
                return False

        return True

# User interaction
if __name__ == "__main__":
    initial_difficulty = 2  # Start with difficulty level 2 (requires hash to start with '00')
    target_block_time = 0.01 # Target time for each block in seconds
    blockchain = Blockchain(initial_difficulty, target_block_time)

    while True:
        print("\n1. Add new block")
        print("2. Print Blockchain")
        print("3. Validate Blockchain")
        print("4. Exit")
        choice = int(input("Choose an option: "))

        if choice == 1:
            num_txns = int(input("Enter number of transactions: "))
            transactions = []
            for i in range(num_txns):
                txn = input(f"Enter transaction {i + 1}: ")
                transactions.append(txn)
            blockchain.add_block(transactions)

        elif choice == 2:
            blockchain.print_chain()

        elif choice == 3:
            if blockchain.is_chain_valid():
                print("Blockchain is valid.")
            else:
                print("Blockchain is invalid.")

        elif choice == 4:
            break

        else:
            print("Invalid choice, please try again.")
