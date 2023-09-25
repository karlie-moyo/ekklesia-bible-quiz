import React from 'react';
import { Routes, Route, useLocation } from 'react-router-dom';
import Home from './pages/Home';
import StartPage from './components/StartPage';
import QuizComponent from './components/QuizComponent';
import { Toast } from './components/Toast';
import BackgroundImage from './components/BackgroundImage';
import LeaderBoards from './components/LeaderBoards';

export default function App() {
  const location = useLocation();
  if (location.pathname === '/') {
    return <Home />;
  }
  return (
    <>
      <Toast />
      <div className="container d-flex justify-content-center align-items-center vh-100 text-black">
        <div className="CenteredRectangle rounded bg-light">
          <Routes>
            <Route path="/start" element={<StartPage />} />
            <Route path="/questions" element={<QuizComponent />} />
            <Route path="/leaderboards" element={<LeaderBoards />} />
          </Routes>
        </div>
      </div>
      <BackgroundImage imageUrl="https://img.freepik.com/premium-photo/happy-epiphany-day-three-kings-day-christian-feast-day-generative-ai_870262-12465.jpg?size=626&ext=jpg&ga=GA1.1.1874357867.1690841151&semt=ais" />
    </>
  );
}
