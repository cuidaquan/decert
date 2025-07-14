#!/usr/bin/env python3
"""
Python 高级概念实践程序
基于 rsa_challenge.py 的概念演示
"""

import hashlib
import time
import json
from pathlib import Path


# 1. 异常处理演示
class CustomError(Exception):
    """自定义异常类"""
    def __init__(self, message, error_code=None):
        super().__init__(message)
        self.error_code = error_code


def exception_handling_demo():
    """异常处理演示"""
    print("=== 异常处理演示 ===")
    
    # 演示不同类型的异常
    test_cases = [
        ("正常情况", lambda: 10 / 2),
        ("除零错误", lambda: 10 / 0),
        ("类型错误", lambda: "hello" + 5),
        ("自定义错误", lambda: raise_custom_error()),
    ]
    
    for name, func in test_cases:
        print(f"\n测试: {name}")
        try:
            result = func()
            print(f"✅ 结果: {result}")
        except ZeroDivisionError:
            print("❌ 捕获到除零错误")
        except TypeError as e:
            print(f"❌ 捕获到类型错误: {e}")
        except CustomError as e:
            print(f"❌ 捕获到自定义错误: {e} (错误码: {e.error_code})")
        except Exception as e:
            print(f"❌ 捕获到其他错误: {e}")
        finally:
            print("🔄 finally 块总是执行")
    
    print()


def raise_custom_error():
    """抛出自定义错误"""
    raise CustomError("这是一个自定义错误", error_code=1001)


# 2. 文件操作和上下文管理器演示
def file_operations_demo():
    """文件操作演示"""
    print("=== 文件操作演示 ===")
    
    # 创建测试数据
    test_data = {
        "name": "Python学习者",
        "level": "高级",
        "topics": ["异常处理", "文件操作", "上下文管理器"]
    }
    
    filename = "test_data.json"
    
    try:
        # 写入文件 (使用 with 语句)
        print("1. 写入JSON文件...")
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(test_data, f, ensure_ascii=False, indent=2)
        print("✅ 文件写入成功")
        
        # 读取文件
        print("\n2. 读取JSON文件...")
        with open(filename, 'r', encoding='utf-8') as f:
            loaded_data = json.load(f)
        print(f"✅ 读取成功: {loaded_data}")
        
        # 演示二进制文件操作
        print("\n3. 二进制文件操作...")
        binary_data = "Hello Python!".encode('utf-8')
        
        with open("test_binary.bin", 'wb') as f:
            f.write(binary_data)
        
        with open("test_binary.bin", 'rb') as f:
            read_binary = f.read()
            decoded_text = read_binary.decode('utf-8')
        
        print(f"✅ 二进制读写成功: {decoded_text}")
        
        # 使用 pathlib (现代文件路径处理)
        print("\n4. 使用 pathlib...")
        file_path = Path(filename)
        print(f"文件存在: {file_path.exists()}")
        print(f"文件大小: {file_path.stat().st_size} 字节")
        print(f"文件后缀: {file_path.suffix}")
        
    except FileNotFoundError:
        print("❌ 文件未找到")
    except PermissionError:
        print("❌ 权限不足")
    except Exception as e:
        print(f"❌ 文件操作错误: {e}")
    finally:
        # 清理测试文件
        for test_file in [filename, "test_binary.bin"]:
            try:
                Path(test_file).unlink(missing_ok=True)
            except:
                pass
    
    print()


# 3. 对象方法和属性演示
class HashCalculator:
    """哈希计算器类 - 演示面向对象概念"""
    
    def __init__(self, algorithm='sha256'):
        """初始化方法"""
        self.algorithm = algorithm
        self.history = []
    
    def calculate_hash(self, data):
        """计算哈希值"""
        if isinstance(data, str):
            data = data.encode('utf-8')
        
        if self.algorithm == 'sha256':
            hash_obj = hashlib.sha256(data)
        elif self.algorithm == 'md5':
            hash_obj = hashlib.md5(data)
        else:
            raise ValueError(f"不支持的算法: {self.algorithm}")
        
        result = hash_obj.hexdigest()
        
        # 记录历史
        self.history.append({
            'data': data.decode('utf-8') if isinstance(data, bytes) else str(data),
            'hash': result,
            'timestamp': time.time()
        })
        
        return result
    
    def get_history(self):
        """获取计算历史"""
        return self.history.copy()
    
    def clear_history(self):
        """清空历史"""
        self.history.clear()
    
    @property
    def history_count(self):
        """历史记录数量 (属性装饰器)"""
        return len(self.history)
    
    @staticmethod
    def supported_algorithms():
        """支持的算法列表 (静态方法)"""
        return ['sha256', 'md5']
    
    @classmethod
    def create_sha256_calculator(cls):
        """创建SHA256计算器 (类方法)"""
        return cls('sha256')
    
    def __str__(self):
        """字符串表示"""
        return f"HashCalculator(algorithm={self.algorithm}, history={self.history_count})"


