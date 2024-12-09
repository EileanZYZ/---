from pyspark import SparkContext, SparkConf
import time
import psutil
import re  # 导入正则表达式模块

# 配置 Spark
conf = SparkConf().setAppName("WordCount") \
                  .set("spark.serializer", "org.apache.spark.serializer.KryoSerializer")

# 初始化 SparkContext
sc = SparkContext(conf=conf)

# 获取当前进程对象
process = psutil.Process()

# 记录开始时间
start_time = time.time()

# 读取 HDFS 中的文件
lines = sc.textFile("hdfs:///user/root/input.txt")

# 定义用于累加单词计数的函数
def count_words(a, b):
    return a + b

# 定义分割每一行文本为单词的函数，并清除标点符号
def word_count_func(line):
    # 清除所有非字母数字的字符，保留字母和数字
    cleaned_line = re.sub(r'[^a-zA-Z0-9\s]', '', line)
    # 将清理后的行转换为小写，并分割成单词
    words = cleaned_line.lower().split()
    return [(word, 1) for word in words]

# 执行单词计数操作
word_counts = (
    lines.flatMap(word_count_func)    # 使用 flatMap 扩展为 (word, 1) 元组
         .reduceByKey(count_words)   # 使用 reduceByKey 对每个单词计数
)

# 保存结果到 HDFS
word_counts.saveAsTextFile("hdfs:///user/root/spark_output6")

# 记录结束时间
end_time = time.time()

# 输出执行时间和资源消耗情况
print(f"Spark 执行时间: {end_time - start_time}秒")
# print(f"Spark 内存使用: {process.memory_info().rss / 1024 ** 2:.2f} MB")  # 以MB为单位
