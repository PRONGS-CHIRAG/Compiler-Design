#!/usr/bin/python
import yacc
import lexer
tokens = lexer.tokens
from subprocess import call
import sys
import ply.yacc as b


def p_file_input(p):
	"""file_input :	single_stmt ENDMARKER
	"""

def p_single_stmt(p):
	"""single_stmt	:	single_stmt NEWLINE
					|	single_stmt stmt
					|
	"""


def p_funcdef(p):
    "funcdef : DEF NAME parameters COLON suite"


def p_parameters(p):
	"""parameters : LPAREN varargslist RPAREN"""



def p_varargslist(p):
    """varargslist 	:
    				| fpdef EQUAL test fpdeflist COMMA
    				| fpdef EQUAL test fpdeflist
    				| fpdef fpdeflist COMMA
    				| fpdef fpdeflist
    """

def p_fpdeflist(p):
	"""fpdeflist 	:
					| fpdeflist COMMA fpdef
					| fpdeflist COMMA fpdef EQUAL test
	"""


def p_fpdef(p):
	"""fpdef 	: NAME
				| LPAREN fplist RPAREN
	"""


def p_fplist(p):
	"""fplist 	: fpdef fplist1 COMMA
				| fpdef fplist1
	"""

def p_fplist1(p):
	"""fplist1 	:
				| fplist1 COMMA fpdef
	"""


def p_stmt(p):
	"""stmt 	: simple_stmt
				| compound_stmt
	"""


def p_simple_stmt(p):
	"""simple_stmt 	: small_stmts NEWLINE
					| small_stmts SEMI NEWLINE
	"""


def p_small_stmts(p):
	"""small_stmts 	: small_stmts SEMI small_stmt
					| small_stmt
	"""



def p_small_stmt(p):
	"""small_stmt 	: flow_stmt
					| expr_stmt
					| print_stmt
					| pass_stmt
					| import_stmt
					| global_stmt
					| assert_stmt
					"""


def p_expr_stmt(p):
	"""expr_stmt 	: testlist augassign testlist
					| testlist eqtestlist
	"""

def p_eqtestlist(p):
	"""eqtestlist 	:
					| eqtestlist EQUAL testlist
	"""


def p_augassign(p):
	"""augassign 	: PLUSEQUAL
					| MINEQUAL
					| STAREQUAL
					| SLASHEQUAL
					| PERCENTEQUAL
					| STARSTAREQUAL
					| SLASHSLASHEQUAL
	"""


def p_print_stmt(p):
	"""print_stmt 	:	PRINT
					|	PRINT testlist
	"""


def p_pass_stmt(p):
	"pass_stmt : PASS"


def p_flow_stmt(p):
	"""flow_stmt 	: break_stmt
					| continue_stmt
					| return_stmt
	"""


def p_break_stmt(p):
	"""break_stmt 	: BREAK
	"""


def p_continue_stmt(p):
	"""continue_stmt 	: CONTINUE
	"""


def p_return_stmt(p):
	"""return_stmt 	:	RETURN
					|	RETURN testlist
	"""

def p_import_stmt(p):
	"""import_stmt 	:	IMPORT NAME
					|	IMPORT NAME AS NAME
	"""


def p_global_stmt(p):
	"""global_stmt 	: GLOBAL NAME namelist
	"""

def p_namelist(p):
	"""namelist 	:
					| COMMA NAME namelist
	"""

def p_assert_stmt(p):
	"""assert_stmt 	: ASSERT testlist
	"""


def p_compound_stmt(p):
	"""compound_stmt 	: if_stmt
						| for_stmt
						| while_stmt
						| funcdef
						| classdef
	"""


def p_if_stmt(p):
	"""if_stmt 	:	IF test COLON suite elif_list
				|	IF test COLON suite elif_list ELSE COLON suite
	"""

def p_elif_list(p):
	"""elif_list 	:
					| ELIF test COLON suite elif_list
	"""


def p_while_stmt(p):
	"""while_stmt 	:	WHILE test COLON suite
					|	WHILE test COLON suite ELSE COLON suite
	"""

