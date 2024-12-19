# 脚本目前有被封风险！！

# 脚本说明

安装完包依赖后 需要opencv-python支持(pip install opencv-python)才能模糊匹配图片

屏幕分辨率1920x1080可直接使用（游戏窗口初始大小是1040×807，调节小窗口后是907×707 这种我觉得都行）

屏幕分辨率和我不一致的大概率可能需要在理解代码条件下进行二次开发使用（在小屏笔记本上试过，运行效果不符合期望，但是如果屏幕足够大一般都可以）。

pyautogui部分不支持mac，在mac上运行应该运行不了

### 关于二次开发：

首先在mhxy->__init__.py中修改以下变量：

* originSize（打开桌面版后桌面版的像素大小，=frameSize实际值），

* smallSize（使用 game_process.py 调整的小窗口像素大小，大部分脚本使用小窗口）（以上两个通过game_process的控制台输出可以看到）

* frameOriginSizeCm（为了方便编写，初始窗口像素大小换算的厘米值，这样可以在屏幕上通过尺子测距来调整坐标），

game_process.py 中执行情况调整到适合自己的位置即可

其次可能需要修改替换资源目录中脚本的截图，最后改脚本中写死的厘米坐标。

### 注意事项

使用时如捉鬼、副本等大部分脚本需要先使用game_process.py调整为小窗口或者resizeToSmall设置为True再运行，其他如挖矿、收商品则使用的原始窗口。
具体的请到resources目录下对应脚本资源文件下有使用说明。

运行的时候需要给.py文件或者ide赋予管理员权限，要不然程序窗口失去焦点后就无法操作控制鼠标。

PS:电脑配置可以的推荐搞个虚拟机运行，这样不仅可以自定义分辨率（调到和我一样就不用二次开发了）而且虚拟机后台运行不会占用电脑。

## 文件说明
* ui/mhxy_pyqt 界面程序
* mhxy_520 副本捉鬼
* mhxy_even_guaji 常用挂机系列汇总 (可用于晚间挂机)
* mhxy_richang 宝图 秘境 答题 押镖
* mhxy_bangpai2 帮派任务(小窗口)
* mhxy_baotu 宝图
* mhxy_mijing 秘境
* mhxy_dati 答题
* mhxy_yabiao 押镖
* mhxy_fuben 日常副本任务
* mhxy_ghost 抓鬼
* mhxy_menpai 周一门派
* mhxy_haidi 周三海底
* mhxy_mihunta 周五迷魂塔
* mhxy_auto_battle 自动战斗工具 (可用于混“28怒”、玲珑石等任务挂机)
* mhxy_hanhua 喊话工具
* mhxy_mine 挖矿
* mhxy_linlongshi 红色玲珑石带队×5
* mhxy_remote_control 远程控制模块 例如接收指令执行任务
* mhxy_remote_client 用于对接 mhxy_shopping2 和 mhxy_remote_control 的工具
* mhxy_shopping 蹲非珍品
* mhxy_shopping2 蹲珍品
* mhxy_shopping3 截胡珍品 (不关注、使用搜索的方式)
