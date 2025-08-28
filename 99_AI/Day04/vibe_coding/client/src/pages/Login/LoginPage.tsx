import React, { useState } from 'react';
import { Link } from 'react-router-dom';
import TextInput from '../../components/Form/TextInput/TextInput';

const LoginPage: React.FC = () => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    // TODO: Dispatch login thunk
    console.log({ email, password });
  };

  return (
    <div className="container mt-5" style={{ maxWidth: '400px' }}>
      <h2 className="text-center mb-4">로그인</h2>
      <form onSubmit={handleSubmit}>
        <TextInput id="email" label="이메일" type="email" value={email} onChange={(e) => setEmail(e.target.value)} />
        <TextInput id="password" label="비밀번호" type="password" value={password} onChange={(e) => setPassword(e.target.value)} />
        <button type="submit" className="btn btn-primary w-100">로그인</button>
        <div className="text-center mt-3">
          <Link to="/register" className="text-dark">회원이 아니신가요?</Link>
        </div>
      </form>
    </div>
  );
};

export default LoginPage;