#!/usr/bin/env python3
"""
RSA 非对称加密挑战
1. 生成RSA公钥和私钥对
2. 使用私钥对满足POW 4个零开头哈希值的"昵称+nonce"进行数字签名
3. 使用公钥验证签名
"""

import hashlib
import time
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.exceptions import InvalidSignature


def generate_rsa_keys():
    """
    生成RSA公钥和私钥对
    
    Returns:
        tuple: (private_key, public_key)
    """
    print("🔑 生成RSA密钥对...")
    
    # 生成私钥 (2048位)
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
    )
    
    # 从私钥获取公钥
    public_key = private_key.public_key()
    
    print("✅ RSA密钥对生成成功!")
    return private_key, public_key


def find_pow_4_zeros(nickname):
    """
    寻找满足4个零开头哈希值的昵称+nonce组合
    
    Args:
        nickname (str): 昵称
        
    Returns:
        tuple: (nonce, content, hash_value, time_spent)
    """
    print(f"\n🎯 寻找满足POW 4个零开头的哈希值...")
    print(f"昵称: {nickname}")
    
    target_prefix = "0000"
    nonce = 0
    start_time = time.time()
    
    while True:
        # 构造内容：昵称 + nonce
        content = f"{nickname}{nonce}"
        
        # 计算SHA256哈希
        hash_object = hashlib.sha256(content.encode('utf-8'))
        hash_value = hash_object.hexdigest()
        
        # 检查是否满足条件
        if hash_value.startswith(target_prefix):
            end_time = time.time()
            time_spent = end_time - start_time
            return nonce, content, hash_value, time_spent
        
        nonce += 1
        
        # 每10000次尝试打印一次进度
        if nonce % 10000 == 0:
            print(f"已尝试 {nonce} 次...")


def sign_message(private_key, message):
    """
    使用私钥对消息进行数字签名
    
    Args:
        private_key: RSA私钥
        message (str): 要签名的消息
        
    Returns:
        bytes: 数字签名
    """
    print(f"\n🔏 使用私钥对消息进行签名...")
    print(f"消息: {message}")
    
    # 将消息转换为字节
    message_bytes = message.encode('utf-8')
    
    # 使用私钥签名
    signature = private_key.sign(
        message_bytes,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    
    print("✅ 签名完成!")
    return signature


def verify_signature(public_key, message, signature):
    """
    使用公钥验证数字签名
    
    Args:
        public_key: RSA公钥
        message (str): 原始消息
        signature (bytes): 数字签名
        
    Returns:
        bool: 验证结果
    """
    print(f"\n🔍 使用公钥验证签名...")
    print(f"消息: {message}")
    
    try:
        # 将消息转换为字节
        message_bytes = message.encode('utf-8')
        
        # 使用公钥验证签名
        public_key.verify(
            signature,
            message_bytes,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        
        print("✅ 签名验证成功! 消息完整性和来源已确认")
        return True
        
    except InvalidSignature:
        print("❌ 签名验证失败! 消息可能被篡改或签名无效")
        return False


def save_keys_to_files(private_key, public_key):
    """
    将密钥保存到文件
    
    Args:
        private_key: RSA私钥
        public_key: RSA公钥
    """
    print("\n💾 保存密钥到文件...")
    
    # 序列化私钥
    private_pem = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()
    )
    
    # 序列化公钥
    public_pem = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )
    
    # 保存私钥
    with open('private_key.pem', 'wb') as f:
        f.write(private_pem)
    
    # 保存公钥
    with open('public_key.pem', 'wb') as f:
        f.write(public_pem)
    
    print("✅ 密钥已保存:")
    print("  - private_key.pem (私钥)")
    print("  - public_key.pem (公钥)")


def display_key_info(private_key, public_key):
    """
    显示密钥信息
    
    Args:
        private_key: RSA私钥
        public_key: RSA公钥
    """
    print("\n📋 密钥信息:")
    print(f"密钥长度: {private_key.key_size} 位")
    print(f"公钥指数: {public_key.public_numbers().e}")
    
    # 获取公钥的模数 (n)
    n = public_key.public_numbers().n
    print(f"模数 (n): {hex(n)[:50]}...")


def main():
    """主函数"""
    print("🔐 RSA 非对称加密挑战")
    print("=" * 60)
    
    # 昵称
    nickname = "cuidaquan"
    
    try:
        # 1. 生成RSA密钥对
        private_key, public_key = generate_rsa_keys()
        
        # 显示密钥信息
        display_key_info(private_key, public_key)
        
        # 2. 寻找满足POW 4个零开头的哈希值
        nonce, content, hash_value, time_spent = find_pow_4_zeros(nickname)
        
        print(f"\n✅ 找到满足条件的哈希值!")
        print(f"花费时间: {time_spent:.4f} 秒")
        print(f"内容: {content}")
        print(f"哈希值: {hash_value}")
        print(f"Nonce: {nonce}")
        
        # 3. 使用私钥对内容进行签名
        signature = sign_message(private_key, content)
        
        # 显示签名信息
        print(f"签名长度: {len(signature)} 字节")
        print(f"签名 (hex): {signature.hex()[:100]}...")
        
        # 4. 使用公钥验证签名
        is_valid = verify_signature(public_key, content, signature)
        
        # 5. 保存密钥到文件
        save_keys_to_files(private_key, public_key)
        
        # 总结
        print("\n" + "=" * 60)
        print("🎉 RSA挑战完成总结")
        print("=" * 60)
        print(f"✅ 生成RSA密钥对 ({private_key.key_size}位)")
        print(f"✅ 找到POW内容: {content}")
        print(f"✅ 哈希值: {hash_value}")
        print(f"✅ 数字签名: 完成")
        print(f"✅ 签名验证: {'通过' if is_valid else '失败'}")
        print(f"✅ 密钥文件: 已保存")
        
    except ImportError:
        print("❌ 错误: 缺少 cryptography 库")
        print("请运行: pip install cryptography")
    except Exception as e:
        print(f"❌ 发生错误: {e}")


if __name__ == "__main__":
    main()
