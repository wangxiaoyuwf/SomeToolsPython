# SomeToolsPython
整合了自己写的一些小工具

1. reduce_image： 均匀的选出很多张序列帧图片中的N分之一

   运行示范例：

   python3 reduce_image.py -f 平面赛博/赛博朋克箭头2/ -n 10


2. do_format: original.txt中是一些加了特殊符号的代码，其中每一行是一个文件，这个工具是把引号中的代码拿出来，把\r\n变成换行，\t变成tab，\\"变成"。然后保存在var = xxxx的xxxx文件中。

   其中，文件名以PS结尾的，文件名去掉PS，后缀为.fs

   文件名以VS结尾的，文件名去掉VS，后缀为.vs

   其他的，后缀为.glsl

   运行范例：

   python3 do_format.py -f original.txt

   结果会保存在do_format_result这个文件夹下面