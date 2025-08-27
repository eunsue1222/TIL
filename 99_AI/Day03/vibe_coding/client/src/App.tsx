import { Outlet } from 'react-router-dom';
import Navbar from './components/Navbar/Navbar';
import './styles/index.scss';

function App() {
  return (
    <>
      <Navbar />
      <main>
        <Outlet />
      </main>
    </>
  );
}

export default App;