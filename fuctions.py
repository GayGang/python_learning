

# default arg value
# arg name

# variable args function

def var_args(name, *args):
    print(name)
    print(args)


var_args("dengxiaobai", 26, "Programmer")


def var_kwargs(name, **kwargs):
    print(name)
    print(kwargs["age"], kwargs["pro"])


var_kwargs(name="dengxiaobai", age=26, pro="Programmer")

"james".title()


# file operation

student_names = []
file_name = "student_names.txt"


def add_student_names(name):
    student_names.append(name)

# w : write text , cover
# r : read text
# a : add content to new or existing file
# wb: write binary file
# rb: read  binary file
def read_file():
    try:
        f = open(file_name,"r")
        for name in f.readlines():
            add_student_names(name.replace("\n", ""))
        f.close()
        print(student_names)
    except Exception:
        print("read_file failed!!")


def save_to_file():
    try:
        f = open(file_name,"a")
        for name in student_names:
            f.write(name + "\n")
        f.close()

    except Exception:
        print("save_to_file failed!!")



read_file()
for index in range(4):
    add_student_names(input("plz input name:"))
save_to_file()



add2Nums = lambda x, y : x + y


print(add2Nums(1, 5))


######### Confused  Part ############
# yield







