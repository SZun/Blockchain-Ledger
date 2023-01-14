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

    # Instance varibales
    sender: str
    receiver: str
    amount: str

# Block Class
@dataclass
class Block:

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
        instance_variables = [self.record,self.creator_id,self.timestamp,self.prev_hash, self.nonce]

        # Loop over instance variables
        for i in instance_variables:
            # Update SHA256 hash with encoded instance variable
            sha.update(str(i).encode())

        # Return SHA256 Hexdigiset
        return sha.hexdigest()

# Pychain class
@dataclass
class PyChain:
    # Instance Vairbales
    chain: List[Block]
    difficulty: int = 4

    def proof_of_work(self, block):

        calculated_hash = block.hash_block()

        num_of_zeros = "0" * self.difficulty

        while not calculated_hash.startswith(num_of_zeros):

            block.nonce += 1

            calculated_hash = block.hash_block()

        print("Wining Hash", calculated_hash)
        return block

    def add_block(self, candidate_block):
        block = self.proof_of_work(candidate_block)
        self.chain += [block]

    def is_valid(self):
        block_hash = self.chain[0].hash_block()

        for block in self.chain[1:]:
            if block_hash != block.prev_hash:
                print("Blockchain is invalid!")
                return False

            block_hash = block.hash_block()

        print("Blockchain is Valid")
        return True

# Adds the cache decorator for Streamlit
@st.cache(allow_output_mutation=True)
def setup():
    print("Initializing Chain")
    return PyChain([Block("Genesis", 0)])


st.markdown("# PyChain")
st.markdown("## Store a Transaction Record in the PyChain")

pychain = setup()

sender = st.text_input("Sender")
receiver = st.text_input("Receiver")
amount = st.text_input("Amount")

if st.button("Add Block"):
    prev_block = pychain.chain[-1]
    prev_block_hash = prev_block.hash_block()

    new_block = Block(
        record=Record(sender=sender,receiver=receiver,amount=amount),
        creator_id=42,
        prev_hash=prev_block_hash
    )

    pychain.add_block(new_block)
    st.balloons()

st.markdown("## The PyChain Ledger")

pychain_df = pd.DataFrame(pychain.chain).astype(str)
st.write(pychain_df)

difficulty = st.sidebar.slider("Block Difficulty", 1, 5, 2)
pychain.difficulty = difficulty

st.sidebar.write("# Block Inspector")
selected_block = st.sidebar.selectbox(
    "Which block would you like to see?", pychain.chain
)

st.sidebar.write(selected_block)

if st.button("Validate Chain"):
    st.write(pychain.is_valid())