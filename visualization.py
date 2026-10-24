
import matplotlib.pyplot as plt
def plot_student_averages(df):
    """Display and save a chart of student averages."""
    plt.figure(figsize=(8, 5))
    plt.bar(df["Student"], df["Average"])
    plt.title("Average Marks by Student")
    plt.xlabel("Student Name")
    plt.ylabel("Average Marks")
    plt.ylim(0, 100)
    plt.tight_layout()
    plt.savefig("average_marks.png")
    plt.show()
