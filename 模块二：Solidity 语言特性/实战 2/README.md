[通过编写 BigBank 实践 Solidity 继承及接口合约交互](https://decert.me/quests/063c14be-d3e6-41e0-a243-54e35b1dde58)
题目#1
在 [该挑战](https://decert.me/quests/c43324bc-0220-4e81-b533-668fa644c1c3) 的 Bank 合约基础之上，编写 IBank 接口及BigBank 合约，使其满足 Bank 实现 IBank， BigBank 继承自 Bank ， 同时 BigBank 有附加要求：

要求存款金额 >0.001 ether（用modifier权限控制）
BigBank 合约支持转移管理员
编写一个 Admin 合约， Admin 合约有自己的 Owner ，同时有一个取款函数 adminWithdraw(IBank bank) , adminWithdraw 中会调用 IBank 接口的 withdraw 方法从而把 bank 合约内的资金转移到 Admin 合约地址。

BigBank 和 Admin 合约 部署后，把 BigBank 的管理员转移给 Admin 合约地址，模拟几个用户的存款，然后

Admin 合约的Owner地址调用 adminWithdraw(IBank bank) 把 BigBank 的资金转移到 Admin 地址。

请提交 github 仓库地址。