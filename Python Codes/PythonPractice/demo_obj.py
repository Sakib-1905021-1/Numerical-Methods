a = 1
def func():
    global a
    a = 5


func()
print(a)


class Student:
    student_count = 0

    def __init__(self, id, name):
        self.name = name
        self.id = id
        Student.student_count += 1


    def show_count(self):
        print("Total number of students ", Student.student_count)

    def show_info(self):
        print("ID: ", self.id, "Name: ", self.name)


if __name__ == "__main__":
    Suvro = Student("1905020", "GFZ Suvro")
    Sakib = Student("1905021" , "Sakib Mohammed Sobaha")

    Suvro.show_info()
    # del Suvro.id
    Suvro.show_info()
    Sakib.show_info()





    print(Student.student_count)

