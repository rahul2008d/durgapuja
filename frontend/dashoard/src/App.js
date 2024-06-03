import { useEffect , useState } from 'react';

function App() {

  const [ data, setData ] = useState({})
    useEffect(()=>{
      fetchData();
    }, []);

  const fetchData = async ()=>{
    try {
      const response = await fetch('http://127.0.0.1:5000/members')
      const jsonData = await response.json()
      setData(jsonData)
    } catch (error) {
      console.log('error', error)
    }
  }


  return (
    <div className="App">
      <h1>frontend</h1>
      <h3>data</h3>
    </div>
  );
}

export default App;
