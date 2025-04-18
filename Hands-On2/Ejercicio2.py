import ply.lex as lex

# Definición de tokens
tokens = (
    'INT',       # Palabra clave 'int'
    'RETURN',    # Palabra clave 'return'
    'ID',        # Identificadores
    'NUMBER',    # Números enteros
    'STRING',    # Cadenas de texto
    'LPAREN',    # Paréntesis izquierdo '('
    'RPAREN',    # Paréntesis derecho ')'
    'LBRACE',    # Llave izquierda '{'
    'RBRACE',    # Llave derecha '}'
    'EQUALS',    # Operador de asignación '='
    'SEMICOLON', # Punto y coma ';'
)

# Expresiones regulares para tokens simples
t_INT = r'int'
t_RETURN = r'return'
t_ID = r'[a-zA-Z_][a-zA-Z0-9_]*'
t_NUMBER = r'\d+'
t_STRING = r'"[^"]*"'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_EQUALS = r'='
t_SEMICOLON = r';'

# Ignorar espacios, tabulaciones y saltos de línea
t_ignore = ' \t\n'

# Expresión regular para comentarios de una línea
def t_COMMENT(t):
    r'//.*'
    pass  # Ignorar comentarios

# Expresión regular para comentarios de múltiples líneas
def t_MULTILINE_COMMENT(t):
    r'/\*(.|\n)*?\*/'
    pass  # Ignorar comentarios

# Manejo de errores
def t_error(t):
    print(f"Carácter ilegal: {t.value[0]}")
    t.lexer.skip(1)

# Construir el analizador léxico
lexer = lex.lex()

# Prueba del analizador léxico
data = """
int main() {
    // Esto es un comentario
    int x = 42;
    /* Esto es un
       comentario multilínea */
    return x;
}
"""

# Alimentar el analizador con la entrada
lexer.input(data)

# Imprimir los tokens reconocidos
for token in lexer:
    print(token)