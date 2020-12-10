# zfjbot-NgGame
a plugin for hoshino
项目地址：[zfjbot-NgGame](https://github.com/zfjdhj/zfjbot-NgGame)
基于[NGWordGame](https://github.com/Li-mz/NGWordGame)魔改，在hoshino中实现NG词语游戏。

## NG词语游戏
出自漫画《辉夜大小姐想让我告白～天才们的恋爱头脑战～》，规则为参与游戏的每个玩家为下一个玩家设置一个“NG词”，
设置完成后展示之，使得除了自己的每个人都能知道自己的NG词。之后所有玩家进行自由谈话，说出自己的NG词的玩家判负，退场。直至只剩一人为止。

## 使用
将本项目原作为nonebot的插件使用。关于nonebot的使用和插件添加方法，参见其[项目文档](https://none.rclab.tk/)。  
- 注册阶段：由超级用户（已魔改）发出指令`NG词语游戏`（或`NGWordGame`，`ng`）开始游戏，所有参与者回复`sign in`参与游戏，超级用户（已魔改）发出指令`stop signing`停止注册
- 设置阶段：所有玩家使用`setNG`指令和机器人私聊设置下一个玩家的NG词。当所有玩家设置完成时，机器人会自动向群里发送通知，由超级用户发出`check`指令加载所有设置的NG词
- 监听阶段：此时开始机器人对群内聊天信息进行监听，当有玩家触发自己的NG词时发出提醒，直至只剩一位玩家，游戏结束。`stop`强制终止游戏。

注意，由于此功能要求NG词语游戏会话对群内所有人的发言都有响应，需要修改nonebot的`nonebot\command\__init__.py`中525行：
```
ctx_id = context_id(ctx)
```
将其改为：
```
ctx_id = context_id(ctx, mode='group')
```
ps:最新版nonebot行数不对应，自行查找。
## 魔改
我也忘了魔改啥，时间太久忘了...
大概就
1. 加入lssv豪华套餐，默认插件名 `zfjbot-NgGame`
2. 重构命令逻辑，使之适应hoshino大家庭
3. 个别命令权限要求改为第一个触发命令的人，管理员不可能时刻在线。
因为游戏涉及bot主动发起临时会话，建议使用mirai-cqhttp。或者加bot为好友。
插件使用截图

![截图1](http://resource.zfjdhj.cn/images/blogPicture/20201210/2020121001.png)

![截图2](http://resource.zfjdhj.cn/images/blogpicture/20201210/2020121002.png)
