import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App.tsx'
import './index.css'
import { Analytics } from '@vercel/analytics/react';
ReactDOM.createRoot(document.getElementById('root')!).render(
  <html lang="en">
  <head>
    <title>Reddit College Results</title>
    <script src="https://cdn.amplitude.com/libs/analytics-browser-2.11.1-min.js.gz"></script><script src="https://cdn.amplitude.com/libs/plugin-session-replay-browser-1.8.0-min.js.gz"></script><script>window.amplitude.add(window.sessionReplay.plugin({sampleRate: 1}));window.amplitude.init('2d8142fdc59dc3cc2f81f3e1d37be13c', {"autocapture":{"elementInteractions":true}});</script>
  </head>
  <body>
  <React.StrictMode>
    <App />
  </React.StrictMode>
    <Analytics />
  </body>
</html>

)
