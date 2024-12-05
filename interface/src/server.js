const express = require('express');
const app = express();
app.get('/health', (req, res) => res.json({status: 'healthy'}));
app.listen(3000, () => console.log('Server running'));
