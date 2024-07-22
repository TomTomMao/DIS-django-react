// src/utils/withAuth.ts
import { LoaderFunctionArgs, redirect } from 'react-router-dom';
import { getAuthToken } from './auth'; // Your function to get auth token from storage
import { jwtDecode } from 'jwt-decode';

const withAuth = (loader: (args: LoaderFunctionArgs) => Promise<any>) => async (args: LoaderFunctionArgs) => {
    const token = getAuthToken();

    if (!token) {
        return redirect('/login');
    }

    const decoded = jwtDecode(token);
    if (decoded.exp < Date.now() / 1000) {
        return redirect('/login');
    }

    return loader(args);
};

export default withAuth;
