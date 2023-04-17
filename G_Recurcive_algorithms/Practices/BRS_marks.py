def print_marks(students_count: int, min_mark: int, max_mark: int, n: int = 0, student_marks: str = ""):
    if n == students_count:
        print(student_marks.strip())
        global counter
        counter += 1
        return
    for mark in range(min_mark + students_count - n - 1, max_mark + 1):
        print_marks(students_count, min_mark, mark - 1, n + 1, student_marks + " " + str(mark))


def main():
    students_number, min_mark, max_mark = map(int, input().split())
    # students_number, min_mark, max_mark = map(int, "3 36 39".split())
    print_marks(students_number, min_mark, max_mark)
    print(counter)


if __name__ == "__main__":
    counter = 0
    main()
