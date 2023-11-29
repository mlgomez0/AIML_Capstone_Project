import React, { useState, useEffect } from 'react';
import './Chat.css';
import { ChatInput } from './ChatInput';
import axios from "axios";
import Cookies from 'js-cookie'

axios.defaults.xsrfCookieName = 'csrftoken';
axios.defaults.xsrfHeaderName = 'X-CSRFToken';
axios.defaults.withCredentials = true;
axios.defaults.withXSRFToken = true;


const Chat = () => {
    const client = axios.create({
        baseURL: process.env.REACT_APP_API_URL
    });
    const [ messages, setMessages ] = useState([]);

    useEffect(() => {
        const fetchChatHistory = async () => {
          try {
            const response = await client.get("/history");
            const chatHistory = JSON.parse(response.data.chat)
            setMessages(chatHistory)
          } catch (error) {
            console.error('Error fetching data:', error);
          }
        };
        fetchChatHistory();
    }, []);

    useEffect(()=>{
        if (messages.length != 0) {
            client.post(
                "/history",
                {
                    chat: JSON.stringify(messages)
                })
                .then(data => {
                    console.log(data.status)
                })
                .catch(err => console.log(err));
            }
    }, [messages])

    const handleSendMessage = (message) => {

        setMessages(x => [ ...x, { user: 'you', text: message } ]);
        client.post(
            "/chat",
            {
                q: message
            })
            .then(data => {
                setMessages(x => [ ...x, {
                    user: 'bot', text: data.data.chat.text
                } ]);
            })
            .catch(err => console.log(err));
    };


    return (
        <div className="chat-container">
            <div className="chat-window">
                {messages.map((msg, index) => (
                    <div key={index} className={`message ${msg.user}`}>
                        {msg.text}
                    </div>
                ))}
            </div>
            <ChatInput onSendMessage={handleSendMessage} />
        </div>
    );
};


export default Chat;
