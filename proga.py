class Game:
    def __init__(self):
        self.rolls = []

    def add(self, pins):
        self.rolls.append(pins)

    def score(self):
        total_score = 0
        roll_index = 0
        for frame in range(10):
            if self.is_strike(roll_index):
                total_score += 10 + self.strike_bonus(roll_index)   #Общий счет
                roll_index += 1
            elif self.is_spare(roll_index):
                total_score += 10 + self.spare_bonus(roll_index)
                roll_index += 2
            else:
                total_score += self.frame_score(roll_index)
                roll_index += 2
            
        return total_score

    def is_strike(self, roll_index):
        return self.rolls[roll_index] == 10
    
    def strike_bonus(self, roll_index):
        return self.rolls[roll_index + 1] + self.rolls[roll_index + 2]

    def is_spare(self, roll_index):
        if roll_index + 1 < len(self.rolls):
            return self.rolls[roll_index] + self.rolls[roll_index + 1] == 10
        return False

    def spare_bonus(self, roll_index):
        if roll_index + 2 < len(self.rolls):
            return self.rolls[roll_index + 2]
        return 0

    def frame_score(self, roll_index):
        return self.rolls[roll_index] + self.rolls[roll_index + 1]

Max = Game()
Max.add(4)
Max.add(2)
Max.add(7)
Max.add(2)
Max.add(8)
Max.add(2)
print(Max.score())