def p_for_stmt(p):
	"""for_stmt 	:	FOR exprlist IN testlist COLON suite
					|	FOR exprlist IN testlist COLON suite ELSE COLON suite
	"""


def p_suite(p):
	"""suite 	: simple_stmt
				| NEWLINE INDENT stmts DEDENT"""


def p_test(p):
	"""test 	: or_test
				| or_test IF or_test ELSE test
	"""


def p_or_test(p):
	"""or_test 	: and_test ortestlist
	"""


def p_ortestlist(p):
	"""ortestlist 	:
					| OR and_test ortestlist
	"""


def p_and_test(p):
	"""and_test 	: not_test andtestlist
	"""


def p_andtestlist(p):
	"""andtestlist 	:
					| AND not_test andtestlist
	"""


def p_not_test(p):
	"""not_test 	: NOT not_test
					| comparison
	"""


def p_comparision(p):
	"""comparison 	: expr compexprlist
	"""


def p_compexprlist(p):
	"""compexprlist 	:
						| comp_op expr compexprlist
	"""


def p_comp_op(p):
	"""comp_op 	: LESS
				| GREATER
				| EQEQUAL
				| GREATEREQUAL
				| LESSEQUAL
				| NOTEQUAL
				| IN
				| NOT IN
				| IS
				| IS NOT
	"""


def p_expr(p):
	"""expr 	: xor_expr xorexprlist
	"""


def p_xorexprlist(p):
	"""xorexprlist 	:
					|	VBAR xor_expr xorexprlist
	"""


def p_xor_expr(p):
	"""xor_expr 	: and_expr andexprlist
	"""


def p_andexprlist(p):
	"""andexprlist 	:
					| CIRCUMFLEX and_expr andexprlist
	"""


def p_and_expr(p):
	"""and_expr 	: shift_expr shiftexprlist
	"""


def p_shiftexprlist(p):
	"""shiftexprlist 	:
						| AMPER shift_expr shiftexprlist
	"""


def p_shift_expr(p):
	"""shift_expr 	: arith_expr arithexprlist
	"""


def p_arithexprlist(p):
	"""arithexprlist 	:
						| LEFTSHIFT arith_expr arithexprlist
						| RIGHTSHIFT arith_expr arithexprlist
	"""


def p_arith_expr(p):
	"""arith_expr 	:	term termlist
	"""


def p_termlist(p):
	"""termlist 	:
					| PLUS term termlist
					| MINUS term termlist
	"""


def p_term(p):
	"""term :	factor factorlist
	"""


def p_factorlist(p):
	"""factorlist 	:
					| STAR factor factorlist
					| SLASH factor factorlist
					| PERCENT factor factorlist
					| SLASHSLASH factor factorlist
	"""


def p_factor(p):
	"""factor 	: power
				| PLUS factor
				| MINUS factor
				| TILDE factor
	"""


def p_power(p):
	"""power 	: atom trailerlist
				| atom trailerlist STARSTAR factor
	"""


def p_trailerlist(p):
	"""trailerlist 	:
					| trailer trailerlist
	"""


def p_atom(p):
	"""atom 	: LPAREN RPAREN
				| LPAREN testlist_comp RPAREN
				| LSQB RSQB
				| LSQB listmaker RSQB
				| LBRACE RBRACE
				| LBRACE dictorsetmaker RBRACE
				| BACKQUOTE testlist1 BACKQUOTE
				| NAME
				| NUMBER
				| FNUMBER
				| stringlist
	"""


def p_stringlist(p):
	"""stringlist 	: STRING
					| STRING stringlist
					| TRIPLESTRING
					| TRIPLESTRING stringlist
	"""


def p_listmaker(p):
	"""listmaker 	: testlist
	"""


def p_testlist_comp(p):
	"""testlist_comp 	: testlist
	"""


def p_trailer(p):
	"""trailer 	: LPAREN RPAREN
				| LPAREN arglist RPAREN
				| LSQB subscriptlist RSQB
				| DOT NAME
	"""


def p_subscriptlist(p):
	"""subscriptlist 	: subscript
						| subscript COMMA
						| subscript COMMA subscriptlist
	"""


