import React, { useState, useEffect, useCallback } from "react";
import axios from "axios";

function ResultPage(props) {
    const [results, setResults] = useState([]);
    const [correct, setCorrect] = useState([]);
    const [loading, setLoading] = useState(true);

    // A function to fetch the results from the API
    const fetchResults = useCallback(async () => {
        try {
            // Make a POST request to the API endpoint with the user answers
            const response = await axios.post(
                "https://example.com/api/results",
                props.answers
            );
            // Set the results state with the data
            setResults(response.data);
            // Set the correct state with the number of correct answers
            setCorrect(response.data.filter((result) => result.correct).length);
            // Set the loading state to false
            setLoading(false);
        } catch (error) {
            // Handle the error
            console.error(error);
            alert("Something went wrong. Please try again later.");
        }
    }, [props.answers]);

    // A function that handles restart
    const handleRestart = () => {
        props.onQuizRestart();
    };

    // Use effect hook to fetch the results when the component mounts
    useEffect(() => {
        fetchResults();
    }, [fetchResults]);

  return (
    <div className="result-page">
        {loading ? (
            <p>Loading...</p>
        ) : (
            <>
                <h1>Quiz App</h1>
                <p>
                    You scored {correct} out of {results.length}
                </p>
                <div className="results">
                    {results.map((result, i) => (
                        <div key={i} className="result">
                            <h2>{result.question}</h2>
                            <p>
                                Your answer:{" "}
                                <span className={result.correct ? "green" : "red"}>
                                    {result.answer}
                                </span>
                            </p>
                        {result.correct ? null : (
                        <p>
                            Correct answer:{" "}
                            <span className="green">{result.correctAnswer}</span>
                        </p>
                    )}
                </div>
            ))}
        </div>
        <button onClick={handleRestart}>Restart</button>
            </>
        )}
    </div>
  );
}

export default ResultPage;
