import logo from './logo_welcome.png'
import './Welcome.css'
import background from "./background.png"
import { useNavigate } from 'react-router-dom';

function Welcome() {

  const navigate = useNavigate()
  /**
   * Direct to the home page
   */
  const onClick = () => {
    navigate("/home")

  }

  return (
    <div className="Welcome" style={{ backgroundImage: `url(${background})`, backgroundRepeat: 'no-repeat', backgroundSize: 'cover' }}>
      <header className="Welcome-header">
        <p>
          Hello! I am VTL
        </p>
        <img src={logo} className="Welcome-logo" alt="logo" />
        <button className="Welcome-button" onClick={onClick}>Start</button>
      </header>
    </div>
  );
}

export default Welcome;
