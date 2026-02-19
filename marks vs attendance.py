import matplotlib.pyplot as plt
Attendance_list=[]
Marks_list=[]
count=int(input("How many subjects do you have?: "))
for i in range(count):
  print("---Subject", i+1, "---")
  a=int(input(" Enter Attendance:"))
  m=int(input("Enter Marks:"))
  Attendance_list.append(a)
  Marks_list.append(m)
plt.bar(Attendance_list, Marks_list)
plt.title("Attendance vs Marks")
plt.xlabel("Attendance ")
plt.ylabel(" Marks")
plt.show()