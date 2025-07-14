// SPDX-License-Identifier: GPL-3.0

pragma solidity ^0.8.0;

import "./IBank.sol";

contract Admin {
    // Admin合约的Owner
    address public owner;
    
    // 事件
    event AdminWithdraw(address indexed bank, uint256 amount);
    
    // 修饰符：只有Owner可以调用
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }
    
    // 构造函数，设置部署者为Owner
    constructor() {
        owner = msg.sender;
    }
    
    // 从Bank合约提取资金的函数
    function adminWithdraw(IBank bank) external onlyOwner {
        // 获取Bank合约的余额
        uint256 bankBalance = bank.getContractBalance();
        require(bankBalance > 0, "Bank has no funds to withdraw");
        
        // 调用Bank合约的withdrawAll函数，将资金转移到Admin合约地址
        bank.withdraw();
        
        // 触发事件
        emit AdminWithdraw(address(bank), bankBalance);
    }
    
    // 获取Admin合约的余额
    function getBalance() external view returns (uint256) {
        return address(this).balance;
    }
    
    // 接收以太币
    receive() external payable {}
    
    // 回退函数
    fallback() external payable {}
}
