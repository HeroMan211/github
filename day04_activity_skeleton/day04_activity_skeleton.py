"""
Day 4 Activity: Parse nested dictionaries (student database).
Tasks:
1) Get Alice's AI301 grade
2) Calculate Bob's GPA (weighted by credits)
3) Find all students in CS101
4) Get average grade across all courses
5) Find student with highest GPA
"""

students = {
    "S001": {
        "name": "Alice Chen",
        "courses": {
            "CS101": {"grade": 92, "credits": 3},
            "MATH201": {"grade": 88, "credits": 4},
            "AI301": {"grade": 95, "credits": 3},
        },
        "advisor": "Dr. Smith",
    },
    "S002": {
        "name": "Bob Lee",
        "courses": {
            "CS101": {"grade": 85, "credits": 3},
            "MATH201": {"grade": 90, "credits": 4},
        },
        "advisor": "Dr. Patel",
    },
}

print(students["S001"]['name'])

print("##########")
##########
count = 0
x = 0
for i in students["S002"]['courses']:
    x += students["S002"]['courses'][i]['credits']
    count += 1

bob_gpa = x/count

print(bob_gpa)

print("##########")
##########

cs101count = 0
for i in students:
    if 'CS101' in students[i]['courses']:
        print(students[i]['name'])

print("##########")
##########
counts = 0
average = 0
for i in students:
    for x in students[i]['courses']:
        average += students[i]['courses'][x]['grade']
        counts += 1

average /= counts

print(average)

print("##########")
##########

g = 0
w = 0
for i in students["S001"]['courses']:
    w += students["S001"]['courses'][i]['credits']
    g += 1

alice_gpa = w/count

if alice_gpa > bob_gpa:
    print('alice', alice_gpa)
else:
    print('bob', bob_gpa)


