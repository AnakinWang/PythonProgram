import copy

def shallow_copy():
    original_list = [1, 2, [3, 4]]
    copied_list = copy.copy(original_list)

    print(copied_list)                  # 输出: [1, 2, [3, 4]]
    print(copied_list is original_list)  # 输出: False
    print(copied_list[2] is original_list[2])  # 输出: True

def deep_copy():
    original_list = [1, 2, [3, 4]]
    deep_copied_list = copy.deepcopy(original_list)

    print(deep_copied_list)                        # 输出: [1, 2, [3, 4]]
    print(deep_copied_list is original_list)        # 输出: False
    print(deep_copied_list[2] is original_list[2])  # 输出: False

def just_copy():
    original_list = [1, 2, [3, 4]]
    pure_list = [6,7]
    pure_list.append(original_list.copy())
    print("pure list is {}" .format(pure_list))


if __name__=='__main__':
    # shallow_copy()
    # deep_copy()
    just_copy()