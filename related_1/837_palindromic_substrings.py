class Solution:
    """
    @param str: s string
    @return: return an integer, denote the number of the palindromic substrings
    """
    def countPalindromicSubstrings(self, str):
        # write your code here
        import collections
        self.opt = collections.defaultdict(bool)
        self.count = 0
        def helper(i,j):
            # j -= 1
            s = str[i:j+1]
            a = str.find(s)
            b = j - i + a
            if (a,b) in self.opt and self.opt[(a,b)]:
                self.count += 1
                return
            if s == s[::-1]:
                self.opt[(i,j)] = True
                self.count += 1
                if i-1>=0 and j+1<len(str) and str[i-1] == str[j+1]:
                    self.opt[(i-1,j+1)] = True
                    helper(i-1,j+1)
            else:
                self.opt[(i,j)] = False
        for i in range(len(str)):
            for j in range(i,len(str)):
                if str[i] == str[j]:
                    if j-i <= 2 or self.opt[(i+1,j-1)] == True:
                        self.opt[(i,j)] = True
                        self.count += 1
        return self.count
    def _countPalindromicSubstrings(self, str):
        count = 0
        for i in range(len(str)):
            for j in range(i,len(str)):
                s = str[i:j+1]
                if s == s[::-1]:
                    count += 1
        return count

if __name__ == '__main__':
    print(Solution()._countPalindromicSubstrings('onoopplplonooomoplnooppnnlmolnmlmmnplopmmmmmmpnnpomponlppmlllnnoomnmlnlplnomnnpllonmllnnoonopmppmmpnmnomolplmmolnoolnllpnpmoppmpnopmmnmmnomppnopmpnpllmpoollpmmolllmmlmpmpmnnnmnllpponnlmlplpnlnnnnppppmmnpmnnnllopnllnoolnnmonnonopmmlponplmlpnnonmpmmlplonllpnomnmnomopmoollpmonnlommnlnolnnomppolmmmpolmlpmppnonmmoonnonplnnmlponpponlmlmnnpnlpmonmlmpopnlpmppllolnonmpompooolmppmlmlololmplmlomonmmponmnnpolmlolmoplpnlmonooomomnpnmnnlnpllnnlpoopmnlloppomnolppommmoopomopopnpmllnlmmpnlnmnpnlopmnppmnnopllppnnmpnnnmpnolmolllmpppplllnllopplpnpnplonmpollooomnoommmpnlopmpoonnmnmnlmmmmopmplmnplnmonmllpplomlopomnlnolnlmllpolllpnpmmmlnnlnolmmnlnmopponomlnpnoomnoponpmmpnomnpmoolnpplmlnoonpononnplmmnnnopmlopomnopplmmpmllmommmplopnpolnopomoooppnmmmmpopnllplonmmmlnlompopnnmomplnnmlnmpnmlmploopoomopmlomonolpmopoopolppplnonpplnonoplolonmlpnmmpllpolmolnnnppmopmnpolompolmnllpnmolopnopmopmnoomomomnopmpmponllmnnnnoonlpnnpolmpolpmlpplmmoonnplpplnmnnnlppmpppoonplmpmmolnonnollppplmlnnnpmnpoonpnploomopmnmlpplmnlpmppnmno'))
    # print(Solution().countPalindromicSubstrings('aba'))