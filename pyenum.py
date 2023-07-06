from enum import Enum, auto

class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

def read_enum():
    print("Color.RED is {}" .format(Color.RED))      # 输出: Color.RED
    print("Color.RED.value is {}" .format(Color.RED.value))    # 输出: 1

    for color in Color:
        print(color)   # 输出Color.RED、Color.GREEN、Color.BLUE

class Result(Enum):
    OPEN = auto()
    CLOSE = auto()

def result_enum():
    print(Result.OPEN.value)
    print(Result.CLOSE.value)

if __name__ == "__main__":
    result_enum()