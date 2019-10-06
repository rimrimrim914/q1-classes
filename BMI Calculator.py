## 12. BMI Calculator
### Write a Python program to calculate body mass index
##### Program Console Sample 1:
###### Enter Height in Cm: 180
###### Enter Weight in Kg: 75
###### Your BMI is 23.15


print(' =================================== BMI Calculator =================================== ')


# Getting input from User

Height = int(input(f'Enter height : ' ))
user_Height = Height / 100

print(f'{user_Height} in m')

Weight = int(input(f'Enter weight : ' ))
print(f'{Weight} in Kg')

result = Weight / (user_Height)**2

#Output

print(result)
