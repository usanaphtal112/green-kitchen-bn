import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Navbar from "./Components/Navbar";
import Footer from "./Components/footer";
import Home from "./Components/home";
import ShowProducts from "./Components/Products/ShowProducts";
import AddProduct from "./Components/Products/AddProduct";
import ProductDetails from "./Components/Products/ProductDetails";

import GuestCart from "./Components/guestUser/guestCart";

import UserSignup from "./Components/Users/UserSignup";
import UserLogin from "./Components/Users/UserLogin";
import UserLogout from "./Components/Users/UserLogout";
import { AuthProvider } from "./Components/Users/Authentication";

function App() {
  return (
    <div className="app-container">
      <Router>
        <AuthProvider>
          <Navbar />
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/product-list" element={<ShowProducts />} />
            <Route path="/products/:id" element={<ProductDetails />} />
            <Route path="/guest-cart" element={<GuestCart />} />
            <Route path="/addProduct" element={<AddProduct />} />
            <Route path="/signup" element={<UserSignup />} />
            <Route path="/login" element={<UserLogin />} />
            <Route path="/logout" element={<UserLogout />} />
          </Routes>
          <Footer />
        </AuthProvider>
      </Router>
    </div>
  );
}

export default App;
