import axios from "axios";

export const addToCart = async (product, navigate) => {
  try {
    console.log("Adding product to cart:", product.id);
    const response = await axios.post(
      `http://localhost:8000/api/v1/guest_cart/${product.id}/`,
      {
        quantity: 1,
      },
      {
        headers: {
          "Content-Type": "application/json",
        },
      }
    );

    if (response.status === 201) {
      navigate("/guest-cart");
    } else {
      throw new Error("Failed to add item to cart.");
    }
  } catch (error) {
    console.error("Error:", error);
  }
};

export const fetchReviewsForProduct = async (productId) => {
  try {
    const response = await axios.get(
      `http://localhost:8000/api/v1/review/${productId}/`
    );
    return response.data;
  } catch (error) {
    console.error("Error fetching reviews:", error);
    return [];
  }
};

export const submitOrder = async (formData) => {
  try {
    const response = await axios.post(
      "http://localhost:8000/api/v1/place-order/",
      formData
    );
    return response.data;
  } catch (error) {
    throw error.response.data;
  }
};

export const fetchCartItems = async () => {
  try {
    const response = await axios.get(
      "http://localhost:8000/api/v1/guest_cart/"
    );
    return response.data;
  } catch (error) {
    throw error.response.data;
  }
};

export const changeQuantity = async (product_id, quantity) => {
  try {
    const response = await axios.patch(
      `http://localhost:8000/api/v1/guest_cart/${product_id}/`,
      { quantity },
      {
        headers: {
          "Content-Type": "application/json",
        },
      }
    );

    if (response.status === 200) {
      return true;
    } else {
      throw new Error("Error changing product quantity.");
    }
  } catch (error) {
    throw error.response.data;
  }
};

export const removeFromCart = async (product_id) => {
  try {
    const response = await axios.delete(
      `http://localhost:8000/api/v1/guest_cart/${product_id}/`,
      {
        data: { quantity: 0 },
      }
    );

    if (response.status === 204) {
      return true;
    } else {
      throw new Error("Error removing product from cart.");
    }
  } catch (error) {
    throw error.response.data;
  }
};
