import React, { useState } from 'react';
import axios from "axios";
import { useNavigate } from 'react-router-dom'
import Cookies from 'js-cookie'
import './Login.css'

axios.defaults.xsrfCookieName = 'csrftoken';
axios.defaults.xsrfHeaderName = 'X-CSRFToken';
axios.defaults.withCredentials = true;

const client = axios.create({
    baseURL: process.env.REACT_APP_API_URL
});


function Login(props) {
    const navigate = useNavigate()
    const [error, setError] = useState(false)
    const [username, setUsername] = useState('')
    const [password, setPassword] = useState('')

    
    function handleLogin(e) {
        e.preventDefault();
        client.post(
        "/login",
        {
            username: username,
            password: password
        }
        ).then(function(res) {
            Cookies.set('userLoggedIn', true)
            navigate("/home")
            props.toggle(true)
        }).catch((error) => {
            setError(true)
        })
    }

    return (
        <div className="popup">
            <div className="popup-inner">
                <button className="buttonclose" onClick={props.toggle}>X</button>
                <form onSubmit={handleLogin}>
                    <label>
                        Username:
                        <input type="text" value={username} onChange={e => setUsername(e.target.value)} />
                    </label>
                    <label>
                        Password:
                        <input type="password" value={password} onChange={e => setPassword(e.target.value)} />
                    </label>
                    {error ? <div className='errmessage'>Sorry, user not registered! </div> : null}
                    <button type="submit">Login</button>
                </form>
            </div>
        </div>
    )
}

export default Login;