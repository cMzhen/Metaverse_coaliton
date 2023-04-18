import random
import json
import time
import numpy as np
users = range(100)
maps = range(5)
video_size_0 = [100.0, 90.0, 80.0, 50.0, 100.0]
video_size = [0.0]*len(maps)
ratio = [0.3, 0.18, 0.1, 0.08, 0.05]
MECs = np.zeros((20, 5, 2), dtype=int) #定义mecs数组 (MEC,用户数量，0表示用户；1表示MEC)
#随机生成用户的位置关系（5*100）
with open('location_2023_04_13_215555.json', 'r') as f:
    location = json.load(f)
# 从 JSON 数据中获取数组

#定义MEC，三维数组（MEC数量，用户列表，0/1)
for i in range(20):
    start = i * 5
    end = (i + 1) * 5
    MECs[i, :, 0] = users[start:end]# 第三维 0 表示MEC编号
    MECs[i, :, 1] = i # 第三维 1 表示对应MEC的用户编号

MEC_NUM = MECs[:, 0, 1]#这里使用了切片 [:, 0, 1]，表示所有 MEC 的编号。作为初始联盟结构
loca = np.array_split(np.array(location).reshape(5, -1), 20,axis=1)#将用户的位置关系按MEC划分为20个（5*5）
alliances = [[0, 1, 2], [3, 4, 5, 6], [7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19]]
for j in alliances:#联盟的MEC集合
    n=[0]*5
    n += loca[j]
    for i, num in enumerate(n):
        print(f'alliance{j}has {num} in map{i}')
'''
# 定义联盟列表
alliances = [[0, 1, 2], [3, 4, 5, 6], [7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19]]
def calculate_alliance_video_size(alliance, MECs, maps, loca, location, video_size_0):
 
    计算联盟内所有MEC在各个数据集上的视频数据量大小。
    :param alliance: 联盟成员列表，包含各个MEC的编号。
    :param MECs: 所有MEC的视频数据信息。
    :param maps: 数据集名称列表。
    :param loca: 各个MEC与数据集之间的位置关系。
    :param location: 各个数据集内视频的位置信息。
    :param video_size_0: 每个数据集内单个视频的大小。
    :return: 包含各个数据集视频数据量大小的一维NumPy数组。
 
    video_size_alliance = np.zeros(len(maps))
    for i in maps:
        for j in alliance:#联盟的MEC集合
            m = np.array(MECs[j][:, 0])#MEC j的用户们的矩阵
            m = m.astype(int)
            n += loca[j]
            number = np.array([np.sum(num) for num in n])
            for n in m:
                if np.any(loca[j][i]):
                    video_size_alliance[i] += np.sum(location[i][n]) * video_size_0[i]
    return video_size_alliance
# 输出每个联盟数据量大小
for i, alliance in enumerate(alliances):
    video_size_alliance = calculate_alliance_video_size(alliance, MECs, maps, loca, location, video_size_0)
    print(f'dataset of alliance {i} is {float(np.sum(video_size_alliance))}')


def calculate_alliance_video_size(alliance, MECs, maps, loca, location, video_size_0):
 
    计算联盟内所有MEC在各个数据集上的视频数据量大小。
    :param alliance: 联盟成员列表，包含各个MEC的编号。
    :param MECs: 所有MEC的视频数据信息。
    :param maps: 数据集名称列表。
    :param loca: 各个MEC与数据集之间的位置关系。
    :param location: 各个数据集内视频的位置信息。
    :param video_size_0: 每个数据集内单个视频的大小。
    :return: 包含各个数据集视频数据量大小的一维NumPy数组。
  
    video_size_alliance = np.zeros(len(maps))
    for i in maps:
        for j in alliance:#联盟的MEC集合
            m = np.array(MECs[j][:, 0])#
            m = m.astype(int)
            for n in m:
                if np.any(loca[j][i]):
                    video_size_alliance[i] += np.sum(location[i][n]) * video_size_0[i]
    return video_size_alliance
# 输出每个联盟数据量大小
for i, alliance in enumerate(alliances):
    video_size_alliance = calculate_alliance_video_size(alliance, MECs, maps, loca, location, video_size_0)
    print(f'dataset of alliance {i} is {float(np.sum(video_size_alliance))}')

# 遍历每个联盟
for alliance in alliances:
    video_size_alliance = np.zeros(len(maps))  # 定义该联盟的视频大小数组
    for j in alliance:  # 遍历该联盟中的每个MEC
        for i in maps:  # 遍历所有数据集
            m = np.array(MECs[j][:, 0])
            m = m.astype(int)
            for n in m:
                if np.any(loca[j][i]):
                    video_size_alliance[i] += np.sum(location[i][n]) * video_size_0[i]
    print(f'dataset of alliance {alliance} is {float(np.sum(video_size_alliance))}')



#计算每个MEC的渲染任务大小
for j in range(20):#遍历所有MEC
    for i in maps:
        m = np.array(MECs[j][:, 0])#取出MEC对应的用户所在地图的位置数组（5*5）
        m = m.astype(int)
        video_size[i] = 0 #清空MEC数据量
        for n in m:
          if np.any(loca[j][i]):# 判断该地图上是否有用户
              video_size[i] += np.sum(location[i][n]) * video_size_0[i]#计算每个MEC在该地图上的任务大小
        if i == maps[-1]:#遍历完地图就输出
            print(f'dataset of MECs{j} is {float(np.sum(video_size))}')  # 输出计算结果
 '''