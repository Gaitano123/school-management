from datetime import datetime

# date_string = '2004/11/13'

# member_date_of_birth = datetime.strptime(date_string, '%Y/%m/%d')

date_string = '13/11/2004'

member_date_of_birth = datetime.strptime(date_string, '%d/%m/%Y')
print(member_date_of_birth)

current_date = datetime.now()

age = current_date.year - member_date_of_birth.year - ((current_date.month, current_date.day) < (member_date_of_birth.month, member_date_of_birth.day))

print("Age:", age)
