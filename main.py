import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
students=[["Student","Python","Maths","English"],
		  ["Chandhu",90,80,70],
		  ["Ravi",80,70,60],
			["Ramesh",70,60,50],
			["Suresh",60,50,40]]
with open("student_data.csv","w",newline="") as file:
	writer=csv.writer(file)
	writer.writerows(students)
print("CSV file created successfully.")
df=pd.read_csv("student_data.csv")
print("\nStudent Marks:")
print(df)
print("\nDataset Shape:")
print(df.shape)
print("\nColumn Names:")
print(df.columns.tolist())
print("\nPython marks:")
print(df["Python"])
print("\nChandhu's marks:")
print(df[df["Student"]=="Chandhu"])
print(df.loc[[0,2]])
print(df.info())
marks=df[["Python","Maths","English"]].to_numpy()
print("Student Marks:")
print(df)
print("\nAverage of all marks:")
print(np.mean(marks))
print("\nSubject-wise average:")
print(np.mean(marks, axis=0))
print("\nHighest mark:", np.max(marks))
print("Lowest mark:", np.min(marks))
df["Average"] = np.mean(marks, axis=1)
print("\nStudent-wise average:")
print(df[["Student", "Average"]])
print("\nStandard deviation:", np.std(marks))
print(np.max(df["Maths"]))
print(np.mean(df["Python"]))
plt.bar(df["Student"], df["Python"])
plt.title("Python Marks of Students")
plt.xlabel("Student Name")
plt.ylabel("Marks")
plt.savefig("python_marks.png")
plt.show(block=False)
students=df["Student"]
python_marks=df["Python"]
maths_marks=df["Maths"]
english_marks=df["English"]
plt.figure()
x=np.arange(len(students))
width=0.25
plt.bar(x-width, python_marks, width, label="Python")
plt.bar(x , maths_marks, width, label="Maths")
plt.bar(x+width, english_marks, width, label="English")
plt.xlabel("Student Name")
plt.ylabel("Marks")
plt.title("Student Marks in Different Subjects")
plt.legend()
plt.xticks(x,students)
plt.tight_layout()
plt.ylim(0,100)
plt.show(block=False)
df["Average"] = df[["Python", "Maths", "English"]].mean(axis=1)
plt.figure()
plt.bar(df["Student"], df["Average"])
plt.title("Average Marks by Student")
plt.xlabel("Student Name")
plt.ylabel("Average Marks")
plt.ylim(0, 100)
plt.tight_layout()
plt.savefig("student_marks.png")
plt.show()
