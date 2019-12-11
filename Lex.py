import ply.lex as lex
import ply.yacc as yacc
import sys

tokens = ['NAME',
          'TRIAD',
          'COMPLEMENTARY',
          'SPLITCOMPLEMENTARY',
          "EQUALS",
          "COLOR"
          ]
reserved = {'red', 'orange', 'yellow', 'green', 'blue', 'violet'}
t_ignore = r' '
t_EQUALS = r'\='
t_TRIAD = 'triad'
t_COMPLEMENTARY = 'complementary'
t_SPLITCOMPLEMENTARY = 'splitcomplementary'
t_COLOR = 'color'


def t_NAME(t):
    r"""[a-zA-Z_][a-zA-Z_0-9]*"""
    if t.value == 'triad':
        t.type = 'TRIAD'
    elif t.value == 'complementary':
        t.type = 'COMPLEMENTARY'
    elif t.value == 'splitcomplementary':
        t.type = 'SPLITCOMPLEMENTARY'
    elif reserved.__contains__(t.value):
        t.type = 'COLOR'
    else:
        t.type = 'NAME'
    return t


def t_error(t):
    print("Illegal Character", t)
    t.lexer.skip(1)


lexer = lex.lex()
for t in lexer:
    print(t)

def p_single_colors(p):
    '''
    colors: COLOR
    '''
    print(p[1])

def p_two_colors(p):
    '''
    colors: COLOR - COLOR
    '''

parser = yacc.yacc()

while True:
    try:
        i = input('>>>')

    except EOFError:
        break
    parser.parse(i)
