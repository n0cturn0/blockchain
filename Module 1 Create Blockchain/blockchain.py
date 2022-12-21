import datetime
import hashlib
import json
from flask import Flask, jsonify

#Parte 1, criar um blockchain

class Blockchain:
    def __init__(self): #Inicializa a classe
    self.chain = []
    self.create_block(proof = 1, previous_hash='0')
    