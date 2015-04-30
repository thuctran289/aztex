"""
	@authors: idgetto, jovanduy, thuctran289

	Main aztex program. Run this program to get the LaTeX 
	output of given aztex code. Creates a .tex file with the
	same name as the input file (if input is text rather than 
	a file, creates a file named newfile.tex) with the analogous
	LaTeX code.

	To run:
		with a certain file filename: python AztexRunner.py filename.txt
		with a file input.txt: python AztexRunner.py
		with "just a few words": python AztexRunner.py just a few words
"""

import sys
from Element import Element
from LatexOutput import *
from Tokenizer import Tokenizer
from Parser import Parser

def run_test(text):
	""" Function to run AztexRunner on some given text input 
		text: string of input text that should be aztex code
		returns: the analogous LaTeX output to text
	"""
	tokenizer = Tokenizer(text)
	parser = Parser()

	elements = []
	block = tokenizer.get_next_block()
	while block:
		element = parser.parseBlock(block)
		elements.append(element)
		block = tokenizer.get_next_block()

	A = LatexOutput()
	return ''.join(A.to_doc(elements))

if __name__ == "__main__":
	if len(sys.argv) > 1:
		args = sys.argv[1:]
		if '.txt' in args[0]:
			filename = args
			w = open(filename[:-4:] + ".tex", 'w')
			f = open(filename, 'r')
			text = f.read()
		else:
			w = open('newfile.tex', 'w')
			text = ' '.join(args)
	else:
		filename = "/Users/Jordan/Documents/SoftDes/azTex/input.txt"
		w = open(filename[:-4:] + ".tex", 'w')
		f = open(filename, 'r')
		text = f.read()

	print "===== ORIGINAL FILE =====\n"
	print text
	print "=========================\n\n"

	from Tokenizer import Tokenizer
	from Parser import Parser

	tokenizer = Tokenizer(text)
	parser = Parser()

	elements = []
	block = tokenizer.get_next_block()
	while block:
	    element = parser.parseBlock(block)
	    elements.append(element)
	    block = tokenizer.get_next_block()


	print "===== DOCUMENT ELEMENTS ====="
	A = LatexOutput()

	#for element in elements:
	#	print element
	#	print ""

	for element in  A.to_doc(elements):
		w.write(str(element))

	print "==============================\n\n"


	print "==============="
	print "=== SUCCESS ==="
	print "==============="