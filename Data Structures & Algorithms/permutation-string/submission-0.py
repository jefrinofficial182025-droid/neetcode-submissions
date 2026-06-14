class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counter = Counter(s1) 
        for i in range(len(s2)-len(s1)+1):
            window = s2[i:i+len(s1)]
            windcounter = Counter(window)
            if counter == windcounter: 
                return True
        return False