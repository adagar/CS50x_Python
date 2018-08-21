from nltk.tokenize import sent_tokenize

def getDupes(a, b):
    """Custom function to return duplicates between two lists"""
    dupeList = []
    for i in range(len(a)):
        if a[i] in b:
            dupeList.append(a[i])
    return dupeList

def makeChunks(a, n):
    """Custom function to turn a list into appropriately sized chunks"""
    chunks = []
    for i in range(0, len(a)-n):
        #print(a[i:i+n])
        chunks.append(a[i:i+n])

    #go through both lists, removing duplicates
    for chunk in chunks:
        while chunks.count(chunk) > 1:
            chunks.remove(chunk)

    return chunks

def lines(a, b):
    """Return lines in both a and b"""
    aList = a.split("\n")
    bList = b.split("\n")

    return getDupes(aList, bList)


def sentences(a, b):
    """Return sentences in both a and b"""
    aSentences = sent_tokenize(a)
    bSentences = sent_tokenize(b)

    return getDupes(aSentences, bSentences)


def substrings(a, b, n):
    """Return substrings of length n in both a and b"""
    aChunks = makeChunks(a, n)
    bChunks = makeChunks(b, n)
    
    return aChunks
