import React, { useState } from "react";
import { Form, Button, Container } from "react-bootstrap";
import axios from "axios";

const UserSignup = () => {
  const [state, setState] = useState({
    first_name: "",
    last_name: "",
    email: "",
    phone_number: "",
    password: "",
  });

  const onChange = (e) => {
    setState({ ...state, [e.target.name]: e.target.value });
  };

  const handleSubmit = (event) => {
    event.preventDefault();

    axios
      .post("http://localhost:8000/api/v1/users/signup/", {
        email: state.email, // Change username to email
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
      });
  };

  return (
    <Container style={{ marginTop: "100px" }}>
      <Form>
        <Form.Group controlId="formBasicFirstName" style={{ width: "300px" }}>
          <Form.Label>First name</Form.Label>
          <Form.Control
            type="text"
            placeholder="Enter First Name"
            name="first_name"
            value={state.first_name}
            onChange={onChange}
          />
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
        </Form.Group>
        <Button variant="primary" type="submit" onClick={handleSubmit}>
          Sign Up
        </Button>
      </Form>
    </Container>
  );
};

export default UserSignup;
