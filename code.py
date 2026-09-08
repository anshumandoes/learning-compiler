from lex import *
import enum

# def main():
    # source = "MAKABHOSDA AAAG"
    # Lexer = lexer(source)

    # while Lexer.peek() != '\0':
    #     print (Lexer.curChar)
    #     Lexer.nextChar()
def main():
    source = "123"
    lexer = Lexer(source)

    token = lexer.getToken()
    while token.kind != TokenType.EOF:
        print(token.kind)
        token = lexer.getToken()
        

main() 