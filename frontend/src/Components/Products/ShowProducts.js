import React, { useState, useEffect } from "react";
import axios from "axios";
import { Card } from "react-bootstrap";
import ReactStars from "react-rating-stars-component";
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

  const ProductStarRating = {
    size: 30,
    value: 4,
    edit: false,
  };

  useEffect(() => {
    fetchProducts();
  }, []);

  return (
    <div className="product-list-container">
      {products.map((product) => (
        <Card key={product.id} className="product-card">
          <a href={`/products/${product.id}`}>
            <Card.Img
              variant="top"
              src={product.image}
              className="display-product-image"
            />
          </a>
          <Card.Body>
            <Card.Title>{product.name}</Card.Title>
            <div className="product-details">
              <div className="rating">
                <p>(4.0)</p>
                <ReactStars {...ProductStarRating} />
              </div>
              <div className="creator">By {product.created_by}</div>
            </div>
            <div className="price-add-to-cart">
              <button className="add-to-cart-btn">Add to Cart</button>
              <div className="price">{product.price} FRW</div>
            </div>
          </Card.Body>
        </Card>
      ))}
    </div>
  );
};

export default ShowProducts;
