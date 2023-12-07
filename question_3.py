#i)
age =0
User_age = int(input('enter your age:'))
if User_age >=18:
    print(f"You are eligible")
else:
    print(f"You are not eligible")
    
    

#ii
def grade_student():
    results = int(input('entermarks:'))
    total =0
    for x in results:
        total += x
    print(total)
    average = total/1
   
    if average >=90:
            print('Grade A')
    elif average >=80 and average <=89:
            print('Grade B')
    elif average >=70 and average <=79:
            print('Grade C')
    elif average >=60 and average <=69:
            print('Grade D')
    elif average >=50 and average  <=59:
            print('Grade D')
    elif average <=60:
            print('Grade F')
grade_student()
      