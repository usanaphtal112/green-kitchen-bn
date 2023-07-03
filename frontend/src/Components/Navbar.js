import { useRef } from "react";
import { FaBars, FaTimes, FaSearch } from "react-icons/fa";
import "../Styles/main.css";
import logoImage from "../images/Logo.png";

function Navbar() {
  const navRef = useRef();

  const showNavbar = () => {
    navRef.current.classList.toggle("responsive_nav");
  };

  return (
    <div>
      <header>
        <div className="logo-container">
          <img src={logoImage} alt="Logo" className="logo" />
          <form className="search-form">
            <div className="search-input">
              <input type="text" placeholder="Search" />
              <button type="submit">
                <FaSearch />
              </button>
            </div>
          </form>
        </div>
        <nav ref={navRef}>
          <a href="/#">Home</a>
          <a href="/#">Events</a>
          <a href="/#">Green School</a>
          <a href="/#">About Us</a>
          <a href="/#">Contact Us</a>
          <button className="nav-btn nav-close-btn" onClick={showNavbar}>
            <FaTimes />
          </button>
        </nav>
        <button className="nav-btn" onClick={showNavbar}>
          <FaBars />
        </button>
      </header>
    </div>
  );
}

export default Navbar;
