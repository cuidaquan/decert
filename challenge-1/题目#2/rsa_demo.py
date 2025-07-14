#!/usr/bin/env python3
"""
RSA 加密演示程序
简化版本，帮助理解RSA的基本概念
"""

from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes, serialization


def simple_rsa_demo():
    """简单的RSA加密解密演示"""
    print("=== RSA 加密解密演示 ===")
    
    # 生成密钥对
    print("1. 生成RSA密钥对...")
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
    )
    public_key = private_key.public_key()
    print("✅ 密钥对生成完成")
    
    # 要加密的消息
    message = "Hello RSA!"
    print(f"\n2. 原始消息: '{message}'")
    
    # 使用公钥加密
    print("3. 使用公钥加密...")
    encrypted = public_key.encrypt(
        message.encode('utf-8'),
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    print(f"✅ 加密完成，密文长度: {len(encrypted)} 字节")
    print(f"密文 (hex): {encrypted.hex()[:50]}...")
    
    # 使用私钥解密
    print("\n4. 使用私钥解密...")
    decrypted = private_key.decrypt(
        encrypted,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    decrypted_message = decrypted.decode('utf-8')
    print(f"✅ 解密完成: '{decrypted_message}'")
    
    # 验证
    if message == decrypted_message:
        print("🎉 加密解密成功!")
    else:
        print("❌ 加密解密失败!")
    
    print()


def signature_demo():
    """数字签名演示"""
    print("=== 数字签名演示 ===")
    
    # 生成密钥对
    print("1. 生成RSA密钥对...")
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
    )
    public_key = private_key.public_key()
    
    # 要签名的消息
    message = "这是一个重要的消息"
    print(f"\n2. 消息: '{message}'")
    
    # 使用私钥签名
    print("3. 使用私钥签名...")
    signature = private_key.sign(
        message.encode('utf-8'),
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    print(f"✅ 签名完成，签名长度: {len(signature)} 字节")
    
    # 使用公钥验证
    print("4. 使用公钥验证签名...")
    try:
        public_key.verify(
            signature,
            message.encode('utf-8'),
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        print("✅ 签名验证成功!")
    except:
        print("❌ 签名验证失败!")
    
    # 测试篡改检测
    print("\n5. 测试消息篡改检测...")
    tampered_message = "这是一个被篡改的消息"
    print(f"篡改后的消息: '{tampered_message}'")
    
    try:
        public_key.verify(
            signature,
            tampered_message.encode('utf-8'),
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        print("❌ 这不应该发生!")
    except:
        print("✅ 成功检测到消息篡改!")
    
    print()


def key_format_demo():
    """密钥格式演示"""
    print("=== 密钥格式演示 ===")
    
    # 生成密钥对
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=1024,  # 使用较小的密钥便于演示
    )
    public_key = private_key.public_key()
    
    # 显示密钥信息
    print("1. 密钥信息:")
    print(f"   密钥长度: {private_key.key_size} 位")
    print(f"   公钥指数: {public_key.public_numbers().e}")
    
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
    
    print("\n2. 私钥 (PEM格式):")
    print(private_pem.decode('utf-8')[:200] + "...")
    
    print("\n3. 公钥 (PEM格式):")
    print(public_pem.decode('utf-8'))
    
    print()


def rsa_vs_symmetric_demo():
    """RSA vs 对称加密对比"""
    print("=== RSA vs 对称加密对比 ===")
    
    print("📊 对比表:")
    print("┌─────────────┬─────────────┬─────────────┐")
    print("│    特性     │     RSA     │  对称加密   │")
    print("├─────────────┼─────────────┼─────────────┤")
    print("│   密钥数量  │   一对(2个) │   一个(1个) │")
    print("│   加密速度  │     慢      │     快      │")
    print("│   密钥分发  │     安全    │   需要协商  │")
    print("│   数字签名  │    支持     │   不支持    │")
    print("│   适用场景  │ 密钥交换/签名│  大量数据   │")
    print("└─────────────┴─────────────┴─────────────┘")
    
    print("\n💡 实际应用中的组合:")
    print("1. 使用RSA交换对称密钥")
    print("2. 使用对称加密处理大量数据")
    print("3. 使用RSA进行数字签名")
    print("4. 这样既保证了安全性又提高了效率")
    
    print()


def main():
    """主函数"""
    print("🔐 RSA 加密技术演示")
    print("=" * 50)
    
    try:
        simple_rsa_demo()
        signature_demo()
        key_format_demo()
        rsa_vs_symmetric_demo()
        
        print("🎓 学习要点:")
        print("1. RSA是非对称加密算法")
        print("2. 公钥加密，私钥解密")
        print("3. 私钥签名，公钥验证")
        print("4. 适合密钥交换和数字签名")
        print("5. 不适合加密大量数据")
        
    except ImportError:
        print("❌ 错误: 缺少 cryptography 库")
        print("请运行: pip install cryptography")
    except Exception as e:
        print(f"❌ 发生错误: {e}")


if __name__ == "__main__":
    main()
