from mhxy import *

class Bangpai:
    # 结束状态
    _rootList = []

    _allList = []

    def __init__(self, idx=0) -> None:
        # init(resizeToNice=True)
        init(idx=idx, resizeToNice=False)
        # 结束状态 下一步是root（除了finish标志）
        leafNode = []

        def clickFunc(locate, chaseWin):
            pyautogui.leftClick(locate.x, locate.y)
            cooldown(0.2)

        def battleFunc(locate, chaseWin):
            while Util.locateCenterOnScreen(r'resources/origin/enter_battle.png') is not None:
                cooldown(1)
            pyautogui.leftClick(locate.x, locate.y)
            cooldown(0.5)
        # 访问任务
        battle = PicNode(r'resources/origin/enter_battle.png', completeFunc=battleFunc)
        qiecuo = PicNode(r'resources/bangpai/qiecuo.png', completeFunc=clickFunc)
        fanwen = PicNode(r'resources/bangpai/fanwen.png')
        qiecuo.setNext([qiecuo])
        fanwen.next = [battle]
        # 访问、已有二级药的任务结束
        leafNode.append(fanwen)
        # 巡逻、挂机场景结束
        leafNode.append(battle)

        # 商店、药店任务
        def shangchenFunc(locate, chaseWin):
            Util.leftClick(-7, 8)
            pyautogui.leftClick(locate.x, locate.y)
            cooldown(2)
            Util.leftClick(-5, -5)

        # 三级药烹饪wupin任务 *购买->总管->上交 二级药wupin2任务 *购买->总管
        shangjiao = PicNode(r'resources/bangpai/shangjiao.png')
        fanwen.next.append(shangjiao)
        wupin = PicNode(r'resources/bangpai/wupin.png', completeFunc=clickFunc)
        # 可能购买失败，所以还是
        wupin.next = [fanwen, wupin]
        wupin2 = PicNode(r'resources/bangpai/wupin2.png', completeFunc=clickFunc)
        wupin2.next = [fanwen]
        shangchen = PicNode(r'resources/bangpai/shangchen.png', completeFunc=shangchenFunc)
        shangchen.next = [fanwen]
        # 二级药结束点
        # leafNode.append(fanwen)
        # 烹饪药结束点
        leafNode.append(shangjiao)

        def fanwenFunc(locate, chaseWin):
            pyautogui.leftClick(locate.x, locate.y)
            cooldown(3)
            pyautogui.leftClick(locate.x, locate.y)
            cooldown(0.3)
        # 喊话任务
        hanhua = PicNode(r'resources/bangpai/hanhua.png', completeFunc=fanwenFunc)
        leafNode.append(hanhua)

        # 结束
        def finishFunc(locate, chaseWin):
            exit(0)

        finish = PicNode(r'resources/bangpai/finish.png', completeFunc=finishFunc)

        self._rootList = [qiecuo, fanwen, wupin, wupin2, hanhua, finish]
        for item in leafNode:
            if item.next is not None:
                for each in self._rootList:
                    item.next.append(each)
            else:
                item.next = self._rootList

    def do(self, chaseWin):

        nodePointer = self._rootList
        findPicNode = None
        while findPicNode is None or findPicNode.next is not None:
            Util.leftClick(chaseWin[0], chaseWin[1])
            idx, locate = self._findPic(nodePointer)
            time = 0
            while locate is None:
                cooldown(0.2)
                time += 1
                cooldown(0.5)
                idx, locate = self._findPic(nodePointer)
                if time >= 5 and locate is None:
                    # 没法判断特征图片的任务都能通过不断点击追踪完成（因为挂机刷怪会停止没发判断，先这么搞）
                    Util.leftClick(chaseWin[0], chaseWin[1])
            findPicNode = nodePointer[idx]
            print("选中：" + findPicNode.elem)
            findPicNode.completeFunc(locate, chaseWin)
            nodePointer = findPicNode.next
            print("后续可能出现：")
            for each in nodePointer:
                print(each.elem)
            cooldown(0.3)

    # 有特征图片的任务
    def _findPic(self, nodeList):
        for idx, each in enumerate(nodeList):
            if each.elem is None:
                continue
            locate = None
            if isinstance(each.elem, list):
                for iid, item in enumerate(each.elem):
                    locate = pyautogui.locateCenterOnScreen(item, confidence=0.9)
                    if locate is not None:
                        break
            else:
                locate = pyautogui.locateCenterOnScreen(each.elem, confidence=0.9)
            if locate is not None:
                return idx, locate
        return None, None


# 大窗口
if __name__ == '__main__':
    pyautogui.PAUSE = 0.5
    print("start task....")
    init()
    Bangpai().do((-0.5, 6 + 0))
