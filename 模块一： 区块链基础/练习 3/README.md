[理解 Gas 机制](https://decert.me/quests/d17a9270-99c3-4aeb-8a46-42ecb5e92792)

题目#1
在以太坊上，用户发起一笔交易 设置了GasLimit 为 10000, Max Fee 为 10 GWei, Max priority fee 为 1 GWei ， 为此用户应该在钱包账号里多少 GWei 的余额？
GasLimit*Max Fee=10*10000=100000

题目#2
在以太坊上，用户发起一笔交易 设置了 GasLimit 为 10000, Max Fee 为 10 GWei, Max priority Fee 为 1 GWei，在打包时，Base Fee 为 5 GWei, 实际消耗的Gas为 5000， 那么矿工（验证者）拿到的手续费是多少 GWei ?
min((Max Fee-Base Fee)*Gas消耗,Max priority Fee*Gas消耗)=1*5000=5000

题目#3
在以太坊上，用户发起一笔交易 设置了 GasLimit 为 10000, Max Fee 为 10 GWei, Max priority Fee 为 1 GWei，在打包时，Base Fee 为 5 GWei, 实际消耗的Gas为 5000， 那么用户需要支付的的手续费是多少 GWei ?
Base Fee * Gas消耗 + min((Max Fee-Base Fee)*Gas消耗,Max priority Fee*Gas消耗)=5*5000+1*5000=30000

题目#4
在以太坊上，用户发起一笔交易 设置了 GasLimit 为 10000, Max Fee 为 10 GWei, Max priority Fee 为 1 GWei，在打包时，Base Fee 为 5 GWei, 实际消耗的 Gas 为 5000， 那么燃烧掉的 Eth 数量是多少 GWei ?
Base Fee*Gas消耗=5*5000=25000