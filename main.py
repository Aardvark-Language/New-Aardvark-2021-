import sys
from termcolor import colored
import strings
from Aardvark import *

def fix(f="main.py"):
	a = open(f).read()
	open(f, "w").write(a.replace("	", "\t"))


fix("main.py")
fix("Aardvark.py")
fix("language/lexer.py")
fix("language/__init__.py")


def error(line, line_num, problem, t, specific, collunm=0):
	thing = line.split(problem)
	sys.stderr.write(f"Error on line {line_num}:\n" + thing[0] +
					 colored(problem, "white", "on_magenta", attrs=["bold"]) +
					 "\033[0;0m")
	sys.stderr.write(thing[1] + f"\n{t}: {specific}")


#error("output(asd)", 1, "asd", 'TypeError', "asd is not defined")
