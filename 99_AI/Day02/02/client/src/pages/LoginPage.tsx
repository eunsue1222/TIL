import React from 'react';
import { Button, Form, Container, Row, Col } from 'react-bootstrap';
import { Link } from 'react-router-dom';

const LoginPage: React.FC = () => {
  return (
    <Container className="mt-5">
      <Row className="justify-content-md-center">
        <Col md={6}>
          <h2 className="text-center mb-4">로그인</h2>
          <Form>
            <Form.Group className="mb-3" controlId="formBasicEmail">
              <Form.Label>이메일 주소</Form.Label>
              <Form.Control type="email" placeholder="이메일을 입력하세요" />
            </Form.Group>

            <Form.Group className="mb-3" controlId="formBasicPassword">
              <Form.Label>비밀번호</Form.Label>
              <Form.Control type="password" placeholder="비밀번호를 입력하세요" />
            </Form.Group>

            <div className="d-grid gap-2">
                <Button variant="primary" type="submit" style={{ backgroundColor: '#007bff', borderColor: '#007bff' }}>
                    로그인
                </Button>
            </div>
          </Form>
          <div className="mt-3 text-center">
            <Link to="/register">회원이 아니신가요? 회원가입</Link>
          </div>
        </Col>
      </Row>
    </Container>
  );
};

export default LoginPage;
