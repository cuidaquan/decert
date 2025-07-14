// SPDX-License-Identifier: GPL-3.0

pragma solidity ^0.8.0;

interface IBank {
    // 存款函数
    function deposit() external payable;
    
    // 管理员提取所有资金
    function withdraw() external;
    
    // 获取合约总余额
    function getContractBalance() external view returns (uint256);
    
    // 获取指定地址的存款余额
    function getBalance(address depositor) external view returns (uint256);
    
    // 获取管理员地址
    function admin() external view returns (address);
    
}
