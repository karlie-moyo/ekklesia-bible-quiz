import React from 'react';
import './BackgroundImage.css';

const BackgroundImage = ({ imageUrl }) => {
  const backgroundStyle = {
    backgroundImage: `url(${imageUrl})`,
  };

  return <div className="background-image" style={backgroundStyle}></div>;
};

export default BackgroundImage;
