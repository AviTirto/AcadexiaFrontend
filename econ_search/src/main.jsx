import React from 'react';
import ReactDOM from 'react-dom';
import './tailwind.css';
import App from './App';
import { Econ301Provider } from './contexts/Econ301Context';

createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <Econ301Provider>
      <App />
    </Econ301Provider>
  </React.StrictMode>,
)
