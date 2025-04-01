class Solution:
    @staticmethod
    def multiply(num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        res = [0] * (len(num1) + len(num2))
        for i in range(len(num1) - 1, -1, -1):
            for j in range(len(num2) - 1, -1, -1):
                mul = (ord(num1[i]) - ord("0")) * (ord(num2[j]) - ord("0"))
                pos1, pos2 = i + j, i + j + 1
                total = mul + res[pos2]
                res[pos2] = total % 10
                res[pos1] += total // 10
        result = ''.join(map(str, res)).lstrip("0")
        return result if result else "0"
