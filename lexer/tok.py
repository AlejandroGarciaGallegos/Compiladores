class Tok:
    def __init__(self, tokenType: str, literal: str):
        self.tokenType:str = tokenType
        self.literal:str = literal

    def __str__(self):
        return self.tokenType + " : " + self.literal

class TokenType:
    ILLEGAL = "ILLEGAL"
    EOF = "EOF"
    IDENT = "IDENT"
    INT = "INT"
    ASSIGN = "="
    PLUS = "+"
    COMMA = ","
    SEMICOLON = ";"
    LPAREN = "("
    RPAREN = ")"
    LBRACE = "{"
    RBRACE = "}"
    FUNCTION = "FUNCTION"
    VAR = "VAR"

keywords = {
    "fn": TokenType.FUNCTION,
    "var": TokenType.VAR
}

def isKeyword(identifier):
    if keywords.get(identifier):
        return keywords[identifier]
    return TokenType.IDENT
