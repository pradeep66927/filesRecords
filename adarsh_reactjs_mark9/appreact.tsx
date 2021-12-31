mport React from "react";
import "./styles.css";
import { useState } from "react"
const movieDB = {
  sci_fiction: [
    { name: "Robot2.0", rating: "4/5" },
    { name: "Love story 2050", rating: "3.5/5" }
  ],

  Action: [
    {
      name: "baghi 3",
      rating: "3.5/5"
    },
    {
      name: "sanak",
      rating: "4.5/5"
    }
  ],
  Romantic: [
    {
      name: "Dil bechara",
      rating: "5/5"
    },
    {
      name: "zero",
      rating: "5/5"
    }
  ]
};
export default function App() {
  const [selectedGenre, setGenre] = useState("Romantic");
  function genreClickHandler(genre) {
    setGenre(genre);
  }
  return (
    <div className="App">
      <h1> 📽️ Hitsmovies 📽️ </h1>
      <p style={{ fontSize: "smaller" }}>
        {" "}
        Checkout my favorite movie. Select a genre to get started{" "}
      </p>

      <div>
        {Object.keys(movieDB).map((genre) => (
          <button
            onClick={() => genreClickHandler(genre)}
            style={{
              cursor: "pointer",
              background: "#E5E7EB",
              borderRadius: "0.5rem",
              padding: "0.5rem  1rem",
              border: "1px solid black",
              margin: "1rem 0.3rem"
            }}
          >
            {genre}
          </button>
        ))}
      </div>
      <hr />
      <div style={{ textAlign: "left" }}>
        <ul style={{ paddingInlineStart: "0" }}>
          {movieDB[selectedGenre].map((movie) => (
            <li
              key={movie.name}
              style={{
                listStyle: "none",
                padding: "1rem",
                border: "1px solid #D1D5DB",
                width: "70%",
                margin: "1rem 0rem",
                borderRadius: "0.5rem"
              }}
            >
              {" "}
              <div style={{ fontSize: "larger" }}> {movie.name} </div>
              <div style={{ fontSize: "smaller" }}> {movie.rating} </div>
            </li>
          ))}
        </ul>
      </div>
    </div>
  );
}