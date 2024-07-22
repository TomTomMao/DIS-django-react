import React, { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { Button, Box, Typography } from '@mui/material';
import { ACCESS_TOKEN, REFRESH_TOKEN } from '../utils/constants';

const Logout = () => {
    const navigate = useNavigate();
    const [loggedOut, setLoggedOut] = useState(false)
    useEffect(() => {
        const handleLogout = () => {
            // Clear authentication tokens
            localStorage.removeItem(ACCESS_TOKEN);
            localStorage.removeItem(REFRESH_TOKEN);
        };
        setTimeout(() => {
            setLoggedOut(true)
        }, 1000);
        handleLogout();

    }, []);

    return (
        <Box
            display="flex"
            flexDirection="column"
            alignItems="center"
            justifyContent="center"
            height="100vh"
            sx={{ p: 2 }}
        >
            <Typography variant="h4" gutterBottom id='logging out'>
                {loggedOut ? 'Logged out' : 'Logging out...'}
            </Typography>
            {loggedOut &&
                <Button
                    variant="contained"
                    color="primary"
                    onClick={() => navigate('/login')}
                >
                    Go to Login
                </Button>
            }
        </Box>
    );
};

export default Logout;