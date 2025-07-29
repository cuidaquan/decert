# NFT市场实现文档

## 项目概述

本项目实现了一个完整的NFT市场系统，包含以下核心组件：

1. **MyNFT.sol** - ERC721标准的NFT合约
2. **ExtendedERC20.sol** - 支持hook功能的扩展ERC20代币合约
3. **NFTMarket.sol** - NFT市场合约，支持代币买卖NFT
4. **DeployAndDemo.sol** - 部署和演示合约

## 合约功能详解

### 1. MyNFT合约 (ERC721)

**主要功能：**
- 基于OpenZeppelin的ERC721实现
- 支持NFT铸造功能
- 提供NFT查询功能

**核心方法：**
```solidity
function mint(address to, string memory tokenURI) public onlyOwner returns (uint256)
function getTokensByOwner(address owner) public view returns (uint256[] memory)
```

### 2. ExtendedERC20合约

**主要功能：**
- 基于OpenZeppelin的ERC20实现
- 添加了`transferWithCallback`功能
- 支持hook机制，可在转账时调用接收方的回调函数

**核心方法：**
```solidity
function transferWithCallback(address to, uint256 amount, bytes calldata data) external returns (bool)
function transferWithCallback(address to, uint256 amount) external returns (bool)
```

### 3. NFTMarket合约

**主要功能：**
- NFT上架和下架
- 传统购买方式（approve + buyNFT）
- Hook购买方式（transferWithCallback）
- 市场手续费机制
- 防重入攻击保护

**核心方法：**
```solidity
function list(uint256 tokenId, uint256 price) external nonReentrant
function buyNFT(uint256 listingId) external nonReentrant
function tokensReceived(address from, uint256 amount, bytes calldata data) external override returns (bool)
function delist(uint256 listingId) external nonReentrant
```

## 使用流程

### 部署合约

1. 部署ExtendedERC20合约
2. 部署MyNFT合约
3. 部署NFTMarket合约（传入ERC20和NFT合约地址）

### 铸造NFT

```solidity
// 铸造单个NFT
uint256 tokenId = nftContract.mint(recipient, "ipfs://your-metadata-hash");

// 批量铸造NFT
string[] memory uris = ["ipfs://hash1", "ipfs://hash2", "ipfs://hash3"];
uint256[] memory tokenIds = nftContract.batchMint(recipient, uris);
```

### 上架NFT

```solidity
// 1. 授权市场合约转移NFT
nftContract.approve(marketAddress, tokenId);

// 2. 上架NFT
marketContract.list(tokenId, price);
```

### 购买NFT

**方式1：传统购买**
```solidity
// 1. 授权市场合约转移代币
tokenContract.approve(marketAddress, price);

// 2. 购买NFT
marketContract.buyNFT(listingId);
```

**方式2：Hook购买**
```solidity
// 使用transferWithCallback直接购买
bytes memory data = abi.encode(listingId);
tokenContract.transferWithCallback(marketAddress, price, data);
```

## NFT元数据结构

NFT元数据遵循OpenSea标准，包含以下字段：

```json
{
  "name": "NFT名称",
  "description": "NFT描述",
  "image": "ipfs://图片哈希",
  "external_url": "外部链接",
  "attributes": [
    {
      "trait_type": "属性类型",
      "value": "属性值"
    }
  ],
  "properties": {
    "category": "分类",
    "creator": "创作者",
    "generation": 1
  }
}
```

## 上传到IPFS的步骤

### 1. 准备图片和元数据
- 创建NFT图片文件
- 创建对应的JSON元数据文件

### 2. 上传到IPFS
可以使用以下服务：
- **Pinata** (https://pinata.cloud/)
- **Infura IPFS** (https://infura.io/product/ipfs)
- **NFT.Storage** (https://nft.storage/)

### 3. 更新元数据
将IPFS哈希更新到JSON文件的image字段中

### 4. 铸造NFT
使用最终的元数据IPFS哈希铸造NFT

## 安全特性

1. **重入攻击防护** - 使用OpenZeppelin的ReentrancyGuard
2. **权限控制** - 使用Ownable进行权限管理
3. **输入验证** - 对所有输入参数进行验证
4. **安全转账** - 使用safeTransferFrom进行NFT转移
5. **手续费机制** - 内置市场手续费，防止恶意操作

## 测试建议

1. 部署到测试网（如Goerli、Sepolia）
2. 铸造测试NFT
3. 测试上架功能
4. 测试两种购买方式
5. 测试下架功能
6. 验证手续费计算

## OpenSea集成

部署到主网后，NFT会自动在OpenSea上显示。确保：
1. 元数据格式正确
2. 图片已上传到IPFS
3. 合约已验证
4. 设置合约的collection信息

## 注意事项

1. 确保所有依赖的OpenZeppelin合约版本兼容
2. 在主网部署前充分测试
3. 考虑gas优化
4. 设置合理的市场手续费率
5. 定期更新合约以修复潜在问题
