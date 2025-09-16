const express = require('express');
const app = express();
const port = 3000;

// Middleware untuk mem-parsing data JSON dari body request
app.use(express.json());

// Array untuk menyimpan data formulir, bertindak sebagai 'database' sederhana
const formDataStore = [];

// Endpoint untuk menerima data formulir (POST)
app.post('/api/submit-form', (req, res) => {
  const formData = req.body;
  // Memastikan data yang diterima tidak kosong
  if (formData) {
    formDataStore.push(formData);
    res.status(200).json({ message: 'Data formulir berhasil disimpan!', data: formData });
  } else {
    res.status(400).json({ message: 'Permintaan tidak valid. Data formulir kosong.' });
  }
});

// Endpoint untuk mengembalikan semua data yang telah disimpan (GET)
app.get('/api/get-data', (req, res) => {
  res.status(200).json({ data: formDataStore });
});

// Jalankan server
app.listen(port, () => {
  console.log(`Server berjalan di http://localhost:${port}`);
});