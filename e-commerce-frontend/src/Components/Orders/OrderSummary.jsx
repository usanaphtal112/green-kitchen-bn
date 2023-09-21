// OrderSummary.js
import React from "react";
import PropTypes from "prop-types";

function OrderSummary({ cartItems, totalPrice }) {
  return (
    <div className="cart-container">
      <div className="cart-items">
        <ul className="list-group">
          {cartItems.map((item) => (
            <li key={item.product.id} className="list-group-item">
              <div className="row">
                <div className="col-3">
                  <img
                    src={item.product.image}
                    alt={item.product.name}
                    className="img-fluid"
                  />
                </div>
                <div className="col-9">
                  <h5 className="mb-1">{item.product.name}</h5>
                  <p className="mb-1">Seller: {item.product.created_by}</p>
                  <p className="mb-1">Price: {item.product.price} FRW</p>
                  <p className="mb-1">Quantity: {item.quantity}</p>
                </div>
              </div>
            </li>
          ))}
        </ul>
      </div>
      <div className="cart-summary">
        <h2 className="section-title">Order Summary</h2>
        <div className="summary-details">
          <p className="detail-row">
            <span className="detail-name">Total Price:</span>
            <span className="detail-value">{totalPrice} FRW</span>
          </p>
        </div>
      </div>
    </div>
  );
}

OrderSummary.propTypes = {
  cartItems: PropTypes.array.isRequired,
  totalPrice: PropTypes.number.isRequired,
};

export default OrderSummary;
