class ValidWordAbbr:
    """
    @param: dictionary: a list of words
    """
    abbr_dict = {}
    def __init__(self, dictionary):
        # do intialization if necessary
        # abbr_dict = set()
        for word in dictionary:
            
            if len(word) <= 2:
                abbr = word
            else:
                abbr = word[0] + str(len(word)-2) + word[-1]
            if abbr in self.abbr_dict:
                self.abbr_dict[abbr].add(word)
            else:
                self.abbr_dict[abbr] = {word}

    """
    @param: word: a string
    @return: true if its abbreviation is unique or false
    """
    def isUnique(self, word):
        # write your code here
        # print(self.abbr_dict)
        
        if len(word) > 2:
            abbr = word[0] + str(len(word)-2) + word[-1]
        else:
            abbr = word
        if abbr not in self.abbr_dict:
            return True
        elif self.abbr_dict[abbr] == {word}:
            return True
        else:
            return False

# Your ValidWordAbbr object will be instantiated and called as such:
# obj = ValidWordAbbr(dictionary)
# param = obj.isUnique(word)

if __name__ == "__main__":
    obj = ValidWordAbbr([ "a", "a", "cake", "card" ])
    print(obj.isUnique('a'))