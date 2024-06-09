// import React, { useEffect } from "react";
// import axios from "axios";
import { useParams } from "react-router-dom";
import "./Dashboard.css";

function Dashboard() {
  const { id } = useParams();

  return (
    <div>
      <Header id={id} />
      <Main />
      <Footer />
    </div>
  );
}

function Header({ id }) {
  return (
    <div>
      <div className="logo">
        <img src={"logo0192.png"} alt="Logo" />
      </div>
      <div className="welcome-message">
        Welcome user, <span>{id}</span>
      </div>
      <div className="profile-pic">
        <img src="https://picsum.photos/200/300" alt="Profile Pic" />
      </div>
      <div className="logout-btn">
        <button>Logout</button>
      </div>
    </div>
  );
}

function Main() {
  return (
    <section className="cards">
      <div className="card">
        <h2>Card 1</h2>
        <ul>
          <li>Data 1</li>
        </ul>
      </div>
      <div className="card">
        <h2>Card 2</h2>
        <ul>
          <li>Data 1</li>
        </ul>
      </div>
      <div className="card">
        <h2>Card 3</h2>
        <ul>
          <li>Data 1</li>
        </ul>
      </div>
    </section>
  );
}

function Footer() {
  return (
    <footer>
      <p>&copy; 2024</p>
    </footer>
  );
}
export default Dashboard;
