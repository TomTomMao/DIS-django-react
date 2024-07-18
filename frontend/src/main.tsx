import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App.tsx'
import '@fontsource/roboto/300.css';
import '@fontsource/roboto/400.css';
import '@fontsource/roboto/500.css';
import '@fontsource/roboto/700.css';
import { BrowserRouter, createBrowserRouter, createRoutesFromElements, Route, RouterProvider, Routes } from 'react-router-dom';
import People, { loader as peopleLoader } from './routes/people'
import Ownership from './routes/ownership.tsx';
import Root from './routes/root.tsx';
import Vehicle, { loader as vehicleLoader } from './routes/vehicle.tsx';
import './index.css'

const router = createBrowserRouter(
  createRoutesFromElements(
    <Route
      path='/'
      element={
        <Root />
      }
    >
      <Route
        path='/people'
        element={
          <People />
        }
        loader={peopleLoader}
      ></Route>
      <Route
        path='/vehicle'
        element={
          <Vehicle />
        }
        loader={vehicleLoader}
      ></Route>
      <Route
        path='/ownership'
        element={
          <Ownership />
        }
      ></Route>
    </Route>
  )
)

ReactDOM.createRoot(document.getElementById('root')!).render(
  <RouterProvider
    router={router}
  />,
)
