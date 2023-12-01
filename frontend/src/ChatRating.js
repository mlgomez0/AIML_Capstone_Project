import React, { useState, useEffect } from 'react';
import axios from "axios";
import './ChatRating.css'
import { styled } from '@mui/material/styles';
import Box from '@mui/material/Box';
import Rating from '@mui/material/Rating';
import FavoriteIcon from '@mui/icons-material/Favorite';
import FavoriteBorderIcon from '@mui/icons-material/FavoriteBorder';
import Typography from '@mui/material/Typography';
import Cookies from 'js-cookie'

const StyledRating = styled(Rating)({
    '& .MuiRating-iconFilled': {
        color: '#ff6d75',
    },
    '& .MuiRating-iconHover': {
        color: '#ff3d47',
    },
});


function ChatRating(props) {
    const [ rating, setRating ] = useState(2)

    function handleRating(value, newValue) {
        setRating(newValue)
    }

    function handleSaveRating(e) {
        e.preventDefault();
        axios.defaults.xsrfCookieName = 'csrftoken';
        axios.defaults.xsrfHeaderName = 'X-CSRFToken';
        axios.defaults.withCredentials = true;
        axios.defaults.headers.post[ 'Authorization' ] = 'Token ' + Cookies.get('token');

        const client = axios.create({
            baseURL: process.env.REACT_APP_API_URL,
        });
        client.post(
            "/rating",
            {
                rating: rating,
            },
        ).then(function (res) {
            props.toggle()
        }).catch((error) => {
            console.log(error)
        })
    }

    useEffect(() => {
        const client = axios.create({
            baseURL: process.env.REACT_APP_API_URL,
        });
        const fetchChatRating = async () => {
            try {
                const response = await client.get("/rating");
                const chatRating = JSON.parse(response.data.rating)
                setRating(chatRating)
            } catch (error) {
                console.error('Error fetching data:', error);
            }
        };
        fetchChatRating();
    }, []);

    return (
        <div className="popup">
            <div className="popup-inner">
                <button className="buttonclose" onClick={props.toggle}>X</button>
                <Box
                    sx={{
                        '& > legend': { mt: 2 },
                    }}
                >
                    <Typography component="legend">Rate your experience with VTL!</Typography>
                    <StyledRating
                        name="customized-color"
                        value={rating}
                        onChange={handleRating}
                        getLabelText={(value) => `${value} Heart${value !== 1 ? 's' : ''}`}
                        precision={0.5}
                        icon={<FavoriteIcon fontSize="inherit" />}
                        emptyIcon={<FavoriteBorderIcon fontSize="inherit" />}
                    />
                </Box>
                <button className="savebutton" onClick={handleSaveRating}>Save</button>
            </div>
        </div>
    )
}

export default ChatRating;