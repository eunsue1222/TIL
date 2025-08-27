import React, { useState } from 'react';
import { Link } from 'react-router-dom';
import TextInput from '../../components/Form/TextInput/TextInput';
import Checkbox from '../../components/Form/Checkbox/Checkbox';

const RegisterPage: React.FC = () => {
  const [name, setName] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [confirmPassword, setConfirmPassword] = useState('');
  const [agreed, setAgreed] = useState(false);

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    // TODO: Dispatch register thunk
    console.log({ name, email, password, confirmPassword, agreed });
  };

  return (
    <div className="container mt-5" style={{ maxWidth: '400px' }}>
      <h2 className="text-center mb-4">회원가입</h2>
      <form onSubmit={handleSubmit}>
        <TextInput id="name" label="이름" value={name} onChange={(e) => setName(e.target.value)} />
        <TextInput id="email" label="이메일" type="email" value={email} onChange={(e) => setEmail(e.target.value)} />
        <TextInput id="password" label="비밀번호" type="password" value={password} onChange={(e) => setPassword(e.target.value)} />
        <TextInput id="confirmPassword" label="비밀번호 확인" type="password" value={confirmPassword} onChange={(e) => setConfirmPassword(e.target.value)} />
        <Checkbox id="terms" label="약관에 동의합니다." checked={agreed} onChange={(e) => setAgreed(e.target.checked)} />
        <button type="submit" className="btn btn-primary w-100">회원가입</button>
        <div className="text-center mt-3">
          <Link to="/login" className="text-dark">이미 회원이신가요?</Link>
        </div>
      </form>
    </div>
  );
};

export default RegisterPage;