from collections import OrderedDict

data = {}

def read_data():
    with open("class.txt", "r") as file:
        for line in file:
            line = line.strip("\n")
            line = line.strip("\t")
            listt = line.split("|")
            data[listt[0]] = []
            data[listt[0]].append(listt[1])
            data[listt[0]].append(listt[2])

def read_other(file_name):
    with open(file_name + ".txt", "r") as file:
        max_marks = file.readline()
        keys = []
        lines = file.readlines()
        for i in lines:
            i = i.strip("\n")
            i = i.strip("\t")
            listt = i.split("|")
            keys.append(listt[0])
            data[listt[0]].append(max_marks)
            data[listt[0]].append(listt[1])
        diff = data.keys() - keys
        for i in diff:
            data[i].append(max_marks)
            data[i].append(0)


def avg_helper(index, input):
    sum = 0
    for key in data:
        sum = sum + float(data[key][index])
    print(input.upper() + " average: " + str(sum/len(data.keys())) + "/" + data[list(data.keys())[0]][index-1])


def avg(input):
    if input == "a1":
        return avg_helper(3, input)
    elif input == "a2":
        return avg_helper(5, input)
    elif input == "t1":
        return avg_helper(7, input)
    elif input == "t2":
        return avg_helper(9, input)
    elif input == "pr":
        return avg_helper(11, input)


def calc_grade():
    for key in data:
        a1 = (float(data[key][3]) * 7.5)/ float(data[key][2])
        a2 = (float(data[key][5]) * 7.5) / float(data[key][4])
        t1 = (float(data[key][7]) * 30) / float(data[key][6])
        t2 = (float(data[key][9]) * 30) / float(data[key][8])
        pr = (float(data[key][11]) * 25) / float(data[key][10])
        count = a1 + a2 + t1 + t2 + pr
        data[key].append(int(count))
        grade = grade_helper(count, int(50/7), 50)
        data[key].append(grade)


def option_five(pfp):
    copy = data.copy()
    for key in copy:
        copy[key][13] = grade_helper(copy[key][12], int((100-pfp)/7), pfp)

    print("ID" + "    " + "LN" + "     " + "FN" + "     " + "A1" + " " + "A2" + " " + "PR" + " " + "T1" + " " + "T2" + " " + "GR" + " " + "FL")
    for key in copy:
        print(str(key) + " " * (6 - len(str(key))) + blank(copy[key][1]) + " " * (7 - len(str(copy[key][1]))) +
              blank(copy[key][0]) + " " * (7 - len(str(copy[key][0]))) + blank(copy[key][3])
              + " " * (3 - len(str(copy[key][3]))) + blank(copy[key][5]) + " " * (3 - len(str(copy[key][5]))) +
              blank(copy[key][11]) + " " * (3 - len(str(copy[key][11]))) + blank(copy[key][7])
              + " " * (3 - len(str(copy[key][7]))) + blank(copy[key][9]) + " " * (3 - len(str(copy[key][9]))) +
              blank(copy[key][12]) + " " * (3 - len(str(copy[key][12]))) + blank(copy[key][13]))


def grade_helper(count, range, pfp):
    if count > 100 - range and count <= 100.0:
        grade = "A+"
    elif count > 100 - range*2 and count <= 100 - range:
        grade = "A"
    elif count > 100 - range*3 and count <= 100 - range*2:
        grade = "A-"
    elif count > 100 - range*4 and count <= 100 - range*3:
        grade = "B+"
    elif count > 100 - range*5 and count <= 100 - range*4:
        grade = "B"
    elif count > 100 - range*6 and count <= 100 - range*5:
        grade = "B-"
    elif count > pfp and count <= 100 - range*6:
        grade = "C"
    else:
        grade = "F"

    return grade


def option_one(input):
    if input == "a1":
        return one_helper(3, input)
    elif input == "a2":
        return one_helper(5, input)
    elif input == "t1":
        return one_helper(7, input)
    elif input == "t2":
        return one_helper(9, input)
    elif input == "pr":
        return one_helper(11, input)


def one_helper(index, input):
    keys = list(data.keys())[0]
    print(input.upper() + " " + "grades" + " " + data[keys][index-1])
    for key in data.keys():
        if str(data[key][3]) != "0":
            print(key + " " + str(data[key][1]) + ","+ str(data[key][0]) +
                  " "*(14-(len(str(data[key][1])) + len(str(data[key][0])) + 1)) + str(data[key][index]))


def blank(input):
    if str(input) == "0":
        return " "
    else:
        return str(input)


def display_data():
    print("ID" + "    " + "LN" + "     " + "FN" + "     " + "A1" + " " + "A2" + " " + "PR" + " " + "T1" + " " + "T2" + " " + "GR" + " " + "FL")
    for key in data:
        print_helper(key)


def print_helper(key):
    print(str(key) + " " * (6 - len(str(key))) + blank(data[key][1]) + " " * (7 - len(str(data[key][1]))) +
          blank(data[key][0]) + " " * (7 - len(str(data[key][0]))) + blank(data[key][3])
          + " " * (3 - len(str(data[key][3]))) + blank(data[key][5]) + " " * (3 - len(str(data[key][5]))) +
          blank(data[key][11]) + " " * (3 - len(str(data[key][11]))) + blank(data[key][7])
          + " " * (3 - len(str(data[key][7]))) + blank(data[key][9]) + " " * (3 - len(str(data[key][9]))) +
          blank(data[key][12]) + " " * (3 - len(str(data[key][12]))) + blank(data[key][13]))


def display_data_sort(sort):
    if sort == "LT":
        index = 1
    elif sort == "GR":
        index = 12
    print("ID" + "    " + "LN" + "     " + "FN" + "     " + "A1" + " " + "A2" + " " + "PR" + " " + "T1" + " " + "T2" + " " + "GR" + " " + "FL")
    for key in OrderedDict([(x, data[x]) for x in sorted(data, key=lambda x: str(data[x][index]))]):
        print_helper(key)

