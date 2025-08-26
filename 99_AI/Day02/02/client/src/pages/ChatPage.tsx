import React, { useState } from 'react';
import { Button, Form, InputGroup } from 'react-bootstrap';

const ChatPage: React.FC = () => {
  const [prompt, setPrompt] = useState('');
  const [imagePreview, setImagePreview] = useState<string | null>(null);

  const handleImageUpload = (e: React.ChangeEvent<HTMLInputElement>) => {
    if (e.target.files && e.target.files[0]) {
      const file = e.target.files[0];
      setImagePreview(URL.createObjectURL(file));
    }
  };

  const handleRemoveImage = () => {
    setImagePreview(null);
    // Also reset the file input if needed
  };

  const handleSend = () => {
    // Logic to send prompt and image
    console.log({ prompt, image: imagePreview });
    setPrompt('');
  };

  return (
    <div style={{ display: 'flex', flexDirection: 'column', height: 'calc(100vh - 56px)' }}>
      {/* Chat History Area */}
      <div style={{ flexGrow: 1, overflowY: 'auto', padding: '1rem' }}>
        {/* Placeholder for chat messages */}
        <div className="d-flex justify-content-end mb-3">
          <div className="bg-primary text-white p-2 rounded" style={{ maxWidth: '60%' }}>
            안녕하세요! 이것은 사용자 질문 예시입니다.
          </div>
        </div>
        <div className="d-flex justify-content-start mb-3">
          <div className="bg-light p-2 rounded" style={{ maxWidth: '60%' }}>
            안녕하세요! AI 응답 예시입니다.
          </div>
        </div>
      </div>

      {/* Input Area */}
      <div className="p-2 bg-light" style={{ borderTop: '1px solid #ddd' }}>
        <InputGroup>
          <div className="position-relative">
            <Button variant="outline-secondary" as="label" htmlFor="image-upload">
              🖼️
              <Form.Control id="image-upload" type="file" accept="image/*" onChange={handleImageUpload} hidden />
            </Button>
            {imagePreview && (
              <div className="position-absolute bottom-100 start-0 mb-2">
                <img src={imagePreview} alt="Preview" height="50" className="rounded" />
                <Button variant="danger" size="sm" className="position-absolute top-0 start-100 translate-middle p-1" onClick={handleRemoveImage}>X</Button>
              </div>
            )}
          </div>
          <Form.Control
            placeholder="프롬프트를 입력하세요..."
            value={prompt}
            onChange={(e) => setPrompt(e.target.value)}
            onKeyPress={(e) => e.key === 'Enter' && handleSend()}
          />
          <Button variant="primary" onClick={handleSend} style={{ backgroundColor: '#007bff', borderColor: '#007bff' }}>
            전송
          </Button>
        </InputGroup>
      </div>
    </div>
  );
};

export default ChatPage;
