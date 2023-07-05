import React, { useState, useEffect } from "react";
import { Form, Button } from "react-bootstrap";
import axios from "axios";

const AddProduct = () => {
  const [name, setName] = useState("");
  const [category, setCategory] = useState("");
  const [image, setImage] = useState(null);
  const [price, setPrice] = useState("");
  const [available, setAvailable] = useState(true);
  const [categories, setCategories] = useState([]);

  useEffect(() => {
    fetchCategories();
  }, []);

  const fetchCategories = async () => {
    try {
      const response = await axios.get(
        "http://localhost:8000/api/v1/products/"
      );
      setCategories(response.data);
    } catch (error) {
      console.error(error);
    }
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    // Create form data to send the image file
    const formData = new FormData();
    formData.append("name", name);
    formData.append("category", category);
    formData.append("image", image);
    formData.append("price", price);
    formData.append("available", available);

    try {
      await axios.post("http://localhost:8000/api/v1/products/", formData, {
        headers: {
          "Content-Type": "multipart/form-data",
        },
      });

      // Clear form fields after successful submission
      setName("");
      setCategory("");
      setImage(null);
      setPrice("");
      setAvailable(true);

      // Optionally show a success message to the user
      alert("Product created successfully!");
    } catch (error) {
      // Handle error, show error message, etc.
      console.error(error);
    }
  };

  return (
    <div>
      <h1>Add Product</h1>
      <Form onSubmit={handleSubmit}>
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
            {categories.map((category) => (
              <option key={category.id} value={category.id}>
                {category.name}
              </option>
            ))}
          </Form.Control>
        </Form.Group>
        <Form.Group controlId="image">
          <Form.Label>Image</Form.Label>
          <Form.Control
            type="file"
            accept="image/jpeg, image/jpg, image/png"
            onChange={(e) => setImage(e.target.files[0])}
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
