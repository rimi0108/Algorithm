# 입력: 학생 번호와 이름 / 39: Justin
# 출력: 학생 번호에 맞는 학생 이름, 해당하는 학생 번호가 없을 시 물음표

# 나의 풀이
def find_student_name(info, num):
    for i in info:
        if i == num:
            return info[i]
    return "?"


student_info = {39: "Justin", 14: "John", 67: "Mike", 105: "Summer"}

print(find_student_name(student_info, 67))

# 책 풀이


def get_name(s_info, find_no):
    if find_no in s_info:
        return s_info[find_no]
    else:
        return "?"


print(find_student_name(student_info, 105))
