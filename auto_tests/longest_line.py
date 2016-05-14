f = open('Test.c', 'r')
x = f.readline()
max_len = 0
biggest_line_content = ""
while x != "":
    if x.__len__() > max_len:
        max_len = x.__len__()
        biggest_line_content = x
    x = f.readline()
print(biggest_line_content)
print("len= "+str(max_len))
