from bouquets import MothersDay, ValentinesDay
from flowers import Alstro, Lilly, Rose


robbie_griffin = MothersDay()
# print(robbie_griffin)
robbie_griffin_rose = Rose("red")
# print(robbie_griffin_rose)
robbie_griffin.enhance(robbie_griffin_rose)

print(robbie_griffin.flowers)