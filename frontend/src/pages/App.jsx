import Dashboard from "./pages/Dashboard";
import Books from "./pages/Books";
import Borrowers from "./pages/Borrowers";
import Transactions from "./pages/Transactions";
import Search from "./pages/Search";

function App() {
  return (
    <div>
      <Dashboard />
      <Books />
      <Borrowers />
      <Transactions />
      <Search />
    </div>
  );
}

export default App;