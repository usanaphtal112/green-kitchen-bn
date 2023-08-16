import React, { useEffect, useState } from "react";
import { useParams, useNavigate } from "react-router-dom";

const ProductDetails = () => {
  const { id } = useParams();
  const [product, setProduct] = useState(null);
  const navigate = useNavigate();

  useEffect(() => {
    const fetchProductDetails = async () => {
      try {
        const response = await fetch(
          `http://localhost:8000/api/v1/products/${id}/`
        );
        if (response.ok) {
          const data = await response.json();
          setProduct(data);
        } else {
          throw new Error("Failed to fetch product details.");
        }
      } catch (error) {
        console.error("Error:", error);
      }
    };

    fetchProductDetails();
  }, [id]);

  if (!product) {
    return <div>Loading...</div>;
  }

  const addToCart = async () => {
    try {
      console.log("Adding product to cart:", product.id);
      const response = await fetch("http://localhost:8000/api/v1/guest_cart/", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          product_id: product.id,
          // quantity: 1,
        }),
      });

      if (response.ok) {
        navigate("/guest-cart"); // Navigate to the cart page
      } else {
        throw new Error("Failed to add item to cart.");
      }
    } catch (error) {
      console.error("Error:", error);
    }
  };

  return (
    <div>
      <h2>Product Details</h2>
      <img
        src={product.image}
        alt="Product"
        style={{ width: "200px", height: "200px" }}
      />
      <p>Name: {product.name}</p>
      <p>Description: {product.description}</p>
      <p>Price: {product.price}</p>
      <p>Available: {product.available ? "Yes" : "No"}</p>
      <button onClick={addToCart}>Add to Cart</button>
    </div>
  );
};

export default ProductDetails;
