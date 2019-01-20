#输入输出
s="hello zx"
print(str(s))
print(repr(s))
input=input("请输入;")
print("您输入的内容:",input)
ifile=open("F://git//PycharmProjects//test.txt","w")
ifile.write(input)
ifile.close()
ofile=open("F://git//PycharmProjects//test.txt","r")
str=ofile.read()
print("获取文件内容:",str)
ofile.close()