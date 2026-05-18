class Dictionary:
    def __init__(self):
        self.words = {}

    def newentry(self, word, description):
        self.words[word] = description

    def look(self, word):
        if word in self.words:
            return self.words[word]
        return "Can't find entry for " + word



