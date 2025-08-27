import React from 'react';

interface TextInputProps {
  id: string;
  label: string;
  type?: string;
  value: string;
  onChange: (e: React.ChangeEvent<HTMLInputElement>) => void;
}

const TextInput: React.FC<TextInputProps> = ({ id, label, type = 'text', value, onChange }) => {
  return (
    <div className="mb-3">
      <label htmlFor={id} className="form-label">{label}</label>
      <input type={type} className="form-control" id={id} value={value} onChange={onChange} />
    </div>
  );
};

export default TextInput;
