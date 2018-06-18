import sys
import compute


def main():
    compute.read_data()
    compute.read_other("a1")
    compute.read_other("a2")
    compute.read_other("test1")
    compute.read_other("test2")
    compute.read_other("project")
    compute.calc_grade()
    display_menu()


def display_menu():
    print("1> Display individual component")
    print("2> Display component average")
    print("3> Display Standard Report")
    print("4> Sort by alternate column")
    print("5> Change Pass/Fail point")
    print("6> Exit")
    option = input("Enter Option : ")

    if option == "1":
        user_input = input("Enter Component : for example, a1 or pr : ")
        compute.option_one(user_input.lower())
    elif option == "2":
        user_input = input("Enter Component : for example, a1 or pr : ")
        compute.avg(user_input.lower())
    elif option == "3":
        compute.display_data()
    elif option == "4":
        user_input = input("Enter Sort Criteria : for example, GR or LT : ")
        compute.display_data_sort(user_input)
    elif option == "5":
        user_input = input("Enter new Pass/Fail Point : ")
        compute.option_five(int(user_input))
        main()
    elif option == "6":
        print("Good Bye")
        sys.exit()

  
if __name__== "__main__":
    main()