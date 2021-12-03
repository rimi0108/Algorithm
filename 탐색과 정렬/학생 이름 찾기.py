# 순차탐색


def find_student(no, no_list, name_list):
    n = len(no_list)
    for i in range(0, n):
        if no_list[i] == no:
            return stu_name[i]
    return "?"


stu_no = [39, 14, 67, 105]
stu_name = ["Justin", "Mike", "John", "Summer"]

print(find_student(20, stu_no, stu_name))
