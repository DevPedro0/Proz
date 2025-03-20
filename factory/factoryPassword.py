from string import ascii_lowercase, ascii_uppercase, digits, punctuation
import random


class FactoryPassword():
    def __init__(self):
        self.lower = ascii_lowercase
        self.upper = ascii_uppercase
        self.digits = int(digits)
        self.chars_special = punctuation
        
    def create_pass(self) -> list:
        ...