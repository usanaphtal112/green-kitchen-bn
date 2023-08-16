import { useState, useEffect } from "react";
import "bootstrap/dist/css/bootstrap.min.css";
import "./FeaturedProducts.css";

function FeaturedProducts() {
  const [featuredProducts, setFeaturedProducts] = useState([]);

  useEffect(() => {
    async function fetchFeaturedProducts() {
      try {
        const response = await fetch("http://127.0.0.1:8000/api/v1/products/");
        const data = await response.json();

        // Assuming your API returns an array of products
        const featuredProductsData = data.slice(0, 4); // Select the first 4 products as featured

        setFeaturedProducts(featuredProductsData);
      } catch (error) {
        console.error("Error fetching data:", error);
      }
    }

    fetchFeaturedProducts();
  }, []);

  return (
    <div className="top-categories">
      {/* <h2 className="top-categories-title">Top Categories</h2> */}
      <h2 className="mb-4">Featured Categories</h2>
      <div className="featured-products container">
        <div className="row">
          {featuredProducts.map((product) => (
            <div key={product.id} className="col-md-3 mb-3">
              <div className="featured-product">
                <img src={product.image} alt={product.name} />
              </div>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}

export default FeaturedProducts;
