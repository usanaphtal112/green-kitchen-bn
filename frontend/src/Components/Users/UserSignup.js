import React, { useState } from "react";
import { Form, Button, Container } from "react-bootstrap";
import axios from "axios";
import "./user.css";

const UserSignup = () => {
  const [state, setState] = useState({
    first_name: "",
    last_name: "",
    email: "",
    phone_number: "",
    password: "",
  });
  const [errors, setErrors] = useState({});

  const onChange = (e) => {
    setState({ ...state, [e.target.name]: e.target.value });
  };

  const handleSubmit = (event) => {
    event.preventDefault();

    // Perform form validation
    const formErrors = {};
    if (!state.first_name) {
      formErrors.first_name = "First name is required.";
    }
    if (!state.last_name) {
      formErrors.last_name = "Last name is required.";
    }
    if (!state.email) {
      formErrors.email = "Email is required.";
    } else if (!isValidEmail(state.email)) {
      formErrors.email = "Invalid email address.";
    }
    if (!state.phone_number) {
      formErrors.phone_number = "Phone number is required.";
    } else if (!isValidPhoneNumber(state.phone_number)) {
      formErrors.phone_number = "Invalid phone number.";
    }
    if (!state.password) {
      formErrors.password = "Password is required.";
    }

    // Update the errors state
    setErrors(formErrors);

    // If there are any form errors, stop form submission
    if (Object.keys(formErrors).length > 0) {
      return;
    }

    axios
      .post("http://localhost:8000/api/v1/users/signup/", {
        email: state.email,
        password: state.password,
        phone_number: state.phone_number,
        first_name: state.first_name,
        last_name: state.last_name,
      })
      .then(function (res) {
        console.log(res);
        // Redirect to the login page
        window.location.href = "/login";
      })
      .catch(function (err) {
        console.log(err);
        if (err.response && err.response.data) {
          // If there are backend errors, update the errors state with the response data
          setErrors(err.response.data);
        }
      });
  };

  const isValidEmail = (email) => {
    // Use a regular expression to validate the email format
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailRegex.test(email);
  };

  const isValidPhoneNumber = (phone) => {
    // Use a regular expression to validate the phone number format
    const phoneRegex = /^0\d{9}$/;
    return phoneRegex.test(phone);
  };

  return (
    <Container style={{ marginTop: "10px" }}>
      <Form>
        <Form.Group controlId="formBasicFirstName" style={{ width: "300px" }}>
          <Form.Label>First name</Form.Label>
          <Form.Control
            type="text"
            placeholder="EnterFirst name"
            name="first_name"
            value={state.first_name}
            onChange={onChange}
          />
          {errors.first_name && (
            <Form.Text className="text-danger">{errors.first_name}</Form.Text>
          )}
        </Form.Group>
        <Form.Group controlId="formBasicLastName" style={{ width: "300px" }}>
          <Form.Label>Last Name</Form.Label>
          <Form.Control
            type="text"
            placeholder="Enter Last Name"
            name="last_name"
            value={state.last_name}
            onChange={onChange}
          />
          {errors.last_name && (
            <Form.Text className="text-danger">{errors.last_name}</Form.Text>
          )}
        </Form.Group>
        <Form.Group controlId="formBasicEmail" style={{ width: "300px" }}>
          <Form.Label>Email address</Form.Label>
          <Form.Control
            type="text"
            placeholder="Enter email"
            name="email"
            value={state.email}
            onChange={onChange}
          />
          {errors.email && (
            <Form.Text className="text-danger">{errors.email}</Form.Text>
          )}
        </Form.Group>

        <Form.Group controlId="formBasicPhoneNumber" style={{ width: "300px" }}>
          <Form.Label>Phone Number</Form.Label>
          <Form.Control
            type="text"
            placeholder="Enter phone number"
            name="phone_number"
            value={state.phone_number}
            onChange={onChange}
          />
          {errors.phone_number && (
            <Form.Text className="text-danger">{errors.phone_number}</Form.Text>
          )}
        </Form.Group>

        <Form.Group controlId="formBasicPassword" style={{ width: "300px" }}>
          <Form.Label>Password</Form.Label>
          <Form.Control
            type="password"
            placeholder="Password"
            name="password"
            value={state.password}
            onChange={onChange}
          />
          {errors.password && (
            <Form.Text className="text-danger">{errors.password}</Form.Text>
          )}
        </Form.Group>
        <Button
          variant="primary"
          type="submit"
          className="form-submit-button"
          onClick={handleSubmit}
        >
          Sign Up
        </Button>
      </Form>
    </Container>
  );
};

export default UserSignup;
