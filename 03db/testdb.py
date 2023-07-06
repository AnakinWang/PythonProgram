import pymysql

def printDB():
    # 连接MySQL(Socket)
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='', charset="utf8")
    cursor = conn.cursor()

    # 1.查看数据库（查看数据库，必须fetchall）
    # 发送指令
    cursor.execute("show databases")
    # 获取指令的结果
    result = cursor.fetchall()
    print(result)  # (('information_schema',), ('mysql',), ('performance_schema',), ('sys',), ('testdb',))

    # 2.创建数据库 (新增、删除、修改必须commit)
    # 发送指令
    cursor.execute("create database db3 default charset utf8 collate utf8_general_ci")
    conn.commit()

    # 3.查看数据库
    # 发送指令
    cursor.execute("show databases")
    # 获取指令的结果
    result = cursor.fetchall()
    print(result)  # (('information_schema',), ('db3',), ('mysql',), ('performance_schema',), ('sys',), ('testdb',))

    # 4.删除数据库
    # 发送指令
    cursor.execute("drop database db3")
    conn.commit()
    
    # 3.查看数据库
    # 发送指令
    cursor.execute("show databases")
    # 获取指令的结果
    result = cursor.fetchall()
    print(result)  # (('information_schema',), ('mysql',), ('performance_schema',), ('sys',), ('testdb',))

    # 5. 进入数据库，查看表
    # 发送指令
    cursor.execute("use mysql")
    cursor.execute("show tables")
    result = cursor.fetchall()
    print(result)  # (('columns_priv',), ('db',), ('engine_cost',), ('event',), ('func',), ('general_log',), ...

    cursor.close()
    conn.close()

def modifyDB():
    # 连接MySQL(Socket)
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='', charset="utf8")
    cursor = conn.cursor()

    # 1.创建数据库 (新增、删除、修改必须commit)
    # 发送指令
    # cursor.execute("create database db4test1 default charset utf8 collate utf8_general_ci")
    # conn.commit()

    # # 2.进入数据库，查看数据表
    # cursor.execute("use db4test1")
    # cursor.execute("show tables")
    # result = cursor.fetchall()
    # print(result)

    # 3.进入数据库、查看数据表
    cursor.execute("use db4test")
    sql = """
    create table L4(
    id int not null primary key auto_increment,
    title varchar(128),
    content text,
    ctime datetime
    )default charset=utf8;
    """
    cursor.execute(sql)
    conn.commit() 

    # 4.查看数据库中的表
    cursor.execute("show tables")
    result = cursor.fetchall()
    print(result)

    cursor.close()
    conn.close()

if __name__ == "__main__":
    modifyDB()