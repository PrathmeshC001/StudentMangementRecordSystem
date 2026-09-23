# ==============================================
#        STUDENT RECORD MANAGEMENT SYSTEM
# ==============================================



students={

    "VIT001":{
         "Name": "Prathmesh Choughule",
         "Age": 18,
         "Status": "H",
         "State": "GJ",
         "Course": "BCY",
         "Semster": 1,

         },

    "VIT002":{
         "Name": "Aryan Gupta",
         "Age": 18,
         "Status": "H",
         "State": "GJ",
         "Course": "AI/ML",
         "Semster": 1,

         },

    "VIT003":{
         "Name": "Aman Singh",
         "Age": 18,
         "Status": "H",
         "State": "PB",
         "Course": "CSE",
         "Semster": 1,

         },

    "VIT004":{
         "Name": "Ajay Desai",
         "Age": 19,
         "Status": "DS",
         "State": "MH",
         "Course": "ECE",
         "Semster": 1,

         },

    "VIT005":{
         "Name": "Niraj Dave",
         "Age": 17,
         "Status": "H",
         "State": "MP",
         "Course": "AI/ML",
         "Semster": 1,

         },

    "VIT006":{
         "Name": "Saurav Kumar",
         "Age": 18,
         "Status": "DS",
         "State": "RJ",
         "Course": "BCY",
         "Semster": 1,

         }


}


# ============================
# FUCTION 1: DISPLAY RECORD
# ============================


def display_record(student_id):

    student=students[student_id]

    print("\n ==============================")
    print("        STUDENT RECORD")
    print(" ================================")


    print("Student ID :", student_id)
    print("Name :", student["Name"])
    print("Age :", student["Age"])
    print("Status :", student["Status"])
    print("Course :", student["Course"])
    print("Semester :", student["Semster"])


    print(" ===============================")


# =====================================
# FUNCTION 2: SEARCH STUDENT RECORD
# =====================================


def search_student():

    student_id=input("\nEnter Student ID: ").upper()

    if student_id in students:

        display_record(student_id)

    else:
        print("\nStudent NOT FOUND!!!!")
        print("PLEASE CHECK THE STUDENT ID.")



# ==========================================
#           ADD NEW STUDENT
# ==========================================


def add_student():

    print("\n===========================")
    print("        ADD NEW STUDENT")
    print("\n==========================")

    student_id= input("Enter Student ID: ").upper()

    
    if student_id in students:

        print("\nStudent ID already exists!")
        print("Please use a DIFFERENT STUDENT ID.")

        return

    name=input("Enter Student Name: ")
    age=int(input("Enter Age: "))

    print("\nH= Hosteler")
    print("D= Day Scholar")
    
    status=input("Enter Status: ")

    while status !="H" and status !="D":
        print("Invalid status!")
        status=input("Enter H or D: ").upper()

    print("\nEnter State Code")
    print("Exxample: GJ=Gujarat, MP=Madhya Pradesh, MH=Maharashtra, RJ=Rajasthan")

    state=input("Enter State code: ").upper()


    print("\nEnter Course Code")
    print("CSE/BCY/AIML")


    course=input("Enter COurse: ").upper()


    semester=input("Enter semester: ")


    # Creating Student Record

    student={

        "Name": name,
        "Age": age,
        "Status": status,
        "Course": course,
        "Semster": semester

    }


    #Adding student to database

    students[student_id]= student

    print("\n Student Added Successfully!!!")

    

# ==================================
# FUNCTION 4: DISPLAY ALL STUDENTS
# ==================================


def display_all_students():

    if len(students)==0:

        print("\nNo student records available.")

    else:
        print("\n==========================")
        print("\n      ALL STUDENTS      ")
        print("============================")

        for student_id in students:

            student=students[student_id]

            print("\nStudent ID :", student_id)
            print("Name     :", student["Name"])
            print("Age      :", student["Age"])
            print("Status   :", student["Status"])
            print("State    :", student["State"])
            print("Course   :", student["Course"])
            print("Semester :", student["Semster"])

            print("-----------------------------")




# =========================
#         MAIN MENU
# =========================



while True:

    print("\n")
    print("=====================================")
    print("     STUDENT RECORD MANAGEMENT       ")
    print("=====================================")


    print("\nEnter Student ID to Directly view record")
    print("OR")
    print("Type NEW to add anew student")
    print("Type MENU to open main menu")
    print("Type EXIT to close the program")

    user_input= input("\nEnter your choice: ").upper()


    # =======================================
    # DIRECT STUDENT RECORD DISPLAY BY ID
    # =======================================


    if user_input in students:

        display_record(user_input)




    # ======================
    # ADD NEW STUDENT DATA
    # ======================


    elif user_input =="NEW":

        add_student()




    # =================
    # OPEN MAIN MENU
    # =================




    elif user_input== "MENU":


        print("\n========================")
        print("        MAIN MENU          ")
        print("==========================")


        print("1. Search Student")
        print("2. Add Student Data")
        print("3. Display All students")
        print("4. Back")


        choice= input("\nEnter your choice: ")


        if choice =="1":

            search_student()

        elif choice =="2":

            add_student()

        elif choice =="3":

            display_all_students()

        elif choice =="4":

            break

        else:

            print("\nIInvalid choice. Please Try again later.")


    # ========
    # EXIT
    # ========


    elif user_input =="EXIT":

        print("\nTHANK YOU FOR USING STUDENT RECORD MANANGEMENT SYSTEM")



    # ================
    # INVALID INPUT
    # ================


    else:

        print("\n Srudent ID Not Found.")
        print("Type MENU for more options")

