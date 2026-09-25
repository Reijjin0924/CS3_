"""
#5, FERRER, Reginald Andrei D.
9-Samat
"""

years = int(input("Enter your birth year: "))
diff_animal = ["Monkey (猴 / Hóu)", "Rooster (鸡 / Jī)", "Dog (狗 / Gǒu)", "Pig (猪 / Zhū)", "Rat (鼠 / Shǔ)", "Ox (牛 / Niú)",
           "Tiger (虎 / Hǔ)", "Rabbit (兔 / Tù)", "Dragon (龙 / Lóng)", "Snake (蛇 / Shé)", "Horse (马 / Mǎ)", "Goat (羊 / Yáng)"]
if years < 1900:
    print("Invalid Year, It should not be earlier than 1900")

else:
    print("Your Chinese Zodiac sign is:", diff_animal[years % 12])
