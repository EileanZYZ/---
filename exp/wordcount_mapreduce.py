import sys
import re

def mapper():
    try:
        for line in sys.stdin:
            line = line.strip()
            if not line:
                continue
            
            # 清除非字母数字的字符，标点符号替换为空格
            cleaned_line = re.sub(r'[^a-zA-Z0-9\s]', ' ', line)
            # 将清理后的行转换为小写，并分割成单词
            words = cleaned_line.lower().split()
            
            for word in words:
                # 输出单词及计数
                print(f"{word}\t1")
    
    except Exception as e:
        sys.stderr.write(f"Error in mapper: {str(e)}\n")
        sys.exit(1)

def reducer():
    try:
        word_count = {}  # 用字典存储每个单词的计数

        for line in sys.stdin:
            line = line.strip()
            if not line:
                continue

            try:
                word, count = line.split("\t")
                count = int(count)  # 将 count 转换为整数
            except ValueError:
                continue  # 如果格式不正确，跳过该行

            # 累加单词的计数
            if word in word_count:
                word_count[word] += count
            else:
                word_count[word] = count

        # 输出所有单词及其总计数
        for word, count in word_count.items():
            print(f"{word}\t{count}")
    
    except Exception as e:
        sys.stderr.write(f"Error in reducer: {str(e)}\n")
        sys.exit(1)

if __name__ == "__main__":
    try:
        if len(sys.argv) != 2:
            sys.stderr.write("Usage error: Please provide 'mapper' or 'reducer'\n")
            sys.exit(1)

        if sys.argv[1] == "mapper":
            mapper()
        elif sys.argv[1] == "reducer":
            reducer()
        else:
            sys.stderr.write(f"Invalid argument: {sys.argv[1]}. Use 'mapper' or 'reducer'.\n")
            sys.exit(1)
    
    except Exception as e:
        sys.stderr.write(f"Error in main: {str(e)}\n")
        sys.exit(1)
