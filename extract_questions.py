#!/usr/bin/env python3
"""Process Quiz Questions from text"""
from models.question import Question
from models.answer import Answer

with open('questions.txt', 'r', encoding='utf-8', newline='') as f:
    data = f.readlines()

index = 1
for line in data:
    text = line.strip()
    text = text.replace('\n', '')
    text = text.replace('*', '')
    is_correct = '*' in line

    if index % 5 == 1:
        question = Question(text=text)
        question.save()
    else:
        answer = Answer(text=text, question=question, is_correct=is_correct)
        answer.save()
    index += 1
