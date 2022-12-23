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
    
    #Método para retornar o bloco anterior
    def get_previsous_block(self):
        return self.chain[-1]
    
    #Dificuldade da tarefa Quanto mais zero a esquerda mais difícil Gerando o hash
    def proof_of_work(self, previous_proof):
        new_proof =1
        check_proof =  False
        while check_proof is False:
            hash_operation = hashlib.sha256(str(new_proof**2 - previous_proof**2).encode()).hexdigest() #Gerando hash
            if hash_operation[:4] ==  '0000':
                check_proof = True
            else:
                new_proof += 1
                return new_proof
            
    def hash(self, block):
        encoded_block = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(encoded_block).hexdigest()
        
                
        
        
        