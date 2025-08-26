import React from 'react';
import { Button, Form, Container, Row, Col } from 'react-bootstrap';
import { Link } from 'react-router-dom';

const RegisterPage: React.FC = () => {
  return (
    <Container className="mt-5">
      <Row className="justify-content-md-center">
        <Col md={6}>
          <h2 className="text-center mb-4">회원가입</h2>
          <Form>
            <Form.Group className="mb-3" controlId="formBasicName">
              <Form.Label>이름</Form.Label>
              <Form.Control type="text" placeholder="이름을 입력하세요" />
            </Form.Group>

            <Form.Group className="mb-3" controlId="formBasicEmail">
              <Form.Label>이메일 주소</Form.Label>
              <Form.Control type="email" placeholder="이메일을 입력하세요" />
            </Form.Group>

            <Form.Group className="mb-3" controlId="formBasicPassword">
              <Form.Label>비밀번호</Form.Label>
              <Form.Control type="password" placeholder="비밀번호를 입력하세요" />
            </Form.Group>

            <Form.Group className="mb-3" controlId="formBasicPasswordConfirm">
              <Form.Label>비밀번호 확인</Form.Label>
              <Form.Control type="password" placeholder="비밀번호를 다시 입력하세요" />
            </Form.Group>

            <Form.Group className="mb-3" controlId="formBasicCheckbox">
              <Form.Check type="checkbox" label="이용약관에 동의합니다." />
            </Form.Group>

            <div className="d-grid gap-2">
                <Button variant="primary" type="submit" style={{ backgroundColor: '#007bff', borderColor: '#007bff' }}>
                    회원가입
                </Button>
            </div>
          </Form>
          <div className="mt-3 text-center">
            <Link to="/login">이미 회원이신가요? 로그인</Link>
          </div>
        </Col>
      </Row>
    </Container>
  );
};

export default RegisterPage;
