# Python 基础教程 - 以 POW 挑战为例

## 📚 目录
1. [文件结构和注释](#文件结构和注释)
2. [导入模块](#导入模块)
3. [变量和数据类型](#变量和数据类型)
4. [函数定义](#函数定义)
5. [字符串操作](#字符串操作)
6. [循环和条件语句](#循环和条件语句)
7. [函数调用和返回值](#函数调用和返回值)
8. [程序入口](#程序入口)

---

## 1. 文件结构和注释

### Shebang 行
```python
#!/usr/bin/env python3
```
- **作用**: 告诉系统使用 Python3 解释器运行这个文件
- **用法**: 在 Linux/Mac 上可以直接执行 `./pow_challenge.py`

### 文档字符串 (Docstring)
```python
"""
POW Challenge - 工作量证明挑战
寻找以指定数量零开头的SHA256哈希值
"""
```
- **语法**: 三个双引号 `"""` 包围的多行字符串
- **作用**: 描述整个模块的功能
- **特点**: 可以包含中文，支持多行

### 单行注释
```python
# 构造哈希内容：昵称 + nonce
```
- **语法**: `#` 开头
- **作用**: 解释代码的功能

---

## 2. 导入模块

```python
import hashlib
import time
```

### 什么是模块？
- **模块**: Python 的功能包，包含预定义的函数和类
- **hashlib**: 提供各种哈希算法（如 SHA256）
- **time**: 提供时间相关的函数

### 使用方式
```python
hashlib.sha256()  # 调用 hashlib 模块的 sha256 函数
time.time()       # 调用 time 模块的 time 函数
```

---

## 3. 变量和数据类型

### 变量赋值
```python
nonce = 0                    # 整数 (int)
nickname = "cuidaquan"       # 字符串 (str)
start_time = time.time()     # 浮点数 (float)
```

### Python 变量特点
- **动态类型**: 不需要声明变量类型
- **自动推断**: Python 会根据值自动确定类型
- **可重新赋值**: 同一个变量可以赋不同类型的值

### 您选中的代码解释
```python
nonce = 0
```
- **nonce**: 变量名，表示"只使用一次的数字"
- **= 0**: 赋值操作，将整数 0 赋给变量 nonce
- **作用**: 初始化计数器，用于POW计算

---

## 4. 函数定义

### 函数语法
```python
def calculate_pow(nickname, target_zeros):
    """
    计算工作量证明
    
    Args:
        nickname (str): 昵称
        target_zeros (int): 目标零的数量
    
    Returns:
        tuple: (nonce, hash_content, hash_value, time_spent)
    """
```

### 关键要素
- **def**: 定义函数的关键字
- **函数名**: `calculate_pow`
- **参数**: `nickname, target_zeros`
- **冒号**: `:` 表示函数体开始
- **缩进**: Python 用缩进表示代码块（通常4个空格）

### 函数文档字符串
- **Args**: 参数说明
- **Returns**: 返回值说明
- **类型注解**: `(str)`, `(int)` 表示参数类型

---

## 5. 字符串操作

### 字符串重复
```python
target_prefix = "0" * target_zeros
```
- **作用**: 创建指定数量的零字符串
- **示例**: `"0" * 4` 结果是 `"0000"`

### f-字符串 (格式化字符串)
```python
print(f"开始寻找以 {target_zeros} 个零开头的哈希值...")
hash_content = f"{nickname}{nonce}"
```
- **语法**: `f"文本 {变量} 更多文本"`
- **作用**: 将变量值插入字符串中
- **示例**: 如果 `nickname="cuidaquan"`, `nonce=123`，则 `hash_content` 为 `"cuidaquan123"`

### 字符串方法
```python
hash_value.startswith(target_prefix)
hash_content.encode('utf-8')
```
- **startswith()**: 检查字符串是否以指定前缀开头
- **encode()**: 将字符串转换为字节序列

---

## 6. 循环和条件语句

### while 循环
```python
while True:
    # 循环体
    if 条件:
        break  # 跳出循环
```
- **while True**: 无限循环
- **break**: 跳出循环的关键字

### if 条件语句
```python
if hash_value.startswith(target_prefix):
    # 满足条件时执行
    return nonce, hash_content, hash_value, time_spent

if nonce % 10000 == 0:
    # 每10000次执行一次
    print(f"已尝试 {nonce} 次...")
```

### 运算符
- **%**: 取模运算符，`nonce % 10000` 表示 nonce 除以 10000 的余数
- **==**: 相等比较
- **+=**: 自增运算，`nonce += 1` 等同于 `nonce = nonce + 1`

---

## 7. 函数调用和返回值

### 函数调用
```python
nonce1, content1, hash1, time1 = calculate_pow(nickname, 4)
```

### 多重赋值 (元组解包)
- **返回值**: 函数返回一个元组 `(nonce, hash_content, hash_value, time_spent)`
- **解包**: 将元组的4个值分别赋给4个变量
- **优势**: 一次性获取多个返回值

### 数字格式化
```python
print(f"花费时间: {time1:.4f} 秒")
```
- **:.4f**: 格式化浮点数，保留4位小数

---

## 8. 程序入口

### 主程序检查
```python
if __name__ == "__main__":
    main()
```

### 解释
- **__name__**: Python 内置变量
- **"__main__"**: 当直接运行脚本时，`__name__` 的值
- **作用**: 确保只有直接运行脚本时才执行 `main()` 函数
- **好处**: 模块可以被其他程序导入而不自动执行

---

## 🎯 核心概念总结

### 1. Python 的简洁性
```python
# Python
nonce = 0
nonce += 1

# 对比其他语言可能需要：
# int nonce = 0;
# nonce = nonce + 1;
```

### 2. 动态类型
```python
# 同一个变量可以存储不同类型
value = 0        # 整数
value = "hello"  # 字符串
value = [1,2,3]  # 列表
```

### 3. 缩进很重要
```python
if condition:
    print("这行有缩进，属于if块")
    print("这行也有缩进，也属于if块")
print("这行没有缩进，不属于if块")
```

### 4. 一切皆对象
```python
# 字符串是对象，有方法
text = "hello"
text.upper()        # 调用方法
text.startswith("h") # 调用方法

# 甚至数字也是对象
num = 42
num.__add__(8)      # 等同于 num + 8
```

---

## 🚀 实践建议

1. **运行代码**: 尝试修改 `nonce = 0` 为其他值看看效果
2. **添加打印**: 在代码中添加 `print()` 语句观察变量值
3. **修改参数**: 尝试修改昵称或目标零的数量
4. **理解流程**: 跟踪程序执行流程，理解每一步的作用

Python 的哲学是"简单优于复杂"，这个POW程序很好地展示了Python的简洁和强大！
