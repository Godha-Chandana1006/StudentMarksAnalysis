
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
