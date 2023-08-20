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
