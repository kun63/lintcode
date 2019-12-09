class Solution:
    """
    @param n: The integer
    @return: Roman representation
    """
    def intToRoman(self, n):
        # write your code here
        complonent_roman = []
        complonent_roman.append(["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"])
        complonent_roman.append(["X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"])
        complonent_roman.append(["C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"])
        complonent_roman.append(["M", "MM", "MMM"])

        n = str(n)
        outcome = ''
        for i in range(1,len(n)+1):
            # i = -i
            if int(n[-i]) != 0:
                outcome = complonent_roman[i-1][int(n[-i])-1] + outcome
        return outcome

if __name__ == "__main__":
    print(Solution().intToRoman(101))
