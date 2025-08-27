import React from 'react';
import './LoadingBubble.css';

const LoadingBubble: React.FC = () => {
  return (
    <div className="d-flex justify-content-start mb-3">
      <div className="p-3 rounded bg-light" style={{ maxWidth: '70%' }}>
        <div className="loading-dots">
          <span></span>
          <span></span>
          <span></span>
        </div>
      </div>
    </div>
  );
};

export default LoadingBubble;
