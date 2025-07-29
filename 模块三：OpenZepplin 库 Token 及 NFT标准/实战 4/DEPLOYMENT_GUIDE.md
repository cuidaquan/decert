# NFT市场部署指南

## 修复的问题

已修复以下OpenZeppelin兼容性问题：
1. 移除了已弃用的`Counters`库，使用简单的`uint256`计数器
2. 修复了`Ownable`构造函数，添加了必需的`msg.sender`参数

## 部署步骤

### 1. 环境准备

确保您的开发环境支持以下版本：
- Solidity: ^0.8.0
- OpenZeppelin Contracts: ^5.0.0

### 2. 按顺序部署合约

#### 步骤1: 部署ExtendedERC20合约
```solidity
// 构造函数参数
constructor(
    string memory name_,        // "MyToken"
    string memory symbol_,      // "MTK"
    uint256 initialSupply      // 1000000 (将自动乘以10^18)
)
```

#### 步骤2: 部署MyNFT合约
```solidity
// 无需构造参数
constructor() // 自动设置名称为"MyNFT"，符号为"MNFT"
```

#### 步骤3: 部署NFTMarket合约
```solidity
// 构造函数参数
constructor(
    address _paymentToken,  // ExtendedERC20合约地址
    address _nftContract    // MyNFT合约地址
)
```

#### 步骤4: (可选) 部署SimpleDemo合约
```solidity
// 无需构造参数，部署后调用setContractAddresses设置合约地址
constructor()
```

### 3. 初始化设置

#### 3.1 设置SimpleDemo合约地址（如果使用）
```solidity
// 调用SimpleDemo合约的setContractAddresses函数
demo.setContractAddresses(nftAddress, tokenAddress, marketAddress);
```

#### 3.2 铸造测试NFT
```solidity
// 方式1: 直接调用MyNFT合约
nft.mint(recipient, "ipfs://your-metadata-hash");

// 方式2: 通过SimpleDemo合约
demo.mintNFT(recipient, "ipfs://your-metadata-hash");
```

#### 3.3 分发测试代币
```solidity
// 方式1: 直接调用ExtendedERC20合约
token.mint(user, amount);

// 方式2: 通过SimpleDemo合约
demo.mintTokens(user, amount);
```

### 4. 测试市场功能

#### 4.1 上架NFT
```solidity
// 方式1: 直接调用合约
nft.approve(marketAddress, tokenId);
market.list(tokenId, price);

// 方式2: 通过SimpleDemo合约（自动处理授权）
demo.listNFT(tokenId, price);
```

#### 4.2 购买NFT (传统方式)
```solidity
// 方式1: 直接调用合约
token.approve(marketAddress, price);
market.buyNFT(listingId);

// 方式2: 通过SimpleDemo合约（自动处理授权）
demo.buyNFTTraditional(listingId);
```

#### 4.3 购买NFT (Hook方式)
```solidity
// 方式1: 直接调用合约
bytes memory data = abi.encode(listingId);
token.transferWithCallback(marketAddress, price, data);

// 方式2: 通过SimpleDemo合约
demo.buyNFTWithHook(listingId);
```

#### 4.4 查询功能
```solidity
// 查询用户NFT余额
uint256 nftBalance = demo.getUserNFTBalance(userAddress);

// 查询用户代币余额
uint256 tokenBalance = demo.getUserTokenBalance(userAddress);

// 查询上架信息
(address seller, address nftAddr, uint256 tokenId, uint256 price, bool active) =
    demo.getListingInfo(listingId);
```

## 示例元数据上传到IPFS

### 使用Pinata上传

1. 注册Pinata账户: https://pinata.cloud/
2. 上传图片文件，获得图片IPFS哈希
3. 更新JSON元数据文件中的image字段
4. 上传JSON文件，获得元数据IPFS哈希
5. 使用元数据哈希铸造NFT

### 示例IPFS哈希格式
```
图片: ipfs://QmYourImageHashHere
元数据: ipfs://QmYourMetadataHashHere
```

## 合约验证

部署到主网或测试网后，建议验证合约源码：

1. 在区块链浏览器上找到您的合约
2. 点击"Verify and Publish"
3. 上传源码和构造参数
4. 完成验证

## OpenSea集成

NFT部署后会自动在OpenSea上显示，确保：

1. 元数据格式符合OpenSea标准
2. 图片已正确上传到IPFS
3. 合约已在主网部署并验证
4. NFT已成功铸造

## 安全注意事项

1. **测试网测试**: 先在测试网充分测试所有功能
2. **权限管理**: 确保只有授权用户可以铸造NFT
3. **手续费设置**: 合理设置市场手续费率
4. **代码审计**: 主网部署前进行代码审计
5. **升级计划**: 考虑合约升级和维护计划

## 故障排除

### 常见错误及解决方案

1. **"Counters not found"**
   - 已修复：使用uint256计数器替代

2. **"Ownable constructor error"**
   - 已修复：添加msg.sender参数

3. **"NFT transfer failed"**
   - 检查NFT授权状态
   - 确认NFT所有权

4. **"Token transfer failed"**
   - 检查代币余额和授权
   - 确认合约地址正确

## 联系支持

如遇到问题，请检查：
1. 合约地址是否正确
2. 交易gas费是否足够
3. 网络连接是否正常
4. 钱包是否正确连接
