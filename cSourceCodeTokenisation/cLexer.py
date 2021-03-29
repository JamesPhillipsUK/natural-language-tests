class CLexer:

  # Start with a lexicon of all valid words in the language, in this case, C Keywords.
  lexicon = [
    # Keywords up to C90:
    "auto", "break", "case", "char", "const", "continue", "default", "do",
    "double", "else", "enum", "extern", "float", "for", "goto", "if",
    "int", "long", "register", "return", "short", "signed", "sizeof", "static",
    "struct", "switch", "typedef", "union", "unsigned", "void", "volatile", "while",
    # Keywords added in C99:
    "_Bool", "_Complex", "_Imaginary", "inline", "restrict",
    # Keywords added in C11:
    "_Alignas", "_Alignof", "_Atomic", "_Generic", "_Noreturn", "_Static_assert", "_Thread_local"
  ]

  def __init__(self):
    pass

  def wordInLexicon(self, word):
    for words in lexicon:
      if (word == words):
        return True
    return False
  
  def addWordToLexicon(self, word):
    for words in lexicon:
      if (word == words):
        return False
    lexicon.append(word)
    return True