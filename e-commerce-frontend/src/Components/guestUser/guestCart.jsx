import React, { useState, useEffect } from "react";
import { Link } from "react-router-dom";
import {
  fetchCartItems,
  changeQuantity,
  removeFromCart,
} from "../Utility/productUtilities";
import "./guestCart.css";

function GuestCart() {
  const [cartItems, setCartItems] = useState([]);
  const [totalPrice, setTotalPrice] = useState(0);
  const [error, setError] = useState(null);

  useEffect(() => {
    loadCartItems();
  }, []);

  const loadCartItems = async () => {
    try {
      const data = await fetchCartItems();
      setCartItems(data.cart_items);
      setTotalPrice(data.total_price);
    } catch (error) {
      setError("Error fetching cart items.");
    }
  };

  const handleChangeQuantity = async (product_id, newQuantity) => {
    try {
      if (newQuantity === 0) {
        // If the new quantity is zero, remove the item from the cart
        const success = await removeFromCart(product_id);

        if (success) {
          loadCartItems();
        } else {
          setError("Error removing product from cart.");
        }
      } else {
        // If the new quantity is not zero, update the quantity
        const success = await changeQuantity(product_id, newQuantity);

        if (success) {
          loadCartItems();
        } else {
          setError("Error changing product quantity.");
        }
      }
    } catch (error) {
      setError("Error changing product quantity.");
    }
  };

  const handleRemoveFromCart = async (product_id) => {
    try {
      const success = await removeFromCart(product_id);
      if (success) {
        loadCartItems();
      } else {
        setError("Error removing product from cart.");
      }
    } catch (error) {
      setError("Error removing product from cart.");
    }
  };

  return (
    <div className="cart-container">
      {error && <p>{error}</p>}
      {cartItems.length === 0 ? (
        <div className="cart-items">
          <p className="product-absence-message">No Product found in Cart</p>
        </div>
      ) : (
        <div className="cart-items">
          <ul>
            {cartItems.map((item) => (
              <li key={item.product.id} className="cart-item">
                <div className="item-left">
                  <a href={`/products/${item.product.id}/`}>
                    <img src={item.product.image} alt={item.product.name} />
                  </a>
                  <div className="item-details">
                    <p className="product-name">{item.product.name}</p>
                    <p className="seller-name">
                      Seller: {item.product.created_by}
                    </p>
                    <p className="item-price">{item.product.price} FRW</p>
                    <div className="quantity-buttons">
                      <button
                        className="styled-button"
                        onClick={() =>
                          handleChangeQuantity(
                            item.product.id,
                            item.quantity + 1
                          )
                        }
                      >
                        +
                      </button>
                      <span className="quantity-display">{item.quantity}</span>
                      <button
                        className="styled-button"
                        onClick={() =>
                          handleChangeQuantity(
                            item.product.id,
                            item.quantity - 1
                          )
                        }
                      >
                        -
                      </button>
                      <div className="btn-remove">
                        <button
                          className="styled-button remove-button"
                          onClick={() => handleRemoveFromCart(item.product.id)}
                        >
                          Remove
                        </button>
                      </div>
                    </div>
                  </div>
                </div>
              </li>
            ))}
          </ul>
        </div>
      )}
      <div className="cart-summary">
        <h2 className="section-title">Price Summary</h2>

        <div className="summary-details">
          <p className="detail-row">
            <span className="detail-name">
              Price ({cartItems.length} items):
            </span>
            <span className="detail-value">{totalPrice} FRW</span>
          </p>
          <p className="detail-row">
            <span className="detail-name">Discount:</span>
            <span className="detail-value">0.00%</span>
          </p>
          <p className="detail-row">
            <span className="detail-name">Delivery Fees:</span>
            <span className="detail-value">0.00FRW</span>
          </p>
          <hr />
          <p className="detail-row bold-total">
            <span className="detail-name">Total Price:</span>
            <span className="detail-value">{totalPrice} FRW</span>
          </p>
          <hr />
        </div>
        <Link to="/place-order">
          <button className="cart-buy-button">BUY NOW</button>
        </Link>
      </div>
    </div>
  );
}

export default GuestCart;
