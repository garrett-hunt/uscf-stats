import "./style.css";

const mockTournamentResults = [
  // temporary until webscraper is connected to the frontend
  {
    id: "202408048532 ",
    endDate: "2024-08-04",
    name: "USCF Tournament4",
    hyperlink: "https://www.uschess.org/msa/XtblMain.php?000000000000",
    rating: "1819 => 1823",
  },
  {
    id: "202407219822",
    endDate: "2024-07-21",
    name: "USCF Tournament3",
    hyperlink: "https://www.uschess.org/msa/XtblMain.php?000000000000",
    rating: "1830 => 1819",
  },
  {
    id: "202407071132",
    endDate: "2024-07-07",
    name: "USCF Tournament2",
    hyperlink: "https://www.uschess.org/msa/XtblMain.php?000000000000",
    rating: "1820 => 1830",
  },
  {
    id: "202406233752",
    endDate: "2024-08-07",
    name: "USCF Tournament1",
    hyperlink: "https://www.uschess.org/msa/XtblMain.php?000000000000",
    rating: "1800 => 1820",
  },
];

export const TournamentResults = () => {
  return (
    <table>
      <tbody>
        <tr>
          <th>End Date</th>
          <th>Tournament Name</th>
          <th>Rating</th>
        </tr>
        {mockTournamentResults.map((tournament) => (
          <tr key={tournament.id}>
            <td>{tournament.endDate}</td>
            <td>
              <a href={tournament.hyperlink}>{tournament.name}</a>
            </td>
            <td>{tournament.rating}</td>
          </tr>
        ))}
      </tbody>
    </table>
  );
};
