
# Vault-Terminal ☢️

Local AI chat interface styled as a Fallout Vault-Tec terminal. Runs completely offline using Ollama and streams responses in real-time with a retro teletype effect.

<img width="1919" height="953" alt="image" src="https://github.com/user-attachments/assets/c6bb5203-600b-42a0-893c-a98265ea88cf" />



### Features
- Real-time streaming responses (SSE)
- Retro Fallout-inspired design with glitch effects and scanlines
- Pure HTML/CSS/JS frontend – no heavy frameworks
- Persistent conversation history (in-memory)
- 100% local – no data leaves your server


### Quick Start
```bash
# Clone and enter
git clone https://github.com/zakefielfd/vault-terminal.git
cd vault-terminal

# Run (make sure Ollama is running with the model pulled)
ollama pull qwen2.5:7b
uvicorn main:app --host 0.0.0.0 --port 3000
