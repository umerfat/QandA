from flask import Flask, url_for, request, render_template
from QandA.app import app
import redis
# connect to redis data store
#r = redis.StrictRedis(host='localhost', port=6379, db=0, charset= "utf-8", decode_responses= True)
# All three lines here are same
# r = redis.StrictRedis()
#r = redis.StrictRedis(host='qanda.redis.cache.windows.net', port=6379, ssl = True, db = 0, password = '')

# Server/create
@app.route('/')
def hello():
    createLink = "<a href = '" + url_for('create') + "'> Create Question </a>"
    return """ <!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="utf-8" />
        <title>Create Question</title>
    </head>
    <body>
        <div> <h2>Welcome to flask</h2> </div>
    </body>
</html>
    """
#Server Create
# @app.route('/create', methods = ['GET', 'POST'])
# def create():
#     if request.method == 'GET':
#         # send the user form
#         return render_template('createQuestion.html')
#     elif request.method == 'POST':
#         # read form data and save it
#         title    = request.form['title']
#         question = request.form['question']
#         answer   = request.form['answer']
#         # store data in db
#         r.set(title + ':question', question)
#         r.set(title + ':answer', answer)
#         return render_template('createdQuestion.html', question = question)
#     else:
#         return "<h2>Invalid request</h2>"
# # Server question/title
# @app.route('/question/<title>', methods = ['GET', 'POST'])
# def question(title):
#     if request.method == 'GET':
#         #send user the form
#         question = r.get(title + ':question')
#         # read question from data store
#
#         return render_template('AnswerQuestion.html', question = question)
#     elif request.method == 'POST':
#         # Means user has submitted answer and we need to validate that
#         submittedAnswer = request.form['submittedAnswer']
#         # read answer from data store
#         answer = r.get(title + ':answer')
#         if submittedAnswer == answer:
#             return render_template('Correct.html')
#         else:
#             return render_template('Incorrect.html', submittedAnswer = submittedAnswer, answer = answer)
#     else:
#         return "<h2>Invalid request</h2>"
