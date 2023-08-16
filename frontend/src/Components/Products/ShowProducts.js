import React, { useState, useEffect } from "react";
import axios from "axios";
import { Card, Button } from "react-bootstrap";
// import StarRatings from "react-star-rating";
import "./ProductList.css";

const ShowProducts = () => {
  const [products, setProducts] = useState([]);

  const fetchProducts = async () => {
    try {
      const response = await axios.get(
        "http://localhost:8000/api/v1/products/"
      );
      setProducts(response.data);
    } catch (error) {
      console.error("Error fetching products:", error);
    }
  };

  useEffect(() => {
    fetchProducts();
  }, []);

  return (
    <div className="product-list-container">
      {products.map((product) => (
        <Card key={product.id} className="product-card">
          <Card.Img
            variant="top"
            src={product.image}
            className="product-image"
          />
          <Card.Body>
            <Card.Title>{product.name}</Card.Title>
            <div className="product-details">
              <div className="rating">
                {/* <StarRatings
                  rating={4} // Replace with actual rating
                  starRatedColor="gold"
                  numberOfStars={5}
                  starDimension="20px"
                  starSpacing="2px"
                /> */}
              </div>
              <div className="creator">
                Created by: {product.creator}{" "}
                {/* Replace with actual creator */}
              </div>
            </div>
            <div className="price-add-to-cart">
              <Button variant="primary" className="add-to-cart">
                Add to Cart
              </Button>
              <div className="price">{product.price}FRW</div>
            </div>
          </Card.Body>
        </Card>
      ))}
    </div>
  );
};

export default ShowProducts;
