def get_value(time, idex):
    try:
        return time[idex]
    except:
        return 0


def check_vaue(strng):
    while True:
        try:
            variable = float(input(strng))
            if variable >= 1 and variable <= 5:
                break
            else:
                print("Please Enter a value between 1 to 5")
        except:
            print("Please Enter a correct value")
    return variable


def hours_decimals(hours, minutes, seconds):
    try:
        decimal_minutes = int(minutes)/60
    except:
        decimal_minutes = 0
    try:
        decimal_seconds = int(seconds)/3600
    except:
        decimal_seconds = 0
    decimal_hours = int(hours)+decimal_minutes+decimal_seconds
    return decimal_hours


def time(h):
    hours = int(h)
    minutes = (h*60) % 60
    seconds = (h*3600) % 60
    return f"{hours}:{int(minutes)}:{int(seconds)}"


# Type of Courses
while True:
    MOOC_selfPlacedCourse = input(
        "Type of Course [MOCC's (0)/ self-Placed-Course (1)]: ")

    if float(MOOC_selfPlacedCourse) == 0:
        while True:
            try:
                total_week = int(input("Total WeeK: "))
                break
            except:
                print("Please Enter a correct Weeks value")
        while True:
            try:
                total_hour = float(input("Total Hour Taken: "))
                break
            except:
                print("Please Enter a correct Hour Value")

        total_time = [total_week*total_hour, 0, 0]
        break
    elif float(MOOC_selfPlacedCourse) == 1:
        while True:
            total_time = input(
                "Total Self-Placed Course Time [HH:MM:SS]: ").split(":")
            if total_time == ['']:
                print("Please Enter a valid Time")
            else:
                try:
                    int(total_time[0])
                    break
                except:
                    print("Please Enter a valid Time")
        break
    else:
        print("Please Select a valid Course")


hours_in_decimals = hours_decimals(
    total_time[0], get_value(total_time, 1), get_value(total_time, 2))


material_familarity = check_vaue(
    "How new are you to the Material? (1 - Very Familiar; 5 - Very New): ")
level_expertise = check_vaue(
    "Desired Level of Expertise? (1 - Elementary; 5 - Expert): ")
course_density = check_vaue(
    "Estimated Level of Density? (1 - Easy ; 5 - Very Dense): ")


required_time = hours_in_decimals * \
    ((material_familarity+level_expertise+course_density)/3)

print(time(required_time))
