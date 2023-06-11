# Here are the 10 short-listed students and their respective points under each category:
# 	Student-ID	AE		SE		CP		SI		LD
# 	1			9		8		8		6		7
# 	2			10		8		7		7		7
# 	3			9		7		7		8		7
# 	4			8		8		7		7		8
# 	5			9		8		6		8		7

scores = {
    "student_scores": [
        {"student_id": 1,
         "points": {"AE": 9, "SE": 8, "CP": 8, "SI": 6, "LD": 7}
         },
        {"student_id": 2,
         "points": {"AE": 10, "SE": 8, "CP": 8, "SI": 6, "LD": 7}
         },
        {"student_id": 3,
         "points": {"AE": 9, "SE": 8, "CP": 8, "SI": 6, "LD": 7}
         },
        {"student_id": 4,
         "points": {"AE": 9, "SE": 8, "CP": 8, "SI": 6, "LD": 7}
         },
        {"student_id": 5,
         "points": {"AE": 9, "SE": 8, "CP": 8, "SI": 6, "LD": 7}
         },
    ]
}


# I want to get the score of student 5 for the discipline "LD"
# print(f'Score of Student 5 for LD: {scores["student_scores"][4]["student_id"]["points"]["LD"]}')
print(f'Score of Student 5 for LD: {scores["student_scores"][4]["points"]["LD"]}')
