import { useRef, useState } from 'react';
import logo from './logo.svg';
import './App.css';

function App() {

  const [ question, setQuestion ] = useState('');
  const apiUrl = useRef('http://127.0.0.1:8000')

  /**
   * Send the question to the backend and display the response in an alert
   */
  const onClick = () => {

    fetch(`${apiUrl.current}/predict?q=${encodeURIComponent(question)}`, { method: 'POST' })
      .then(response => response.json())
      .then(data => alert(data.text))
      .catch(err => console.log(err));

  }

  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Hello World VTL!
        </p>
        <input
          type="text"
          placeholder="Enter your question"
          className="btn"
          value={question}
          onChange={(e) => setQuestion(e.target.value)}
        />
        <input
          type="button"
          value="Send"
          onClick={onClick}
        />
      </header>
    </div>
  );
}

export default App;
