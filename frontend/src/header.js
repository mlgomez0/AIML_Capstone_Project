import axios from "axios";
import Cookies from 'js-cookie';
import React, { useState } from "react";
import { useNavigate } from 'react-router-dom';
import Login from './LogIn';
import './header.css';

axios.defaults.xsrfCookieName = 'csrftoken';
axios.defaults.xsrfHeaderName = 'X-CSRFToken';
axios.defaults.withCredentials = true;
axios.defaults.headers.post[ 'Authorization' ] = 'Token ' + Cookies.get('token');

const client = axios.create({
    baseURL: process.env.REACT_APP_API_URL
});


function Header() {
    const navigate = useNavigate()
    const [ seen, setSeen ] = useState(false)
    const [ loggedIn, setLoggedIn ] = useState(Cookies.get('userLoggedIn') === 'true')

    function togglePop(success_login = false) {
        if (success_login === true) {
            setLoggedIn(true)
        }
        setSeen(!seen)
    }


    function handleLogout(e) {
        e.preventDefault();
        client.post(
            "/logout",
        ).then(function (res) {
            Cookies.remove('userLoggedIn')
            setLoggedIn(false)
            navigate("/")
        }).catch((error) => {
            console.log("There was an error")
        })
    }
    return (
        <>
            <header className="headervtl">
                <nav className="navi-bar">
                    {/* <NavLink exact activeClassName="active" to="/home">
                        Home
                    </NavLink> */}
                    {/* <NavLink activeClassName="active" to="/">
                        Welcome
                    </NavLink> */}
                </nav>
                <div className="loginout">
                    {loggedIn ? <button
                        className="logoin-button"
                        onClick={handleLogout}>
                        Logout
                    </button> : <button
                        className="logout-button"
                        onClick={togglePop}>
                        Login
                    </button>}
                </div>
                {seen ? <Login toggle={togglePop} /> : null}
            </header>
        </>
    );
}
export default Header;