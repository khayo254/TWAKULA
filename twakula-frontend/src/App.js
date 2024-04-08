import React, { useState, useEffect } from 'react';
import axios from 'axios'; // Import Axios for making HTTP requests

function App() {
  const [data, setData] = useState(null);

  useEffect(() => {
    // Make a GET request to your Flask endpoint when the component mounts
    axios.get('/api/data')
      .then(response => {
        setData(response.data); // Set the response data to the state
      })
      .catch(error => {
        console.error('Error fetching data:', error);
      });
  }, []);

  return (
    <div>
      <h1>React App</h1>
      {data && (
        <div>
          <h2>Data from Flask:</h2>
          <p>{data}</p>
        </div>
      )}
    </div>
  );
}

export default App;
