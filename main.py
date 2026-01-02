from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, StreamingResponse
from fastapi.templating import Jinja2Templates
import ollama
import markdown
import asyncio

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# Historial global simple (en producción usarías Redis o algo, pero para esto vale)
conversation = [
    {"role": "assistant", "content": "~ Vault-Tec Artificial Intelligence System v3.7 online ~\n\nBienvenido, Overseer. Todos los sistemas operativos.\n¿Qué directiva desea ejecutar hoy?"}
]

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.get_template("index.html").render({
        "request": request,
        "conversation": conversation
    })

async def stream_response(message: str):
    # Añadir mensaje usuario
    conversation.append({"role": "user", "content": message})
    
    # Streaming desde Ollama
    stream = ollama.chat(
        model='qwen2.5:7b',
        messages=conversation,
        stream=True
    )
    
    full_response = ""
    for chunk in stream:
        content = chunk['message']['content']
        full_response += content
        yield content
        await asyncio.sleep(0.01)  # Simula velocidad de teletipo
    
    # Guardar respuesta completa
    conversation.append({"role": "assistant", "content": full_response})

@app.post("/chat", response_class=StreamingResponse)
async def chat(message: str = Form(...)):
    return StreamingResponse(stream_response(message), media_type="text/event-stream")

if __name__ == "__main__":
    import uvicorn
    print("☢️  VAULT-TEC OPERATING SYSTEM v3.7 BOOTED ☢️")
    print("Terminal accesible en: http://localhost:3000")
    uvicorn.run(app, host="0.0.0.0", port=3000)
