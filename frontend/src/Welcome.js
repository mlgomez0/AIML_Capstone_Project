import React, { useState } from 'react';
import logo from './logo_welcome.png'
import './Welcome.css'
import background from "./background.png"
import Cookies from 'js-cookie'
import { useNavigate } from 'react-router-dom'

function Welcome() {
  const navigate = useNavigate()
  const [error, setError] = useState(false)
  const loggedIn = Cookies.get('userLoggedIn')

  function handleClick () {
    if (loggedIn){
      navigate("/home")
    } else {
      setError(true)
    }
  }


  return (
    <div className="Welcome" style={{ backgroundImage: `url(${background})`, backgroundRepeat: 'no-repeat', backgroundSize: 'cover' }}>
      <header className="Welcome-header">
        <p>
          Hello! I am VTL
        </p>
        <img src={logo} className="Welcome-logo" alt="logo" />
        {
          error ? <p>Please, Login</p> :
          <button className="Welcome-button" onClick={handleClick}>Start</button>
        }
      </header>
    </div>
  );
}

export default Welcome;
