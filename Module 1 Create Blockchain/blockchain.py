import datetime
import hashlib
import json
from flask import Flask, jsonify

#Parte 1, criar um blockchain

class Blockchain:
    def __init__(self): #Inicializa a classe
        self.chain=[]
        self.create_block(proof = 1, previous_hash='0')
    
    #criando dicionário do bloco
    def create_block(self, proof,previous_hash): #Método
        block ={'index': len(self.chain)+1,
                'timestamp':str(datetime.datetime.now()),
                'proof': proof,
                'previous_hash': previous_hash}
        #Incluindo o bloco a cadeia a blockchain
        self.chain.append(block) # append adiciona blck ao chain []
        return block