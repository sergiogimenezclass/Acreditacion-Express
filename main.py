from fastapi import FastAPI, WebSocket, WebSocketDisconnect, Request, Form
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from sqlalchemy import create_all_metadata, create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import datetime
import json

# --- CONFIGURACIÓN DE BASE DE DATOS ---
SQLALCHEMY_DATABASE_URL = "sqlite:///./leads.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class Lead(Base):
    __tablename__ = "leads"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String)
    email = Column(String)
    telefono = Column(String)
    cfp = Column(String)
    curso = Column(String)
    fecha = Column(DateTime, default=datetime.datetime.utcnow)

Base.metadata.create_all(bind=engine)

# --- LÓGICA DE WEBSOCKETS ---
class ConnectionManager:
    def __init__(self):
        self.active_connections: list[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def broadcast(self, message: str):
        for connection in self.active_connections:
            await connection.send_text(message)

manager = ConnectionManager()

# --- APP FASTAPI ---
app = FastAPI(title="Acreditación Express")

# Servir archivos estáticos (HTML, JS, CSS)
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def read_index():
    with open("static/index.html", "r", encoding="utf-8") as f:
        return f.read()

@app.post("/registro")
async def registro(
    nombre: str = Form(...),
    email: str = Form(...),
    telefono: str = Form(""),
    cfp: str = Form(...),
    curso: str = Form(...)
):
    db = SessionLocal()
    nuevo_lead = Lead(nombre=nombre, email=email, telefono=telefono, cfp=cfp, curso=curso)
    db.add(nuevo_lead)
    db.commit()
    db.refresh(nuevo_lead)
    db.close()

    # Notificar por WebSocket a la pantalla del stand
    mensaje = json.dumps({
        "tipo": "NUEVO_REGISTRO",
        "nombre": nombre,
        "curso": curso
    })
    await manager.broadcast(mensaje)
    
    return {"status": "ok", "message": f"¡Gracias {nombre}! Te registraste correctamente."}

@app.get("/api/leads")
async def listar_leads():
    db = SessionLocal()
    leads = db.query(Lead).order_by(Lead.fecha.desc()).all()
    db.close()
    return leads

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await manager.connect(websocket)
    try:
        while True:
            await websocket.receive_text() # Mantener conexión viva
    except WebSocketDisconnect:
        manager.disconnect(websocket)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
