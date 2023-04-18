

import random
import json
import time
import numpy as np
users = range(100)
maps = range(5)
video_size_0 = [100.0, 90.0, 80.0, 50.0, 100.0]
video_size = [0.0]*len(maps)

# 定义二元数组，表示用户和地图之间的关系
relationships = [[0] * len(users) for i in maps]#定义地图*用户（5*100）的矩阵，保证每个用户只在一个地图中
for i in users:
    pos = random.randint(0, 4)#定义用户所在地图
    relationships[pos][i] = 1#生成二元数组

# 保存到文件
timestamp = int(time.time())
file_time = time.strftime("%Y_%m_%d_%H%M%S", time.localtime(timestamp))
filename = f"relationship_{file_time}.json"
with open(filename, "w") as f:
    json.dump(relationships, f)

with open("relationship.json", "w") as f:
     json.dump(relationships, f)

print(relationships)
 # 从文件中读取
with open(filename, "r") as f:
#with open("relationship_2023_04_13_165037.json", "w") as f:
    relationships = json.load(f)
ship = np.array_split(np.array(relationships).reshape(5, -1), 20,axis=1)

# 打印所有切割后的子数组
for i in range(len(ship)):
    print(f"子数组{i+1}:")
    print(ship[i])
'''
# 定义每个MEC的任务集
# 定义5个地图的单位视频chunk大小（） M=5
video_size_0 = [100.0, 90.0, 80.0]
video_size = [0.0, 0.0, 0.0]


'users = ['user1', 'user2', 'user3', 'user4']
maps = ['map1', 'map2', 'map3']

# 定义二元数组，表示用户和地图之间的关系
relationships = [
    [1, 0, 0, 1],  # map1:user1,user4 ,
    [0, 1, 0, 0],  # map2:user2:
    [0, 0, 1, 0]   # map3:user3
]

# 输出二元数组中每个元素的取值，并计算 video_size
for i in range(len(maps)):
    for j in range(len(users)):
        if relationships[i][j]:
            video_size[i] += relationships[i][j] * video_size_0[i]
    print(f'dataset of {maps[i]} is {video_size[i]}')




users = range(100)
MECs = np.zeros((10, 5, 2), dtype=int)#(MEC,用户数量，0表示用户；1表示MEC)

for i in range(10):
    start = i * 5
    end = (i + 1) * 5
    MECs[i, :, 0] = users[start:end]
    MECs[i, :, 1] = i

print(MECs[2, :, 0])

'''