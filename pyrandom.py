import random

# random.random(): 生成一个范围在 [0, 1) 之间的浮点数。
# random.randint(a, b): 生成一个范围在 [a, b] 之间的整数。
# random.randrange(start, stop[, step]): 从指定的范围内返回一个随机整数，可以设置步长。

# 生成随机数
def print_random():
    print("random.random() is {}" .format(random.random()))             # 输出：0.1234567890...
    print("random.randint(1, 10) is {}" .format(random.randint(1, 10)))    # 输出：1到10之间的随机整数
    print("random.randrange(0, 100, 5) is {}" .format(random.randrange(0, 100, 5))) # 输出：0到100之间以步长为5的随机整数

# 随机选择元素
def random_element():
    fruits = ['apple', 'banana', 'cherry']
    print("random.choice(fruits) is {}" .format(random.choice(fruits)))        # 输出：随机选择一个水果
    print("random.sample(fruits, 2) is {}" .format(random.sample(fruits, 2)))        # 输出：随机选择两个独立的水果作为列表返回

# 打乱序列
def random_shuffle():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    random.shuffle(numbers)
    print("random.shuffle(numbers) is {}" .format(numbers))                     # 输出：[5, 2, 4, 1, 3] 或其他的随机顺序

# 设置随机数种子
def random_seed():
    random.seed(42)  # 设置随机数种子为 42
    print(random.randint(1, 10))    # 输出：5
    random.seed(42)  # 再次设置相同的种子
    print(random.randint(1, 10))    # 输出：5，与上一次调用结果相同
    random.seed(30)  # 再次设置相同的种子
    print(random.randint(1, 10))    # 输出：5，与上一次调用结果相同



if __name__=='__main__':
    # print_random()
    # random_element()
    # random_shuffle()
    random_seed()