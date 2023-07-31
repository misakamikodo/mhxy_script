# 梦幻西游手游脚本

安装完包依赖后还至少需要opencv-python支持(pip install opencv-python)。

屏幕分辨率1920*1080可直接使用（可能1920*xx都行），否则拉了代码后首先再mhxy.py中修改originSize（打开桌面版后桌面版的像素大小，=frameSize实际值），niceSize（使用game_process调整的小窗口像素大小，部分脚本使用小窗口）（以上两个通过game_process的控制台输出可以看到），resizeOffset（调整窗口大小时对右下角操作使用的偏移量，取能使用的值即可，应该不用改），frameSizeCm（为了方便编写，像素大小换算的厘米值，这样可以通过尺子在屏幕上测距来调整坐标），其次修改替换需要脚本的截图，最后改脚本中写死的厘米值。

使用时如捉鬼、副本需要先game_process中调整为小窗口或者resizeToNice设置为True再运行；

运行的时候需要给.py文件或者ide赋予管理员权限，要不然程序窗口失去焦点后就无法操作控制鼠标。

有条件的可以搞个虚拟机运行，这样就不会占用电脑了

## 文件说明
* mhxy_520 520/320/550 任务汇总
* mhxy_even_guaji 常用挂机系列汇总 可用于晚间挂机
* mhxy_bangpai 帮派任务
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
* mhxy_shopping4 多商品选一购买
