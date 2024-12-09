# import matplotlib.pyplot as plt
# import pandas as pd
# from datetime import datetime

# # 示例数据（请根据实际数据进行替换）
# data = [
#     ("a3ac8972e5bb", "Master", 146.63, 2.65, 7.761, 34.15, 10.7, 93.2),
#     ("a3ac8972e5bb", "Master", 146.43, 2.652, 7.761, 34.18, 10.7, 93.2),
#     ("a3ac8972e5bb", "Master", 142.46, 2.653, 7.761, 34.18, 10.7, 93.2),
#     ("a3ac8972e5bb", "Master", 142.46, 2.653, 7.761, 34.18, 10.7, 93.2),
#     ("a3ac8972e5bb", "Master", 144.92, 2.653, 7.761, 34.18, 10.7, 93.2),
#     ("a3ac8972e5bb", "Master", 144.92, 2.653, 7.761, 34.18, 10.7, 93.2),
#     ("a3ac8972e5bb", "Master", 145.33, 2.653, 7.761, 34.18, 10.7, 93.2),
#     ("a3ac8972e5bb", "Master", 145.33, 2.653, 7.761, 34.18, 10.7, 93.2),
#     ("a3ac8972e5bb", "Master", 127.83, 2.646, 7.761, 34.09, 10.7, 93.2),
#     ("a3ac8972e5bb", "Master", 127.83, 2.646, 7.761, 34.09, 10.7, 93.2),
#     ("a3ac8972e5bb", "Master", 14.56, 2.377, 7.761, 30.63, 11, 93.2),
#     ("a3ac8972e5bb", "Master", 14.56, 2.377, 7.761, 30.63, 11, 93.2),
#     ("a3ac8972e5bb", "Master", 8.78, 2.153, 7.761, 27.74, 11, 93.2),
#     ("a3ac8972e5bb", "Master", 8.78, 2.153, 7.761, 27.74, 11, 93.2),
#     ("a3ac8972e5bb", "Master", 1.64, 2.153, 7.761, 27.74, 11, 93.2),
#     ("a3ac8972e5bb", "Master", 1.64, 2.153, 7.761, 27.74, 11, 93.2),
#     ("a3ac8972e5bb", "Master", 1.28, 2.153, 7.761, 27.74, 11, 93.2),
#     ("a3ac8972e5bb", "Master", 0.99, 2.153, 7.761, 27.74, 11, 93.2),
#     ("a3ac8972e5bb", "Master", 0.99, 2.153, 7.761, 27.74, 11, 93.2),
#     ("a3ac8972e5bb", "Master", 1.61, 2.153, 7.761, 27.74, 11, 93.2),
#     ("a3ac8972e5bb", "Master", 1.61, 2.153, 7.761, 27.74, 11, 93.2),
#     ("a3ac8972e5bb", "Master", 3.29, 2.158, 7.761, 27.81, 11, 93.2),
#     ("a3ac8972e5bb", "Master", 3.29, 2.158, 7.761, 27.81, 11, 93.2),
# ]

# # 将数据转化为 pandas DataFrame
# df = pd.DataFrame(data, columns=["CONTAINER_ID", "NAME", "CPU%", "MEM_USAGE", "MEM_LIMIT", "MEM%", "NET_IO", "BLOCK_IO"])

# # 处理数据，添加时间戳，作为横坐标
# df['Timestamp'] = pd.date_range(start=datetime.now(), periods=len(df), freq='S')

# # 绘制折线图
# plt.figure(figsize=(10, 6))

# # CPU 使用率折线图
# plt.subplot(2, 1, 1)
# plt.plot(df['Timestamp'], df['CPU%'], label='CPU Usage (%)', color='tab:red')
# plt.title('Container CPU Usage Over Time')
# plt.xlabel('Time')
# plt.ylabel('CPU Usage (%)')
# plt.xticks(rotation=45)
# plt.grid(True)

# # 内存使用率折线图
# plt.subplot(2, 1, 2)
# plt.plot(df['Timestamp'], df['MEM%'], label='Memory Usage (%)', color='tab:blue')
# plt.title('Container Memory Usage Over Time')
# plt.xlabel('Time')
# plt.ylabel('Memory Usage (%)')
# plt.xticks(rotation=45)
# plt.grid(True)

# plt.tight_layout()
# plt.show()

import matplotlib.pyplot as plt
import pandas as pd

# 从 CSV 文件读取数据
file_path = r"....\container_stats.csv"  # 替换为实际的文件路径

# 读取 CSV 文件
df = pd.read_csv(file_path)

# 提取 CPU 和 MEM 使用率列，并转换为浮动值
df['CPU %'] = df['CPU %'].str.replace('%', '').astype(float)  # 去除百分号并转换为浮动数值
df['MEM %'] = df['MEM %'].str.replace('%', '').astype(float)  # 去除百分号并转换为浮动数值

# 创建一个整数序列作为横坐标，表示时间间隔（单位：秒）
df['Time Interval (s)'] = range(len(df))

# 绘制图形
plt.figure(figsize=(10, 6))

# 绘制 CPU 使用率
plt.plot(df['Time Interval (s)'], df['CPU %'], marker='o', color='b',markersize=2, label="CPU Usage (%)")

# 绘制内存使用率
plt.plot(df['Time Interval (s)'], df['MEM %'], marker='x', color='r',markersize=2, label="Memory Usage (%)")

# 设置图形标题和标签
plt.xlabel("Time Interval (s)")  # 横坐标标签
plt.ylabel("Usage (%)")  # 纵坐标标签
plt.title("Spark -- CPU and Memory Usage Over Time")  # 图形标题
plt.grid(True)  # 显示网格
plt.legend()  # 显示图例

# 显示图形
plt.show()