def p_subscript(p):
	"""subscript 	: DOT DOT DOT
					| test
					| test COLON test sliceop
					| COLON test sliceop
					| test COLON sliceop
					| test COLON test
					| test COLON
					| COLON test
					| COLON sliceop
					| COLON
	"""


def p_sliceop(p):
	"""sliceop 	: COLON
				| COLON test
	"""


def p_exprlist(p):
	"""exprlist 	: expr
					| expr COMMA
					| expr COMMA exprlist
	"""


def p_testlist(p):
	"""testlist 	: test
					| test COMMA
					| test COMMA testlist
	"""


def p_dictorsetmaker(p):
	"""dictorsetmaker 	: testcolonlist
						| testlist
	"""


def p_testcolonlist(p):
	"""testcolonlist 	: test COLON test
						| test COLON test COMMA
						| test COLON test COMMA testcolonlist
	"""


def p_classdef(p):
	"""classdef 	: CLASS NAME COLON suite
					| CLASS NAME LPAREN RPAREN COLON suite
					| CLASS NAME LPAREN testlist RPAREN COLON suite
	"""


def p_arglist(p):
	"""arglist 	: argument
				| argument COMMA
				| argument COMMA arglist
	"""

def p_argument(p):
	"""argument 	: test
					| test EQUAL test
	"""

def p_testlist1(p):
	"""testlist1 	: test
					| test COMMA testlist1
	"""

def p_stmts(p):
	"""stmts 	: stmts stmt
				| stmt"""

def p_error(p):
    print( "Syntax Error near "+str(p.value)+ "' in line "+str(p.lineno))
    sys.exit()
import sys

def isAction(x):
	first = x[:x.find(":")]
	if first=="Action ":
		return True

def isReduce(x):
	third = x[x.find(":")+2:x.find(":")+3]
	if third == "R":
		return True
	else:
		return False

def getRule(x):
	rule = x[x.find("[")+1:x.find("]")]
	return rule

def left(x):
	return x[:x.find(" ")]

def right(x):
	children = x[x.find("->")+3:]
	children = children.split()
	return children

def getValue(x):
	value = x[x.find("with [")+6:x.find("] and")]
	value = value.replace("\\","\\\\")
	value = value.replace('"','\\\"')
	ans = []
	i = 0
	while i < len(value):
		if(value[i]==','):
			i+=1
		S = ""
		count = 0
		if value[i]!="'":
			while i<len(value) and value[i]!=',':
				S+=value[i]
				i+=1
			count = 2
		while(count!=2):
			S += value[i]
			if(value[i]=="'"):
				count+=1
			i+=1
		ans.append(S)
	return ans

class G1Parser(object):
	def __init__(self, mlexer=None):
		if mlexer is None:
			mlexer = lexer.G1Lexer()
		self.mlexer = mlexer
		self.parser = yacc.yacc(start="file_input", debug=True)
	def parse(self, code):
		self.mlexer.input(code)
		result = self.parser.parse(lexer = self.mlexer, debug=True)
		return result

if __name__=="__main__":
	z = G1Parser()
	data = open('for.py').read()
	sys.stderr = open('dump','w')
	root =  z.parse(data)
	a=open('dump').read()
	sys.stderr.close()
	lines = open('dump').readlines()
	lines = [line for line in lines if isAction(line)]
	lines = reversed(lines)
	stack = []
	nodeId = 0
	sys.stdout = open('a.txt','w')
	stack.append(("program",0,None))
	print ("digraph G \n{\n")

	print ("\tnode0 [label=\"program\"];")
	for line in lines:
		if isReduce(line):
			item = stack.pop()
			rule = getRule(line)
			children = right(rule)
			i=0
			value = getValue(line)
			for child in children:
				if(child=="<empty>"):
					continue
				nodeId+=1
				stack.append((child,nodeId,item[2]))
				if(value[i]!="None"):
					print( "\tnode"+str(nodeId)+" [label= \""+child+"\\n"+value[i]+"\"];")
				else:
					print ("\tnode"+str(nodeId)+" [label= \""+child+"\"];")

				print ("\tnode"+str(item[1])+" -> node"+str(nodeId)+";")
				i+=1
		else:
			stack.pop()
			pass
	print( "}")
	assert(len(stack)==0)
	print(stack)
