class Solution:
    """
    @param s: Roman representation
    @return: an integer
    """
    def _romanToInt(self, s):
    
        # write your code here
        if s == '':
            return 0
        roman = [['IX','VIII','VII','VI','V','VI','III','II','I'],['XC','LXXX','LXX','LX','L','XL','XXX','XX','X'],['CM','DCCC','DCC','DC','D','CD','CCC','CC','C'],['MMM','MM','M']]
        index = 0
        result = 0
        s = s[::-1]
        while s:
            for i, t in enumerate(roman[index]):
                if s.find(t[::-1]) == 0:
                    s = s[len(t):]
                    result += (9-i)*(10**index)
                    
                    break
            index += 1
        return result
    def romanToInt(self, s):
        roman = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        result = 0
        for i in range(len(s)-1):
            if roman[s[i]] < roman[s[i+1]]:
                result -= roman[s[i]]
            else:
                result += roman[s[i]]
        result += roman[s[i+1]]
        return result

if __name__ == "__main__":
    print(Solution().romanToInt('IV'))



