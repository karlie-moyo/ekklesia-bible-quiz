import React, { useCallback, useEffect, useMemo, useState } from "react";
import './LandingPage.scss';
import PageHero from "../../components/Page Hero/PageHero";

function LandingPage(props) {
    const [name, setName] = useState("");
    const [email, setEmail] = useState("");
    
    const [backgroundImageIndex, setBackgroundImageIndex] = useState(0);

    const backgroundImages = useMemo(() => [
        'url(https://images.unsplash.com/photo-1586202690944-7282c12105f0?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8OHx8aG9seSUyMGJpYmxlfGVufDB8fDB8fHww&auto=format&fit=crop&w=500&q=60)',
        'url(https://images.unsplash.com/photo-1599964815811-30b9aea11d17?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8OHx8d29yZCUyMG9mJTIwR29kfGVufDB8fDB8fHww&auto=format&fit=crop&w=500&q=60)',
        'url(https://images.unsplash.com/photo-1600546706018-9e1267462ddc?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTB8fHdvcmQlMjBvZiUyMEdvZHxlbnwwfHwwfHx8MA%3D%3D&auto=format&fit=crop&w=500&q=60)',
        'url(https://images.unsplash.com/photo-1537806411245-54cba05fd745?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTd8fGhvbHklMjBiaWJsZXxlbnwwfHwwfHx8MA%3D%3D&auto=format&fit=crop&w=500&q=60)',
    ], []);

    // A function to change background image
    const changeBackground = useCallback((increment) => {
        const newIndex = (backgroundImageIndex + increment + backgroundImages.length) % backgroundImages.length;
        setBackgroundImageIndex(newIndex);
    }, [backgroundImageIndex, backgroundImages]);
    
    useEffect(() => {
        console.log("useEffect triggered"); // Add this line
        const interval = setInterval(() => {
          changeBackground(1); // Move to the next background image
        }, 9000); // Change the background every 9 seconds
    
        return () => clearInterval(interval); // Clear the interval on component unmount
    }, [changeBackground]);

    // A function to handle form submission
    const handleSubmit = (e) => {
        e.preventDefault();

        if (name.trim() === "" || email.trim() === "") {
        alert("Please enter your name and email");
        } else {
        props.onUserSubmit({ name, email });
        }
    };

  return (
    <div 
        className="landing-page"
        style={{
            backgroundImage: `radial-gradient(circle, rgba(15,4,71,0.0984768907563025) 0%, rgba(7,4,48,0.7595413165266106) 58%), ${backgroundImages[backgroundImageIndex]}`,
            backgroundPosition: 'center',
            backgroundRepeat: 'no-repeat',
            backgroundSize: 'cover'
        }}>
        <div className="form-center">
            <h1>Welcome to the Bible Quiz App</h1>
            <p>Please enter your name and email to start the quiz</p>
            <form onSubmit={handleSubmit}>
                <div className="form-group">
                <label htmlFor="name">Name</label>
                <input
                    type="text"
                    id="name"
                    value={name}
                    onChange={(e) => setName(e.target.value)}
                />
                </div>
                <div className="form-group">
                <label htmlFor="email">Email</label>
                <input
                    type="email"
                    id="email"
                    value={email}
                    onChange={(e) => setEmail(e.target.value)}
                />
                </div>
                <button type="submit">Start</button>
            </form>
        </div>
        <PageHero/>
    </div>
  );
}

export default LandingPage;
