n=int(input('Enter number of studens'))
students=[]
for i in range(n):
    s=Student()
name=input('Enter Student name')
marks=int(input('Enter marks'))
s.setName(name)
s.setMarks(marks)
students.append(s)
for s in students :
    print('hello',s.getName())
    print('yours marks:',s.getMarks())
    print