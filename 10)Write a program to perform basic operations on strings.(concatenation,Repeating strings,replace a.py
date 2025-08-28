#10)Write a program to perform basic operations on strings.(concatenation,Repeating strings,replace a string with other string by using replace(),Removing spaces from a given string)

s1="Hello"
s2="World"

concat=s1+" " + s2
print(concat)

repeat = s1*4
print(repeat)

replacestr=concat.replace("Hello" , "Hi")
print(replacestr)

replace_=concat.replace(" " , "")
print(replace_)
