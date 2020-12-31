from language import *
class Token:
	def __init__(self, ttype, value, col = 1, ln = 1):
		self.type = ttype
		self.value = value
		self.column = col
		self.line = ln 

	def setPosition(self, col, line):
		self.column = col
		self.line = line

class Lexer:
	def __init__(self, language):
		self.symbols = ["+", '//', '\\\\']
		self.keywords = ["return", "continue", "await"]
		self.other_keywords = []
		self.KEYWORDS = self.symbols + self.keywords + self.other_keywords
		self.language = language
		self.divider = " "

	def lex(self, string, symbols):#Unless you would like it differently than using language.gettype
		curchar = string[0]
		length = len(string)

		index = 0
		column = 1
		line = 1

		tokens = []

		SYMBOLS

		def advance(amt):
			global index
			global column
			index += amt
			column += amt

			if (index >= length):
				curchar = '\0'
				return curchar

			curchar = string[index]
			return curchar

		def isAlpha(c): # return true if the character is a-z / A-Z or false if it isnt
			return ('a' <= c and 'z' >= c) or ('A' <= c and 'Z' >= c)

		def isDigit(c):
			return '0' <= c and '9' >= c

		def isWhitespace(c):
			return (
				c == ' '  or
				c == '\r' or
				c == '\t'
			)

		def tokenizeQuote():
			global curchar#The thing is, the lexer needs to support non-builting strings and stuff, I am tryin g to make this language as flexible as possible, so flexible that bit can support no strings
			
			
			
		while curchar != '\0':
			lastIndex = index

			if isWhitespace(curchar):
				advance()

			if isQuote(curchar):
				tokenizeQuote()

			if curchar == '\n':
				tok = Token("Linebreak", '\n', column, line)
				line += 1
				column = 0
				advance()

			if lastIndex == index:
				pass# error here (unknown symbol / character)

	# def lex(self, string):
	# 	lexeme = ''
	# 	tokens = []
	# 	KEYWORDS = self.KEYWORDS
	# 	for i, char in enumerate(string):
	# 		if char != self.divider:
	# 			lexeme += char  # adding a char each time
	# 		if (i + 1 < len(string)):  # prevents error
	# 			if string[i + 1] == self.divider or string[
	# 			    i +
	# 			    1] in KEYWORDS or lexeme in KEYWORDS:  # if next char == ' '
	# 				if lexeme != '':
	# 					tokens.append(lexeme.replace('\n', '<newline>'))
	# 					lexeme = ''
	# 	tokens.append(lexeme)
	# 	return tokens


