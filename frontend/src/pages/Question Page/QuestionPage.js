import React, { useState, useEffect } from 'react';
import axios from 'axios';
import Loader from 'react-loaders';
import './QuestionPage.scss';

function QuestionPage(props) {
  const [questions, setQuestions] = useState([]);
  const [index, setIndex] = useState(0);
  const [answers, setAnswers] = useState([]);
  const [loading, setLoading] = useState(true);

  // A function to fetch the questions from the API
  const fetchQuestions = async () => {
    try {
      // Make a GET request to the API endpoint
      const response = await axios.get('http://kamvamindpal.com/v1/questions');

      // Set the questions state with the data
      setQuestions(response.data);
      console.log(response.data);

      // Set the loading state to false
      setLoading(false);
    } catch (error) {
      // Handle the error
      console.error(error);
      alert('Something went wrong. Please try again later.');
    }
  };

  // A function to handle the user answer selection
  const handleAnswer = (e) => {
    // Get the value of the selected option
    const value = e.target.value;
    // Update the answers state with the value at the current index
    setAnswers((prev) => {
      return [...prev.slice(0, index), value, ...prev.slice(index + 1)];
    });
  };

  // A function to handle the next button click
  const handleNext = () => {
    // Check if the user has answered the current question
    if (answers[index] == null) {
      alert('Please select an answer before proceeding');
    } else {
      // Increment the index state by one
      setIndex((prev) => prev + 1);
    }
  };

  // A function to handle the submit button click
  const handleSubmit = () => {
    // Check if the user has answered all the questions
    if (answers.length < questions.length) {
      alert('Please answer all the questions before submitting');
    } else {
      // Pass the user answers to the parent component
      props.onQuizSubmit(answers);
    }
  };

  useEffect(() => {
    fetchQuestions();
  }, []);

  return (
    <div className="question-page">
      {loading ? (
        <Loader type="pacman" />
      ) : (
        <div className="question-center">
          <h1>Quiz</h1>
          <p>
            Question {index + 1} of {questions.length}
          </p>
          {questions.length > 0 && (
            <div className="question">
              <h2>{questions[index].text}</h2>
              <div className="options">
                {questions[index].answers.map((option, i) => (
                  <div key={option.id} className="option">
                    <input
                      type="radio"
                      id={`option-${i}`}
                      name="answer"
                      value={option.text}
                      checked={answers[index] === option.text}
                      onChange={handleAnswer}
                    />
                    <label htmlFor={`option-${i}`}>{option.text}</label>
                  </div>
                ))}
              </div>
            </div>
          )}
          {index === questions.length - 1 ? (
            <button onClick={handleSubmit}>Submit</button>
          ) : (
            <button onClick={handleNext}>Next</button>
          )}
        </div>
      )}
    </div>
  );
}

export default QuestionPage;
