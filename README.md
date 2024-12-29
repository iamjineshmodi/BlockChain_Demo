# Python Blockchain Project

## Overview
This project is a Python-based implementation of a simple blockchain system. It allows users to create and manage a blockchain with the following features:

- Customizable mining difficulty
- Adjustable block mining time
- Genesis block creation
- Transaction management
- Proof-of-work mining algorithm
- Blockchain validation

## Features
- **Genesis Block:** The blockchain starts with a genesis block.
- **Mining:** Blocks are mined using a proof-of-work algorithm that adjusts difficulty dynamically.
- **Transaction Handling:** Users can add blocks containing multiple transactions.
- **Blockchain Validation:** Ensures the integrity of the blockchain by validating hashes and links between blocks.
- **Dynamic Difficulty Adjustment:** Automatically adjusts the mining difficulty based on the time taken to mine previous blocks.

## Usage

1. Run the Python script:
   ```bash
   python3 Blockchain_basics.py
   ```
2. Choose from the menu options:
   - **1:** Add a new block (input transactions).
   - **2:** Print the blockchain to view its current state.
   - **3:** Validate the blockchain to ensure integrity.
   - **4:** Exit the application.

## Code Structure

### Block Class
- Represents an individual block in the blockchain.
- Attributes:
  - `index`: Position of the block in the chain.
  - `transactions`: List of transactions in the block.
  - `previous_hash`: Hash of the previous block.
  - `nonce`: Counter used for mining.
  - `current_hash`: SHA-256 hash of the block.
- Methods:
  - `calculate_hash()`: Computes the block's hash.
  - `mine_block(difficulty)`: Mines the block by finding a hash starting with a certain number of zeros.

### Blockchain Class
- Manages the chain of blocks.
- Attributes:
  - `chain`: List of blocks in the blockchain.
  - `difficulty`: Current mining difficulty.
  - `target_block_time`: Target time to mine a block (in seconds).
- Methods:
  - `create_genesis_block()`: Initializes the blockchain with the first block.
  - `get_latest_block()`: Retrieves the most recent block.
  - `adjust_difficulty()`: Adjusts difficulty based on block mining time.
  - `add_block(transactions)`: Mines and adds a new block to the chain.
  - `print_chain()`: Displays the blockchain.
  - `is_chain_valid()`: Validates the entire blockchain.

## Example

1. Add a new block:
   - Input the number of transactions.
   - Enter each transaction.
   - The block is mined and added to the blockchain.

2. Print the blockchain:
   ```plaintext
   Block 0 [Time: 2024-12-29 00:00:00]
   Transactions: ['Genesis Block']
   Previous Hash: 0
   Hash: 00a3...xyz
   Nonce: 348

   Block 1 [Time: 2024-12-29 00:01:00]
   Transactions: ['Transaction 1', 'Transaction 2']
   Previous Hash: 00a3...xyz
   Hash: 00b4...abc
   Nonce: 472
   ```

3. Validate the blockchain:
   ```plaintext
   Blockchain is valid.
   ```

## Customization
- **Initial Difficulty:** Adjust the `initial_difficulty` parameter to change the mining difficulty.
- **Target Block Time:** Modify `target_block_time` to set the desired time for mining blocks.

## Dependencies
This project uses only Python's standard library:
- `hashlib`
- `time`

## License
This project is licensed under the MIT License.