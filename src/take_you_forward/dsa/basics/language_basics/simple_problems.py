class SOlution:
    # 1. Complete the function printNumber which takes an integer input from the user and prints it on the screen.
    def print_number(self):
        print(int(input()))

    # 2. Given an integer age, print on the screen:
    #    Adult if age >= 18
    #    Teen if age < 18
    #    Do not change the case of any letter in "Adult" and "Teen" while printing the answer.
    def is_adult(self, age: int) -> str:
        if not isinstance(age, int):
            raise TypeError("Age must be int value")

        if age < 0:
            raise ValueError("Age must be positive number")

        if age < 18:
            print("Teen")

        print("Adult")

    # 3. Given marks of a student, print on the screen:
    #     Grade A if marks >= 90
    #     Grade B if marks >= 70
    #     Grade C if marks >= 50
    #     Grade D if marks >= 35
    #     Fail, otherwise.
    def student_grade(self, mark: int) -> str:
        if not isinstance(mark, int):
            raise TypeError("Invalid mark type, int expected")

        if mark >= 90:
            print("Grade A")
        elif mark >= 70:
            print("Grade B")
        elif mark >= 50:
            print("Grade C")
        elif mark >= 35:
            print("Grade D")
        else:
            print("Fail")
