# Imports
import streamlit as st
from dataclasses import dataclass
from typing import Any, List
import datetime as datetime
import pandas as pd
import hashlib

# Record class
@dataclass
class Record:

    """
        Class to hold Block record
    """

    # Instance varibales
    sender: str
    receiver: str
    amount: str

# Block Class
@dataclass
class Block:

    """
        Class for single Block within Blockchain ledger
    """

    # Instance Variables
    record: Record
    creator_id: int
    prev_hash: str = "0"
    timestamp: str = datetime.datetime.utcnow().strftime("%H:%M:%S")
    nonce: int = 0

    # Method to get block hash
    def hash_block(self):
        # SHA256 hash
        sha = hashlib.sha256()

        # Array of instance variables    
        instance_variables = [self.record,self.creator_id,self.timestamp,self.prev_hash,self.nonce]

        # Loop over instance variables
        for i in instance_variables:
            # Update SHA256 hash with encoded instance variable
            sha.update(str(i).encode())

        # Return SHA256 Hexdigiset
        return sha.hexdigest()

# Pychain class
@dataclass
class PyChain:

    """
        Class for blockchain/ledger chain
    """

    # Instance Vairbales
    chain: List[Block]
    difficulty: int = 4

    # Method for proof of work
    def proof_of_work(self, block):
        # Store the block's hash
        calculated_hash = block.hash_block()

        # Loop while hash doesn't start with amount of difficulty zeros
        while not calculated_hash.startswith("0" * self.difficulty):
            # Increment Nonce
            block.nonce += 1
            # Update block's hash
            calculated_hash = block.hash_block()
        
        # Print the wining hash
        print(f"Wining Hash {calculated_hash}")

        # Return the block
        return block

    def add_block(self, candidate_block):
        self.chain += [self.proof_of_work(candidate_block)]

    def is_valid(self):
        # Store hash
        block_hash = self.chain[0].hash_block()

        # Loop over chain of blocks
        for block in self.chain[1:]:
            # If current hash doesn't equal previous hash
            if block_hash != block.prev_hash:
                # Print invalid blockchain message
                print("Blockchain is invalid!")
                # Return false
                return False

            # Set hash to new hash
            block_hash = block.hash_block()

        # Print valid blockchain message
        print("Blockchain is Valid")
        
        # Return true
        return True

# Adds the cache decorator for Streamlit
@st.cache(allow_output_mutation=True)

# Method to setup chain
def setup():
    # Print initalization message
    print("Initializing Chain")
    # Return Genesis Block PyChain class instance
    return PyChain([Block("Genesis", 0)])

# Adding header markdown
st.markdown("# PyChain")
st.markdown("## Store a Transaction Record in the PyChain")

# Setting up chain
pychain = setup()

# Variables to store text input
sender,receiver,amount = [st.text_input(i) for i in ["Sender","Receiver","Amount"]]

# If the button is selected
if st.button("Add Block"):
    # Adding new block to chain
    pychain.add_block(
        Block(
            record=Record(sender=sender,receiver=receiver,amount=amount),
            creator_id=42,
            prev_hash=pychain.chain[-1].hash_block()
        )
    )
    st.balloons()

# Adding header mardown for ledger
st.markdown("## The PyChain Ledger")

# Adding DataFrame to ledger
st.write(pd.DataFrame(pychain.chain).astype(str))

# Chain difficulty slider
pychain.difficulty = st.sidebar.slider("Block Difficulty", 1, 5, 2)

# Inspector header
st.sidebar.write("# Block Inspector")
# Dropdown for block selector
st.sidebar.write(st.sidebar.selectbox("Which block would you like to see?", pychain.chain))

# If the button is selected
if st.button("Validate Chain"):
    # Show True or False for validation value 
    st.write(pychain.is_valid())