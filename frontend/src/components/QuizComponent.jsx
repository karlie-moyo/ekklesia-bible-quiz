import React, { useEffect, useState } from 'react';
import './styles.css';
import Spinner from '../components/Spinner';
import api from '../api';
import { showToast } from './Toast';
import './styles.css';

function zfill(number, width) {
  const numString = String(number);
  return '0'.repeat(Math.max(0, width - numString.length)) + numString;
}

export default function QuizComponent() {
  const [questions, setQuestions] = useState([]);
  const [index, setIndex] = useState(0);
  const [answers, setAnswers] = useState({});
  const [score, setScore] = useState(null);
  const [timer, setTimer] = useState(null);

  useEffect(() => {
    if (!localStorage.getItem('email')) {
      window.location = '/start';
    }
    api
      .get('/questions')
      .then((response) => {
        setQuestions(response.data.data.questions);
        setTimer(response.data.data.questions.length * 1);
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
      if (timer !== 0) {
        showToast('All questions must me answered!');
        return;
      } else {
        console.log(questions);
        console.log(answers);
        for (let q of questions) {
          if (!answers.hasOwnProperty(q.id)) {
            answers[q.id] = null;
          }
        }
      }
    }
    setTimer(null);

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

  useEffect(() => {
    const interval = setInterval(() => {
      if (timer !== null) {
        setTimer((x) => x - 1);
      }
    }, 1000);

    if (timer <= 0 && timer !== null) {
      handleQuizSubmit();
    }

    return () => {
      clearInterval(interval);
    };
  }, [timer]);

  if (questions.length === 0) {
    return <Spinner />;
  }
  return (
    <div>
      {score !== null ? (
        <div className="alert alert-success" role="alert">
          <strong>[You scored {`${score} out of ${questions.length}`}]</strong>{' '}
          {score < questions.length / 3 && score !== 0
            ? "Great effort! Keep studying and you'll improve. You're on the right path to mastering the Scripture. 🤗🤗"
            : score > questions.length / 3 && score < questions.length
            ? "Well done! You're making good progress. Keep going, and you'll become even more knowledgeable about the Bible. 🎉🎉"
            : score === questions.length
            ? "Congratulations! You've achieved a perfect score! Your knowledge of the Bible is exceptional. Keep up the excellent work!"
            : 'Well this is awkward! 😂😂😂'}
        </div>
      ) : (
        ''
      )}
      <div className="d-flex justify-content-between">
        <h6 className="display-6">
          Question {`${index + 1} of ${questions.length}`}
        </h6>

        <h6>
          {zfill(Math.floor(timer / 60), 2)}:{zfill(timer % 60, 2)}
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
        <div className="row">
          <div className="col-md">
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
            ) : (
              ''
            )}
          </div>
          <div className="col-md d-flex justify-content-end">
            <input
              type="button"
              value="Home"
              className="btn btn-md btn-primary me-3 mt-3 ms-auto"
              onClick={() => (window.location = '/')}
            />
            {score === null || timer !== null ? (
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
          </div>
        </div>
      </div>
    </div>
  );
}
