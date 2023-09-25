import React from 'react';
import img from '../../static/religious-summer-camp.png';
import BackgroundImage from '../../components/BackgroundImage';

export default function Home() {
  return (
    <>
      <div className="container">
        <div className="row">
          <div className="col-lg-7 col-12">
            <h1 className="display-3 text-primary">Ekklesia Bible Quiz</h1>
            <p>
              The purpose of the quiz is to encourage believers to deepen their
              understanding of the Bible, foster spiritual growth, and promote
              biblical literacy. These ideas find a place in church events,
              study groups, and educational settings, encouraging friendly
              competition and assessment of biblical knowledge. They also play a
              role in evangelism, outreach, and cultural understanding, making
              them versatile tools for personal and communal reflection on the
              Scriptures.
            </p>

            <small>
              Ekklesia means the called-out ones dedicated to the Lord. Enjoy!
            </small>
            <div>
              <div className="mt-4">
                <a href="/start" className="btn btn-lg btn-primary me-4 mb-2">
                  Start Quiz
                </a>
                <a
                  href="/leaderboards"
                  className="btn btn-lg btn-secondary me-4 mb-2"
                >
                  Show Leader Boards
                </a>
              </div>
            </div>
          </div>
          <div className="col-lg-5 d-none d-lg-block">
            <img src={img} alt="" style={{ width: '100%' }} />
          </div>
        </div>
      </div>
      <BackgroundImage imageUrl="https://img.freepik.com/premium-photo/happy-epiphany-day-three-kings-day-christian-feast-day-generative-ai_870262-12465.jpg?size=626&ext=jpg&ga=GA1.1.1874357867.1690841151&semt=ais" />
    </>
  );
}
