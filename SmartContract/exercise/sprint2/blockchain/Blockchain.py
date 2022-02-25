import hashlib
import json
from time import time

class Blockchain(object):

    def __init__(self):
        self.chain = []
        self.current_transaction = []
        self.chain =[]

    def new_block(self, proof, previous_hash = None):
        # creates a new Block and adds its to the chain
        """
            Creates a new block in the block chain
            :param proof: <int> The proof given by the Proof of work algorithm
            :param previous_hash:(optional) <str> Hash of the previous Block
            :return <dict> New Block
        """
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transactions': self.current_transaction,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1])
        }
        
        self.current_transaction = []
        self.chain.append(block)
        return block
        

    def new_transaction(self, sender, recipient, amount):
        """
        create a new transaction to go into the next mined Block
        : param sender: <str> Address to the sender
        : param recepient: <str> Address to the receipient
        : param amount:<int> Amount
        : return: <int> The Index of the Block that will hold this transaction
        """
        
        self.current_transaction.append({
            'sender': sender, 
            'receipient': recipient,
            'amount': amount
        })
        
        return self.last_block['index'] + 1

    @staticmethod
    def hash(block):
        # hashes a block 
        pass
    
    @property
    def last_block(self):
        # returns the last block in the chain
        pass
    
