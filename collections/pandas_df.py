import pandas

student_scores = {
    'student': ['John', 'James', 'Dave'],
    'score': [56, 76, 98]
}

student_df = pandas.DataFrame(student_scores)
print(f'Student Scores in Pandas Dataframe: {student_df}')

# Regular dictionary key / value pairing with one addition:
# adding index value with each key as well as with each value.
for (k, v) in student_df.items():
    print(f'Key is: {k} and the value is:  {v}')

# Row-based retrieval using pandas dataframe looping:
for (index, row) in student_df.iterrows():
    print(f'the row value is: {row}')
    print(f'calling the method on row object: {row.student}')


