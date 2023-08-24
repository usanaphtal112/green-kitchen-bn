import React, { useState, useEffect } from "react";
import axios from "axios";
import { Card } from "react-bootstrap";
import { useNavigate } from "react-router-dom";
import ReactStars from "react-rating-stars-component";
import { addToCart, fetchReviewsForProduct } from "../Utility/productUtilities";
import "./ProductList.css";

const ShowProducts = () => {
  const [products, setProducts] = useState([]);
  const navigate = useNavigate();

  const fetchProductsAndReviews = async () => {
    try {
      const productsResponse = await axios.get(
        "http://localhost:8000/api/v1/products/"
      );
      const productsWithReviews = await Promise.all(
        productsResponse.data.map(async (product) => {
          const reviewsResponse = await fetchReviewsForProduct(product.id);
          const averageRating = calculateAverageRating(reviewsResponse);
          return { ...product, averageRating };
        })
      );
      setProducts(productsWithReviews);
    } catch (error) {
      console.error("Error fetching products:", error);
    }
  };

  const calculateAverageRating = (reviews) => {
    if (!Array.isArray(reviews) || reviews.length === 0) {
      return 3;
    }

    const totalReviews = reviews.reduce(
      (sum, review) => sum + review.reviews,
      0
    );
    return totalReviews / reviews.length;
  };

  useEffect(() => {
    fetchProductsAndReviews();
  }, []);

  const handleAddToCart = (product) => {
    addToCart(product, navigate);
  };

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
                <p>({product.averageRating.toFixed(1)})</p>
                <ReactStars
                  size={30}
                  value={product.averageRating}
                  edit={false}
                />
              </div>
              <div className="creator">By {product.created_by}</div>
            </div>
            <div className="price-add-to-cart">
              <button
                className="add-to-cart-btn"
                onClick={() => handleAddToCart(product)}
              >
                Add to Cart
              </button>
              <div className="price">{product.price} FRW</div>
            </div>
          </Card.Body>
        </Card>
      ))}
    </div>
  );
};

export default ShowProducts;
