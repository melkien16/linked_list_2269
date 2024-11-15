class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        st = str(num)
        count = 0
        for i in range(len(st)):
            ptr = i
            newSt = ''
            if i + k - 1 >= len(st):
                break
            for j in range(k):
                newSt += st[ptr]
                ptr += 1
            if int(newSt) != 0 and num % int(newSt) == 0:
                count += 1
        return count