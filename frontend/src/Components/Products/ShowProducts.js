import axios from "axios";
import React, { useState, useEffect } from "react";
import { Card, Button, Row, Col } from "react-bootstrap";
import "./product_main.css";

const ShowProducts = () => {
  const [products, setProducts] = useState([]);

  const getProducts = async () => {
    const response = await axios.get("http://localhost:8000/api/v1/products/");
    setProducts(response.data);
  };

  useEffect(() => {
    getProducts();
  }, []);

  const chunkArray = (array, chunkSize) => {
    const chunkedArray = [];
    for (let i = 0; i < array.length; i += chunkSize) {
      const chunk = array.slice(i, i + chunkSize);
      chunkedArray.push(chunk);
    }
    return chunkedArray;
  };

  const chunkedProducts = chunkArray(products, 4);

  return (
    <div className="product-card-info">
      {chunkedProducts.map((chunk, index) => (
        <Row key={index} className="image-row">
          {chunk.map((product, innerIndex) => (
            <Col key={innerIndex} xs={12} md={6} lg={3} className="image-col">
              <Card className="m-2 rounded shadow-lg" style={{ width: "100%" }}>
                <Card.Img
                  variant="top"
                  src={product.image}
                  className="product-image"
                />
                <Card.Body>
                  <Card.Title>{product.name}</Card.Title>
                  <Card.Text>{product.price}</Card.Text>
                  <Button variant="primary">Show Details</Button>
                </Card.Body>
              </Card>
            </Col>
          ))}
          {/* Add empty columns to create spacing */}
          {chunk.length < 4 &&
            Array.from({ length: 4 - chunk.length }, (_, i) => (
              <Col
                key={chunk.length + i}
                xs={12}
                md={6}
                lg={3}
                className="empty-col"
              />
            ))}
        </Row>
      ))}
    </div>
  );
};

export default ShowProducts;
