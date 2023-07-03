import React from "react";
import Navbar from "./Components/Navbar";
import Footer from "./Components/footer";
import Home from "./Components/home";

function App() {
  return (
    <div className="app-container">
      <Navbar />
      <React.Fragment>
        <div className="navbar-shadow"></div>
      </React.Fragment>

      <React.Fragment>
        <Home />
      </React.Fragment>
      <React.Fragment>
        <Footer />
      </React.Fragment>
    </div>
  );
}

export default App;
