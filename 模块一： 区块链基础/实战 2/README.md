[模拟实现最小的区块链原理](https://decert.me/quests/ed2d8324-54b0-4b7a-9cee-5e97d3c30030)



题目#1
用自己熟悉的语言模拟实现最小的区块链， 包含两个功能：

POW 证明出块，难度为 4 个 0 开头
每个区块包含previous_hash 让区块串联起来。
如下是一个参考区块结构：

block = {
'index': 1,
'timestamp': 1506057125,
'transactions': [
    { 'sender': "xxx", 
    'recipient': "xxx", 
    'amount': 5, } ], 
'proof': 324984774000,
'previous_hash': "xxxx"
}
请提交完成的 github 代码仓库链接， 在 Readme 中包含运行说明及运行日志或截图。