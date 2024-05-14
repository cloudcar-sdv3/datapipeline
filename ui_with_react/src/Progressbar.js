import React from "react";
import "./App.css"; // Import the CSS file

const stages = [
  "Images Imported",
  "Labeling Started",
  "Labeling Completed",
  "Training Started",
  "Training Completed",
  "Model Saved",
  "Ota Triggered"
];

const Progressbar = ({ currentStage }) => {
  const parts = stages.length;
  const partWidth = 100 / parts;
  const progressParts = stages.indexOf(currentStage) + 1;

  return (
    <div className="progress-bar">
      <div
        className="progress-bar-success"
        style={{ width: `${progressParts * partWidth}%` }}
      ></div>
      {stages.map((stage, i) => (
        <div
          key={i}
          className="progress-bar-stage"
          style={{ left: `${(i + 1) * partWidth}%` }}
        >
          {i < progressParts ? (
            <img src="/app_icons/ok.png" width="40rem" alt="✓" />
          ) : (
            ""
          )}
          <div className="progress-bar-stage-text">{stage}</div>
        </div>
      ))}
    </div>
  );
};

export default Progressbar;
