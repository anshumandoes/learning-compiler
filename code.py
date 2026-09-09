from lex import *
from parse import * 
import sys 
import enum

def main ():
    print("mupiler")

    if len(sys.argv) < 2:
        sys.exit("error: compiler needs source file as arguments ")
    with open(sys.argv[1], 'r') as inputFile:
        source = inputFile.read()
    
    lexer = Lexer(source)
    parser = Parser(lexer)

    parser.program()
    print("parsing completed")


main()