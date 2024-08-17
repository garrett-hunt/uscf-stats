import "./style.css";
import { useState, useEffect } from "react";

export const Header = () => {
  const [id, setId] = useState("");
  const [name, setName] = useState("");
  const [classical, setClassical] = useState("");
  const [quick, setQuick] = useState("");
  const [blitz, setBlitz] = useState("");
  const [onlineClassical, setOnlineClassical] = useState("");
  const [onlineQuick, setonlineQuick] = useState("");
  const [onlineBlitz, setOnlineBlitz] = useState("");

  useEffect(() => {
    fetch("/api/name")
      .then((res) => res.json())
      .then((data) => setName(data.name))
      .catch((err) => console.error("Error fetching name:", err));
  }, []);

  useEffect(() => {
    fetch("/api/id")
      .then((res) => res.json())
      .then((id) => setId(id))
      .catch((err) => console.error("Error fetching id:", err));
  }, []);

  const tournamentResultsURL =
    "https://www.uschess.org/msa/MbrDtlTnmtHst.php?" + `${id}`;

  return (
    <div className="header">
      <h1>USCF Stats</h1>
      <h2>{name}</h2>
      <h2>
        USCF ID: <a href={tournamentResultsURL}>{id}</a>
      </h2>
    </div>
  );
};
