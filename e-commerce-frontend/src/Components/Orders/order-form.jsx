import React, { useState, useEffect } from "react";
import { Button } from "react-bootstrap";
import OrderSummary from "./OrderSummary";
import { submitOrder, fetchCartItems } from "../Utility/productUtilities";
import "./OrderForm.css";

const OrderForm = () => {
  const [formData, setFormData] = useState({
    full_name: "",
    phone_number: "",
    district: "",
    sector: "",
    address: "",
    payment_method: "MTN",
    message: "",
  });

  const [cartItems, setCartItems] = useState([]);
  const [totalPrice, setTotalPrice] = useState(0);

  const buttonStyles = {
    backgroundColor: "green",
    color: "white",
    border: "none",
    borderRadius: "5px",
    padding: "10px 20px",
    cursor: "pointer",
    display: "block",
    margin: "0 auto",
  };

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setFormData((prevData) => ({
      ...prevData,
      [name]: value,
    }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      const response = await submitOrder(formData);
      console.log(response);
    } catch (error) {
      console.error(error.response.data);
    }
  };

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

  return (
    <div>
      <div className="order-form-heading">
        <h2>Confirm and Pay</h2>
      </div>

      <div className="place-order-form-container">
        <div className="order-detail-form-container">
          <div className="order-form-input">
            <h2>DELIVERY ADDRESS</h2>
            <p>08:00 a.m to 8:00pm</p>
            <form onSubmit={handleSubmit}>
              <div className="order-form-input-group">
                <label>Full Name:</label>
                <br />
                <input
                  type="text"
                  name="full_name"
                  placeholder="Full Name"
                  value={formData.full_name}
                  onChange={handleInputChange}
                />
              </div>
              <div className="order-form-input-group">
                <label htmlFor="phonenumber">Phone Number:</label>
                <br />
                <input
                  type="tel"
                  name="phone_number"
                  placeholder="Phone Number"
                  value={formData.phone_number}
                  onChange={handleInputChange}
                />{" "}
              </div>
              <div className="address-order-form">
                <div className="order-form-input-group">
                  <label> District:</label>
                  <br />

                  <input
                    type="text"
                    name="district"
                    placeholder="District"
                    value={formData.district}
                    onChange={handleInputChange}
                  />
                </div>
                <div className="order-form-input-group">
                  <label>Sector:</label>
                  <br />
                  <input
                    type="text"
                    name="sector"
                    placeholder="Sector"
                    value={formData.sector}
                    onChange={handleInputChange}
                  />
                </div>
              </div>
              <div className="order-form-input-group">
                <label>Payment Method:</label>
                <br />
                <select
                  name="payment_method"
                  value={formData.payment_method}
                  onChange={handleInputChange}
                  className="order-custom-input"
                >
                  <option value="MTN">MTN</option>
                  <option value="Card">Card</option>
                  <option value="Airtel">Airtel</option>
                  <option value="Cash">Cash</option>
                </select>{" "}
              </div>
              <div className="order-form-input-group">
                <label>Message:</label> <br />
                <textarea
                  name="message"
                  placeholder="Message"
                  value={formData.message}
                  onChange={handleInputChange}
                />{" "}
              </div>
            </form>
          </div>

          <Button
            type="submit"
            style={buttonStyles}
            className="place-order-button"
          >
            Place Order
          </Button>
        </div>
        <div className="order-form-product-container">
          <h3>Order Summary</h3>
          <div className="order-details-summary">
            {/* Use the OrderSummary component here */}
            <OrderSummary cartItems={cartItems} totalPrice={totalPrice} />
          </div>
        </div>
      </div>
    </div>
  );
};

export default OrderForm;
