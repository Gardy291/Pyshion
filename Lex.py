import ply.lex as lex
import ply.yacc as yacc
from ColorSelector import *
 

tokens = ['NAME',
          'TRIAD',
          'COMPLEMENTARY',
          'SPLITCOMPLEMENTS',
          "EQUALS",
          "COLOR",
          "DASH"
          ]
reserved = {'red','red-orange','orange','yellow-orange','yellow','yellow-green','green','blue-green','blue','blue-violet','violet','red-violet'}
t_ignore = r' '
t_EQUALS = r'\='
t_TRIAD = r'triad'
t_COMPLEMENTARY = r'complementary'
t_SPLITCOMPLEMENTS = r'splitcomplements'
t_COLOR = r'color'
t_DASH = r'\-'


def t_NAME(t):
    r"""[a-zA-Z_][a-zA-Z_0-9]*"""
    if t.value == 'triad':
        t.type = 'TRIAD'
    elif t.value == 'complementary':
        t.type = 'COMPLEMENTARY'
    elif t.value == 'splitcomplements':
        t.type = 'SPLITCOMPLEMENTS'
    elif reserved.__contains__(t.value):
        t.type = 'COLOR'
    else:
        t.type = 'NAME'
    return t


def t_error(t):
    print("Illegal Character", t)
    t.lexer.skip(1)


lexer = lex.lex()


def p_expression(p):
    '''
    expression : NAME
                | colors
                | var_assign
                | complement
                | triads
                | split
                | empty
    '''
    print(run(p[1]))


def p_empty(p):
    '''
    empty :
    '''
    p[0] = None


def p_single_colors(p):
    '''
    colors : COLOR
    '''
    p[0] = p[1]


def p_two_colors(p):
    '''
    colors : COLOR DASH COLOR
    '''
    p[0] = (p[1]+p[2]+p[3])


def p_var_assign(p):
    '''
    var_assign : NAME EQUALS colors
                | NAME EQUALS NAME
                | NAME EQUALS complement
                | NAME EQUALS split
                | NAME EQUALS triads
    '''
    p[0] = (p[1], p[2], p[3])


def p_triads(p):
    '''
    triads : TRIAD colors
    '''
    p[0] = (p[1], p[2])


def p_complement(p):
    '''
    complement : COMPLEMENTARY colors
    '''
    p[0] = (p[1], p[2])


def p_splitcomplement(p):
    '''
    split : SPLITCOMPLEMENTS colors
    '''
    p[0] = (p[1], p[2])


def p_error(p):
    print("Syntax error!!")


def run(p):
    if type(p) == tuple:
        if p[0]=='complementary':
           return ColorSelector.complementary(p[1])
        elif p[0]=='triad':
            return ColorSelector.triad(p[1])
        elif p[0]=='splitcomplements':
            return ColorSelector.splitComplements(p[1])
        elif p[1]=='=':
            return run(p[2])
    else:
        if reserved.__contains__(p):
            return ColorSelector.allCombinations(p)
        return p;


parser = yacc.yacc()

while True:
    try:
        i = input('>>>')

    except EOFError:
        break
    parser.parse(i)
