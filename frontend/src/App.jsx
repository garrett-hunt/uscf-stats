import { createRoot } from "react-dom/client";
import { Header } from "./Components/Header/Header";
import { TournamentResults } from "./Components/TournamentResults/TournamentResults";
import { ResultsSelection } from "./Components/ResultsSelection/ResultsSelection";
import "./style.css";

function App() {
  return (
    <>
      <Header />
      <ResultsSelection />
      <TournamentResults />
    </>
  );
}

export default App;

const container = document.getElementById("root");
const root = createRoot(container);
root.render(<App />);
