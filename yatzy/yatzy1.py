class Yatzy:

    @staticmethod
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

    @staticmethod
    def three_of_a_kind(d1, d2, d3, d4, d5):
        t = [0] * 6
        t[d1 - 1] += 1
        t[d2 - 1] += 1
        t[d3 - 1] += 1
        t[d4 - 1] += 1
        t[d5 - 1] += 1
        for i in range(6):
            if (t[i] >= 3):
                return (i + 1) * 3
        return 0

    @staticmethod
    def smallStraight(d1, d2, d3, d4, d5):
        tallies = [0] * 6
        tallies[d1 - 1] += 1
        tallies[d2 - 1] += 1
        tallies[d3 - 1] += 1
        tallies[d4 - 1] += 1
        tallies[d5 - 1] += 1
        if (tallies[0] == 1 and
                tallies[1] == 1 and
                tallies[2] == 1 and
                tallies[3] == 1 and
                tallies[4] == 1):
            return 15
        return 0

    @staticmethod
    def largeStraight(d1, d2, d3, d4, d5):
        tallies = [0] * 6
        tallies[d1 - 1] += 1
        tallies[d2 - 1] += 1
        tallies[d3 - 1] += 1
        tallies[d4 - 1] += 1
        tallies[d5 - 1] += 1
        if (tallies[1] == 1 and
                tallies[2] == 1 and
                tallies[3] == 1 and
                tallies[4] == 1
                and tallies[5] == 1):
            return 20
        return 0

    @staticmethod
    def fullHouse(d1, d2, d3, d4, d5):
        tallies = []
        _2 = False
        i = 0
        _2_at = 0
        _3 = False
        _3_at = 0

        tallies = [0] * 6
        tallies[d1 - 1] += 1
        tallies[d2 - 1] += 1
        tallies[d3 - 1] += 1
        tallies[d4 - 1] += 1
        tallies[d5 - 1] += 1

        for i in range(6):
            if (tallies[i] == 2):
                _2 = True
                _2_at = i + 1

        for i in range(6):
            if (tallies[i] == 3):
                _3 = True
                _3_at = i + 1

        if (_2 and _3):
            return _2_at * 2 + _3_at * 3
        else:
            return 0