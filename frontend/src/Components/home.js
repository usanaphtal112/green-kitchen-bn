import React from "react";
import "../Styles/main.css";
import homeImages from "../images/personal_veg.png";
import homevegetableImages from "../images/veg_1.png";
import homepersonalvegImage from "../images/personal_vegetar.png";
function HomePage() {
  const productImages = [
    "image1.jpg",
    "image2.jpg",
    "image3.jpg",
    "image4.jpg",
  ];

  const productsList = [
    { name: "Product 1", price: "$10.99", image: "product1.jpg" },
    { name: "Product 2", price: "$8.99", image: "product2.jpg" },
    { name: "Product 3", price: "$12.99", image: "product3.jpg" },
    { name: "Product 4", price: "$9.99", image: "product4.jpg" },
    { name: "Product 1", price: "$10.99", image: "product1.jpg" },
    { name: "Product 2", price: "$8.99", image: "product2.jpg" },
    { name: "Product 3", price: "$12.99", image: "product3.jpg" },
    { name: "Product 4", price: "$9.99", image: "product4.jpg" },
    { name: "Product 1", price: "$10.99", image: "product1.jpg" },
    { name: "Product 2", price: "$8.99", image: "product2.jpg" },
    { name: "Product 3", price: "$12.99", image: "product3.jpg" },
    { name: "Product 4", price: "$9.99", image: "product4.jpg" },
  ];
  return (
    <div className="main-container">
      <div className="box-container">
        <div className="box-content">
          <h2 className="box-title">
            Make a healthy life with fresh vegetables
          </h2>
          <p className="box-text">
            Our platform connects you directly with local farmers. By purchasing
            fresh produce from our farmers.
          </p>
          <div className="box-link">
            <a href="/#" className="box-link-btn">
              Shop Now
            </a>
          </div>
        </div>
        <div className="box-photo">
          <img src={homeImages} alt="Carrot" />
        </div>
      </div>
      <div className="top-categories">
        <h2 className="top-categories-title">Top Categories</h2>
        <div className="category-boxes">
          {productImages.map((image, index) => (
            <div className="category-box" key={index}>
              <img src={image} alt="Product" className="product-image" />
            </div>
          ))}
        </div>
      </div>

      <div className="featured-container">
        <h2 className="section-title">Featured Vegetables</h2>
        <p className="section-sentence">
          Checkout our fresh and seasonal vegetables from our local farmers.
        </p>
        <div className="product-grid">
          {productsList.map((product, index) => (
            <div className="product-item" key={index}>
              <img src={product.image} alt="Product" />
              <h3 className="product-name">{product.name}</h3>
              <p className="product-price">{product.price}</p>
            </div>
          ))}
        </div>
      </div>

      <div className="box-container">
        <div className="box-content">
          <h2 className="box-title">Order Vegetables online and stay safe</h2>
          <p className="box-text">
            Our platform connects you directly with local farmers. By purchasing
            fresh produce from our farmers.
          </p>
          <div className="box-link">
            <a href="/#" className="box-link-btn">
              Order Now
            </a>
          </div>
        </div>
        <div className="box-photo">
          <img src={homevegetableImages} alt="Carrot" />
        </div>
      </div>

      <div className="third-featured-container">
        <div className="left-section">
          <img src={homepersonalvegImage} alt="personal-veg" />
        </div>
        <div className="right-section">
          <h2 className="section-title">Why should you use our service</h2>
          <p className="section-text">
            Our platform connects you directly with local farmers. By purchasing
            fresh produce from our farmers. You're supporting local agriculture.
          </p>
          <ul className="section-list">
            <li className="list-item">Fast and reliable derivery</li>
            <li className="list-item">No additional fees for Orders</li>
            <li className="list-item">We provide the fastest service</li>
          </ul>
        </div>
      </div>
    </div>
  );
}

export default HomePage;
