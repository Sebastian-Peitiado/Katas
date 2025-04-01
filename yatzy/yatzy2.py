
class Yatzy:


    def score(self, dice, category: str) -> int:
        counts = {}
        for key in dice:
            counts[key] = counts.get(key,0) + 1
        
        
        match category:
            case "CHANCE":
               
                return sum(dice)

            case "YATZY":

               return 50 if 5 in counts.values() else 0

            case "ONE"|"TWO"|"THREES"|"FOURS"|"FIVES"|"SIXES":
                number = ["ONE", "TWO", "THREES", "FOURS", "FIVES", "SIXES"].index(category) + 1
                return counts.get(number, 0) * number

            case "PAIR":

                for key in range( 6, 0, -1):  
                    if counts.get(key,0) >= 2:
                        return key * 2

            case "THREE_OF_KIND":
                for key in range(6, 0, -1):
                    if (counts.get(key,0) >= 3):
                     return (key) * 3

            case "FOUR_OF_A_KIND":

                for key in range(6, 0, -1):
                    if (counts.get(key,0) >= 4):
                        return (key) * 4

            case "SMALL_STRAIGHT":

                # score if dice contains 1,2,3,4,5
                straight = {1,2,3,4,5}
                result = all(valor in dice for valor in straight)
                if(result == True):
                    return 15

            case "LARGE_STRAIGHT":
                straight = {6,2,3,4,5}
                result = all(valor in dice for valor in straight)
                if(result == True):
                    return 20

            case "TWO_PAIRS":
                pairs = []
                for key in range(6, 0, -1):
                    if counts.get(key, 0) >= 2:
                        pairs.append(key)
                if len(pairs) == 2:
                    return (pairs[0] + pairs[1]) * 2
             
            case "FULL_HOUSE":
                for key in range(6, 0, -1):
                    if (counts.get(key,0) == 3 and 2):
                        return 18
                    
        return 0