class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num < 6:
            return False
        summ = 1
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                summ += i
                if i != num // i:
                    summ += (num // i)
        return summ == num