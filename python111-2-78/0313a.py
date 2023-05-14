f = open("hello.dat", "a", encoding="utf-8")
for i in range(5):
    f.write("你好aa\n")
f.close()