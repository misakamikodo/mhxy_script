# 脚本说明

安装完包依赖后 需要opencv-python支持(pip install opencv-python)才能模糊匹配图片

屏幕分辨率1920x1080可直接使用（理论上 1920 x XX都行）

屏幕分辨率和我不一致的大概率需要在理解代码条件下进行二次开发使用（在小屏笔记本上试过，运行效果不符合期望）。

### 关于二次开发：

首先在mhxy->__init__.py中修改以下变量：

* originSize（打开桌面版后桌面版的像素大小，=frameSize实际值），

* smallSize（使用 game_process.py 调整的小窗口像素大小，部分脚本使用小窗口）（以上两个通过game_process的控制台输出可以看到），

* resizeOffset（调整窗口大小时对右下角操作使用的偏移量，取能使用的值即可，应该不用改），

* frameOriginSizeCm（为了方便编写，初始窗口像素大小换算的厘米值，这样可以在屏幕上通过尺子测距来调整坐标），

game_process.py 中执行情况调整到适合自己的位置即可

其次可能需要修改替换资源目录中脚本的截图，最后改部分脚本中写死的厘米坐标。

### 注意事项

使用时如捉鬼、副本等大部分脚本需要先使用game_process.py调整为小窗口或者resizeToSmall设置为True再运行，其他如挖矿、收商品则使用的原始窗口。
具体的请到resources目录下对应脚本资源文件下有使用说明。

运行的时候需要给.py文件或者ide赋予管理员权限，要不然程序窗口失去焦点后就无法操作控制鼠标。

PS:电脑配置可以的推荐搞个虚拟机运行，这样不仅可以自定义分辨率（调到和我一样就不用二次开发了）而且虚拟机后台运行不会占用电脑。


### 打包方法：
```shell
pyinstaller --onefile --noconsole mhxy_script.py
```

打包完后exe目录需要放置资源文件，并且exe也需要管理员权限。虽然打包能用，但是opencv无法支持，尝试使用了以下命令
```shell
pyinstaller --hidden-import cv2 --hidden-import numpy --onefile --noconsole mhxy_script.py
pyinstaller --paths="E:\Program Files\anaconda3\lib\site-packages\cv2" --onefile --noconsole mhxy_script.py
```
依然不行，因此需要重新替换下截图。解决这个问题后再分享一个打包好的程序

而且打包生成的exe文件有270多MB（已使用upx压缩），这对于一个小脚本来说还是太大了，不打算继续更新界面程序。

## 文件说明
* mhxy_script 界面程序
* mhxy_520 520/320/550 任务汇总
* mhxy_even_guaji 常用挂机系列汇总 可用于晚间挂机
* mhxy_bangpai 帮派任务
* mhxy_bangpai2 帮派任务(小窗口)
* mhxy_fuben 日常副本任务
* mhxy_ghost 抓鬼
* mhxy_ghost_withshop 抓鬼+收碎片(可改收其他非珍品)
* mhxy_menpai 周一门派
* mhxy_haidi 周三海底
* mhxy_mihunta 周五迷魂塔
* mhxy_auto_battle 自动战斗工具 可用于混“28怒”、玲珑石等任务挂机
* mhxy_hanhua 喊话工具
* mhxy_mine 挖矿
* mhxy_mine_withshop 挖矿+收碎片(可改收其他非珍品)
* mhxy_remote_control 远程控制模块 例如接收指令执行520(可改其他程序)
* mhxy_remote_client 用于对接 mhxy_shoopping2 和 mhxy_remote_control 的工具
* mhxy_shopping 蹲非珍品
* mhxy_shopping2 蹲珍品
* mhxy_shopping3 截胡珍品
