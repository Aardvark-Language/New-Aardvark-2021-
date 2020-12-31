from language import *

DType = DType
import sys



import language.lexer#imports the lexer, not done yet

Aardvark = Language()#Initiates Aardvark as a language
a = Lexer(Aardvark)
print(a.lex("'hi'+'hi'"))
