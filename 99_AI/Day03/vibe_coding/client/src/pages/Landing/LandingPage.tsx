import React from 'react';
import './LandingPage.css';

const LandingPage: React.FC = () => {
  return (
    <div className="landing-container">
      <div className="landing-content">
        <h1>SSAFY AI 챗봇 서비스</h1>
        <p>
          당신의 모든 질문에 <span style={{ color: '#FE7E1D', fontWeight: 'bold' }}>지능적인 답변</span>을 실시간으로 제공합니다.
        </p>
      </div>
    </div>
  );
};

export default LandingPage;
