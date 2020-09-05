class Puzzle:
    def findStrobogrammatic(self, n: int) -> List[str]:
        rp = [6,9] #mirror reflections must repeat equal number of times
        sym = [0,1,8] #symmetric
        result = {}
        #establish some rules for finding Strobogrammatic list:
        #all numbers that contain 6, must be followed with 9 and viceversa
        #all numbers that start with sym must end with sym if n >=2 
        #n=1 , return sym
        if n == 1:
            return sym
        #work n = 2 manually
        #elif n == 2:
        #69, 96, 11,88
        #111,181,818,101, 808, 609,906,696,969, 616, 689, 888,
        #all numbers except reflecting pairs, can repeat
        #no numbers start with 0
        number = [0]*n
        for i in range(0,len(number)):
            