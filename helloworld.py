print("hello world again")

answer = 42
name = "DengXiaoBai"

print(answer)


# String
isDigit = "123".isdigit()
splitedList = "some,css,table".split()
print(splitedList)

result = "Nice to meet you {0},my answer is {1}".format(name,answer)
print(result)
result = f"Nice to meet you {name},my answer is {answer}"
print(result)

# Boolean and None


# if statement, using : replace {} enrolling block
# true and false values,just lick OC
if 0:
    print("0 is true")
else:
    print("0 is false")

if 0 and 1:
    print("0 and 1 is true")

if 0 or 1:
    print("0 or 1 is true")

if not 0 and 1:
    print("0 and 1 is not true")


for element in splitedList:
    print(element)


# for loops
# 实际上 range(arg1,arg2,arg3)会被转换成一个 List
for index in range(10):
    print("index is {0}".format(index))

print("--------")
for index in range(5, 10):
    print("index is {0}".format(index))

print("--------")

for index in range(5, 10, 2):
    print("index is {0}".format(index))

# Dictionary
# 为不存在的key 设置默认值,避免KeyError

student = {
    "name": "DengXiaoBai",
    "age": 11
}

print(student.get("last_name", "Idiot"))

# exceptions
try:
    lastName = student["aa"]
except KeyError:
    print("Error finding aa")
except TypeError as error:
    print("Type Error")
    print("error message same as not handled {0}".format(error))

except Exception:  # 不推荐这么做,因为我们总是想知道具体的exception
    print("handle all exceptions")


# Other Date Types

