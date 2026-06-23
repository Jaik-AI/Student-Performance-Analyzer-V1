import os 

def add_student(n,m):
    print("\nAdding Student...")
    with open("students.txt","a") as f:
        f.write(f"{n.capitalize()},{m}\n")
    print("Student added!")

def view_student():
    print("\nShowing student..")
    with open("students.txt","r") as f:
        content = f.read()
        if(content == ""):
            print("No record exists!")
        else:
            print(content)

def average_marks():
    total_marks = 0
    student_count = 0
    with open("students.txt","r") as f:
        content = f.read()
        if(content==""):
            print("No record exists!")
            return
        for i in content.splitlines():
            marks = i.split(",")[1]
            marks = int(marks)
            total_marks += marks
            student_count += 1
    print(f"\nAverage Marks :{total_marks/student_count}")

def topper_marks():
    Topper_name = ""
    Topper_mark = -1
    with open("students.txt","r") as f:
        content = f.read()
        if(content == ""):
            print("No record exists.")
            return
        for i in content.splitlines():
            name,mark = i.split(",")
            mark = int(mark)
            if(mark>Topper_mark):
                Topper_name = name
                Topper_mark = mark

    print(f"Topper is {Topper_name} with marks {Topper_mark}.")
            
def lowest_marks():
    Lowest_name = ""
    Lowest_mark = 100
    with open("students.txt","r") as f:
        content = f.read()
        if(content==""):
            print("No Record exists!")
            return
        for i in content.splitlines():
            name,mark = i.split(",")
            mark = int(mark)
            if(mark<Lowest_mark):
                Lowest_name = name
                Lowest_mark = mark
    
    print(f"Lowest marks are {Lowest_mark} and scored by {Lowest_name}.")


if not(os.path.exists("students.txt")):
    print("No Record exists.")
    with open("students.txt","a") as f:
        pass
while(True):
    try:
        o = int(input("\nOperations:\n1.Add Student.\n2.View Student.\n3.Average Marks.\n4.Topper Student.\n5.Lowest Scorer Student.\n6.Exit\nSelect:"))
    except ValueError:
        print("Please select a valid option!.")
        continue

    if(o==1):
        n = input("Enter Student name:")
        try:
            m = int(input("Enter Student marks:"))
            if not(0<=m<=100):
                print("Please enter marks between 0 and 100!")
                continue
                
        except ValueError:
            print("Please enter a valid marks!.")
            continue
        add_student(n,m)
    elif(o==2):
        view_student()
    
    elif(o==3):
        average_marks()
    elif(o==4):
        topper_marks()

    elif(o==5):
        lowest_marks()
    elif(o==6):
        print("Goodbye...")
        exit()
