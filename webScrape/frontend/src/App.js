import React, { useState } from 'react';

function App() {
    const [url, setUrl] = useState('');
    const [books, setBooks] = useState([]);

    const fetchBooks = async () => {
        const response = await fetch('http://localhost:5000/scrape', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ url }),
        });
        const data = await response.json();
        setBooks(data.books || []);
    };

    return (
        <div>
            <h1>Web Scraper</h1>
            <input
                type="text"
                placeholder="Enter URL"
                value={url}
                onChange={(e) => setUrl(e.target.value)}
            />
            <button onClick={fetchBooks}>Scrape</button>
            <ul>
                {books.map((book, index) => (
                    <li key={index}>{book}</li>
                ))}
            </ul>
        </div>
    );
}

export default App;
