#!/usr/bin/env python3
"""Question API Module"""

from api.v1.views import app_views, postdata
from flask import jsonify, abort, request
from models.question import Question
from models.answer import Answer
from models.result import Result
from models.user import User
from models import storage
from random import choice
from sqlalchemy.exc import IntegrityError

QUESTION_PER_ROUND = 25


@app_views.route('/questions', methods=['GET'])
def get_questions():
    """Returns a list of questions"""
    questions = list(storage.all(Question).values())

    user_questions = []
    if len(questions) > QUESTION_PER_ROUND:
        for _ in range(QUESTION_PER_ROUND):
            question = choice(questions)
            index = questions.index(question)
            user_questions.append(questions.pop(index))
    else:
        user_questions = questions

    return jsonify({
        "status": "success",
        "message": "Questions retrieved successfully",
        "data": {
            "questions": [q.to_dict() for q in user_questions],
            "count": len(user_questions)
        }
    })


@app_views.route('/questions', methods=['POST'])
def grade_questions():
    """Returns answers to User's questions"""
    email = request.headers.get('email')
    user = storage.match(User, email=email)

    data = postdata()
    if data is None:
        abort(400)

    questions = []
    user_score = 0

    for question_id, answer_id in data.items():
        question: Question = storage.get(Question, question_id)
        answer: Answer = storage.get(Answer, answer_id)
        if answer in question.answers and answer.is_correct:
            user_score += 1

        q_dict = question.to_dict()
        q_dict.update({'user_answer': answer_id,
                      'correct_answer': question.get_correct_answer().id})
        questions.append(q_dict)

    result = Result(user=user, score=user_score)
    try:
        result.save()
    except IntegrityError as exc:
        storage.rollback()
        return jsonify({
            "status": "error",
            "message": "Integrity Error: " + str(exc),
            "data": None
        }), 422

    return jsonify({
        "status": "success",
        "message": "Questions graded successfully",
        "data": {
            "questions": questions,
            "count": len(questions),
            "score": user_score
        }

    })
