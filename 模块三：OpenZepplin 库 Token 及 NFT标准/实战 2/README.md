Solidity 编写 TokenBank

题目#1
编写一个 TokenBank 合约，可以将自己的 Token 存入到 TokenBank， 和从 TokenBank 取出。

TokenBank 有两个方法：

deposit() : 需要记录每个地址的存入数量；
withdraw（）: 用户可以提取自己的之前存入的 token。
在回答框内输入你的代码或者 github 链接



扩展 ERC20 加入Hook，并使用 Hook：
https://decert.me/quests/4df553df-fbab-49c8-a05f-83256432c6af
https://learnblockchain.cn/article/3074
```sol
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/master/contracts/token/ERC20/SafeERC20.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/master/contracts/token/ERC20/IERC20.sol";

contract TestContract {
    using SafeERC20 for IERC20;

    function safeInteractWithToken(uint256 sendAmount) external {
        IERC20 token = IERC20(address(this));
        token.safeTransferFrom(msg.sender, address(this), sendAmount);
    }
}
```
https://learnblockchain.cn/2019/09/27/erc777
https://learnblockchain.cn/article/8549
```sol
pragma solidity ^0.8.20;

import "@openzeppelin/contracts/interfaces/IERC1363Receiver.sol";
import "@openzeppelin/contracts/interfaces/IERC1363.sol";

contract TokenReceiver is IERC1363Receiver {
	address internal erc1363Token;

	constructor(address erc1363Token_) {
		erc1363Token = erc1363Token_;
	}

	mapping(address user => uint256 balance) public balances;

	function onTransferReceived(
		address operator,
		address from,
		uint256 value,
		bytes calldata data
	) external returns (bytes4) {
		
		require(msg.sender == erc1363Token, "not the expected token");
		balances[from] += value;
		return this.onTransferReceived.selector;
	}

	function withdraw(uint256 value) external {
		require(balances[msg.sender] >= value, "balance too low");
		balances[msg.sender] -= value;
	
		IERC1363(erc1363Token).transfer(msg.sender, value);
	}

}
``

扩展 ERC20 加入Hook，并使用 Hook

题目#1
扩展 ERC20 合约 ，添加一个有hook 功能的转账函数，如函数名为：transferWithCallback ，在转账时，如果目标地址是合约地址的话，调用目标地址的 tokensReceived() 方法。

继承 TokenBank 编写 TokenBankV2，支持存入扩展的 ERC20 Token，用户可以直接调用 transferWithCallback 将 扩展的 ERC20 Token 存入到 TokenBankV2 中。

（备注：TokenBankV2 需要实现 tokensReceived 来实现存款记录工作）

请贴出代码库链接