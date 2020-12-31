from Aardvark import *


@Aardvark.Type("string")
class String(DType):#DType is the base
    def __init__(self, string):
        self.string=string
    def check(self, what):
      lex(what, ["'", '"', *what])
    def __repr__(self):
      return self.string