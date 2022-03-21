import sys, getopt


# 定义保存运行结果的路径
FILES_PATH = "do_format_result/"


# 逐行读取，并把读到的整行交给replace_some_character方法
def read_lines(path):
    f = open(path)
    while 1:
        line = f.readline()
        if len(line) == 1:
            continue
        if not line:
            break
        # print(len(line))
        # 替换一些字符，并且保存成代码文件
        replace_some_character(line)
    f.close()


# 替换换行，tab, \"等特殊字符，并且保存在文件中
# var BlitScreenPS = "#if defined 为例。去掉后缀PS， BlitScreen是文件名，如果是PS结尾的，后缀为.fs
# VS结尾的，后缀名为.vs,其他的，文件名不变，后缀为.glsl
def replace_some_character(str):
    # 字符串经过处理后，拿到文件名
    # 文件名为.fs .vs 或 .glsl
    file_name = str.split(" ")[1]
    if file_name.endswith("PS"):
        file_name = FILES_PATH + file_name[:-2] + ".fs"
    elif file_name.endswith("VS"):
        file_name = FILES_PATH + file_name[:-2] + ".vs"
    else:
        file_name = FILES_PATH + file_name + ".glsl"
    print("file name: ", file_name)
    # 把最后的三个字符（";还有换行符）去掉
    str = str[:-3]
    # 把第一个引号前面的内容去掉
    str = str.split('= \"')[1]
    # \t 替换成 tab
    str = str.replace("\\t", "\t")
    # \r\n 替换成换行
    str = str.replace("\\r\\n", "\r\n")
    # \" 替换成"
    str = str.replace('\\"', '\"')
    # print(str)
    # 把内容写入文件
    with open(file_name, 'w', encoding='utf-8') as f:
        f.write(str)
    f.close()


def main(argv):
    path = ""

    try:
        opts, args = getopt.getopt(argv, "h:f:", ["file="])
    except getopt.GetoptError:
        print("Please input the right command(do_format.py -f <filename>)")

        sys.exit(2)

    for opt, arg in opts:
        if opt == "-h":
            print("Please input the right command(do_format.py -f <filename>)")
            exit()
        elif opt in ("-f", "--file"):
            path = arg
    read_lines(path)


if __name__ == '__main__':
    main(sys.argv[1:])
