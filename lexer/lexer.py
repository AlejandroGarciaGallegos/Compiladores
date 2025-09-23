from tok import Tok
from tok import TokenType
from tok import isKeyword

class Lexer:
    def __init__(self, input):
        self.input = input
        self.position = 0        # current position in input (points to current char)
        self.read_position = 0   # current reading position in input (after current char)
        self.ch = ''             # current char under examination
        self.readChar()

    def isEOF(self):
        return self.ch != ''

    def readChar(self):
        if self.read_position >= len(self.input):
            self.ch = ''
        else:
            self.ch = self.input[self.read_position]
        self.position = self.read_position
        self.read_position += 1

    def readToken(self):

        tk = {}
        self.skipWhitespace()

        match self.ch:
            case '=':
                tk = Tok(TokenType.ASSIGN , self.ch)
            case ';':
                tk = Tok(TokenType.SEMICOLON, self.ch)
            case '(':
                tk = Tok(TokenType.LPAREN, self.ch)
            case ')':
                tk = Tok(TokenType.RPAREN, self.ch)
            case ',':
                tk = Tok(TokenType.COMMA, self.ch)
            case '+':
                tk = Tok(TokenType.PLUS, self.ch)
            case '{':
                tk = Tok(TokenType.LBRACE, self.ch)
            case '}':
                tk = Tok(TokenType.RBRACE, self.ch)
            case 0:
                tk = Tok(TokenType.EOF, '')
            case _:
                if isIdentifierLetter(self.ch):
                    literal = self.readIdentifier()
                    type = isKeyword(literal)
                    tk = Tok(type, literal)
                    print(tk)
                    return tk
                elif isDigit(self.ch):
                    tk = Tok(TokenType.INT, self.readNumber())
                    print(tk)
                    return tk
                else:
                    tk = Tok(TokenType.ILLEGAL, self.ch)

        self.readChar()
        print(tk)
        return tk

    def readIdentifier(self):
        start = self.position
        while isIdentifierLetter(self.ch):
            self.readChar();

        return self.input[start:self.position]

    def readNumber(self):
        start = self.position
        while isDigit(self.ch):
            self.readChar();

        return self.input[start:self.position]

    def skipWhitespace(self):
        while self.ch == ' ' or self.ch == '\t' or self.ch == '\n' or self.ch == '\r':
            self.readChar()

def isIdentifierLetter(ch):
    return ('a' <= ch and ch <= 'z') or ('A' <= ch and ch <= 'Z') or ch == '_'

def isDigit(ch):
    return '0' <= ch and ch <= '9'
