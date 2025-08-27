import React from 'react';
import { useAppDispatch, useAppSelector } from '../../../app/hooks';
import { clearImage } from '../../../features/chat/chatSlice';

const ImagePreview: React.FC = () => {
  const dispatch = useAppDispatch();
  const { uploadedImage } = useAppSelector((state) => state.chat);

  if (!uploadedImage) {
    return null;
  }

  return (
    <div style={{ position: 'absolute', bottom: '80px', left: '1rem' }}>
      <div className="position-relative d-inline-block">
        <img src={uploadedImage} alt="Preview" style={{ width: '100px', height: '100px', objectFit: 'cover', borderRadius: '8px' }} />
        <button
          type="button"
          className="btn-close"
          aria-label="Close"
          onClick={() => dispatch(clearImage())}
          style={{
            position: 'absolute',
            top: '5px',
            right: '5px',
            backgroundColor: 'rgba(0, 0, 0, 0.5)',
            borderRadius: '50%',
            padding: '4px',
            filter: 'invert(1) grayscale(100%) brightness(200%)' // Makes the X white
          }}
        ></button>
      </div>
    </div>
  );
};

export default ImagePreview;
