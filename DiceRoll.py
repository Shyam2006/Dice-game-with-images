#Dice Game with Images
import random
from PIL import Image
dice=random.randint(1,6)
picname = "images\\" + str(dice) + ".png"
print("dice = ", dice)
img = Image.open(picname)
img.show()