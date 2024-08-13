import "./style.css";

const mockName = "Garrett Hunt";
const mockUscfId = "30269749";

export const Header = () => {
  return (
    <div className="header">
      <h1>USCF Stats</h1>
      <h2>{mockName}</h2>
      <h2>USCF ID: {mockUscfId}</h2>
    </div>
  );
};
