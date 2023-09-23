import React, { useEffect, useState } from 'react';
import './styles.css';
import Spinner from '../components/Spinner';
import api from '../api';
import { showToast } from './Toast';
import './styles.css';

export default function QuizComponent() {
  const [questions, setQuestions] = useState([]);
  const [index, setIndex] = useState(0);
  const [answers, setAnswers] = useState({});
  const [score, setScore] = useState(null);

  useEffect(() => {
    if (!localStorage.getItem('email')) {
      window.location = '/start';
    }
    api
      .get('/questions')
      .then((response) => {
        setQuestions(response.data.data.questions);
      })
      .catch((error) => {
        showToast(error);
      });
  }, []);

  const handleAnswerChange = (e) => {
    const questionId = e.target.name;
    const answerId = e.target.value;
    setAnswers({ ...answers, [questionId]: answerId });
  };

  const handleQuizSubmit = () => {
    if (Object.keys(answers).length !== questions.length) {
      showToast('All questions must me answered!');
      return;
    }
    showToast('Submitting quiz...');
    const headers = { email: localStorage.getItem('email') };
    api
      .post('/questions', answers, { headers })
      .then((response) => {
        setQuestions(response.data.data.questions);
        setScore(response.data.data.score);
        setIndex(0);
      })
      .catch((error) => {
        showToast(error);
      });
  };

  if (questions.length === 0) {
    return <Spinner />;
  }
  return (
    <div>
      {score !== null ? (
        <div className="alert alert-success" role="alert">
          <strong>[You scored {`${score} out of ${questions.length}`}]</strong>{' '}
          {score < questions.length / 3 && score !== 0
            ? "Great effort! Keep studying and you'll improve. You're on the right path to mastering the Bible. 🤗🤗"
            : score > questions.length / 3 && score < questions.length
            ? "Well done! You're making good progress. Keep going, and you'll become even more knowledgeable about the Bible. 🎉🎉"
            : score === questions.length
            ? "Congratulations! You've achieved a perfect score! Your knowledge of the Bible is exceptional. Keep up the excellent work!"
            : 'Well this is awkward! 😂😂😂'}
        </div>
      ) : (
        ''
      )}
      <div>
        <h6 className="display-6">
          Question {`${index + 1} of ${questions.length}`}
        </h6>
      </div>
      <div>
        <div>
          <p className="question-text">{questions[index].text}</p>
        </div>
        <hr />
        <div className="row g-2 p-2">
          {questions[index].answers.map((answer) => {
            let style = '';
            if (score !== null) {
              if (
                questions[index].correct_answer ===
                  questions[index].user_answer &&
                questions[index].correct_answer === answer.id
              ) {
                style = 'correct-answer';
              } else if (questions[index].correct_answer === answer.id) {
                style = 'correct-answer';
              } else if (
                questions[index].user_answer !==
                  questions[index].correct_answer &&
                questions[index].user_answer === answer.id
              ) {
                style = 'wrong-answer';
              }
            }

            return (
              <div
                className={`form-check col-12 col-md-6 ${style}`}
                key={answer.id}
              >
                <input
                  className="form-check-input"
                  type="radio"
                  name={questions[index].id}
                  id={answer.id}
                  value={answer.id}
                  onChange={handleAnswerChange}
                  checked={answers[questions[index].id] === answer.id}
                />
                <label className="form-check-label" htmlFor={answer.id}>
                  {answer.text}
                </label>
              </div>
            );
          })}
        </div>
        <div>
          <input
            type="button"
            value="Prev"
            className="btn btn-md btn-secondary me-3 mt-3"
            onClick={() => {
              if (index === 0) return;
              setIndex(index - 1);
            }}
          />
          {index + 1 < questions.length ? (
            <input
              type="button"
              value="Next"
              className="btn btn-md btn-secondary me-3 mt-3"
              onClick={() => {
                if (Object.keys(answers).includes(questions[index].id)) {
                  setIndex(index + 1);
                } else {
                  showToast('Answer this question before proceeding.');
                }
              }}
            />
          ) : score === null ? (
            <input
              type="button"
              value="Submit"
              className="btn btn-md btn-danger me-3 mt-3"
              onClick={handleQuizSubmit}
            />
          ) : (
            <input
              type="button"
              value="Start Again"
              className="btn btn-md btn-danger me-3 mt-3"
              onClick={() => (window.location = '/questions')}
            />
          )}

          {score !== null ? (
            <input
              type="button"
              value="Home"
              className="btn btn-md btn-primary me-3 mt-3"
              onClick={() => (window.location = '/')}
            />
          ) : (
            ''
          )}
        </div>
      </div>
    </div>
  );
}
