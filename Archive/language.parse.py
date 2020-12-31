from language import *
import re
stuff = []
blocks = {}



def lex(text, toks, language):
		number=0
		l=[]
		s=text
		while True:
			number+=1
			s=text[:-1]
			test=self.gettype(s)
			if test!=None:
				s=text[len(text)-number:]
				l.append(test)
			if s in sep:
				l.append(s)
				s=text[len(text)-number:]
		return l
				
def parser(toks, tokens):
  pass
			


class Preparer:
	def __init__(self,
							 language,
							 comstart="/",
							 comend="\\",
							 line_sep=";",
							 endline_required=False):
		self.comstart = comstart
		self.language = language
		self.comend = comend
		self.line_sep = line_sep
		self.endline_required = endline_required

	def prep(self, text):
		s = ""
		newtext = ""
		incomment = False
		for i in text:
			s += i
			if i == self.comstart:
				incomment = True
			if incomment == True and i == self.comend:
				incomment = False
				i = ""
			if incomment == False:
				newtext += i
		return newtext


class Statement:
	def __init__(self, language: Language, name: str, eval, starter="#"):
		self.name = name
		self.eval = eval
		stuff.append(self)
		self.language = language

	def check(self, text):
		if text.startswith(self.starter + name + " "):
			args = self.language.separate(
					text[len(self.starter) + len(self.name) + 1:])
			self.eval(args)
			return args
		return False


class Block:
	def __init__(self, language: Language, string, eval, init=lambda x: ""):
		self.language = language
		stuff.append(self)
		self.init = init
		self.eval = eval
		self.regex = re.compile(string + "[ \t]*{")

	def check(self, text):
		m = self.regex.match(text)
		if m:
			self.init(m)
			blocks[self] = [m]
			return m
		return False


class Keyword:
	def __init__(self, language: Language, name: str, eval, argsep=","):
		self.language = language
		stuff.append(self)
		self.name = name
		self.eval = eval

	def check(self, text):
		if text.startswith(self.name + " "):
			args = self.language.separate(text[len(self.name) + 1:])
			self.eval(*args)
			return args
		return False


def parse(language, text, varis=""):
	linenum = 0
	global blocks
	if varis == "":
		varis = variables
	for line in text.split("\n"):
		for block in blocks:
			blocks[block].append(line)
		linenum += 1

		t = language.gettype(line)
		if t != None:
			continue
		for s in stuff:
			s = s.check(line)
			if s != False:
				continue

		if line == "}":
			b = blocks[-1]
			if len(blocks) == 0:
				b.eval(blocks[b])
			blocks = blocks[:-1]
