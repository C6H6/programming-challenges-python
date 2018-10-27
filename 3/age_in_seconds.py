import datetime

date = input("Born date (DD-MM-YYYY): ")

born = None
try:
    born = datetime.datetime.strptime(date, '%d-%m-%Y')
except ValueError:
    print("Invalid date")
    exit(255)

now = datetime.datetime.now()

print(str(round((now-born).total_seconds())) + " seconds")
