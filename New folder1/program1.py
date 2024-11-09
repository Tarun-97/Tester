name=input("Enter name ")
current_year=int(input("Enter current year "))
yob=int(input("Enter year of birth "))
age=current_year-yob
if age>60:
    status=name+" is a senior citizen"
else:
    status=name+" is not a senior citizen"
print(status)
