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

    # 4. Given the integer day denoting the day number,
    #     print on the screen which day of the week it is.
    #     Week starts from Monday and
    #     for values greater than 7 or less than 1, print Invalid.
    #     Ensure only the 1st letter of the answer is capitalised.
    def which_week_day(self, day: int):
        match day:
            case 1:
                print("Monday")
            case 2:
                print("Tuesday")
            case 3:
                print("Wednesday")
            case 4:
                print("Thursday")
            case 5:
                print("Friday")
            case 6:
                print("Saturday")
            case 7:
                print("Sunday")
            case _:
                print("Invalid")

    # 5. Sum of first last element in array
    # Given an integer array nums, return the sum of the 1st and last element of the array.
    def sum_of_first_and_last(self, nums: list[int]) -> int:
        if len(nums) > 0:
            return nums[0] + nums[-1]

    # 5. Print X N numbers of times
    #   Given two integers X and N, print the value X on the screen N times.
    #   Separate each number by a single space.
    #   Do not add a space after the last number.
    #   After printing all N numbers, move to the next line.
    #   If N = 0, still move to the next line (print an empty line).
    def print_x(self, x: int, n: int):
        for i in range(n):
            if i < n - 1:
                print(x, end=" ")
            else:
                print(x, end="")
        print()

    # 6. Print last character of string
    #   Given a string s. Return the last character of the given string s.
    def last_char(self, string: str):
        if string:
            return string[-1]
