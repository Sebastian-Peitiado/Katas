class Yatzy:

   
    def chance(*dice):
        return sum(dice)

    
    def yatzy(dice):
        counts = [0] * (len(dice) + 1)
        for die in dice:
            counts[die - 1] += 1
        for i in range(len(counts)):
            if counts[i] == 5:
                return 50
        return 0

    
    def ones(*dice):
        sum = 0
        for i in dice:
            if (i == 1):
                sum += 1
        return sum 

    
    def twos(*dice):
        sum = 0
        for i in dice:
            if (i == 2):
                sum += 2
        return sum 

    
    def threes(*dice):
        sum = 0
        for i in dice:
            if (i == 3):
                sum += 3
        return sum 


    def __init__(self, *dice):
        self.dice = list(dice)

    def fours(self):
        sum = 0
        for at in range(5):
            if (self.dice[at] == 4):
                sum += 4
        return sum

    def fives(self):
        s = 0
        i = 0
        for i in range(len(self.dice)):
            if (self.dice[i] == 5):
                s = s + 5
        return s

    def sixes(self):
        sum = 0
        for at in range(len(self.dice)):
            if (self.dice[at] == 6):
                sum = sum + 6
        return sum

    def score_pair(self):
        counts = {}
        for key in self.dice:
            counts[key] = counts.get(key,0) + 1
        for key in range( 6, 0, -1):  
            if counts.get(key,0) >= 2:
                return key * 2
        return 0

    
    def two_pair(self):
        
        counts = {}
        pairs = []
        for key in self.dice:
            counts[key] = counts.get(key, 0) + 1
        for key in range(6, 0, -1):
            if counts.get(key, 0) >= 2:
                pairs.append(key)
        if len(pairs) == 2:
            return (pairs[0] + pairs[1]) * 2
        else:
            return 0

    
    def four_of_a_kind(self):
        counts = {}
        for key in self.dice:
            counts[key] = counts.get(key, 0) + 1
        for key in range(6, 0, -1):
            if (counts.get(key,0) >= 4):
                return (key) * 4
        return 0

    
    def three_of_a_kind(self):
        counts = {}
        for key in self.dice:
            counts[key] = counts.get(key, 0) + 1
        for key in range(6, 0, -1):
            if (counts.get(key,0) >= 3):
                return (key) * 3
        return 0

    
    def smallStraight(self):
        straight = {1,2,3,4,5}
        result = all(valor in self.dice for valor in straight)
        if(result == True):
            return 15
        return 0

    
    def largeStraight(self):
        straight = {6,2,3,4,5}
        result = all(valor in self.dice for valor in straight)
        if(result == True):
            return 20
        return 0

    def fullHouse(self):
        counts = {}
        for key in self.dice:
            counts[key] = counts.get(key, 0) + 1
        for key in range(6, 0, -1):
            if (counts.get(key,0) == 3 and 2):
                return 18
        return 0