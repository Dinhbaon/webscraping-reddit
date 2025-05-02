import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App.tsx'
import './index.css'
import { Analytics } from '@vercel/analytics/react';
ReactDOM.createRoot(document.getElementById('root')!).render(
  <html lang="en">
  <head>
    <title>Reddit College Results</title>
  </head>
  <body>
  <React.StrictMode>
    <App />
  </React.StrictMode>
    <Analytics />
  </body>
</html>

)
