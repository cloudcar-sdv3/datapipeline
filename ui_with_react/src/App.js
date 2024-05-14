/* eslint-disable react/jsx-pascal-case */
import React, { useState, useEffect } from "react";

import Toolbar from "./Toolbar"; // Add this line
import "./App.css";
import Progressbar from "./Progressbar";

const App = () => {
  const [status, setStatus] = useState({});

  useEffect(() => {
    const intervalId = setInterval(() => {
      fetch("/update.json")
        .then((response) => response.json())
        .then((data) => {
          setStatus(data);
        })
        .catch((error) => {
          console.error("Error fetching status:", error);
        });
    }, 500); // Check for updates every second

    return () => clearInterval(intervalId); // Cleanup function
  }, []);

  return (
    <div>
      <Toolbar />
      <div className="app-container">
        <Progressbar currentStage={status.cloud_status} />

        <div className="right-half"></div>
      </div>
    </div>
  );
};

export default App;
