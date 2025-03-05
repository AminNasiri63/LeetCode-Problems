class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        w = 0
        text = {}
        k = 0
        self.allText = []
        self.maxWidth = maxWidth

        while w < len(words):

            if k in text:

                if text[k][0] + len(text[k][1:]) + len(words[w]) <= self.maxWidth:
                    text[k].append(words[w])
                    text[k][0] += len(words[w])
                
                else:
                    self.leftJustified(text[k])

                    k += 1
                    text[k] = [len(words[w]), words[w]]
            
            else:
                k += 1
                text[k] = [len(words[w]), words[w]]
            
            w += 1
            if w == len(words):
                self.RightJustified(text[k])

        return self.allText


    def leftJustified(self, inputText):
        newLine = ''
        remainSpace = self.maxWidth - inputText[0]

        if len(inputText[1:]) == 1:
            newLine += inputText[1] + ' ' * remainSpace
            self.allText.append(newLine)
        
        else:
            while remainSpace > 0:
                for v in range(len(inputText[1:]) - 1):
                    inputText[v+1] = inputText[v+1] + " "
                    remainSpace -= 1
                    if remainSpace == 0:
                        break
            newLine = ''.join(inputText[1:])
            self.allText.append(newLine)

    def RightJustified(self, inputText):

        newLine = ''

        eachSpace = 1
        reaminSpace = self.maxWidth - inputText[0] 

        for v in range(len(inputText[1:])):
            if v == len(inputText[1:]) - 1:
                newLine += inputText[1:][v] + ' ' * reaminSpace
                self.allText.append(newLine)
            else:
                newLine += inputText[1:][v] + ' ' * eachSpace
                reaminSpace -= eachSpace