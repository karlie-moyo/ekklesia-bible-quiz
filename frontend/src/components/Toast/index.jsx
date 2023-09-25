import React from 'react';
import './styles.css';

export function Toast() {
  return (
    <>
      <div id="myToast" className="myToast"></div>
    </>
  );
}

export function showToast(message) {
  var toast = document.getElementById('myToast');
  toast.innerHTML = message;
  toast.classList.add('show');

  setTimeout(function () {
    toast.classList.remove('show');
  }, 5000);
}
