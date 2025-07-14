#!/usr/bin/env python3
"""
Python 基础概念演示程序
通过简单例子理解 Python 语法
"""

# 1. 变量和数据类型演示
def demo_variables():
    print("=== 1. 变量和数据类型 ===")
    
    # 整数
    nonce = 0
    print(f"整数变量 nonce = {nonce}, 类型: {type(nonce)}")
    
    # 字符串
    nickname = "cuidaquan"
    print(f"字符串变量 nickname = '{nickname}', 类型: {type(nickname)}")
    
    # 浮点数
    time_spent = 2.3166
    print(f"浮点数变量 time_spent = {time_spent}, 类型: {type(time_spent)}")
    
    # 布尔值
    is_found = True
    print(f"布尔值变量 is_found = {is_found}, 类型: {type(is_found)}")
    
    print()


# 2. 字符串操作演示
def demo_strings():
    print("=== 2. 字符串操作 ===")
    
    # 字符串重复
    zeros = "0" * 4
    print(f"字符串重复: '0' * 4 = '{zeros}'")
    
    # f-字符串格式化
    name = "Python"
    version = 3.13
    message = f"我正在学习 {name} {version}"
    print(f"f-字符串: {message}")
    
    # 字符串方法
    text = "0000abc123"
    print(f"原字符串: '{text}'")
    print(f"是否以'0000'开头: {text.startswith('0000')}")
    print(f"转为大写: '{text.upper()}'")
    print(f"字符串长度: {len(text)}")
    
    print()


# 3. 循环演示
def demo_loops():
    print("=== 3. 循环演示 ===")
    
    # for 循环
    print("for 循环示例:")
    for i in range(5):
        print(f"  循环第 {i+1} 次, i = {i}")
    
    # while 循环
    print("\nwhile 循环示例 (寻找第一个能被7整除的数):")
    number = 1
    while True:
        if number % 7 == 0:
            print(f"  找到了! {number} 能被7整除")
            break
        number += 1
        if number > 20:  # 防止无限循环
            print("  超过20，停止搜索")
            break
    
    print()


# 4. 条件语句演示
def demo_conditions():
    print("=== 4. 条件语句演示 ===")
    
    numbers = [15, 8, 23, 4, 16]
    
    for num in numbers:
        if num > 20:
            result = "大数"
        elif num > 10:
            result = "中数"
        else:
            result = "小数"
        
        print(f"数字 {num} 是 {result}")
    
    print()


# 5. 函数演示
def demo_functions():
    print("=== 5. 函数演示 ===")
    
    # 定义一个简单的函数
    def calculate_square(number):
        """计算数字的平方"""
        return number * number
    
    # 定义一个返回多个值的函数
    def get_info(name, age):
        """返回格式化的信息"""
        message = f"姓名: {name}, 年龄: {age}"
        is_adult = age >= 18
        return message, is_adult
    
    # 调用函数
    result = calculate_square(5)
    print(f"5 的平方是: {result}")
    
    # 多重赋值
    info, adult = get_info("小明", 20)
    print(f"信息: {info}")
    print(f"是否成年: {adult}")
    
    print()


# 6. 模拟简化的POW过程
def simple_pow_demo():
    print("=== 6. 简化的POW演示 ===")
    
    nickname = "test"
    target = "00"  # 寻找以两个零开头的哈希
    
    print(f"寻找 '{nickname}' + 数字 的组合，使其包含 '{target}'")
    
    nonce = 0
    while True:
        # 简化版：不用真正的哈希，只是字符串包含检查
        content = f"{nickname}{nonce}"
        
        # 模拟哈希值（实际应该用 hashlib.sha256）
        fake_hash = f"{target}abc{nonce:04d}"
        
        print(f"  尝试 {nonce}: '{content}' -> 模拟哈希: '{fake_hash}'")
        
        if fake_hash.startswith(target):
            print(f"✅ 找到了! Nonce: {nonce}, 内容: '{content}'")
            break
        
        nonce += 1
        
        if nonce >= 3:  # 限制演示次数
            break
    
    print()


# 7. 错误处理演示
def demo_error_handling():
    print("=== 7. 错误处理演示 ===")
    
    try:
        # 可能出错的代码
        number = int("abc")  # 这会出错
    except ValueError as e:
        print(f"捕获到错误: {e}")
        print("无法将 'abc' 转换为整数")
    
    try:
        result = 10 / 0  # 除零错误
    except ZeroDivisionError:
        print("不能除以零!")
    
    print("程序继续运行...")
    print()


# 主函数
def main():
    print("🐍 Python 基础概念演示")
    print("=" * 50)
    
    # 运行所有演示
    demo_variables()
    demo_strings()
    demo_loops()
    demo_conditions()
    demo_functions()
    simple_pow_demo()
    demo_error_handling()
    
    print("🎉 演示完成! 现在您对Python有了基本了解")


# 程序入口
if __name__ == "__main__":
    main()
