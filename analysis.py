
import pandas as pd
def calculate_averages(df):
    """Calculate each student's average marks."""
    subjects = ["Python", "Maths", "English"]
    df["Average"] = df[subjects].mean(axis=1)
    return df
def get_subject_averages(df):
    """Calculate the average for each subject."""
    subjects = ["Python", "Maths", "English"]
    return df[subjects].mean()
def get_top_student(df):
    """Find the student with the highest average."""
    top_index = df["Average"].idxmax()
    return df.loc[top_index, "Student"]
def assign_grades(df):
    """Assign a grade based on each student's average."""
    def get_grade(average):
        if average >= 90:
            return "A"
        elif average >= 80:
            return "B"
        elif average >= 70:
            return "C"
        elif average >= 60:
            return "D"
        else:
            return "F"
    df["Grade"] = df["Average"].apply(get_grade)
    return df
def calculate_results(df):
    """Calculate pass/fail status and class pass percentage."""
    subjects = ["Python", "Maths", "English"]
    df["Result"] = (df[subjects].ge(40).all(axis=1).map({True: "Pass", False: "Fail"}))
    total_students = len(df)
    if total_students == 0:
        return df, 0.0
    passed = (df["Result"] == "Pass").sum()
    failed = (df["Result"] == "Fail").sum()
    pass_percentage = (passed / total_students) * 100
    return df, pass_percentage
