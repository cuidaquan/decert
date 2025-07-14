#!/usr/bin/env python3
"""
POW Challenge - 工作量证明挑战
寻找以指定数量零开头的SHA256哈希值
"""

import hashlib
import time


def calculate_pow(nickname, target_zeros):
    """
    计算工作量证明
    
    Args:
        nickname (str): 昵称
        target_zeros (int): 目标零的数量
    
    Returns:
        tuple: (nonce, hash_content, hash_value, time_spent)
    """
    target_prefix = "0" * target_zeros
    nonce = 0
    start_time = time.time()
    
    print(f"\n开始寻找以 {target_zeros} 个零开头的哈希值...")
    print(f"目标前缀: {target_prefix}")
    
    while True:
        # 构造哈希内容：昵称 + nonce
        hash_content = f"{nickname}{nonce}"
        
        # 计算SHA256哈希
        hash_object = hashlib.sha256(hash_content.encode('utf-8'))
        hash_value = hash_object.hexdigest()
        
        # 检查是否满足条件
        if hash_value.startswith(target_prefix):
            end_time = time.time()
            time_spent = end_time - start_time
            return nonce, hash_content, hash_value, time_spent
        
        nonce += 1
        
        # 每10000次尝试打印一次进度
        if nonce % 10000 == 0:
            print(f"已尝试 {nonce} 次...")


def main():
    # 使用昵称 (可以根据需要修改)
    nickname = "cuidaquan"
    
    print("=" * 60)
    print("POW 工作量证明挑战")
    print("=" * 60)
    print(f"使用昵称: {nickname}")
    
    # 挑战1: 寻找以4个零开头的哈希值
    print("\n🎯 挑战1: 寻找以4个零开头的哈希值")
    nonce1, content1, hash1, time1 = calculate_pow(nickname, 4)
    
    print("\n✅ 找到满足条件的哈希值!")
    print(f"花费时间: {time1:.4f} 秒")
    print(f"哈希内容: {content1}")
    print(f"哈希值: {hash1}")
    print(f"Nonce: {nonce1}")
    
    # 挑战2: 寻找以5个零开头的哈希值
    print("\n🎯 挑战2: 寻找以5个零开头的哈希值")
    nonce2, content2, hash2, time2 = calculate_pow(nickname, 5)
    
    print("\n✅ 找到满足条件的哈希值!")
    print(f"花费时间: {time2:.4f} 秒")
    print(f"哈希内容: {content2}")
    print(f"哈希值: {hash2}")
    print(f"Nonce: {nonce2}")
    
    # 总结
    print("\n" + "=" * 60)
    print("挑战完成总结")
    print("=" * 60)
    print(f"4个零挑战 - 时间: {time1:.4f}秒, Nonce: {nonce1}")
    print(f"5个零挑战 - 时间: {time2:.4f}秒, Nonce: {nonce2}")
    print(f"总耗时: {time1 + time2:.4f}秒")


if __name__ == "__main__":
    main()
