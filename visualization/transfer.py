import re
import csv

# 原始数据，每一行是一个记录
log_data = """
CONTAINER ID   NAME      CPU %     MEM USAGE / LIMIT     MEM %     NET I/O          BLOCK I/O   PIDS
7c241c635ddc   Master    1.60%     3.027GiB / 15.43GiB   19.62%    8.69MB / 183MB   0B / 0B     739
CONTAINER ID   NAME      CPU %     MEM USAGE / LIMIT     MEM %     NET I/O          BLOCK I/O   PIDS
7c241c635ddc   Master    1.55%     3.027GiB / 15.43GiB   19.62%    8.69MB / 183MB   0B / 0B     739
CONTAINER ID   NAME      CPU %     MEM USAGE / LIMIT     MEM %     NET I/O          BLOCK I/O   PIDS
7c241c635ddc   Master    1.55%     3.027GiB / 15.43GiB   19.62%    8.69MB / 183MB   0B / 0B     739
CONTAINER ID   NAME      CPU %     MEM USAGE / LIMIT     MEM %     NET I/O          BLOCK I/O   PIDS
7c241c635ddc   Master    1.62%     3.027GiB / 15.43GiB   19.62%    8.69MB / 183MB   0B / 0B     739
CONTAINER ID   NAME      CPU %     MEM USAGE / LIMIT     MEM %     NET I/O          BLOCK I/O   PIDS
7c241c635ddc   Master    1.62%     3.027GiB / 15.43GiB   19.62%    8.69MB / 183MB   0B / 0B     739
CONTAINER ID   NAME      CPU %     MEM USAGE / LIMIT     MEM %     NET I/O          BLOCK I/O   PIDS
7c241c635ddc   Master    2.43%     3.028GiB / 15.43GiB   19.62%    8.69MB / 183MB   0B / 0B     740
CONTAINER ID   NAME      CPU %     MEM USAGE / LIMIT     MEM %     NET I/O          BLOCK I/O   PIDS
7c241c635ddc   Master    2.43%     3.028GiB / 15.43GiB   19.62%    8.69MB / 183MB   0B / 0B     740
CONTAINER ID   NAME      CPU %     MEM USAGE / LIMIT     MEM %     NET I/O          BLOCK I/O   PIDS
7c241c635ddc   Master    1.50%     3.027GiB / 15.43GiB   19.62%    8.69MB / 183MB   0B / 0B     740
CONTAINER ID   NAME      CPU %     MEM USAGE / LIMIT     MEM %     NET I/O          BLOCK I/O   PIDS
7c241c635ddc   Master    1.50%     3.027GiB / 15.43GiB   19.62%    8.69MB / 183MB   0B / 0B     740
CONTAINER ID   NAME      CPU %     MEM USAGE / LIMIT     MEM %     NET I/O          BLOCK I/O   PIDS
7c241c635ddc   Master    1.40%     3.027GiB / 15.43GiB   19.62%    8.69MB / 183MB   0B / 0B     740
CONTAINER ID   NAME      CPU %     MEM USAGE / LIMIT     MEM %     NET I/O          BLOCK I/O   PIDS
7c241c635ddc   Master    1.40%     3.027GiB / 15.43GiB   19.62%    8.69MB / 183MB   0B / 0B     740
CONTAINER ID   NAME      CPU %     MEM USAGE / LIMIT     MEM %     NET I/O          BLOCK I/O   PIDS
7c241c635ddc   Master    1.74%     3.027GiB / 15.43GiB   19.62%    8.69MB / 183MB   0B / 0B     740
CONTAINER ID   NAME      CPU %     MEM USAGE / LIMIT     MEM %     NET I/O          BLOCK I/O   PIDS
7c241c635ddc   Master    1.74%     3.027GiB / 15.43GiB   19.62%    8.69MB / 183MB   0B / 0B     740
CONTAINER ID   NAME      CPU %     MEM USAGE / LIMIT     MEM %     NET I/O         BLOCK I/O   PIDS
7c241c635ddc   Master    1.62%     3.027GiB / 15.43GiB   19.62%    8.7MB / 183MB   0B / 0B     740
CONTAINER ID   NAME      CPU %     MEM USAGE / LIMIT     MEM %     NET I/O         BLOCK I/O   PIDS
7c241c635ddc   Master    1.62%     3.027GiB / 15.43GiB   19.62%    8.7MB / 183MB   0B / 0B     740
CONTAINER ID   NAME      CPU %     MEM USAGE / LIMIT     MEM %     NET I/O         BLOCK I/O   PIDS
7c241c635ddc   Master    1.56%     3.027GiB / 15.43GiB   19.62%    8.7MB / 183MB   0B / 0B     740
CONTAINER ID   NAME      CPU %     MEM USAGE / LIMIT     MEM %     NET I/O         BLOCK I/O   PIDS
7c241c635ddc   Master    1.56%     3.027GiB / 15.43GiB   19.62%    8.7MB / 183MB   0B / 0B     740
CONTAINER ID   NAME      CPU %     MEM USAGE / LIMIT     MEM %     NET I/O         BLOCK I/O   PIDS
7c241c635ddc   Master    1.53%     3.027GiB / 15.43GiB   19.62%    8.7MB / 183MB   0B / 0B     740
CONTAINER ID   NAME      CPU %     MEM USAGE / LIMIT     MEM %     NET I/O         BLOCK I/O   PIDS
7c241c635ddc   Master    1.53%     3.027GiB / 15.43GiB   19.62%    8.7MB / 183MB   0B / 0B     740
CONTAINER ID   NAME      CPU %     MEM USAGE / LIMIT     MEM %     NET I/O         BLOCK I/O   PIDS
7c241c635ddc   Master    1.62%     3.027GiB / 15.43GiB   19.62%    8.7MB / 183MB   0B / 0B     740
CONTAINER ID   NAME      CPU %     MEM USAGE / LIMIT     MEM %     NET I/O         BLOCK I/O   PIDS
7c241c635ddc   Master    1.62%     3.027GiB / 15.43GiB   19.62%    8.7MB / 183MB   0B / 0B     740
CONTAINER ID   NAME      CPU %     MEM USAGE / LIMIT     MEM %     NET I/O         BLOCK I/O   PIDS
7c241c635ddc   Master    1.36%     3.027GiB / 15.43GiB   19.62%    8.7MB / 183MB   0B / 0B     740
CONTAINER ID   NAME      CPU %     MEM USAGE / LIMIT     MEM %     NET I/O         BLOCK I/O   PIDS
7c241c635ddc   Master    1.36%     3.027GiB / 15.43GiB   19.62%    8.7MB / 183MB   0B / 0B     740
CONTAINER ID   NAME      CPU %     MEM USAGE / LIMIT     MEM %     NET I/O         BLOCK I/O   PIDS
7c241c635ddc   Master    23.98%    3.061GiB / 15.43GiB   19.84%    8.7MB / 183MB   0B / 0B     774
CONTAINER ID   NAME      CPU %     MEM USAGE / LIMIT     MEM %     NET I/O         BLOCK I/O   PIDS
7c241c635ddc   Master    23.98%    3.061GiB / 15.43GiB   19.84%    8.7MB / 183MB   0B / 0B     774
CONTAINER ID   NAME      CPU %     MEM USAGE / LIMIT     MEM %     NET I/O         BLOCK I/O   PIDS
7c241c635ddc   Master    252.82%   3.195GiB / 15.43GiB   20.71%    8.7MB / 183MB   0B / 0B     779
CONTAINER ID   NAME      CPU %     MEM USAGE / LIMIT     MEM %     NET I/O         BLOCK I/O   PIDS
7c241c635ddc   Master    252.82%   3.195GiB / 15.43GiB   20.71%    8.7MB / 183MB   0B / 0B     779
CONTAINER ID   NAME      CPU %     MEM USAGE / LIMIT     MEM %     NET I/O          BLOCK I/O   PIDS
7c241c635ddc   Master    153.46%   3.287GiB / 15.43GiB   21.30%    8.72MB / 184MB   0B / 0B     784
CONTAINER ID   NAME      CPU %     MEM USAGE / LIMIT     MEM %     NET I/O          BLOCK I/O   PIDS
7c241c635ddc   Master    153.46%   3.287GiB / 15.43GiB   21.30%    8.72MB / 184MB   0B / 0B     784
CONTAINER ID   NAME      CPU %     MEM USAGE / LIMIT     MEM %     NET I/O          BLOCK I/O   PIDS
7c241c635ddc   Master    3.67%     3.287GiB / 15.43GiB   21.30%    8.72MB / 184MB   0B / 0B     784
CONTAINER ID   NAME      CPU %     MEM USAGE / LIMIT     MEM %     NET I/O          BLOCK I/O   PIDS
7c241c635ddc   Master    3.67%     3.287GiB / 15.43GiB   21.30%    8.72MB / 184MB   0B / 0B     784
CONTAINER ID   NAME      CPU %     MEM USAGE / LIMIT     MEM %     NET I/O          BLOCK I/O   PIDS
7c241c635ddc   Master    3.14%     3.289GiB / 15.43GiB   21.32%    8.72MB / 184MB   0B / 0B     784
CONTAINER ID   NAME      CPU %     MEM USAGE / LIMIT     MEM %     NET I/O          BLOCK I/O   PIDS
7c241c635ddc   Master    3.14%     3.289GiB / 15.43GiB   21.32%    8.72MB / 184MB   0B / 0B     784
CONTAINER ID   NAME      CPU %     MEM USAGE / LIMIT     MEM %     NET I/O          BLOCK I/O   PIDS
7c241c635ddc   Master    7.01%     3.284GiB / 15.43GiB   21.29%    8.96MB / 184MB   0B / 0B     785
CONTAINER ID   NAME      CPU %     MEM USAGE / LIMIT     MEM %     NET I/O          BLOCK I/O   PIDS
7c241c635ddc   Master    7.01%     3.284GiB / 15.43GiB   21.29%    8.96MB / 184MB   0B / 0B     785
CONTAINER ID   NAME      CPU %     MEM USAGE / LIMIT     MEM %     NET I/O          BLOCK I/O   PIDS
7c241c635ddc   Master    4.01%     3.285GiB / 15.43GiB   21.29%    8.96MB / 184MB   0B / 0B     784
CONTAINER ID   NAME      CPU %     MEM USAGE / LIMIT     MEM %     NET I/O          BLOCK I/O   PIDS
7c241c635ddc   Master    4.01%     3.285GiB / 15.43GiB   21.29%    8.96MB / 184MB   0B / 0B     784
CONTAINER ID   NAME      CPU %     MEM USAGE / LIMIT     MEM %     NET I/O          BLOCK I/O   PIDS
7c241c635ddc   Master    296.12%   3.461GiB / 15.43GiB   22.43%    8.97MB / 184MB   0B / 0B     873
CONTAINER ID   NAME      CPU %     MEM USAGE / LIMIT     MEM %     NET I/O          BLOCK I/O   PIDS
7c241c635ddc   Master    296.12%   3.461GiB / 15.43GiB   22.43%    8.97MB / 184MB   0B / 0B     873
CONTAINER ID   NAME      CPU %     MEM USAGE / LIMIT     MEM %     NET I/O          BLOCK I/O   PIDS
7c241c635ddc   Master    559.25%   3.885GiB / 15.43GiB   25.18%    8.98MB / 184MB   0B / 0B     899
CONTAINER ID   NAME      CPU %     MEM USAGE / LIMIT     MEM %     NET I/O          BLOCK I/O   PIDS
7c241c635ddc   Master    559.25%   3.885GiB / 15.43GiB   25.18%    8.98MB / 184MB   0B / 0B     899
CONTAINER ID   NAME      CPU %     MEM USAGE / LIMIT     MEM %     NET I/O          BLOCK I/O   PIDS
7c241c635ddc   Master    348.48%   3.898GiB / 15.43GiB   25.27%    8.98MB / 184MB   0B / 0B     899
CONTAINER ID   NAME      CPU %     MEM USAGE / LIMIT     MEM %     NET I/O          BLOCK I/O   PIDS
7c241c635ddc   Master    348.48%   3.898GiB / 15.43GiB   25.27%    8.98MB / 184MB   0B / 0B     899
CONTAINER ID   NAME      CPU %     MEM USAGE / LIMIT     MEM %     NET I/O          BLOCK I/O   PIDS
7c241c635ddc   Master    466.87%   3.904GiB / 15.43GiB   25.30%    8.98MB / 184MB   0B / 0B     897
CONTAINER ID   NAME      CPU %     MEM USAGE / LIMIT     MEM %     NET I/O          BLOCK I/O   PIDS
7c241c635ddc   Master    466.87%   3.904GiB / 15.43GiB   25.30%    8.98MB / 184MB   0B / 0B     897
CONTAINER ID   NAME      CPU %     MEM USAGE / LIMIT     MEM %     NET I/O          BLOCK I/O   PIDS
7c241c635ddc   Master    202.95%   3.904GiB / 15.43GiB   25.30%    8.99MB / 184MB   0B / 0B     897
CONTAINER ID   NAME      CPU %     MEM USAGE / LIMIT     MEM %     NET I/O          BLOCK I/O   PIDS
7c241c635ddc   Master    202.95%   3.904GiB / 15.43GiB   25.30%    8.99MB / 184MB   0B / 0B     897
CONTAINER ID   NAME      CPU %     MEM USAGE / LIMIT     MEM %     NET I/O          BLOCK I/O   PIDS
7c241c635ddc   Master    216.88%   3.905GiB / 15.43GiB   25.31%    8.99MB / 184MB   0B / 0B     895
CONTAINER ID   NAME      CPU %     MEM USAGE / LIMIT     MEM %     NET I/O          BLOCK I/O   PIDS
7c241c635ddc   Master    216.88%   3.905GiB / 15.43GiB   25.31%    8.99MB / 184MB   0B / 0B     895
CONTAINER ID   NAME      CPU %     MEM USAGE / LIMIT     MEM %     NET I/O          BLOCK I/O   PIDS
7c241c635ddc   Master    305.20%   3.902GiB / 15.43GiB   25.29%    8.99MB / 184MB   0B / 0B     892
CONTAINER ID   NAME      CPU %     MEM USAGE / LIMIT     MEM %     NET I/O          BLOCK I/O   PIDS
7c241c635ddc   Master    305.20%   3.902GiB / 15.43GiB   25.29%    8.99MB / 184MB   0B / 0B     892
CONTAINER ID   NAME      CPU %     MEM USAGE / LIMIT     MEM %     NET I/O          BLOCK I/O   PIDS
7c241c635ddc   Master    206.74%   3.899GiB / 15.43GiB   25.27%    8.99MB / 184MB   0B / 0B     889
CONTAINER ID   NAME      CPU %     MEM USAGE / LIMIT     MEM %     NET I/O          BLOCK I/O   PIDS
7c241c635ddc   Master    206.74%   3.899GiB / 15.43GiB   25.27%    8.99MB / 184MB   0B / 0B     889
CONTAINER ID   NAME      CPU %     MEM USAGE / LIMIT     MEM %     NET I/O          BLOCK I/O   PIDS
7c241c635ddc   Master    232.84%   3.906GiB / 15.43GiB   25.32%    8.99MB / 184MB   0B / 0B     889
CONTAINER ID   NAME      CPU %     MEM USAGE / LIMIT     MEM %     NET I/O          BLOCK I/O   PIDS
7c241c635ddc   Master    232.84%   3.906GiB / 15.43GiB   25.32%    8.99MB / 184MB   0B / 0B     889
CONTAINER ID   NAME      CPU %     MEM USAGE / LIMIT     MEM %     NET I/O       BLOCK I/O   PIDS
7c241c635ddc   Master    225.00%   3.911GiB / 15.43GiB   25.35%    9MB / 184MB   0B / 0B     894
CONTAINER ID   NAME      CPU %     MEM USAGE / LIMIT     MEM %     NET I/O       BLOCK I/O   PIDS
7c241c635ddc   Master    225.00%   3.911GiB / 15.43GiB   25.35%    9MB / 184MB   0B / 0B     894
CONTAINER ID   NAME      CPU %     MEM USAGE / LIMIT    MEM %     NET I/O          BLOCK I/O   PIDS
7c241c635ddc   Master    181.43%   3.92GiB / 15.43GiB   25.41%    9.02MB / 184MB   0B / 0B     884
CONTAINER ID   NAME      CPU %     MEM USAGE / LIMIT    MEM %     NET I/O          BLOCK I/O   PIDS
7c241c635ddc   Master    181.43%   3.92GiB / 15.43GiB   25.41%    9.02MB / 184MB   0B / 0B     884
CONTAINER ID   NAME      CPU %     MEM USAGE / LIMIT     MEM %     NET I/O          BLOCK I/O   PIDS
7c241c635ddc   Master    16.80%    3.304GiB / 15.43GiB   21.41%    9.02MB / 184MB   0B / 0B     788
CONTAINER ID   NAME      CPU %     MEM USAGE / LIMIT     MEM %     NET I/O          BLOCK I/O   PIDS
7c241c635ddc   Master    16.80%    3.304GiB / 15.43GiB   21.41%    9.02MB / 184MB   0B / 0B     788
CONTAINER ID   NAME      CPU %     MEM USAGE / LIMIT     MEM %     NET I/O          BLOCK I/O   PIDS
7c241c635ddc   Master    3.40%     3.304GiB / 15.43GiB   21.41%    9.03MB / 184MB   0B / 0B     788
CONTAINER ID   NAME      CPU %     MEM USAGE / LIMIT     MEM %     NET I/O          BLOCK I/O   PIDS
7c241c635ddc   Master    3.40%     3.304GiB / 15.43GiB   21.41%    9.03MB / 184MB   0B / 0B     788
CONTAINER ID   NAME      CPU %     MEM USAGE / LIMIT     MEM %     NET I/O          BLOCK I/O   PIDS
7c241c635ddc   Master    176.67%   3.434GiB / 15.43GiB   22.25%    9.03MB / 184MB   0B / 0B     830
CONTAINER ID   NAME      CPU %     MEM USAGE / LIMIT     MEM %     NET I/O          BLOCK I/O   PIDS
7c241c635ddc   Master    176.67%   3.434GiB / 15.43GiB   22.25%    9.03MB / 184MB   0B / 0B     830
CONTAINER ID   NAME      CPU %     MEM USAGE / LIMIT     MEM %     NET I/O          BLOCK I/O   PIDS
7c241c635ddc   Master    206.42%   3.537GiB / 15.43GiB   22.92%    9.04MB / 184MB   0B / 0B     833
CONTAINER ID   NAME      CPU %     MEM USAGE / LIMIT     MEM %     NET I/O          BLOCK I/O   PIDS
7c241c635ddc   Master    206.42%   3.537GiB / 15.43GiB   22.92%    9.04MB / 184MB   0B / 0B     833
CONTAINER ID   NAME      CPU %     MEM USAGE / LIMIT     MEM %     NET I/O          BLOCK I/O   PIDS
7c241c635ddc   Master    103.41%   3.538GiB / 15.43GiB   22.93%    9.04MB / 184MB   0B / 0B     833
CONTAINER ID   NAME      CPU %     MEM USAGE / LIMIT     MEM %     NET I/O          BLOCK I/O   PIDS
7c241c635ddc   Master    103.41%   3.538GiB / 15.43GiB   22.93%    9.04MB / 184MB   0B / 0B     833
CONTAINER ID   NAME      CPU %     MEM USAGE / LIMIT     MEM %     NET I/O          BLOCK I/O   PIDS
7c241c635ddc   Master    103.25%   3.539GiB / 15.43GiB   22.94%    9.04MB / 184MB   0B / 0B     833
CONTAINER ID   NAME      CPU %     MEM USAGE / LIMIT     MEM %     NET I/O          BLOCK I/O   PIDS
7c241c635ddc   Master    103.25%   3.539GiB / 15.43GiB   22.94%    9.04MB / 184MB   0B / 0B     833
CONTAINER ID   NAME      CPU %     MEM USAGE / LIMIT    MEM %     NET I/O          BLOCK I/O   PIDS
7c241c635ddc   Master    192.21%   3.56GiB / 15.43GiB   23.07%    9.05MB / 184MB   0B / 0B     843
CONTAINER ID   NAME      CPU %     MEM USAGE / LIMIT    MEM %     NET I/O          BLOCK I/O   PIDS
7c241c635ddc   Master    192.21%   3.56GiB / 15.43GiB   23.07%    9.05MB / 184MB   0B / 0B     843
CONTAINER ID   NAME      CPU %     MEM USAGE / LIMIT    MEM %     NET I/O          BLOCK I/O   PIDS
7c241c635ddc   Master    152.31%   3.56GiB / 15.43GiB   23.07%    9.05MB / 184MB   0B / 0B     843
CONTAINER ID   NAME      CPU %     MEM USAGE / LIMIT    MEM %     NET I/O          BLOCK I/O   PIDS
7c241c635ddc   Master    152.31%   3.56GiB / 15.43GiB   23.07%    9.05MB / 184MB   0B / 0B     843
CONTAINER ID   NAME      CPU %     MEM USAGE / LIMIT    MEM %     NET I/O          BLOCK I/O   PIDS
7c241c635ddc   Master    149.81%   3.56GiB / 15.43GiB   23.07%    9.05MB / 184MB   0B / 0B     843
CONTAINER ID   NAME      CPU %     MEM USAGE / LIMIT    MEM %     NET I/O          BLOCK I/O   PIDS
7c241c635ddc   Master    149.81%   3.56GiB / 15.43GiB   23.07%    9.05MB / 184MB   0B / 0B     843
CONTAINER ID   NAME      CPU %     MEM USAGE / LIMIT     MEM %     NET I/O          BLOCK I/O   PIDS
7c241c635ddc   Master    150.62%   3.562GiB / 15.43GiB   23.08%    9.05MB / 184MB   0B / 0B     843
CONTAINER ID   NAME      CPU %     MEM USAGE / LIMIT     MEM %     NET I/O          BLOCK I/O   PIDS
7c241c635ddc   Master    150.62%   3.562GiB / 15.43GiB   23.08%    9.05MB / 184MB   0B / 0B     843
CONTAINER ID   NAME      CPU %     MEM USAGE / LIMIT     MEM %     NET I/O          BLOCK I/O   PIDS
7c241c635ddc   Master    150.95%   3.562GiB / 15.43GiB   23.09%    9.05MB / 184MB   0B / 0B     843
CONTAINER ID   NAME      CPU %     MEM USAGE / LIMIT     MEM %     NET I/O          BLOCK I/O   PIDS
7c241c635ddc   Master    150.95%   3.562GiB / 15.43GiB   23.09%    9.05MB / 184MB   0B / 0B     843
CONTAINER ID   NAME      CPU %     MEM USAGE / LIMIT     MEM %     NET I/O          BLOCK I/O   PIDS
7c241c635ddc   Master    151.94%   3.562GiB / 15.43GiB   23.09%    9.06MB / 184MB   0B / 0B     843
CONTAINER ID   NAME      CPU %     MEM USAGE / LIMIT     MEM %     NET I/O          BLOCK I/O   PIDS
7c241c635ddc   Master    151.94%   3.562GiB / 15.43GiB   23.09%    9.06MB / 184MB   0B / 0B     843
CONTAINER ID   NAME      CPU %     MEM USAGE / LIMIT     MEM %     NET I/O          BLOCK I/O   PIDS
7c241c635ddc   Master    139.45%   3.579GiB / 15.43GiB   23.20%    9.35MB / 184MB   0B / 0B     833
CONTAINER ID   NAME      CPU %     MEM USAGE / LIMIT     MEM %     NET I/O          BLOCK I/O   PIDS
7c241c635ddc   Master    139.45%   3.579GiB / 15.43GiB   23.20%    9.35MB / 184MB   0B / 0B     833
CONTAINER ID   NAME      CPU %     MEM USAGE / LIMIT   MEM %     NET I/O          BLOCK I/O   PIDS
7c241c635ddc   Master    6.97%     3.3GiB / 15.43GiB   21.39%    9.35MB / 184MB   0B / 0B     786
CONTAINER ID   NAME      CPU %     MEM USAGE / LIMIT   MEM %     NET I/O          BLOCK I/O   PIDS
7c241c635ddc   Master    6.97%     3.3GiB / 15.43GiB   21.39%    9.35MB / 184MB   0B / 0B     786
CONTAINER ID   NAME      CPU %     MEM USAGE / LIMIT     MEM %     NET I/O          BLOCK I/O   PIDS
7c241c635ddc   Master    11.30%    3.047GiB / 15.43GiB   19.75%    9.36MB / 184MB   0B / 0B     746
CONTAINER ID   NAME      CPU %     MEM USAGE / LIMIT     MEM %     NET I/O          BLOCK I/O   PIDS
7c241c635ddc   Master    11.30%    3.047GiB / 15.43GiB   19.75%    9.36MB / 184MB   0B / 0B     746
CONTAINER ID   NAME      CPU %     MEM USAGE / LIMIT     MEM %     NET I/O          BLOCK I/O   PIDS
7c241c635ddc   Master    1.71%     3.046GiB / 15.43GiB   19.74%    9.36MB / 184MB   0B / 0B     746
CONTAINER ID   NAME      CPU %     MEM USAGE / LIMIT     MEM %     NET I/O          BLOCK I/O   PIDS
7c241c635ddc   Master    1.71%     3.046GiB / 15.43GiB   19.74%    9.36MB / 184MB   0B / 0B     746
CONTAINER ID   NAME      CPU %     MEM USAGE / LIMIT     MEM %     NET I/O          BLOCK I/O   PIDS
7c241c635ddc   Master    1.39%     3.046GiB / 15.43GiB   19.74%    9.36MB / 184MB   0B / 0B     746
"""

