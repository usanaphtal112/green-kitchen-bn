import React from "react";
import "../Styles/main.css";
import { FaTwitter, FaInstagram, FaFacebook } from "react-icons/fa";

const Footer = () => {
  return (
    <footer className="footer">
      <div className="footer-lists">
        <div className="footer-list">
          <div className="footer-logo">
            <img src="/images/Logo.png" alt="Logo" className="logo-in-footer" />
            <div className="footer-text-container">
              <p className="footer-text">
                Our platform connects you directly with local farmers. By
                purchasing fresh produce from our farmers.
              </p>
            </div>
          </div>
        </div>
        <div className="footer-list">
          <h3>Support</h3>
          <ul>
            <li>
              <a href="/#">Help Center</a>
            </li>
            <li>
              <a href="/#">Safety Information</a>
            </li>
            <li>
              <a href="/#">Report Complaint</a>
            </li>
          </ul>
        </div>
        <div className="footer-list">
          <h3>Quick links</h3>
          <ul>
            <li>
              <a href="/#">About Us</a>
            </li>
            <li>
              <a href="/#">Contact</a>
            </li>
            <li>
              <a href={`/login/`}>Login</a>
            </li>
          </ul>
        </div>

        <div className="footer-list">
          <h3>community</h3>
          <ul>
            <li>
              <a href="/#">Customer Review</a>
            </li>
            <li>
              <a href="/#">Training</a>
            </li>
          </ul>
        </div>
      </div>
      <hr className="footer-line" />
      <div className="footer-bottom">
        <div className="footer-copyright">
          &copy; 2023 Green Kitchen. All rights reserved.
        </div>
        <div className="footer-social">
          <a href="/#">
            <FaTwitter size={24} />
          </a>
          <a href="/#">
            <FaInstagram size={24} />
          </a>
          <a href="/#">
            <FaFacebook size={24} />
          </a>
        </div>
      </div>
    </footer>
  );
};

export default Footer;
