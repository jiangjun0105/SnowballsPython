# Ask the name from the terminal and store the user answer
# \n means "new line"
name = raw_input('Enter your name: \n')
#in the shell user write his name
#ask the age from the terminal and store the user answer
#in the shell user write his age
age = raw_input('Enter your age: \n')
#ask the country from the terminal and store the user answer
#in the shell user write his country
country = raw_input('Enter your country: \n')

#open a file called profile.txt
file = open('profile.txt', 'w')
#write name in the file
file.write('name:' + name + '\n')
#write age in the file
file.write('age:' + age + '\n')
#write country in the file
file.write('country:' + country)
file.close()
