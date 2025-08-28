import React from 'react';

interface CheckboxProps {
  id: string;
  label: string;
  checked: boolean;
  onChange: (e: React.ChangeEvent<HTMLInputElement>) => void;
}

const Checkbox: React.FC<CheckboxProps> = ({ id, label, checked, onChange }) => {
  return (
    <div className="form-check mb-3">
      <input type="checkbox" className="form-check-input" id={id} checked={checked} onChange={onChange} />
      <label className="form-check-label" htmlFor={id}>{label}</label>
    </div>
  );
};

export default Checkbox;
