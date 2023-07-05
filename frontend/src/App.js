import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Navbar from "./Components/Navbar";
import Footer from "./Components/footer";
import Home from "./Components/home";
import ShowProducts from "./Components/Products/ShowProducts";
import AddProduct from "./Components/Products/AddProduct";

function App() {
  return (
    <div className="app-container">
      <Router>
        <Navbar />
        <Routes>
          <Route path="/product-list" element={<ShowProducts />} />
          <Route path="/addProduct" element={<AddProduct />} />
          <Route path="/" element={<Home />} />
        </Routes>
        <Footer />
      </Router>
    </div>
  );
}

export default App;
