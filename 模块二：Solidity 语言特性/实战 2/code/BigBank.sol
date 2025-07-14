// SPDX-License-Identifier: GPL-3.0

pragma solidity ^0.8.0;

import "./Bank.sol";

contract BigBank is Bank {

    // 更改管理员（只有当前管理员可以调用）
    function changeAdmin(address newAdmin) external onlyAdmin {
        require(newAdmin != address(0), "New admin cannot be zero address");
        admin = newAdmin;
    }
    
    // 修饰符：存款金额必须大于0.001 ether
    modifier minDeposit() {
        require(msg.value > 0.001 ether, "Deposit amount must be greater than 0.001 ether");
        _;
    }
    
    // 重写存款函数，添加最小存款限制
    function deposit() public payable override minDeposit {
        // 调用父合约的存款逻辑
        super.deposit();
    }
    
    // 重写receive函数，添加最小存款限制
    receive() external payable override {
        deposit();
    }

    // 重写fallback函数，添加最小存款限制
    fallback() external payable override {
        deposit();
    }
}
