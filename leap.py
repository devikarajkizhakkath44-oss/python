from datetime import datetime

current_year = datetime.now().year
final_year = int(input("Enter the final year: "))

print("Future leap years:")

for year in range(current_year + 1, final_year + 1):
    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        print(year)