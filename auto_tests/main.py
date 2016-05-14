import random

percentage_chance = 5
stop_chance = 20
stop_chance_2 = 5
chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
         'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
         'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '!', '@', '#', '$',
         ';', '&', '*']
types = ['d', 'f', 'u', 'x', 's', 'c']
temp_list = []
f = open('Test.c', 'w')
f.write('#include <stdio.h>\n#include <stdlib.h>\n#include "snprintf.h"\n#include <string.h>\n#include <stdint.h>\n')
f.write('\n#define ARR_SIZE 100\n\nint main(){\n   char my_arr[ARR_SIZE];\n   int32_t my_res;\n   '
        'char c_arr[ARR_SIZE];\n   int32_t c_res;\n\n')


def rnd_str():
    my_str = ""
    while random.randint(0, stop_chance_2) != 0:
        my_str += str(chars[random.randint(0, chars.__len__() - 1)])
    return my_str


def get_str():
    temp_list.clear()
    my_str = ""
    while random.randint(0, stop_chance) != 0:
        if random.randint(0, percentage_chance) != 0:
            my_str += str(chars[random.randint(0, chars.__len__()-1)])
        else:
            my_str += '%'
            curr_type = types[random.randint(0, types.__len__()-1)]
            my_str += curr_type
            if curr_type == 'd':
                temp_list.append(random.randint(-9999999, 9999999))
            elif curr_type == 'f':
                temp_list.append(random.uniform(-9999999, 9999999))
            elif curr_type == 'u' or curr_type == 'x':
                temp_list.append(random.randint(0, 100))
            elif curr_type == 'c':
                temp_list.append('\''+chars[random.randint(0, chars.__len__()-1)]+'\'')
            elif curr_type == 's':
                temp_list.append('"'+rnd_str()+'"')
    return my_str


def write_tests(n):
    for i in range(n):
        temp_srt = get_str()
        f.write('   my_res=mysnprintf(my_arr,ARR_SIZE,"')
        f.write(temp_srt)
        f.write('"')
        for var in temp_list:
            f.write(",")
            f.write(str(var))
        f.write(');\n')
        f.write('   c_res=snprintf(c_arr,ARR_SIZE,"')
        temp_srt = temp_srt.replace("%f", "%.3f")
        f.write(temp_srt)
        f.write('"')
        for var in temp_list:
            f.write(",")
            f.write(str(var))
        f.write(');\n')
        f.write('   if( my_res != c_res || strcmp(my_arr, c_arr) ) printf("err in (%s:%d).\\n", __FILE__, __LINE__);'
                '\n\n')

write_tests(1000000)

f.write('	return 0;\n}\n')
