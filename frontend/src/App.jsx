import React from 'react';
import { Routes, Route, useLocation } from 'react-router-dom';
import Home from './pages/Home';
import StartPage from './components/StartPage';
import QuizComponent from './components/QuizComponent';
import { Toast } from './components/Toast';

export default function App() {
  const location = useLocation();
  if (location.pathname === '/') {
    return <Home />;
  }
  return (
    <>
      <Toast />
      <div className="container d-flex justify-content-center align-items-center vh-100">
        <div className="CenteredRectangle rounded bg-light">
          <Routes>
            <Route path="/start" element={<StartPage />} />
            <Route path="/questions" element={<QuizComponent />} />
          </Routes>
        </div>
      </div>
    </>
  );
}
