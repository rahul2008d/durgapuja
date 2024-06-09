import Dashboard from "./components/Dashboard";
// import NotFound from "./components/NotFound";

import {
  BrowserRouter as Router,
  Route,
  Routes,
  // Navigate,
} from "react-router-dom";

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/dashboard/:id" element={<Dashboard />} />
        {/* <Route path="*" element={<Navigate to="/DashboardWithoutId " />} /> */}
      </Routes>
    </Router>
  );
}

export default App;
