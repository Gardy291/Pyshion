import ply.lex as lex
import ply.yacc as yacc
import sys

tokens = ['NAME',
          'TRIAD',
          'COMPLEMENTARY',
          'SPLITCOMPLEMENTARY',
          "EQUALS"
          ]
reserved = {'red','red-orange', 'orange', 'yellow-orange', 'yellow', 'yellow green', 'green', 'blue-green', 'blue', 'blue-violet', 'violet', 'red-violet'}
t_ignore = r' '
t_EQUALS = r'\='
t_LPAR = '\('
t_RPAR = '\)'
t_COMA = '\,'

def t_NAME(t):
    r"""[a-zA-Z_][a-zA-Z_0-9]*"""
    t.type = 'NAME'
    return t

def t_TRIAD(t):
    r"""[a-zA-Z_]*"""
    t.type = 'NAME'
    return t

def t_error(t):
    print("Illegal Character", t)
    t.lexer.skip(1)


lexer = lex.lex()
lexer.input('(a =,, orange ( )')
for t in lexer:
    print(t)


# def pas(p):
#     '''
#     Color := reserved
#     '''
#     print(p[1])
    # while True:
    #     try:
    #         i = input('>>>')
    #
    #     except EOFError:
    #         break
