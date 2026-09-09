import sys 
from lex import *

class Parser:
    def __init__(self, lexer):
        self.lexer = lexer

        self.curToken = None
        self.peekToken = None
        self.nextToken()
        self.nextToken()

    def checkToken(self, kind):
        return kind == self.curToken.kind

    def checkPeek(self, kind):
        return kind == self.peekToken.kind

    def match(self , kind):
        if not self.checkToken(kind):
            self.abort("Expected " + kind.name + ", got " + self.curToken.kind.name)
        self.nextToken()

    def nextToken(self):
        self.curToken = self.peekToken
        self.peekToken = self.lexer.getToken()
    
    def abort(self, message):
        sys.exit("Error: " + message)

# valid statements look like: print "hello"

    def program(self):
        print('program')

        while not self.checkToken(TokenType.EOF):
            self.statement()

    def say(self):
        self.statement()

    def statement(self):
        if self.checkToken(TokenType.PRINT):
            self.nextToken()

            if self.checkToken(TokenType.STRING):
                self.nextToken()
            else:
                self.expression()
        self.nl()

    def expression(self):
        if self.checkToken(TokenType.NUMBER):
            self.nextToken()
        elif self.checkToken(TokenType.IDENT):
            self.nextToken()
        elif self.checkToken(TokenType.STRING):
            self.nextToken()
        else:
            self.abort("Expected expression, got " + self.curToken.kind.name)

    def nl(self):
        print('NEWLINE')
        self.match(TokenType.NEWLINE)
        while self.checkToken(TokenType.NEWLINE):
            self.nextToken()