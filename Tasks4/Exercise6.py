def daysOnMonth(month, year):
    match month:
        case 1 | 3 | 5 | 7 | 8 | 10 | 12:
            return 31

        case 4 | 6 | 9 | 11:
            return 30

        case 2:
            isLeap = (year % 4 == 0 and year % 100 != 0) or (year %400 == 0)
            return 29 if isLeap else 28

        case _:
            print("Incorrect input enter (1-12)")

while True:
    month = int(input("Enter month: "))
    year = int(input("Enter year: "))
    print(f"{month} in {year} has {daysOnMonth(month, year)} days\n")