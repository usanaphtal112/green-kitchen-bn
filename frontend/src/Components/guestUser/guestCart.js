import React, { useState, useEffect } from "react";
import axios from "axios";

function GuestCart() {
  const [cartItems, setCartItems] = useState([]);
  const [totalPrice, setTotalPrice] = useState(0);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetchCartItems();
  }, []);

  const fetchCartItems = async () => {
    try {
      const response = await axios.get(
        "http://localhost:8000/api/v1/guest_cart/"
      );
      // const response = await axios.get(
      //   "http://127.0.0.1:8000/api/v1/guest_cart/"
      // );
      console.log(response.data.cart_items);
      setCartItems(response.data.cart_items);
      setTotalPrice(response.data.total_price);
    } catch (error) {
      setError("Error fetching cart items.");
    }
  };

  const handleChangeQuantity = async (product_id, quantity) => {
    try {
      const response = await fetch(`http://localhost:8000/api/v1/guest_cart/`, {
        method: "PATCH",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          product_id,
          quantity,
        }),
      });

      if (response.ok) {
        fetchCartItems(); // Refresh cart items after changing quantity
      } else {
        setError("Error changing product quantity.");
      }
    } catch (error) {
      setError("Error changing product quantity.");
    }
  };

  const handleRemoveFromCart = async (product_id) => {
    try {
      await axios.delete("http://localhost:8000/api/v1/guest_cart/", {
        data: {
          product_id,
          quantity: 0, // Set a dummy quantity of 0, or any value that indicates removal
        },
      });
      fetchCartItems(); // Refresh cart items after removing
    } catch (error) {
      setError("Error removing product from cart.");
    }
  };

  return (
    <div>
      <h2>Cart Items</h2>
      {error && <p>{error}</p>}
      {cartItems.length === 0 ? (
        <p>No Product in Cart</p>
      ) : (
        <ul>
          {cartItems.map((item) => (
            <li key={item.product.id}>
              Product Name: {item.product.name}, Quantity: {item.quantity}
              <button
                onClick={() =>
                  handleChangeQuantity(item.product_id, item.quantity + 1)
                }
              >
                +
              </button>
              <button
                onClick={() =>
                  handleChangeQuantity(item.product_id, item.quantity - 1)
                }
              >
                -
              </button>
              <button onClick={() => handleRemoveFromCart(item.product_id)}>
                Remove
              </button>
            </li>
          ))}
        </ul>
      )}
      <p>Total Price: {totalPrice}</p>
    </div>
  );
}

export default GuestCart;
