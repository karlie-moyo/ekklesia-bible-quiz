import React, { useState } from "react";
import "./App.scss";
import LandingPage from "./pages/Landing Page/LandingPage";
import QuestionPage from "./pages/Question Page/QuestionPage";
import ResultPage from "./pages/Result Page/ResultPage";

function App() {
  const [user, setUser] = useState(null);
  const [quiz, setQuiz] = useState(false);

  const handleUserSubmit = (userData) => {
    setUser(userData);
    setQuiz(true);
  };

  const handleQuizSubmit = (userAnswers) => {
    setUser((prev) => {
      return { ...prev, answers: userAnswers };
    });
    setQuiz(false);
  };

  const handleQuizRestart = () => {
    setUser(null);
    setQuiz(false);
  };

  return (
    <div className="app">
      {user == null ? (
        <LandingPage onUserSubmit={handleUserSubmit} />
      ) : quiz ? (
        <QuestionPage onQuizSubmit={handleQuizSubmit} />
      ) : (
        <ResultPage answers={user.answers} onQuizRestart={handleQuizRestart} />
      )}
    </div>
  );
}

export default App;
