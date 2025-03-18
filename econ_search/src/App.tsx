import { useState } from 'react'
import './App.css'
import Router from './components/pages/Router'

function App() {
  const [count, setCount] = useState(0)

  return (
    <div className="bg-slate-950 min-h-screen text-[#cae9ff]">
      <Router/>
    </div>
  )
}

export default App
