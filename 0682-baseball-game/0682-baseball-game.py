class Solution:
    def calPoints(self, operations: List[str]) -> int:
        total = []
        for i in range(len(operations)):
            if operations[i] == 'C':
                total.pop()
            elif operations[i] == 'D':
                total.append(2*total[-1])
            elif operations[i] == '+':
                total.append(total[-1]+total[-2])
            else:
                total.append(int(operations[i]))
        
        return sum(total)
