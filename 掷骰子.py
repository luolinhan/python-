from random import randint
import pygal


class Die():
    """表示一个骰子的类"""

    def __init__(self, num_sides=6):
        """骰子默认6面"""
        self.num_sides = num_sides

    def roll(self):
        """返回一个位于1和骰子面数之间的随机值"""
        return randint(1, self.num_sides)
    
    
# 投掷一个骰子
die_1 = Die()
print(die_1.roll())
results = []
for roll_num in range(100):
    result = die_1.roll()
    results.append(result)
print(results)
for num in range(1, 7):
    print("面为%-2d的出现的次数为：%d)" % (num, results.count(num)))

# 投掷两个骰子
die_1 = Die()
die_2 = Die()
# 掷几次骰子，并将结果存储在一个列表中
results = []
for roll_num in range(100):
    result = die_1.roll() + die_2.roll()
    results.append(result)
# 打印掷骰子的结果
print("1", results)
# 分析结果
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2,max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)
    print("面为%-2d的出现的次数为：%d)" % (value, results.count(value)))
# 打印每个面出现的次数
print(frequencies)

# 对结果进行可视化
hist = pygal.Bar()
hist.title = "Results of rolling one D6 1000 times"
hist.x_labels = [str(i) for i in range(2, 13)]
hist.x_tile = "Result"
hist.y_title = "Frequency of Result"

hist.add("D6+D6", frequencies)
hist.render_to_file("dice_visual.svg")
print("图表制作成功")