def readFile(name):
  with open(name, "r", errors="ignore") as file:
    return file.read()

def wordCount(text):
  return len(text.split())

def uniqueWordCount(text):
  return len(set(text.split()))

def findContent(text, word):
  return  text.split().count(word)