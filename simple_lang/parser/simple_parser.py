# Get the token map from the lexer.  This is required.
from ply import yacc

from simple_lang.ast.e import E
from simple_lang.ast.if_node import If
from simple_lang.ast.num import Num
from simple_lang.ast.print import Print

start = 'statement'


def p_print(p):
    'print : PRINT e'
    p[0] = Print(p[2])


def p_begin(p):
    'begin : BEGIN statement list'
    p[0] = [p[2]] + p[3]


def p_list(p):
    '''list : END
            | SEMICOLON statement list  '''
    if len(p) == 2:
        p[0] = []
    else:
        p[0] = [p[2]] + p[3]


def p_statement(p):
    """statement : if
                | begin
                | print
                |  """
    p[0] = p[1]


def p_if(p):
    """if : IF e THEN statement ELSE statement"""
    p[0] = If(p[2], p[4], p[6])


def p_e(p):
    """e : num EQUALS num"""
    p[0] = E(p[1], p[3])


def p_num(p):
    """num : NUM"""
    p[0] = Num(p[1])


# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input: ", p)


# Build the parser
parser = yacc.yacc()
