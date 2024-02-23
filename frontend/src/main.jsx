import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App.jsx'
import './index.css'
import { createBrowserRouter, RouterProvider } from "react-router-dom";
import LoginSignup from "./components/LoginSignup/LoginSignup.jsx";
import ProfilePage from "./components/pages/ProfilePage.jsx";
import ProfilesPage from "./components/pages/ProfilesPage.jsx";
import NotFoundPage from "./components/pages/NotFoundPage.jsx";

const router = createBrowserRouter([
  {
    path: "/",
    element: <App></App>,
    errorElement: <NotFoundPage></NotFoundPage>,
  },
  {
    path: "/auth",
    element: <LoginSignup></LoginSignup>,
    errorElement: <NotFoundPage></NotFoundPage>,
  },
  {
    path: "/profiles",
    element: <ProfilesPage></ProfilesPage>,
    errorElement: <NotFoundPage></NotFoundPage>,
    children: [
      {
        path: "/profiles/:profileID", // Dynamic Routing
        element: <ProfilePage></ProfilePage>,
        errorElement: <NotFoundPage></NotFoundPage>,
      },
    ],
  },
]);
ReactDOM.createRoot(document.getElementById("root")).render(
  <React.StrictMode>
    <RouterProvider router={router}></RouterProvider>
  </React.StrictMode>
);
