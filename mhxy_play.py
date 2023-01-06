from mhxy import *

# from mingus.containers import *
# from mingus.core import notes
# from mingus.midi import fluidsynth


def getMusic(r):
    f = open(r, 'r')
    try:
        pu = []
        for line in f.readlines():
            for sign in line.split(","):
                yin = None
                time = 1
                for char in sign:
                    if char == '|':
                        # 半音 1/4音 等
                        time /= 2
                    elif char == '.':
                        # 附点
                        time += 0.5
                    elif char == '+':
                        # 高音
                        yin += 7
                    elif char == '-' and yin is not None:
                        # 低音
                        yin -= 8
                    elif char == '-' and yin is None:
                        # 延长
                        pu[len(pu) - 1][1] += 1
                        pass
                    elif char != '\n':
                        # 音符+休止符
                        if yin is not None:
                            # 半个音
                            pu.append([yin, time])
                        yin = int(char)
                        time = 1
                if yin is not None:
                    # 延长音已处理跳过
                    pu.append([yin, time])
        return pu
    finally:
        f.close()


# def playMusic():
#     track = Track()
#     b = Bar('C', (8, 4))
#     b.place_rest(1)
#     for each in pu:
#         bar = Bar('C', (8, 4))
#         if each[0] == 0:
#             bar.place_rest(2 / each[1])
#         else:
#             note = Note(name[each[0] % 7], int(each[0] / 7) + 1)
#             bar.place_notes(note, 2 / each[1])
#         track.add_bar(bar)
#     fluidsynth.init(r'F:\ccy\temp\pupupu\base\GeneralUser GS 1.44 SoftSynth\GeneralUser GS SoftSynth v1.44.sf2')
#     fluidsynth.set_instrument(1, 9)
#     fluidsynth.play_Track(track, channel=1, bpm=150)


keymap2 = {
    -7: (3.5  , 13+2),
    -6: (6.5  , 13+2),
    -5: (9.5  , 13+2),
    -4: (12.5 , 13+2),
    -3: (15   , 13+2),
    -2: (18   , 13+2),
    -1: (21   , 13+2),
    1:  (3.5  , 13),
    2:  (6.5  , 13),
    3:  (9.5  , 13),
    4:  (12.5 , 13),
    5:  (15   , 13),
    6:  (18   , 13),
    7:  (21   , 13) ,
    8:  (3.5  , 13-2),
    9:  (6.5  , 13-2),
    10: (9.5  , 13-2),
    11: (12.5 , 13-2),
    12: (15   , 13-2),
    13: (18   , 13-2),
    14: (21   , 13-2)
}

keymap = {
    -7: (6.5  , 14.5),
    -6: (9.2  , 14.5),
    -5: (12   , 14.5),
    -4: (14.8 , 14.5),
    -3: (17.5 , 14.5),
    -2: (20.5 , 14.5),
    -1:  (23.5 , 14.5),
    1:  (6.5  , 13),
    2:  (9.2  , 13),
    3:  (12   , 13),
    4:  (14.8 , 13),
    5:  (17.5 , 13),
    6:  (20.5 , 13),
    7:  (23.5 , 13) ,
    8:  (6.5  , 11.5),
    9:  (9.2  , 11.5),
    10: (12   , 11.5),
    11: (14.8 , 11.5),
    12: (17.5 , 11.5),
    13: (20.5 , 11.5),
    14: (23.5 , 11.5),
    15: (17.5 , 10),
    16: (20.5 , 10),
    17: (23.5 , 10),
}

if __name__ == '__main__':
    '''
    track在这个库中表示音轨，bar表示的应该是小节，但是我偷懒了，把bar直接存储乐句了。在track的开头，我添加了一个2拍的休止符，
    因为这个库不知道是bug还是什么，如果track开头没有休止符，则乐曲的第一个音会被吞掉
    bar的构造函数有两个参数，前者随便填无影响，可能只是元信息，后者比较重要，它描述了这个小节的时长，
    如果小节里放的音符总时长超过了这个小节的时长最后一个音符会被扔掉，所以一定要计算好。这个时长用分数表示，
    但它的计算方式很奇怪，(4, 4)表示2拍，以此类推(8, 4)表示4拍，和正常情况完全不一样。之后对于每个乐句，
    我首先把时长转化成数，然后计算乐句的时长，因为我的乐谱8为2拍，所以要除8再乘4。
    库里1234567分别用CDEFGAB代替；
    库中对时值的描述和我们的描述是倒数关系，它是8为¼拍，4为½拍，2为1拍，以此类推，所以在传入place_notes和place_rest我们的时值要用8除
    note.transpose用来转调，它能够把音符提升一定的半音数。
    '''
    pu = getMusic(r'resources/play/shuaicongge.txt')
    print(pu)
    init(resizeToNice=False)
    # for i in range(0,20):
    for each in pu:
        if each[0] != 0:
            Util.leftClick(keymap[each[0]][0],keymap[each[0]][1])
        cooldown(each[1] / 4)

