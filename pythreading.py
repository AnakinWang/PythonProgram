import threading

# def print_numbers():
#     for i in range(1, 6):
#         print(i)

# thread = threading.Thread(target=print_numbers)

def threading_lock():
    # 创建锁对象
    lock = threading.Lock()
    global counter

    def increment_counter():
        
        with lock:  # 获取锁
            counter += 1
            print("Counter:", counter)

    # 创建多个线程并启动
    threads = []
    for _ in range(5):
        thread = threading.Thread(target=increment_counter)
        threads.append(thread)
        thread.start()

    # 等待所有线程执行完成
    for thread in threads:
        thread.join()

if __name__ == '__main__':
    threading_lock()
