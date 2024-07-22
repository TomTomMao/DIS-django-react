import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App.tsx'
import '@fontsource/roboto/300.css';
import '@fontsource/roboto/400.css';
import '@fontsource/roboto/500.css';
import '@fontsource/roboto/700.css';
import { createBrowserRouter, createRoutesFromElements, Route, RouterProvider } from 'react-router-dom';
import People, { loader as peopleLoader } from './routes/people'
import Ownership, { action as ownershipAction } from './routes/ownership.tsx';
import Root from './routes/root.tsx';
import Vehicle, { loader as vehicleLoader } from './routes/vehicle.tsx';
import './index.css'
import ProtectedRoute from './components/ProtectedRoute.tsx';
import Login from './routes/login.tsx';
import Logout from './routes/logout.tsx';
import withAuth from './utils/withAuth.tsx';

const router = createBrowserRouter(
  createRoutesFromElements(
    <>
      <Route path='/logout' element={<Logout />} />
      <Route path='/login' element={<Login />} />
      <Route
        path='/'
        element={
          <ProtectedRoute>
            <Root />
          </ProtectedRoute>
        }
      >
        <Route
          path='/people'
          element={
            <ProtectedRoute>
              <People />
            </ProtectedRoute>
          }
          loader={withAuth(peopleLoader)}
        ></Route>
        <Route
          path='/vehicle'
          element={
            <ProtectedRoute>
              <Vehicle />
            </ProtectedRoute>
          }
          loader={withAuth(vehicleLoader)}
        ></Route>
        <Route
          path='/ownership'
          action={withAuth(ownershipAction)}
          element={
            <ProtectedRoute>
              <Ownership />
            </ProtectedRoute>
          }
        ></Route>
        {/* <Route path='/register' element={<RegisterAndLogout />} /> */}
      </Route>
    </>
  )
)

ReactDOM.createRoot(document.getElementById('root')!).render(
  <RouterProvider
    router={router}
  />,
)
