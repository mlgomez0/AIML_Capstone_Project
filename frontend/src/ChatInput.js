import React, { useState } from 'react';
import './Chat.css';

export const ChatInput = ({ onSendMessage }) => {

    const [ input, setInput ] = useState('');

    const handleSubmit = (e) => {
        e.preventDefault();
        if (!input.trim())
            return;
        onSendMessage(input);
        setInput('');
    };

    return (
        <div className="chat-input">
            <input
                type="text"
                value={input}
                onChange={(e) => setInput(e.target.value)}
                placeholder="Write a message..."
            />
            <button type="button" onClick={handleSubmit}>Send</button>
        </div>
    );
};
