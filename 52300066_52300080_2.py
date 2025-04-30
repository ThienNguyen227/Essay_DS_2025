import csv
import os

# Đặt thư mục làm việc thành thư mục chứa file Python
os.chdir(os.path.dirname(os.path.abspath(__file__)))
print("Thư mục làm việc hiện tại:", os.getcwd())

# ------ 1. Hàm đọc dữ liệu học sinh từ file csv ------

def read_data_students(file_path):
    students = []
    
    # Mở file CSV và đọc dữ liệu
    with open(file_path, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        
        for row in reader:
           
            student = {
                'StudentID': row[0],
                'StudentName': row[1],
                'DayOfBirth': row[2],
                'Math': float(row[3]),
                'CS': float(row[4]),
                'Eng': float(row[5])
            }
            students.append(student)

    return students

# Đọc dữ liệu từ file students.csv
students = read_data_students('students.csv')

# In dữ liệu ra để kiểm tra
for student in students:
    print(student)



# ------ 2. Định nghĩa các predicates (trả về True/False) ------

#2.1> Hàm kiểm tra tất cả điểm số >= 5 
def is_passing(student):
    return student['Math'] >= 5 and student['CS'] >= 5 and student['Eng'] >= 5

#2.2> Hàm kiểm tra điểm toán >= 9
def is_high_math(student):
    return student['Math'] >= 9

#2.3> Hàm kiểm tra điểm toán và điểm CS < 6
def is_struggling(student):
    return student['Math'] < 6 and student['CS'] < 6

#2.4> Hàm kiểm tra điểm CS > điểm toán
def improved_in_cs(student):
    return student['CS'] > student['Math']



# ------ 3. ------

# --- ∀ ---
# 1. Với mọi học sinh pass tất cả các môn học
def all_students_passed_all_subjects(students):
    return all(is_passing(student) for student in students)

# 2. Với mọi học sinh có điểm toán trên 3(>3)
def all_students_have_score_math_above_3(students):
    return all(student['Math'] > 3 for student in students)

# --- ∃ ---
# 3. Tồn tại ít nhất một học sinh có điểm toán trên 9(>9)
def exists_a_student_scored_math_above_9(students):
    return any(student['Math'] > 9 for student in students)

# 4. Tồn tại ít nhất một học sinh có điểm CS > điểm toán
def exists_a_student_improved_in_cs(students):
    return any(improved_in_cs(student) for student in students)

# --- ∀,∃ ---
# 5. Với mọi học sinh, tồn tại ít nhất một môn học trên 6 điểm(>6)
def all_students_exists_a_subject_above_6(students):
    return all(any(score > 6 for score in [student['Math'], student['CS'], student['Eng']]) for student in students)

# 6. Với mọi học sinh dưới 6(<6) điểm toán, thì tồn tại ít nhất một môn học khác trên 6 điểm(>6)
def all_students_below_6_math_exists_a_subject_above_6(students):
    return all(student['Math']>=6 or any(score > 6 for score in [student['CS'], student['Eng']]) for student in students)

# Ghi chú: Phạm vi hàm này chỉ những học sinh dưới 6(<6) điểm toán
# Nên -> 1. Nếu mà điểm toán >=6 thì học sinh đó không liên quan trong hàm này -> hàm trả về True
# Nên -> 2. Nếu mà điểm toán không >=6 thì nó sẽ là trường hợp <6 và rơi vào any(score > 6 for score in [student['CS'], student['Eng']]) nếu đúng thì hàm trả về True



# ------ 4. Phủ định ------

# --- ∀ ---

# Với mọi học sinh pass tất cả các môn học
# -> 7. Phủ định: Tồn tại ít nhất một học sinh không pass tất cả các môn học
def negation_of_all_students_passed_all_subjects(students):
    return any(not is_passing(student) for student in students)

# Với mọi học sinh có điểm toán trên 3(>3) 
# -> 8. Phủ định: Tồn tại ít nhất một học sinh có điểm toán <= 3
def negation_of_all_students_have_score_math_above_3(students):
    return any(student['Math'] <= 3 for student in students)

# --- ∃ ---

# Tồn tại ít nhất một học sinh có điểm toán trên 9(>9)
# -> 9. Phủ định: Với mọi học học sinh có điểm toán <= 9
def negation_of_exists_a_student_scored_math_above_9(students):
    return all(student['Math'] <= 9 for student in students)

# Tồn tại ít nhất một học sinh có điểm CS > điểm toán
# -> 10. Phủ định: Với mọi học học sinh có điểm CS <= điểm toán 
def negation_of_exists_a_student_improved_in_cs(students):
    return all(not improved_in_cs(student) for student in students)

# --- ∀,∃ ---

# Với mọi học sinh, tồn tại ít nhất một môn học trên 6 điểm(>6)
# -> 11. Phủ định: Tồn tại ít nhất một học sinh, với mọi môn học <= 6 điểm
def negation_of_all_students_exists_a_subject_above_6(students):
    return any(all(score <= 6 for score in [student['Math'], student['CS'], student['Eng']]) for student in students)

# Với mọi học sinh dưới 6(<6) điểm toán, thì tồn tại ít nhất một môn học khác trên 6 điểm(>6)
# -> 12.Phủ định: Tồn tại ít nhất một học sinh dưới 6 (<6) điểm toán, với mọi môn học khác <= 6 điểm
def negation_of_all_students_below_6_math_exists_a_subject_above_6(students):
    return any(student['Math'] < 6 and all(score <= 6 for score in [student['CS'], student['Eng']]) for student in students) 

print()
# In kết quả kiểm tra các hàm
print("1. Tất cả học sinh đã pass tất cả các môn học: ", all_students_passed_all_subjects(students))
print("2. Tất cả học sinh có điểm toán > 3: ", all_students_have_score_math_above_3(students))
print("3. Tồn tại ít nhất một học sinh có điểm toán > 9: ", exists_a_student_scored_math_above_9(students))
print("4. Tồn tại ít nhất một học sinh có điểm CS > điểm toán: ", exists_a_student_improved_in_cs(students))
print("5. Với mọi học sinh, tồn tại ít nhất một môn học > 6 điểm: ", all_students_exists_a_subject_above_6(students))
print("6. Với mọi học sinh có điểm toán < 6, tồn tại ít nhất một môn học khác > 6 điểm: ", all_students_below_6_math_exists_a_subject_above_6(students))

print()
# Kiểm tra phủ định
print("7. Phủ định: Tồn tại ít nhất một học sinh không pass tất cả các môn học: ", negation_of_all_students_passed_all_subjects(students))
print("8. Phủ định: Tồn tại ít nhất một học sinh có điểm toán <= 3: ", negation_of_all_students_have_score_math_above_3(students))
print("9. Phủ định: Với mọi học học sinh có điểm toán <= 9: ", negation_of_exists_a_student_scored_math_above_9(students))
print("10. Phủ định: Với mọi học học sinh có điểm CS <= điểm toán: ", negation_of_exists_a_student_improved_in_cs(students))
print("11. Phủ định: Tồn tại ít nhất một học sinh, với mọi môn học <= 6 điểm: ", negation_of_all_students_exists_a_subject_above_6(students))
print("12. Phủ định: Tồn tại ít nhất một học sinh có điểm toán < 6, với mọi môn học khác <= 6 điểm: ", negation_of_all_students_below_6_math_exists_a_subject_above_6(students))
