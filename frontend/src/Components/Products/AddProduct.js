import React, { useState, useEffect, useContext } from "react";
import { Form, Button } from "react-bootstrap";
import axios from "axios";
import AuthenticationContext from "../Users/Authentication"; // Import the authentication context

const AddProduct = () => {
  const { authTokens } = useContext(AuthenticationContext); // Get the authentication tokens from the context
  const [name, setName] = useState("");
  const [category, setCategory] = useState("");
  const [image, setImage] = useState(null);
  const [price, setPrice] = useState("");
  const [available, setAvailable] = useState(true);
  const [categories, setCategories] = useState([]);
  const [error, setError] = useState(null);
  const [description, setDescription] = useState("");

  useEffect(() => {
    fetchCategories();
  }, []);

  const fetchCategories = async () => {
    try {
      const response = await axios.get(
        "http://localhost:8000/api/v1/categories/",
        {
          headers: {
            Authorization: `Bearer ${authTokens.access}`,
          },
        }
      );
      setCategories(response.data);
    } catch (error) {
      console.error(error);
    }
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    const formData = new FormData();
    formData.append("name", name);
    formData.append("category", category);
    formData.append("description", description);
    if (image && image.length > 0) {
      formData.append("image", image[0]);
    }
    formData.append("price", price);
    formData.append("available", available);

    try {
      await axios.post("http://localhost:8000/api/v1/products/", formData, {
        headers: {
          "Content-Type": "multipart/form-data",
          Authorization: `Bearer ${authTokens.access}`,
        },
      });

      setName("");
      setCategory("");
      setImage(null);
      setPrice("");
      setAvailable(true);
      setDescription("");

      alert("Product created successfully!");
    } catch (error) {
      if (error.response) {
        setError(error.response.data.detail); // Set the error message from the server response
      } else {
        setError("An error occurred while creating the product."); // Set a generic error message
      }
    }
  };

  return (
    <div>
      <h1>Add Product</h1>
      {error && <div className="error-message">{error}</div>}
      <Form onSubmit={handleSubmit} enctype="multipart/form-data">
        <Form.Group controlId="name">
          <Form.Label>Name</Form.Label>
          <Form.Control
            type="text"
            value={name}
            onChange={(e) => setName(e.target.value)}
            required
          />
        </Form.Group>
        <Form.Group controlId="category">
          <Form.Label>Category</Form.Label>
          <Form.Control
            as="select"
            value={category}
            onChange={(e) => setCategory(e.target.value)}
            required
          >
            <option value="">Select a category</option>
            {/* Render the category options dynamically */}
            {categories.map((categoryOption) => (
              <option key={categoryOption.id} value={categoryOption.id}>
                {categoryOption.name}
              </option>
            ))}
          </Form.Control>
        </Form.Group>
        <Form.Group controlId="description">
          <Form.Label>Description</Form.Label>
          <Form.Control
            as="textarea"
            value={description}
            onChange={(e) => setDescription(e.target.value)}
          />
        </Form.Group>
        <Form.Group controlId="image">
          <Form.Label>Image</Form.Label>

          <Form.Control
            type="file"
            name="image"
            accept="image/jpeg, image/jpg, image/png"
            onChange={(e) => setImage(e.target.files)}
          />
        </Form.Group>
        <Form.Group controlId="price">
          <Form.Label>Price</Form.Label>
          <Form.Control
            type="number"
            value={price}
            onChange={(e) => setPrice(e.target.value)}
            required
          />
        </Form.Group>
        <Form.Group controlId="available">
          <Form.Check
            type="checkbox"
            label="Available"
            checked={available}
            onChange={(e) => setAvailable(e.target.checked)}
          />
        </Form.Group>
        <Button variant="primary" type="submit">
          Create Product
        </Button>
      </Form>
    </div>
  );
};

export default AddProduct;
