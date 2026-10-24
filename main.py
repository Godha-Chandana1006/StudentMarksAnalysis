
import logging
import pandas as pd
from analysis import (
    calculate_averages,
    get_subject_averages,
    get_top_student,
    assign_grades,
    calculate_results
)
from visualization import plot_student_averages

logging.basicConfig(
    filename="student_analysis.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
def main():
    try:
        logging.info("Student Marks Analysis started")
        df = pd.read_csv("student_data.csv")
        required_columns = ["Student", "Python", "Maths", "English"]
        if not all(column in df.columns for column in required_columns):
            raise ValueError("CSV is missing one or more required columns.")
        df = calculate_averages(df)
        df = assign_grades(df)
        df,pass_percentage = calculate_results(df) 
        print("Student Marks and Results:")
        print(df[["Student", "Python", "Maths", "English", "Average","Result"]].round(2))
        print("\n Class Pass/Fail Results:")
        print(df[["Student", "Result"]])
        print(f"\nClass Pass Percentage: {pass_percentage:.2f}%")
        print(f"Class Fail Percentage: {100 - pass_percentage:.2f}%")
        print("\nSubject Averages:")
        print(get_subject_averages(df).round(2))
        print("\nTop Student:")
        print(get_top_student(df))
        plot_student_averages(df)
        logging.info("Analysis completed successfully")
    except FileNotFoundError:
        logging.exception("Student data file was not found")
        print("Error: student_data.csv was not found.")
    except (ValueError, KeyError) as error:
        logging.exception("Data processing failed")
        print("Error: Check your CSV data and column names.")
        print(error)
    except Exception:
        logging.exception("Unexpected error occurred")
        print("An unexpected error occurred. Check student_analysis.log.")
if __name__ == "__main__":
    main()
