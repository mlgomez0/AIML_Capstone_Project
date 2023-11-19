import React, { useState, useRef } from 'react';
import './Chat.css';
import { ChatInput } from './ChatInput';

const Chat = () => {

    const apiUrl = useRef('http://127.0.0.1:8000')
    const [ messages, setMessages ] = useState([]);

    const handleSendMessage = (message) => {

        setMessages(x => [ ...x, { user: 'you', text: message } ]);

        fetch(`${apiUrl.current}/predict?q=${encodeURIComponent(message)}`, { method: 'POST' })
            .then(response => response.json())
            .then(data => {
                setMessages(x => [ ...x, {
                    user: 'bot', text: data.text
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
