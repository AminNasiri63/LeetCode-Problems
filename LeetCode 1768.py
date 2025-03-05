class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        Output = []

        for i in range(len(word1)):
            Output.append(word1[i])

            if i < len(word2):
                Output.append(word2[i]) 
        i += 1
        if i < len(word2):
            Output.append(word2[i:])
        
        return ''.join(Output)
        