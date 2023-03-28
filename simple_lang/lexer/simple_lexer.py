import ply.lex as lex

# List of token names.   This is always required
tokens = (
    'IF',
    'THEN',
    'ELSE',
    'BEGIN',
    'PRINT',
    'EQUALS',
    'SEMICOLON',
    'END',
    'NUM',
)

literal_to_token = {
    "if": "IF",
    "then": "THEN",
    "else": "ELSE",
    "begin": "BEGIN",
    "print": "PRINT",
    "end": "END",
}


def t_KEYWORD(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = literal_to_token.get(t.value)
    return t


def t_EQUALS(t):
    r'='
    t.type = "EQUALS"
    return t


def t_SEMICOLON(t):
    r';'
    t.type = "SEMICOLON"
    return t


# A regular expression rule with some action code
def t_NUM(t):
    r'\d+'
    t.value = int(t.value)
    return t


# A string containing ignored characters (spaces and tabs)
t_ignore = ' \t'


# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


# Build the lexer
lexer = lex.lex()


def lex_string(string):
    lexer.input(string)
    tokens = []
    while True:
        token = lexer.token()
        if not token:
            break  # No more input
        tokens.append(token)
    return tokens
