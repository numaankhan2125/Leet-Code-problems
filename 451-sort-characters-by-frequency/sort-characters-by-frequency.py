class Solution:
    def frequencySort(self, s: str) -> str:
        counter = Counter(s)
        n= [(-freq, char) for char, freq in counter.items()]
        heapq.heapify(n)
        result = ''
        while n:
            freq, char = heapq.heappop(n)
            result += char * -freq
        return result

