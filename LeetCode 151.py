class Solution:
    def reverseWords(self, s: str) -> str:

        output = ''
        word = ''
        firstch = False

        for w in range(len(s)-1, -1, -1):
            if s[w] == ' ' and not firstch:
                continue
            else:
                firstch = True
            
            if firstch:
                if s[w] != ' ':
                    word = s[w] + word
                else:
                    if not output:
                        output += word
                    elif word:
                        output = output + ' ' + word
                    word = ''

            if w == 0 and word:
                if not output:
                    output += word
                elif word:
                    output = output + ' ' + word
                word = ''
        
        return output