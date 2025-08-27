import React, { useState } from 'react';
import { Link } from 'react-router-dom';
import './Navbar.css';

const Navbar: React.FC = () => {
  const [isNavCollapsed, setIsNavCollapsed] = useState(true);

  const handleNavCollapse = () => setIsNavCollapsed(!isNavCollapsed);

  return (
    <nav className="navbar navbar-expand-lg navbar-dark navbar-transparent">
      <div className="container-fluid">
        <Link className="navbar-brand" to="/">
          <span>SSAFY</span>
        </Link>
        <button
          className="navbar-toggler"
          type="button"
          data-bs-toggle="collapse"
          data-bs-target="#navbarNav"
          aria-controls="navbarNav"
          aria-expanded={!isNavCollapsed ? true : false}
          aria-label="Toggle navigation"
          onClick={handleNavCollapse}
        >
          <span className="navbar-toggler-icon"></span>
        </button>
        <div className={`${isNavCollapsed ? 'collapse' : ''} navbar-collapse justify-content-end`} id="navbarNav">
          <ul className="navbar-nav">
            <li className="nav-item">
              <Link className="nav-link" to="/chat" onClick={() => setIsNavCollapsed(true)}>채팅</Link>
            </li>
            <li className="nav-item">
              <Link className="nav-link" to="/login" onClick={() => setIsNavCollapsed(true)}>로그인</Link>
            </li>
            <li className="nav-item">
              <Link className="nav-link" to="/register" onClick={() => setIsNavCollapsed(true)}>회원가입</Link>
            </li>
          </ul>
        </div>
      </div>
    </nav>
  );
};

export default Navbar;
