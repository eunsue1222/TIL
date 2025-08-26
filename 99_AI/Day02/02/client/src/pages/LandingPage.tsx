import React from 'react';

const LandingPage: React.FC = () => {
  return (
    <div className="container mt-5">
      <div className="p-5 mb-4 bg-light rounded-3">
        <div className="container-fluid py-5">
          <h1 className="display-5 fw-bold">SSAFY AI 챗봇 서비스</h1>
          <p className="col-md-8 fs-4">SSAFY 브랜드의 AI 챗봇 서비스에 오신 것을 환영합니다. 최신 AI 기술을 통해 궁금한 점을 해결해 보세요.</p>
        </div>
      </div>

      <div className="row align-items-md-stretch">
        <div className="col-md-6">
          <div className="h-100 p-5 text-white bg-dark rounded-3">
            <h2>주요 기능</h2>
            <p>실시간 채팅, 이미지 질문 등 다양한 기능을 통해 AI와 소통할 수 있습니다.</p>
          </div>
        </div>
        <div className="col-md-6">
          <div className="h-100 p-5 bg-light border rounded-3">
            <h2>시작하기</h2>
            <p>지금 바로 회원가입하고 SSAFY AI 챗봇의 모든 기능을 경험해 보세요.</p>
          </div>
        </div>
      </div>
    </div>
  );
};

export default LandingPage;
