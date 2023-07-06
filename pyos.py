import os
import datetime

def current_directory():
    current_dir = os.getcwd()
    print("current_directory is {}" .format(current_dir))

# 切换工作目录
def change_directory():
    new_dir = "/path/to/new/directory"
    os.chdir(new_dir)

# 列出目录中的文件和子目录
def all_files():
    files = os.listdir(".")
    for file in files:
        print(file)

# 创建目录
def createFile():
    new_dir = r"E:\00CodeFile\13PythonProgram\FileTest"   # 路径前加个r，防止系统将\0认为是空字符
    os.mkdir(new_dir)

# 删除目录
def delete_file():
    dir_to_delete = r"E:\00CodeFile\13PythonProgram\FileTest"
    os.rmdir(dir_to_delete)

# 检查文件或目录是否存在
def path_check():
    path_to_check = r"E:\00CodeFile\13PythonProgram\FileTest"
    if os.path.exists(path_to_check):
        print("Exists")
    else:
        print("Does not exist")

# 获取当前进程 ID
def get_PID():
    pid = os.getpid()
    print("current PID is {}" .format(pid))

# 杀死指定进程
# def kill_PID():
#     pid_to_kill = 12345
#     os.kill(pid_to_kill, signal.SIGTERM)

# 获取指定环境变量的值
def environment_PATH():
    value = os.environ.get("PATH")
    print("environment PATH is {}" .format(value))

    # 设置环境变量的值
    # os.environ["MY_VARIABLE"] = "my_value"

def saveTXT():
    text = "Already saved"
    current_time = datetime.datetime.now()
    formatted_time = current_time.strftime("%H%M%S")
    txt_name = formatted_time + '.txt'

    txt_file = r"E:\00CodeFile\13PythonProgram\FileTest"

    if not os.path.exists(txt_file):
        os.mkdir(txt_file)

        # 2. 创建/进入当天日期的目录
    dateDir_name = current_time.strftime("%Y-%m-%d")
    dateDir_path = os.path.join(txt_file, dateDir_name)
    if not os.path.exists(dateDir_path):
        os.mkdir(dateDir_path)

    txt_name = os.path.join(dateDir_path,txt_name)

    # 打开文件，以写入模式（'w'）创建/覆盖文件
    with open(txt_name, "w", encoding="utf-8") as file:
        # 将内容写入文件
        file.write(text)

    print("文件保存成功！保存到：",txt_name)

if __name__=='__main__':
    # current_directory()
    # all_files()
    # createFile()
    # delete_file()
    # path_check()
    # environment_PATH()
    saveTXT()