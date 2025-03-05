class Solution:
    def intToRoman(self, num: int) -> str:
        self.ValueToSymbol = {1:"I", 5:'V', 10:'X', 50:'L', 100:'C', 500:'D', 1000:'M'}
        self.strnum = str(num)
        self.Output = ''

        for i in range(len(self.strnum)):
            j = -1 - i
            element = self.strnum[j] + '0'*int(abs(j)-1)

            if element[0] == '0':
                continue
            elif element[0] in ['4', '9']:
                self.Output = self.subtractive(int(element)) + self.Output
            else:
                self.Output = self.convert(int(element)) + self.Output
        
        return self.Output

    def convert(self, element):
        symbol = ''

        if element in self.ValueToSymbol:
            return self.ValueToSymbol[element]
        
        for k in [*self.ValueToSymbol]:
            if element > k:
                maxKey = k
            else:
                break
        
        symbol = self.ValueToSymbol[maxKey]
        remain = element - maxKey

        return symbol + self.convert(remain)

    def subtractive(self, element):
        symbol = ''

        if element in self.ValueToSymbol:
            return self.ValueToSymbol[element]
        
        for k in [*self.ValueToSymbol]:
            if element < k:
                maxKey = k
                break

        symbol = self.ValueToSymbol[maxKey]
        remain = maxKey - element

        return self.convert(remain) + symbol
          