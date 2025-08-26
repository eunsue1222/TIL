import React from 'react';
import { Navbar, Nav, Container, Button } from 'react-bootstrap';
import { LinkContainer } from 'react-router-bootstrap'; // react-router-bootstrap is a good choice for integrating react-router with react-bootstrap

const AppNavbar: React.FC = () => {
  const pointColor = '#00EEFF';

  return (
    <Navbar bg="dark" variant="dark" expand="lg">
      <Container>
        <LinkContainer to="/">
          <Navbar.Brand style={{ color: pointColor, fontWeight: 'bold' }}>SSAFY AI</Navbar.Brand>
        </LinkContainer>
        <Navbar.Toggle aria-controls="basic-navbar-nav" />
        <Navbar.Collapse id="basic-navbar-nav">
          <Nav className="ms-auto">
            <LinkContainer to="/chat">
              <Nav.Link>채팅</Nav.Link>
            </LinkContainer>
            <LinkContainer to="/login">
              <Nav.Link>로그인</Nav.Link>
            </LinkContainer>
            <LinkContainer to="/register">
              <Button variant="outline-info" style={{ borderColor: pointColor, color: pointColor }}>회원가입</Button>
            </LinkContainer>
          </Nav>
        </Navbar.Collapse>
      </Container>
    </Navbar>
  );
};

export default AppNavbar;
