import argparse
from lexer import Lexer
from tok import TokenType

def run(src: str):
    lex = Lexer(src)
    print("Tokens:")
    while True:
        tk = lex.readToken()
        if tk.tokenType == TokenType.EOF:
            break
        print(f'\t{tk}')
    lex.printTotal()

if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("-s", dest="s", help="string a escanear")
    p.add_argument("-f", dest="f", help="ruta del archivo a escanear")
    args = p.parse_args()

    if args.s:
        source = args.s
    elif args.f:
        with open(args.f, "r", encoding="utf-8") as fh:
            source = fh.read()
    else:
        source = 'print x = 10;'

    run(source)
