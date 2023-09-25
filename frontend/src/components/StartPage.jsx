import React, { useState } from 'react';
import { showToast } from './Toast';
import api from '../api';

export default function StartPage() {
  const [name, setName] = useState('');
  const [email, setEmail] = useState('');

  if (localStorage.getItem('email')) {
    window.location = '/questions';
  }

  const handleSubmit = () => {
    if (name === '' || email === '') {
      showToast('Name or Email cannot be blank!');
      return;
    } else {
      api
        .post('/users', { name, email })
        .then((response) => {
          if ([200, 201].includes(response.status)) {
            showToast('Loading Quiz Page...');
          }

          localStorage.setItem('email', email);
          window.location = '/questions';
        })
        .catch((error) => {
          showToast(error);
        });
    }
  };

  return (
    <div className="row g-2">
      <h2 className="display-5">Enter Name and Email</h2>
      <div className="col-md">
        <div className="form-floating mb-3">
          <input
            type="text"
            className="form-control"
            id="floatingInput"
            placeholder="John Doe"
            value={name}
            onChange={(e) => setName(e.target.value)}
          />
          <label htmlFor="floatingInput">Full Name</label>
        </div>
      </div>
      <div className="col-md">
        <div className="form-floating">
          <input
            type="email"
            className="form-control"
            id="floatingEmail"
            placeholder="Password"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
          />
          <label htmlFor="floatingEmail">Email</label>
        </div>
      </div>
      <input
        type="submit"
        value="Fetch Questions"
        className="btn btn-lg btn-primary mt-4 mt-md-1"
        onClick={handleSubmit}
      />
    </div>
  );
}
