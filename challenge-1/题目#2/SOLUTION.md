# RSA 非对称加密挑战解决方案

## 挑战描述
练习非对称加密 RSA：
1. 首先生成一对公钥和私钥
2. 使用私钥对满足 POW 4 个零起始哈希值的"昵称+随机数"进行签名
3. 使用公钥进行验证

## 解决方案

### 程序文件
- `rsa_challenge.py` - RSA非对称加密挑战程序
- `private_key.pem` - 生成的RSA私钥文件
- `public_key.pem` - 生成的RSA公钥文件

### 运行结果

使用昵称: `cuidaquan`

#### 1. RSA密钥对生成
- **密钥长度**: 2048 位
- **公钥指数**: 65537
- **算法**: RSA-PSS with SHA256

#### 2. POW 4个零开头哈希值
- **花费时间**: 0.0110 秒
- **内容**: cuidaquan16384
- **哈希值**: 0000bda4d08d1119809f83d8d21a51c69e2b45dcc3ea93934614d89d0b3e5ccd
- **Nonce**: 16384

#### 3. 数字签名
- **签名算法**: RSA-PSS with SHA256
- **签名长度**: 256 字节 (2048位密钥)
- **签名内容**: "cuidaquan16384"
- **签名结果**: 成功

#### 4. 签名验证
- **验证结果**: ✅ 通过
- **消息完整性**: 已确认
- **来源认证**: 已确认

## 如何运行

### 前置要求
```bash
py -m pip install cryptography
```

### 运行程序
```bash
py rsa_challenge.py
```

## 技术实现详解

### 1. RSA密钥生成
```python
private_key = rsa.generate_private_key(
    public_exponent=65537,  # 标准公钥指数
    key_size=2048,         # 2048位密钥长度
)
public_key = private_key.public_key()
```

### 2. POW算法复用
- 复用了题目#1中的POW算法
- 寻找满足4个零开头的哈希值
- 使用相同的昵称"cuidaquan"

### 3. 数字签名 (RSA-PSS)
```python
signature = private_key.sign(
    message_bytes,
    padding.PSS(
        mgf=padding.MGF1(hashes.SHA256()),
        salt_length=padding.PSS.MAX_LENGTH
    ),
    hashes.SHA256()
)
```

### 4. 签名验证
```python
public_key.verify(
    signature,
    message_bytes,
    padding.PSS(
        mgf=padding.MGF1(hashes.SHA256()),
        salt_length=padding.PSS.MAX_LENGTH
    ),
    hashes.SHA256()
)
```

## RSA加密原理

### 非对称加密特点
1. **密钥对**: 公钥和私钥成对出现
2. **公钥加密**: 任何人都可以用公钥加密
3. **私钥解密**: 只有私钥持有者能解密
4. **数字签名**: 私钥签名，公钥验证

### 数字签名流程
1. **签名**: 使用私钥对消息哈希进行签名
2. **验证**: 使用公钥验证签名的有效性
3. **完整性**: 确保消息未被篡改
4. **认证**: 确认消息来源

### 安全性保证
- **2048位密钥**: 提供足够的安全强度
- **RSA-PSS**: 概率签名方案，更安全
- **SHA256**: 安全的哈希算法
- **随机盐值**: 防止签名重放攻击

## 文件说明

### private_key.pem
```
-----BEGIN PRIVATE KEY-----
MIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQCeASk2DWTGrZyb...
-----END PRIVATE KEY-----
```
- PEM格式的RSA私钥
- 用于数字签名
- 需要妥善保管，不能泄露

### public_key.pem
```
-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAngEpNg1kxq2cm4ANuR4V...
-----END PUBLIC KEY-----
```
- PEM格式的RSA公钥
- 用于验证签名
- 可以公开分享

## 实际应用场景

1. **数字证书**: HTTPS、SSL/TLS证书
2. **代码签名**: 软件包、应用程序签名
3. **电子邮件**: PGP/GPG加密和签名
4. **区块链**: 交易签名和验证
5. **身份认证**: SSH密钥、API认证

## 安全注意事项

1. **私钥保护**: 私钥必须安全存储，不能泄露
2. **密钥长度**: 2048位是当前推荐的最小长度
3. **随机数**: 使用安全的随机数生成器
4. **算法选择**: 使用经过验证的加密算法
5. **定期更新**: 定期更换密钥对

## 总结

本挑战成功演示了：
- ✅ RSA密钥对生成
- ✅ POW工作量证明
- ✅ 数字签名创建
- ✅ 签名验证
- ✅ 密钥文件管理

这是现代密码学和区块链技术的基础，为理解更复杂的加密应用奠定了基础。
