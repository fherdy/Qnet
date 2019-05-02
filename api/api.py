from flask import Flask, jsonify, request
# import pandas
import json

app = Flask(__name__)

# def __readInFile(path, list):
#     list = []
#     data = pandas.read_csv(path)
#     for i, row in data.iterrows():
#         for school in row:
#             list.append(school)
#     return jsonify(list)

@app.route('/')
def root():
    return 'api'

@app.route('/readInSchools')
def getSchools():
    with open('schools.json') as f:
        data = json.load(f)
    return jsonify(data)

@app.route('/readInCourses')
def getCourses():
    with open('courses.json') as f:
        data = json.load(f)
    return jsonify(data)

@app.route('/readInQuestions')
def getQuestions():
    with open('questions.json') as f:
        data = json.load(f)
    return jsonify(data)


# __editDistanceMemo = {}

# def editDistance(str1, str2):
#     return editDistance(str1, str2, len(str1), len(str2))

# def editDistance(str1, str2, i, j):
#     if (str1, str2, i, j) in __editDistanceMemo:
#         return __editDistanceMemo[(str1, str2, i, j)]
#     if i==0:
#         ans = j
#     if j==0:
#         ans = i
#     if str1[i]==str2[j]:
#         ans = editDistance(str1, str2, i-1, j-1)
#     else:
#         ans = 1 + min(editDistance(str1, str2, i-1, j), editDistance(str1, str2, i, j-1), editDistance(str1, str2, i-1, j-1))
#     __editDistanceMemo[(str1, str2, i, j)] = ans
#     return ans

@app.route('/writeToQuestions')
def writeToQuestions():
    text = request.args.get('text')
    if text is None or text is '':
        return 'text is null'
    school = request.args.get('school') 
    if school is None or school is '':
        return 'school is null'
    course = request.args.get('course')
    if course is None or course is '':
        return 'course is null'

    with open('schools.json') as f:
        schools = json.load(f)
    with open('courses.json') as f:
        courses = json.load(f)

    if school not in schools:
        with open('schools.json', 'w') as outfile:
            schools.append(school)
            json.dump(schools, outfile)

    if course not in courses:
        with open('courses.json', 'w') as outfile:
            courses.append(course)
            json.dump(courses, outfile)

    with open('questions.json') as f:
        questions = json.load(f)

    with open('questions.json', 'w') as outfile:
        questions.append({
            'text': text,
            'school': school,
            'course': course,
        })
        json.dump(questions, outfile)

    return text

app.run(debug=True)

