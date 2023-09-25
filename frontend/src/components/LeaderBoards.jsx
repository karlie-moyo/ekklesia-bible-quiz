import React, { useEffect, useState } from 'react';
import Spinner from './Spinner';
import api from '../api';
import { showToast } from './Toast';

export default function LeaderBoards() {
  const [leaderboards, setLeaderboards] = useState([]);

  useEffect(() => {
    api
      .get('/leaderboards')
      .then((response) => {
        setLeaderboards(response.data.data.leaderboards);
      })
      .catch((error) => {
        showToast(error);
      });
  }, []);

  return (
    <>
      <div>
        <h4 className="display-5">Leaderboards</h4>
        <small className="text-muted">
          Here, you can track your progress and see how you rank among fellow
          Bible enthusiasts. Discover where you stand in the world of biblical
          knowledge as you compete with others in answering challenging
          questions from the Scriptures. Whether you're aiming for the top spot
          or simply seeking to improve your understanding of the Bible, our
          Leaderboard provides insight into your performance and achievements.
        </small>
      </div>

      {leaderboards.length === 0 ? (
        <Spinner />
      ) : (
        <>
          <div className="mt-4 table-container">
            <table className="table table-striped table-hover">
              <thead>
                <tr>
                  <th scope="col">#</th>
                  <th scope="col">Name</th>
                  <th scope="col">Score</th>
                  <th scope="col">Date</th>
                </tr>
              </thead>
              <tbody>
                {leaderboards.map((item, index) => {
                  const dateObject = new Date(item.created_at);
                  return (
                    <tr key={item.id}>
                      <th scope="row">{index + 1}</th>
                      <td>{item.user.name}</td>
                      <td>{item.score}</td>
                      <td>{dateObject.toLocaleString('en-US')}</td>
                    </tr>
                  );
                })}
              </tbody>
            </table>
          </div>
        </>
      )}

      <input
        type="button"
        value="Home"
        className="btn btn-lg btn-primary me-3 mt-3 ms-auto"
        onClick={() => (window.location = '/')}
      />
    </>
  );
}
