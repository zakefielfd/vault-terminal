const express = require('express');
const { Ollama } = require('ollama');
const path = require('path');

const app = express();
const ollama = new Ollama({ host: 'http://localhost:11434' });

app.use(express.static('public'));
app.use(express.json());

app.post('/chat', async (req, res) => {
  const { messages } = req.body;
  try {
    const response = await ollama.chat({
      model: 'qwen2.5:7b',
      messages: messages,
      stream: false
    });
    res.json({ content: response.message.content });
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname, 'public', 'index.html'));
});

app.listen(3000, () => {
  console.log('Vault-Tec Chat Terminal activo en http://localhost:3000');
  console.log('Abre en tu navegador (o forwardea por SSH si es remoto)');
});
