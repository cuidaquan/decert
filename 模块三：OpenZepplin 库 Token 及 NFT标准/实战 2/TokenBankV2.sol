// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "./BaseERC20.sol";
import "./TokenBank.sol";

/**
 * @title ITokenReceiver
 * @dev 接收代币的接口
 */
interface ITokenReceiver {
    function tokensReceived(address from, uint256 amount) external returns (bool);
}

/**
 * @title ExtendedERC20
 * @dev 扩展的ERC20合约，添加了hook功能的转账函数
 */
contract ExtendedERC20 is BaseERC20 {

    constructor() {
        name = "ExtendedERC20";
        symbol = "EERC20";
        decimals = 18;
        totalSupply = 100000000 * 10 ** uint256(decimals);

        balances[msg.sender] = totalSupply;
    }
    
    /**
     * @dev 检查地址是否为合约地址
     * @param account 要检查的地址
     * @return 如果是合约地址返回true，否则返回false
     */
    function isContract(address account) internal view returns (bool) {
        uint256 size;
        assembly {
            size := extcodesize(account)
        }
        return size > 0;
    }
    
    /**
     * @dev 带回调功能的转账函数
     * @param to 接收地址
     * @param amount 转账金额
     * @return 转账是否成功
     */
    function transferWithCallback(
        address to,
        uint256 amount
    ) external returns (bool) {
        // 执行标准转账
        require(
            balances[msg.sender] >= amount,
            "ERC20: transfer amount exceeds balance"
        );

        balances[msg.sender] -= amount;
        balances[to] += amount;

        emit Transfer(msg.sender, to, amount);

        // 如果目标地址是合约，调用其tokensReceived方法
        if (isContract(to)) {
            try ITokenReceiver(to).tokensReceived(msg.sender, amount) {
                // 回调成功
            } catch {
                // 回调失败，但不影响转账
                // 可以选择revert或者继续，这里选择继续
            }
        }

        return true;
    }
}

/**
 * @title TokenBankV2
 * @dev 支持hook功能的代币银行合约V2
 */
contract TokenBankV2 is TokenBank, ITokenReceiver {

    // 扩展的ERC20代币合约地址
    ExtendedERC20 public extendedToken;

    /**
     * @dev 构造函数
     * @param _token 扩展的ERC20代币合约地址
     */
    constructor(address _token) TokenBank(_token) {
        require(_token != address(0), "Invalid token address");
        extendedToken = ExtendedERC20(_token);
    }

    /**
     * @dev 实现tokensReceived接口，处理通过hook接收的代币
     * @param from 发送者地址
     * @param amount 代币数量
     */
    function tokensReceived(
        address from,
        uint256 amount
    ) external override returns (bool) {
        // 确保调用者是我们支持的代币合约
        require(msg.sender == address(token), "Invalid token contract");
        require(amount > 0, "Amount must be greater than 0");

        // 记录用户的存入数量（累加到原有余额）
        balances[from] += amount;

        emit Deposit(from, amount);
        
        return true;
    }
}
