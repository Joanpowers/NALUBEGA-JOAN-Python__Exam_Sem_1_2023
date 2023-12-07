
#write a python function named "calculte_area" that takes the radius of a circle as a parameter and returns the area of the circle.
def calculate_area(radius):
    area_of_the_circle = 3.14 * radius**2
    return area_of_the_circle
    print(area_of_the_circle)

calculate_area(5)
radius = 5
area_of_circle = calculate_area(radius)
print(f"The area of the circle with radius {radius} is: {area_of_circle}")



#ii)
numbers =(1,2,3,4)
def sum_of_natural_numbers(n):
    if n == 0:
        return 0
    else:
        return n + sum_of_natural_numbers(n - 1)
n = 4
result = sum_of_natural_numbers(n)


print(f"The sum of natural numbers up to {n} is: {result}")


#iii)
#removing element at index 2
numbers = [2,3,5,7,9]
numbers.remove(5)
print(numbers)

#adding a new value
numbers = [2,3,5,7,9]
new_number =10
numbers.append(new_number)
print(numbers)

#iv
even_numbers =[2,4,6,8,10]
new_list = [x for x in even_numbers if x %2 ==0]
print(new_list)
 
#v
student_info ={
    'name' :'Alice',
    'age':20,
    'grade':'A',
}

#updating age to 25 from 20
student_info['age'] = 25
print(student_info)


#adding a new keay -value 

student_info['city'] = 'New York'
print(student_info)

original_dict = {
    'a':3,
    'b':8,
    'c':2,
    'd':7
}

#finding a new dictionary with values greater than 5
new_dict = {key: value for key,
            value in original_dict.items() 
            if value > 5}
print(new_dict)



