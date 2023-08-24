import React, { useState } from "react";
import axios from "axios";
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
      const response = await axios.post(
        "http://localhost:8000/api/v1/place-order/",
        formData
      );
      console.log(response.data);
    } catch (error) {
      console.error(error.response.data);
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
              <label>
                Full Name:
                <input
                  type="text"
                  name="full_name"
                  placeholder="Full Name"
                  value={formData.full_name}
                  onChange={handleInputChange}
                />
              </label>
              <label>
                Phone Number:
                <input
                  type="tel"
                  name="phone_number"
                  placeholder="Phone Number"
                  value={formData.phone_number}
                  onChange={handleInputChange}
                />{" "}
              </label>
              <div className="address-order-form">
                <label>
                  District:
                  <input
                    type="text"
                    name="district"
                    placeholder="District"
                    value={formData.district}
                    onChange={handleInputChange}
                  />
                </label>

                <label>
                  sector:
                  <input
                    type="text"
                    name="sector"
                    placeholder="Sector"
                    value={formData.sector}
                    onChange={handleInputChange}
                  />
                </label>
              </div>

              <label>
                Payment Method:
                <select
                  name="payment_method"
                  value={formData.payment_method}
                  onChange={handleInputChange}
                >
                  <option value="MTN">MTN</option>
                  <option value="Card">Card</option>
                  <option value="Airtel">Airtel</option>
                  <option value="Cash">Cash</option>
                </select>{" "}
              </label>
              <label>
                Message:
                <textarea
                  name="message"
                  placeholder="Message"
                  value={formData.message}
                  onChange={handleInputChange}
                />{" "}
              </label>
            </form>
          </div>

          <button type="submit">Place Order</button>
        </div>
        <div className="order-form-product-container">
          <h3>Order Summary</h3>
          <div className="order-details-summary"></div>
        </div>
      </div>
    </div>
  );
};

export default OrderForm;
