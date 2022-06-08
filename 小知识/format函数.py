print("{1} {0} {0}".format("hello", "world"))#输出world hello hello
print("{:.2f}".format(3.14159)) #输出3.14
print("{:0>2d}".format(5))#输出05（左边补0，宽度为2）
print("{:*<10d}".format(5))#输出5*********
print("{:0^11d}".format(5))#输出00000500000
#总结：<右对齐，>左对齐，^居中