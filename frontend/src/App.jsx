import { createRoot } from "react-dom/client";
import "./style.css";

function App() {
  return <h1>Hello World</h1>;
}

export default App;

const container = document.getElementById("root");
const root = createRoot(container);
root.render(<App />);
