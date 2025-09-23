from lexer import Lexer

s = "var abc = 12"

lex = Lexer(s)

while lex.isEOF():
    lex.readToken()
