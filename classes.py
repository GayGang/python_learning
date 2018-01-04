
students = []


class Student:
    # Python 没有权限控制, 所有的方法都是 public ,可以通过规范命名去说明

    # class property
    school_name = "SHICHENGZHOGNXUE"

    def __init__(self, name, stu_id=110):
        # instance property
        self.name = name
        self.stu_id = stu_id

        students.append(self)

    def get_name_capitalize(self):
        return self.name.capitalize()

    def __str__(self):
        return "Student name is {0}, id is {1}".format(self.name, self.stu_id)


class HighSchoolStudent(Student):
    def __str__(self):
        result_str = super().__str__()
        return "This is High School ,{0}".format(result_str)





