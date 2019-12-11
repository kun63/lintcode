class Solution:
    """
    @param dict: an array of n distinct non-empty strings
    @return: an array of minimal possible abbreviations for every word
    """
    def wordsAbbreviation(self, dict):
        # write your code here
        def trans_abbr(word_set):
            temp = word_set.pop()
            l = len(temp)
            word_set.add(temp)
            output = []
            for i in range(1,l-2):
                if len(word_set) == 1:
                    i = i - 1
                    out = word_set.pop()
                    _abbr_out = [out[0:i+1]+str(l-i-2)+out[-1],out]
                    if len(_abbr_out[0]) == len(_abbr_out[1]):
                        _abbr_out[0] = _abbr_out[1]
                    output.append(_abbr_out)
                    break
                out_set = set()
                for w in word_set:
                    if w[i] != temp[i]:
                        out_set.add(w)
                
                if len(out_set) != 0:
                    for o in out_set:
                        word_set.remove(o)
                    if len(out_set) == 1:
                        out = out_set.pop()
                        abbr_out = [out[0:i+1]+str(l-i-2)+out[-1],out]
                        if len(abbr_out[0]) == len(abbr_out[1]):
                            abbr_out[0] = abbr_out[1]
                        output.append(abbr_out)
                    else:
                        out_set = trans_abbr(out_set)
                        for o in out_set:
                            output.append(o)
            if len(word_set) != 0:
                for w in word_set:
                    output.append([w,w])
                #  output.append(abbr_out)
            return output

        # return trans_abbr(dict)
        abbr_dict = {}
        for word in dict:
            if len(word) <= 3:
                abbr = word
                abbr_dict[abbr] = {word}
            else:
                abbr = word[0] + str(len(word)-2) + word[-1]
                if abbr in abbr_dict:
                    abbr_dict[abbr].add(word)
                else:
                    abbr_dict[abbr] = {word}


        trash = []
        new_abbr = []
        for abbr in abbr_dict:
            if len(abbr_dict[abbr]) > 1:
                abbr_list = trans_abbr(abbr_dict[abbr])
                # print(abbr_list)
                for k in abbr_list:
                    new_abbr.append(k)
                trash.append(abbr)
        for t in trash:
            del abbr_dict[t]
        for k in new_abbr:
            a = k[0]
            w = k[1]
            abbr_dict[a] = {w}
        outcome_dict = {}
        # print(abbr_dict)
        for abbr in abbr_dict:
            outcome_dict[list(abbr_dict[abbr])[0]] = abbr
        outcome = []
        for w in dict:
            outcome.append(outcome_dict[w])
        return outcome

if __name__ == "__main__":
    # print(Solution().wordsAbbreviation({"internal","internet","interval"}))
    print(Solution().wordsAbbreviation(["like","god","internal","me","internet","interval","intension","face","intrusion"]))
    # print(Solution().wordsAbbreviation(["where","there","is","beautiful","way"]))