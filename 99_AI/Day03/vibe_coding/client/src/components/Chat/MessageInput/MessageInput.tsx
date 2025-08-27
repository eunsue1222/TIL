import React, { useState, useRef } from 'react';
import { useAppDispatch, useAppSelector } from '../../../app/hooks';
import { sendMessage } from '../../../features/chat/thunks';
import { setPrompt, uploadImage, clearImage } from '../../../features/chat/chatSlice';
import ImagePreview from '../ImagePreview/ImagePreview';

const MessageInput: React.FC = () => {
  const dispatch = useAppDispatch();
  const { currentPrompt, isLoading, uploadedImage } = useAppSelector((state) => state.chat);
  const [imageFile, setImageFile] = useState<File | null>(null);
  const fileInputRef = useRef<HTMLInputElement>(null);

  const handleFileChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    const file = event.target.files?.[0];
    if (file) {
      setImageFile(file);
      const reader = new FileReader();
      reader.onloadend = () => {
        dispatch(uploadImage(reader.result as string));
      };
      reader.readAsDataURL(file);
    }
  };

  const handleSend = () => {
    if ((currentPrompt.trim() === '' && !imageFile) || isLoading) return;
    
    dispatch(sendMessage({ prompt: currentPrompt, file: imageFile }));

    dispatch(setPrompt(''));
    dispatch(clearImage());
    setImageFile(null);
    if(fileInputRef.current) {
        fileInputRef.current.value = '';
    }
  };

  return (
    <div className="fixed-bottom bg-light p-3">
      <ImagePreview />
      <div className="input-group">
        <input
          type="file"
          ref={fileInputRef}
          onChange={handleFileChange}
          className="d-none"
          id="imageUpload"
          accept="image/*"
        />
        <label htmlFor="imageUpload" className="btn btn-light btn-lg" style={{ border: 'none' }}>
          <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M9 22H15C20 22 22 20 22 15V9C22 4 20 2 15 2H9C4 2 2 4 2 9V15C2 20 4 22 9 22Z" stroke="#6c757d" strokeWidth="1.5" strokeLinecap="round" strokeLinejoin="round"/>
            <path d="M8 12H16" stroke="#6c757d" strokeWidth="1.5" strokeLinecap="round" strokeLinejoin="round"/>
            <path d="M12 16V8" stroke="#6c757d" strokeWidth="1.5" strokeLinecap="round" strokeLinejoin="round"/>
          </svg>
        </label>
        <input
          type="text"
          className="form-control"
          placeholder="메시지를 입력하세요..."
          value={currentPrompt}
          onChange={(e) => dispatch(setPrompt(e.target.value))}
          onKeyPress={(e) => e.key === 'Enter' && handleSend()}
          disabled={isLoading}
        />
        <button className="btn btn-primary" onClick={handleSend} style={{backgroundColor: '#00EEFF', borderColor: '#00EEFF'}}>
          전송
        </button>
      </div>
    </div>
  );
};

export default MessageInput;
