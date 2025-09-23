class Tok:
    def __init__(self, tokenType: str, literal: str):
        self.tokenType:str = tokenType
        self.literal:str = literal

    def __str__(self):
        return self.tokenType + ": " + self.literal

class TokenType:
    KEYWORD = "KEYWORD"
    PUNCTUATION = "PUNCTUATION"
    IDENTIFIER = "IDENTIFIER"
    OPERATOR = "OPERATOR"
    CONSTANT = "CONSTANT"

    EOF = "EOF"
    INVALID = "INVALID"

keywords = [
    "fn",
    "var"
]

def isKeyword(identifier):
    if identifier in keywords:
        return TokenType.KEYWORD
    return TokenType.IDENTIFIER
