class CSynter:
  '''
  CSynter

  Basic tools for syntactic analysis of the C Programming Language, up to C17 and the proposed standards for C23.
  '''
  # A list of grammatical symbols used in the C Programming language
  # TODO: Complete this list.  THere must be symbols I'm missing.
  grammaticalSymbolList = [
    "!", "\"", "\\", "%", "^", "&", "*", "(", 
    ")", "|", "[", "]", "{", "}", "-", "+", 
    "=", "/", ",", ".", ":", ";", "?", "<", 
    ">", "'", "#"]
  
  