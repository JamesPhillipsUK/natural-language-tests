class CLexer:
  '''
  CLexer

  Basic tools for lexical analysis of the C Programming Language, up to C17 and the proposed standards for C23.
  '''

  # A lexicon of valid words in the language, in this case, C 'Keywords'.
  lexicon = [
    # Keywords up to C90:
    "auto", "break", "case", "char", "const", "continue", "default", "do",
    "double", "else", "enum", "extern", "float", "for", "goto", "if",
    "int", "long", "register", "return", "short", "signed", "sizeof", "static",
    "struct", "switch", "typedef", "union", "unsigned", "void", "volatile", "while",
    # Keywords added in C99:
    "_Bool", "_Complex", "_Imaginary", "inline", "restrict",
    # Keywords added in C11:
    "_Alignas", "_Alignof", "_Atomic", "_Generic", "_Noreturn", "_Static_assert", "_Thread_local",
    # Keywords to be added in C23:
    "_Decimal32", "_Decimal64", "_Decimal128"
  ]

  # C has an extra lexicon, only for use in a preprocessor directive.  These must be marked with hash '#' symbols.
  preprocessorExtendedLexicon = [
    # Keywords up to C17:
    "if", "elif", "else", "endif", "ifdef", "ifndef", "define", "undef", "include", "line", "error", "pragma", "defined",
    # Keywords to be added in C23:
    "__has_c_attribute"
  ]

  # C also has another extra lexicon, only for use NOT in a preprocessor directive.
  nonPreprocessorExtendedLexicon = [
    # Keywords up to C99:
    "_Pragma"
  ]
  # C also has another final extra lexicon of language extensions.  'asm' and 'fortran' are standard, but some compilers like to be different.
  compilerSpecificLanguageExtensionLexicon = [
    # Calling assembly - three common ways of doing it, one is the standard, the other two are what's actually used by compilers.
    "asm", "__asm", "__asm__",
    # Please, no.  Just no.
    "fortran"
  ]

  def __init__(self):
    '''
    Constructor for the lexical analyser.

    Parameters
    ----------
    self: object
      The instance of the lexical analyser.
    '''
    #for words in self.lexicon:
    #  print(words)
    pass

  def isWordInLexicon(self, word):
    '''
    Checks if a given word is in the lexicon.

    Parameters
    ----------
    self: object
      The instance of the lexical analyser.
    word: string
      The string which we're checking.

    Returns
    -------
    boolean
      Is the word in the lexicon?
    '''
    for words in self.lexicon:
      if (word == words):
        return True
    return False

  def isWordInPreprocessorExtendedLexicon(self, word):
    '''
    Checks if a given word is in the preprocessor extended lexicon.

    Parameters
    ----------
    self: object
      The instance of the lexical analyser.
    word: string
      The string which we're checking.

    Returns
    -------
    boolean
      Is the word in the lexicon?
    '''
    for words in self.preprocessorExtendedLexicon:
      if (word == words):
        return True
    return False

  def isWordInNonPreprocessorExtendedLexicon(self, word):
    '''
    Checks if a given word is in the non-preprocessor extended lexicon.

    Parameters
    ----------
    self: object
      The instance of the lexical analyser.
    word: string
      The string which we're checking.

    Returns
    -------
    boolean
      Is the word in the lexicon?
    '''
    for words in self.nonPreprocessorExtendedLexicon:
      if (word == words):
        return True
    return False

  def isWordInCompilerSpecificLanguageExtensionLexicon(self, word):
    '''
    Checks if a given word is in the compiler-specific language extension lexicon.

    Parameters
    ----------
    self: object
      The instance of the lexical analyser.
    word: string
      The string which we're checking.

    Returns
    -------
    boolean
      Is the word in the lexicon?
    '''
    for words in self.compilerSpecificLanguageExtensionLexicon:
      if (word == words):
        return True
    return False

  def isWordInLanguage(self, word):
    '''
    Checks if a given word is in any of the lexica.  One method is easier to call than four.

    Parameters
    ----------
    self: object
      The instance of the lexical analyser.
    word: string
      The string which we're checking.

    Returns
    -------
    boolean
      Is the word... a word?
    '''
    if(self.isWordInLexicon(word) 
      or self.isWordInPreprocessorExtendedLexicon(word)
      or self.isWordInNonPreprocessorExtendedLexicon(word)
      or self.isWordInCompilerSpecificLanguageExtensionLexicon(word)):
        return True
    return False
  
  def addWordToLexicon(self, word):
    '''
    Adds a given word to the lexicon.  This would be called when a word is #define-d.

    Parameters
    ----------
    self: object
      The instance of the lexical analyser.
    word: string
      The string which we're adding.

    Returns
    -------
    boolean
      True if it added, false if it's already in there.
    '''
    for words in self.lexicon:
      if (word == words):
        return False
    lexicon.append(word)
    return True