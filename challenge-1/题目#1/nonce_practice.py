#!/usr/bin/env python3
"""
Nonce 练习程序 - 理解 nonce 的作用
"""

def simple_nonce_demo():
    """简单的 nonce 演示"""
    print("=== Nonce 的作用演示 ===")
    
    nickname = "test"
    nonce = 0  # 从0开始
    
    print(f"昵称: {nickname}")
    print("让我们看看不同的 nonce 值会产生什么:")
    
    # 演示前5个nonce值
    for i in range(5):
        content = f"{nickname}{nonce}"
        print(f"  nonce = {nonce:2d} -> 内容: '{content}'")
        nonce += 1  # 递增
    
    print()

def find_special_number():
    """寻找特殊数字的演示"""
    print("=== 寻找特殊数字 ===")
    print("目标: 找到一个数字，使得 'hello' + 数字 的长度等于 8")
    
    word = "hello"  # 长度为5
    nonce = 0
    target_length = 8
    
    while True:
        content = f"{word}{nonce}"
        current_length = len(content)
        
        print(f"  尝试 nonce={nonce}: '{content}' (长度: {current_length})")
        
        if current_length == target_length:
            print(f"✅ 找到了! nonce={nonce}, 内容='{content}'")
            break
        
        nonce += 1
        
        if nonce > 1000:  # 防止无限循环
            print("❌ 超过1000次尝试，停止")
            break
    
    print()

def understand_pow_concept():
    """理解POW概念"""
    print("=== 理解POW工作量证明概念 ===")
    print("目标: 找到一个数字，使得组合后的字符串包含'00'")
    
    name = "pow"
    nonce = 0
    target = "00"
    
    while True:
        content = f"{name}{nonce}"
        
        # 简化版检查（实际POW用哈希）
        contains_target = target in content
        
        print(f"  nonce={nonce:3d}: '{content}' -> 包含'{target}': {contains_target}")
        
        if contains_target:
            print(f"✅ 成功! 找到包含'{target}'的组合")
            break
        
        nonce += 1
        
        if nonce > 20:  # 限制演示
            print("演示结束")
            break
    
    print()

def variable_types_demo():
    """变量类型演示"""
    print("=== Python 变量类型演示 ===")
    
    # 不同类型的变量
    nonce = 0                    # 整数
    nickname = "python"          # 字符串
    time_spent = 1.23           # 浮点数
    is_found = False            # 布尔值
    results = [1, 2, 3]         # 列表
    
    variables = [
        ("nonce", nonce),
        ("nickname", nickname), 
        ("time_spent", time_spent),
        ("is_found", is_found),
        ("results", results)
    ]
    
    for name, value in variables:
        print(f"  {name:12} = {str(value):15} (类型: {type(value).__name__})")
    
    print()
    
    # 演示变量可以改变类型
    print("Python 变量可以改变类型:")
    x = 42
    print(f"  x = {x} (类型: {type(x).__name__})")
    
    x = "现在是字符串"
    print(f"  x = '{x}' (类型: {type(x).__name__})")
    
    x = [1, 2, 3]
    print(f"  x = {x} (类型: {type(x).__name__})")
    
    print()

def main():
    print("🎓 Nonce 和 Python 基础练习")
    print("=" * 50)
    
    simple_nonce_demo()
    find_special_number()
    understand_pow_concept()
    variable_types_demo()
    
    print("🎉 练习完成!")
    print("\n💡 关键要点:")
    print("1. nonce = 0 是初始化一个计数器")
    print("2. Python 变量不需要声明类型")
    print("3. 缩进决定代码块的范围")
    print("4. f-字符串让字符串格式化变得简单")
    print("5. while 循环可以重复执行直到满足条件")

if __name__ == "__main__":
    main()
