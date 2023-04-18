import random
import time
import json
users = range(100)
maps = range(5)
# 定义二元数组，表示用户和地图之间的关系
location = [[0] * len(users) for i in maps]#定义地图*用户（5*100）的矩阵，保证每个用户只在一个地图中
for i in users:
    pos = random.randint(0, 4)#定义用户所在地图
    location[pos][i] = 1#生成二元数组

# 保存到文件
timestamp = int(time.time())
file_time = time.strftime("%Y_%m_%d_%H%M%S", time.localtime(timestamp))
filename = f"location_{file_time}.json"
with open(filename, "w") as f:
    json.dump(location, f)

with open("relationship.json", "w") as f:
     json.dump(location, f)

 # 从文件中读取
with open(filename, "r") as f:
#with open("relationship_2023_04_13_165037.json", "w") as f:
    location = json.load(f)