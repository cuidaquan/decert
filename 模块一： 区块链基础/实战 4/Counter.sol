// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract Counter {
    // 状态变量：存储计数器的值
    uint256 public counter;
    
    // 构造函数，初始化计数器为0
    constructor() {
        counter = 0;
    }
    
    // 获取计数器的当前值
    function get() public view returns (uint256) {
        return counter;
    }
    
    // 给计数器加上指定的值
    function add(uint256 x) public {
        counter += x;
    }
    
}
