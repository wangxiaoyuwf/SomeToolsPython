import sys, getopt


FILES_PATH = "do_format_result/"

def read_lines(path):
    f = open(path)
    while 1:
        line = f.readline()
        if len(line) == 1:
            continue
        if not line:
            break
        # print(len(line))
        replace_some_character(line)
    f.close()


def replace_some_character(str):
    file_name = str.split(" ")[1]
    if file_name.endswith("PS"):
        file_name = FILES_PATH + file_name[:-2] + ".fs"
    elif file_name.endswith("VS"):
        file_name = FILES_PATH + file_name[:-2] + ".vs"
    else:
        file_name = FILES_PATH + file_name + ".glsl"
    print("file name: ", file_name)
    str = str[:-3]
    str = str.split('= \"')[1]
    str = str.replace("\\t", "\t")
    str = str.replace("\\r\\n", "\r\n")
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