# 使用正则表达式提取信息
pattern = re.compile(r'([a-f0-9]+)\s+([A-Za-z0-9]+)\s+([0-9.]+%)\s+([0-9.]+[GMK]iB)\s*/\s*([0-9.]+[GMK]iB)\s+([0-9.]+%)\s+([0-9.]+MB)\s*/\s*([0-9.]+MB)\s+([0-9]+)')

# 匹配所有记录
matches = pattern.findall(log_data)

# 输出到 CSV 文件
with open('container_stats.csv', 'w', newline='') as csvfile:
    fieldnames = ['CONTAINER ID', 'NAME', 'CPU %', 'MEM USAGE', 'MEM LIMIT', 'MEM %', 'NET I/O', 'BLOCK I/O', 'PIDS']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()  # 写入表头
    for match in matches:
        # 写入每条记录
        writer.writerow({
            'CONTAINER ID': match[0],
            'NAME': match[1],
            'CPU %': match[2],
            'MEM USAGE': match[3],
            'MEM LIMIT': match[4],
            'MEM %': match[5],
            'NET I/O': f"{match[6]} / {match[7]}",  # 将 NET I/O 和 BLOCK I/O 合并
            'BLOCK I/O': '0B / 0B',
            'PIDS': match[8]
        })

print("CSV 文件已生成：container_stats.csv")