def object_methods_demo():
    """对象方法演示"""
    print("=== 对象方法演示 ===")
    
    # 创建对象实例
    calc = HashCalculator('sha256')
    print(f"1. 创建计算器: {calc}")
    
    # 调用实例方法
    test_data = ["hello", "world", "python"]
    for data in test_data:
        hash_value = calc.calculate_hash(data)
        print(f"   '{data}' -> {hash_value[:16]}...")
    
    # 使用属性
    print(f"\n2. 历史记录数量: {calc.history_count}")
    
    # 使用静态方法
    print(f"3. 支持的算法: {HashCalculator.supported_algorithms()}")
    
    # 使用类方法
    calc2 = HashCalculator.create_sha256_calculator()
    print(f"4. 通过类方法创建: {calc2}")
    
    # 方法链式调用演示
    result = (HashCalculator('md5')
              .calculate_hash("test")
              [:8])  # 取前8个字符
    print(f"5. 链式调用结果: {result}")
    
    print()


# 4. 函数参数和返回值演示
def advanced_function_demo():
    """高级函数概念演示"""
    print("=== 高级函数概念演示 ===")
    
    # 演示不同类型的参数
    def flexible_function(pos_arg, *args, **kwargs):
        """演示灵活的参数处理"""
        print(f"位置参数: {pos_arg}")
        print(f"可变位置参数: {args}")
        print(f"关键字参数: {kwargs}")
        return len(args) + len(kwargs)
    
    print("1. 灵活参数函数:")
    result = flexible_function("必需参数", "额外1", "额外2", name="张三", age=25)
    print(f"返回值: {result}\n")
    
    # 演示函数返回多个值
    def calculate_stats(numbers):
        """计算统计信息 - 返回多个值"""
        if not numbers:
            return 0, 0, 0, 0
        
        total = sum(numbers)
        count = len(numbers)
        average = total / count
        maximum = max(numbers)
        
        return total, count, average, maximum
    
    print("2. 多返回值函数:")
    data = [1, 2, 3, 4, 5]
    total, count, avg, max_val = calculate_stats(data)
    print(f"数据: {data}")
    print(f"总和: {total}, 数量: {count}, 平均: {avg:.2f}, 最大: {max_val}")
    
    # 演示默认参数和关键字参数
    def format_message(message, prefix="INFO", timestamp=None, uppercase=False):
        """格式化消息"""
        if timestamp is None:
            timestamp = time.time()
        
        formatted_time = time.strftime("%H:%M:%S", time.localtime(timestamp))
        result = f"[{formatted_time}] {prefix}: {message}"
        
        return result.upper() if uppercase else result
    
    print("\n3. 默认参数和关键字参数:")
    print(format_message("普通消息"))
    print(format_message("错误消息", prefix="ERROR"))
    print(format_message("重要消息", prefix="WARN", uppercase=True))
    
    print()


# 5. 字符串和字节处理演示
def string_bytes_demo():
    """字符串和字节处理演示"""
    print("=== 字符串和字节处理演示 ===")
    
    # 字符串编码
    original = "Python编程 🐍"
    print(f"1. 原始字符串: '{original}'")
    
    # 不同编码方式
    encodings = ['utf-8', 'utf-16', 'ascii']
    for encoding in encodings:
        try:
            encoded = original.encode(encoding)
            decoded = encoded.decode(encoding)
            print(f"   {encoding}: {len(encoded)} 字节, 解码: '{decoded}'")
        except UnicodeEncodeError:
            print(f"   {encoding}: ❌ 编码失败")
    
    # 十六进制表示
    utf8_bytes = original.encode('utf-8')
    hex_string = utf8_bytes.hex()
    print(f"\n2. 十六进制表示: {hex_string}")
    print(f"   从十六进制恢复: '{bytes.fromhex(hex_string).decode('utf-8')}'")
    
    # 字符串格式化的高级用法
    data = {"name": "Alice", "score": 95.678, "rank": 1}
    print(f"\n3. 高级字符串格式化:")
    print(f"   基本: {data['name']} 得分 {data['score']}")
    print(f"   格式化: {data['name']} 得分 {data['score']:.2f}")
    print(f"   对齐: {data['name']:>10} 排名 {data['rank']:03d}")
    
    # 条件表达式在字符串中的使用
    status = "优秀" if data['score'] >= 90 else "良好" if data['score'] >= 80 else "一般"
    print(f"   条件: {data['name']} 评级 {status}")
    
    print()


def main():
    """主函数 - 演示所有概念"""
    print("🐍 Python 高级概念实践")
    print("=" * 50)
    
    try:
        exception_handling_demo()
        file_operations_demo()
        object_methods_demo()
        advanced_function_demo()
        string_bytes_demo()
        
        print("🎓 学习总结:")
        print("1. 异常处理让程序更稳定")
        print("2. with 语句确保资源正确释放")
        print("3. 面向对象提供了代码组织方式")
        print("4. 函数参数提供了灵活性")
        print("5. 字符串和字节的转换很重要")
        print("6. 这些概念在 rsa_challenge.py 中都有体现")
        
    except Exception as e:
        print(f"❌ 程序执行错误: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()
