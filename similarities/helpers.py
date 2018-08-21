from nltk.tokenize import sent_tokenize


def getDupes(a, b):
    """Custom function to return duplicates between two lists"""
    dupeList = []
    for i in range(len(a)):
        if a[i] in b:
            dupeList.append(a[i])
    return dupeList


def removeDupes(dirtyList):
    """Accepts a list, and removes all duplicates"""

    for item in dirtyList:
        while dirtyList.count(item) > 1:
            dirtyList.remove(item)

    return dirtyList


def makeChunks(a, n):
    """Custom function to turn a list into appropriately sized chunks"""
    chunks = []
    for i in range(0, len(a) - n + 1):
        # print(a[i:i+n])
        chunks.append(a[i:i + n])

    #  go through both lists, removing duplicates
    chunks = removeDupes(chunks)

    return chunks


def lines(a, b):
    """Return lines in both a and b"""
    aList = removeDupes(a.split("\n"))
    bList = removeDupes(b.split("\n"))

    return getDupes(aList, bList)


def sentences(a, b):
    """Return sentences in both a and b"""
    aSentences = removeDupes(sent_tokenize(a))
    bSentences = removeDupes(sent_tokenize(b))

    return getDupes(aSentences, bSentences)


def substrings(a, b, n):
    """Return substrings of length n in both a and b"""
    aChunks = makeChunks(a, n)
    bChunks = makeChunks(b, n)

    return getDupes(aChunks, bChunks)
