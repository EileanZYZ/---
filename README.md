# 大规模数据处理系统 - 期中作业

&emsp;&emsp;&emsp; 组内成员：张倚中、雷智、程磊鑫、张炜琪

## 实验目的

比较 MapReduce 和 Spark 的性能差异，验证：Spark因为基于内存计算并将中间计算结果保存在内存中，因此其运行速度应比MapReduce要快。

## 实验细节

### 实验设计

搭建Mapreduce和Spark集群，并设计词频统计实验验证其迭代性能。

### 实验环境

- Docker 25.0.3
- JDK 1.8
- Hadoop 3.1.2
- Hive 3.1.2
- mysql 8.0.1
- mysql-connector-java-8.0.1.jar
- hive_jdbc_2.5.15.1040

### 数据集

[《浮士德》英文原文文本](www.qcenglish.com)，经过扩充，总计100万字字符。

### 环境安装

#### 拉取Docker镜像，搭建Hadoop集群

1、拉取镜像

```bash
docker pull registry.cn-hangzhou.aliyuncs.com/hadoop_test/hadoop_base
```

2、建立使用桥接模式的docker子网

```bash
docker network create --driver=bridge --subnet=172.19.0.0/16 hadoop
```

3、启动master、slave1、slave2三个容器作为集群节点

```bash
docker run -it --network  hadoop --ulimit nofile=65535 -h Slave1 --name Slave1 registry.cn-hangzhou.aliyuncs.com/hadoop_test/hadoop_base bash
docker run -it --network hadoop  --ulimit nofile=65535 -h Slave2 --name Slave2 registry.cn-hangzhou.aliyuncs.com/hadoop_test/hadoop_base bash
docker run -it --network hadoop --ulimit nofile=100000  -h Master --name Master -p 9870:9870 -p 8088:8088 -p 10000:10000 registry.cn-hangzhou.aliyuncs.com/hadoop_test/hadoop_base bash 
```

查看容器状态
![docker](/images/docker_condition.png)
4、配置ubuntu 镜像

- 备份镜像源
- 修改 `/etc/apt/sources.list`，添加国内镜像源
- 更新软件仓库
- 对三个节点的`/etc/hosts`进行修改，进行主机名映射

5、ssh配置，免密登录

- 修改`/etc/ssh/sshd_config`，增加如下字段
![shh配置](/images/ssh.png)

6、配置环境变量

- 配置`/etc/profile`，添加路径
- 配置`.bashrc`，添加以下内容：

  ```bash
  source /etc/profile
  service ssh start
  ```

- 让环境变量生效：

  ```bash
  source ~/.bashrc
  ```

7、启动Hadoop

- 初始化

```bash
hadoop namenode -format
```

- 启动服务

```bash
cd /usr/local/hadoop/sbin

start-all.sh
```

![hadoop启动](/images/start.png)

- 键入`jps`命令，查看进程

![主节点](/images/jps.png)

![从节点1](/images/jps2.png)

![从节点2](/images/jps3.png)

#### Spark 集群搭建

1、安装

- 将spark压缩包拷贝到节点

```bash
docker cp spark-3.1.2-bin-hive3.1.2.tgz Master:/root
```

- 解压

```bash
  tar -xvf /root/spark-3.1.2-bin-hive3.1.2 /usr/local/
```

- 修改文件名称

```bash
mv spark-3.1.2-bin-hive3.1.2 spark
```

2、配置环境变量

- 配置`/spark/conf/spark-env.sh`

```bash
cd spark/conf

mv spark-env.sh.template spark-env.sh
vim spark-env.sh
```

- 添加如下内容

```bash
export SPARK_DIST_CLASSPATH=$(/usr/local/hadoop/bin/hadoop classpath)
```

- 配置worker
- 将spark文件拷贝到从节点

3、启动Spark

```bash
cd /usr/local/spark/sbin/

start-all.sh

jps
```

![Spark启动](/images/spark_start.png)

#### pyspark环境配置

使用conda管理python虚拟环境
1、下载miniconda

```bash
wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh

```

2、安装miniconda

```bash
bash Miniconda3-latest-Linux-x86_64.sh
```

3、创建虚拟环境

```bash
conda create -n spark python==3.8

conda activae spark
```

4、安装必要的库，并将配置拷贝到其他节点

#### 编写word count代码
此处略。

### 实验目标

1、使用MapReduce和Spark实现目标文本的词频统计；
2、通过开始与结束的时间差值计算作业耗时，对比MapReduce和Spark的性能；

## 实验结果

### MapReduce运算结果

### Spark运算结果
输入命令
```bash
/usr/local/spark/bin/spark-submit --master spark://Master:7077 --num-executors 3 /root/wordcount_spark.py
```
![spark运算结果](/images/spark_wordcount.png)

- 部分输出结果
![spark输出结果](/images/spark_wordcount_output.png)

![spark输出结果](/images/spark_wordcount_output_part.png)

结果：spark执行时长约为9021ms。

## 组内分工
- 雷智：Spark环境搭建：贡献度25%
- 张倚中：MapReduce环境搭建：贡献度25%
- 程磊鑫：实验程序编写与运行：贡献度25%
- 张炜琪：实验设计、数据集、仓库搭建及PPT制作：贡献度25%
