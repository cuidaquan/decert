# NFT市场部署指南

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
参数：MyToken,MTK,1000000
交易Hash：0x1d2a29bc7846d62170f53bf76bb13307e9b4a90c317c4aec33e90da36eb5c7c0
合约地址：0xbf2a074c014d847ae838191b3e957826851c74ec

#### 步骤2: 部署MyNFT合约
```solidity
// 无需构造参数
constructor() // 自动设置名称为"MyNFT"，符号为"MNFT"
```
参数：无
交易Hash：0xabc38a149beb2ca2d93b94b8db6f55bc7cfc8b630431fd7e56050047382c510e
合约地址：0x08dcaa6de0ca584b8c5d810b027afe23d31c4af1

#### 步骤3: 部署NFTMarket合约
```solidity
// 构造函数参数
constructor(
    address _paymentToken,  // ExtendedERC20合约地址
    address _nftContract    // MyNFT合约地址
)
```
参数：0xbf2a074c014d847ae838191b3e957826851c74ec,0x08dcaa6de0ca584b8c5d810b027afe23d31c4af1
交易Hash：0x85ede19fe3a03aa72912528b7f8af867c1a44ac3d8e928faecc1cc020d3a491f
合约地址：0x9d206682e9837b02479a5010ed312045eaeacdb2

### 3. 初始化设置

#### 3.1 铸造测试NFT
```solidity
// 调用MyNFT合约
nft.mint(recipient, "ipfs://your-metadata-hash");
```
Crypto Dragon #1
参数：0x6cc3Aac8a7d769B5fe464b406849392539f22bf5,ipfs://bafkreigtxcgvvvrjh6sf22h4mfc3kd37egckxcs3xbuayovwyg4c4ylpca
交易Hash：0x60bb035bea942fbfd194cc839ede82292f3d77fdf43657da36842491a52ca2f8
链接：https://sepolia.etherscan.io/nft/0x08dcaa6de0ca584b8c5d810b027afe23d31c4af1/1

Cyber Phoenix #2
参数：0x6cc3Aac8a7d769B5fe464b406849392539f22bf5,ipfs://bafkreiff7ddr6yq5qyc5ckt6dopnxeurgbie4hkjeljwih22kwlogplo54
交易Hash：0x2287e7b0e19f813a7977410f9eab03c409c26d6d0823f7dcc21348f79b05a611
链接：https://sepolia.etherscan.io/nft/0x08dcaa6de0ca584b8c5d810b027afe23d31c4af1/4

Mystic Unicorn #3
参数：0x6cc3Aac8a7d769B5fe464b406849392539f22bf5,ipfs://bafkreidatrllynxmvvvrw6yu5o74i5fddpaucrhknf2e6rzhe4icu4qemm
交易Hash：0xa1030459f319417dc7d97ff66961ff4e54943c460623bf65339c011de1b69d2e
链接：https://sepolia.etherscan.io/nft/0x08dcaa6de0ca584b8c5d810b027afe23d31c4af1/5


#### 3.2 分发测试代币
```solidity
// 调用ExtendedERC20合约
token.mint(user, amount);
```
参数：0x3dd6ba106b13cb6538a9ed9fe1a51e115f9ee664,100000000000000000000
交易Hash：0x524052eb01ce5bae721e245dc583cbc3d57da4cd1b6b56e2770122b62a1870f6


### 4. 测试市场功能

#### 4.1 上架NFT
```solidity
nft.approve(marketAddress, tokenId);
market.list(tokenId, price);
```
用户：0x6cc3Aac8a7d769B5fe464b406849392539f22bf5
参数：0x9d206682e9837b02479a5010ed312045eaeacdb2,1
交易Hash：0x1c269f293fac0c589d96396feb35a576d63cb644d13459df590f8b474a56f5b4

用户：0x6cc3Aac8a7d769B5fe464b406849392539f22bf5
参数：1,3000000000000000000
交易Hash：0xa8234b6ef3671de108bea4b4b1178aec8e3ede18047ea4f77e73b4a680454428

用户：0x6cc3Aac8a7d769B5fe464b406849392539f22bf5
参数：0x9d206682e9837b02479a5010ed312045eaeacdb2,4
交易Hash：0x275a7be79b25543de9fc4c3bb64699fe32b9ced1fda300e67e843e81b51f9194

用户：0x6cc3Aac8a7d769B5fe464b406849392539f22bf5
参数：4,7000000000000000000
交易Hash：0x6645ea2bc993e77009b770133294d7f140dd4b10b5d25e50d6ae6f312d2a4fa9

#### 4.2 购买NFT (传统方式)
```solidity
token.approve(marketAddress, price);
market.buyNFT(listingId);
```
用户：0x3dd6ba106b13cb6538a9ed9fe1a51e115f9ee664
参数：0x9d206682e9837b02479a5010ed312045eaeacdb2,3000000000000000000
交易Hash：0xd2504d7f66cd5e2ffc3fe51730f995c64e9a6385e7256e21d81662b12204660a

用户：0x3dd6ba106b13cb6538a9ed9fe1a51e115f9ee664
参数：1
交易Hash：0xacd7855f17730d303c78c79a12a947f796b6adb1d99dff842adfcb3fa6c5f07e

#### 4.3 购买NFT (Hook方式)
```solidity
bytes memory data = abi.encode(listingId);
token.transferWithCallback(marketAddress, price, data);
```
用户：0x3dd6ba106b13cb6538a9ed9fe1a51e115f9ee664
参数：0x9d206682e9837b02479a5010ed312045eaeacdb2,7000000000000000000,0x0000000000000000000000000000000000000000000000000000000000000002
交易Hash：0x5512339c04a4339e11e02983e4e5ef5366cce14c4acee7349465ba7edcc70719

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