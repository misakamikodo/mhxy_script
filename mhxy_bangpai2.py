import argparse
import os
from configparser import ConfigParser

from mhxy import *

nxtNode = PicNode(r'resources/bangpai/small/next.png')

class BangpaiPicNode(PicNode):

    def setNext(self, nxt):
        super().setNext(nxt)
        # 防止卡了的情况，自己下一个包含自己
        self.next.append(self)
        self.next.append(nxtNode)


# 小窗口
class Bangpai(MhxyScript):
    chaseWin = [-0.5, 3.8 + 0]
    # 结束状态
    _rootList = []

    _allList = []

    def __init__(self, idx=0, changWinPos=True) -> None:
        super().__init__(idx=idx, changWinPos=changWinPos)
        file_path = os.path.join(os.path.abspath('.'), 'resources/bangpai/small/bangpai.ini')
        if not os.path.exists(file_path):
            raise FileNotFoundError("文件不存在")
        conn = ConfigParser()
        conn.read(file_path)
        chasepos = float(conn.get('main', 'chasepos'))
        self.chaseWin[1] = 3.8 + chasepos * 2

        # 结束状态 下一步是root（除了finish标志）
        leafNode = []

        def clickFunc(locate, chaseWin):
            pyautogui.leftClick(locate.x, locate.y)
            cooldown(0.2)

        def shangchen(locate, chaseWin):
            cooldown(1)
            shangchen = Util.locateCenterOnScreen(r'resources/bangpai/small/shangchen.png') is not None
            # 选择第二个商品（防止商品被买）
            if shangchen:
                Util.leftClick(17, 7)
                cooldown(0.3)
                pyautogui.leftClick(locate.x, locate.y)
            else:
                clickFunc(locate, chaseWin)

        def battleFunc(locate, chaseWin):
            while Util.locateCenterOnScreen(r'resources/small/enter_battle_flag.png') is not None:
                cooldown(1)
            pyautogui.leftClick(locate.x, locate.y)
            cooldown(0.5)

        # 访问任务
        battle = BangpaiPicNode(r'resources/small/enter_battle_flag.png', completeFunc=battleFunc)
        qiecuo = BangpaiPicNode(r'resources/bangpai/small/qiecuo.png', completeFunc=clickFunc)
        fanwen = BangpaiPicNode(r'resources/bangpai/small/fanwen.png')
        qiecuo.setNext([battle])
        fanwen.next = [battle, nxtNode]
        # 访问、已有二级药的任务结束
        leafNode.append(fanwen)
        # 巡逻、挂机场景结束
        leafNode.append(battle)

        # 三级药烹饪wupin任务 *购买->总管->上交 二级药wupin2任务 *购买->总管
        shangjiao = BangpaiPicNode(r'resources/bangpai/small/shangjiao.png')
        fanwen.next.append(shangjiao)
        wupin = BangpaiPicNode(r'resources/bangpai/small/wupin.png', completeFunc=shangchen)
        # 可能购买失败，所以还是
        wupin.setNext([fanwen])
        wupin2 = BangpaiPicNode(r'resources/bangpai/small/wupin2.png', completeFunc=clickFunc)
        wupin2.next = [fanwen, nxtNode]
        # 二级药结束点
        # leafNode.append(fanwen)
        # 烹饪药结束点
        leafNode.append(shangjiao)

        def fanwenFunc(locate, chaseWin):
            pyautogui.leftClick(locate.x, locate.y)
            cooldown(3)
            pyautogui.leftClick(locate.x, locate.y)
            cooldown(0.3)

        def hanhuaFunc(locate, chaseWin):
            Util.leftClick(-3.5, -3)
            cooldown(3)
            Util.leftClick(-3.5, -3)
            cooldown(0.3)
        # 喊话任务
        hanhua = BangpaiPicNode(r'resources/bangpai/small/hanhua.png', completeFunc=hanhuaFunc)
        leafNode.append(hanhua)

        # 结束
        def finishFunc(locate, chaseWin):
            sys.exit(0)

        finish = BangpaiPicNode(r'resources/bangpai/small/finish.png', completeFunc=finishFunc)

        self._rootList = [qiecuo, fanwen, wupin, wupin2, hanhua] #  finish

        for item in leafNode:
            if item.next is not None:
                for each in self._rootList:
                    item.next.append(each)
            else:
                item.next = self._rootList
                item.next.append(nxtNode)
        nxtNode.next = self._rootList

    def do(self):

        nodePointer = self._rootList
        findPicNode = None
        while findPicNode is None or findPicNode.next is not None:
            Util.leftClick(self.chaseWin[0], self.chaseWin[1])
            idx, locate = self._findPic(nodePointer)
            time = 0
            while locate is None:
                if not self._stopCheck():
                    sys.exit(0)
                cooldown(0.2)
                time += 1
                cooldown(0.5)
                idx, locate = self._findPic(nodePointer)
                if time >= 5 and locate is None and time % 4 == 0:
                    # 没法判断特征图片的任务都能通过不断点击追踪完成（因为挂机刷怪会停止没发判断，先这么搞）
                    Util.leftClick(self.chaseWin[0], self.chaseWin[1])
            findPicNode = nodePointer[idx]
            log("选中：" + findPicNode.elem)
            findPicNode.completeFunc(locate, self.chaseWin)
            nodePointer = findPicNode.next
            log("后续可能出现：")
            for each in nodePointer:
                log(each.elem)
            cooldown(0.3)

    # 有特征图片的任务
    def _findPic(self, nodeList):
        for idx, each in enumerate(nodeList):
            if each.elem is None:
                continue
            locate = None
            if isinstance(each.elem, list):
                for iid, item in enumerate(each.elem):
                    locate = Util.locateCenterOnScreen(item)
                    if locate is not None:
                        break
            else:
                locate = Util.locateCenterOnScreen(each.elem)
            if locate is not None:
                return idx, locate
        return None, None


# 大窗口
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='OF Generate')
    parser.add_argument('-i', '--idx', required=False, default=0, type=int)
    args = parser.parse_args()
    pyautogui.PAUSE = 0.5
    log("start task....")

    def func(idx):
        Bangpai(idx=idx).do()

    if args.idx == -1:
        i = 0
        while args.idx == -1 and len(getWindowList()) > i:
            func(i)
            i = i + 1
    else:
        func(args.idx)

