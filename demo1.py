def greet_user(name, age:int=10 , location:str="Atlanta"):
    print(f"Hello, {name}, are you {age} years old ?. do you currently live in {location}")

#greet_user(name="joe",location="Chicago")    


class Student:
    def create_student():  
        print("student created")


    def list_student():
        student = [
            {
                "name": "John Doe",
                "age": 20,
                "location": "Accra"
            },
            {
                "name": "Jane Doe",
                "age": 20,
                "location": "Accra"
            }
        ]
        print(student)
    def student_info():
        student_information= [
            {
                "name":"John Doe",
                "age": 20,
                "id_number":55455
            }
            ]
        print(student_information)   


Student.student_info()        