import sys, getopt
import os
import shutil


def reduce_and_copy(path, num):
    newPath = mkdir(path)
    list = os.listdir(path)
    list.sort()
    for i in range(0, len(list), num):
        imgFile = os.path.join(path, list[i])
        print("imgFile: ", imgFile)
        if os.path.isfile(imgFile):
            shutil.copy(imgFile, newPath)


def mkdir(path):
    path = path.rstrip("\/")
    path = path.rstrip("\\")
    print("path: ", path)
    pathReduced = path + "_reduced"

    # 判断路径是否存在
    isExists = os.path.exists(pathReduced)
    if not isExists:
        os.makedirs(pathReduced)
        print(pathReduced + " 创建成功！")
    else:
        print(pathReduced + " 已存在！")
        exit()
    return pathReduced


def main(argv):
    path = ""
    num = ""

    try:
        opts, args = getopt.getopt(argv, "h:f:n:", ["file=", "number="])
    except getopt.GetoptError:
        print("Please input the right command(reduce_image.py -f <filename> -n <number>)")

        sys.exit(2)

    for opt, arg in opts:
        if opt == "-h":
            print("Please input the right command(reduce_image.py -f <filename> -n <number>)")
            exit()
        elif opt in ("-f", "--file"):
            path = arg
        elif opt in ("-n", "--number"):
            num = int(arg)

    print("path: ", path)
    print("num: ", num)
    reduce_and_copy(path, num)


if __name__ == '__main__':
    main(sys.argv[1:])
