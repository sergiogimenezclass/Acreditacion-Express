# Ecosistema Digital de Acreditación Express 🚀

Proyecto para la Noche de los Oficios (CFP N°11 / CFP N°27)

Este repositorio contiene el código fuente de la plataforma web en tiempo real diseñada para capturar de manera ágil ($T \le 20\text{ segundos}$) los datos de contacto de potenciales estudiantes (leads) durante la feria Noche de los Oficios.

El sistema elimina cualquier tipo de fricción (sin logins ni contraseñas) y utiliza una arquitectura de comunicación bidireccional: cuando un visitante se registra desde su celular, la pantalla principal del stand reacciona saludándolo de manera pública e inmediata mediante WebSockets.

🛠️ Stack Tecnológico

Backend: Python (FastAPI o Flask-SocketIO)

Comunicación: WebSockets (Socket.IO o protocolo nativo)

Persistencia: SQLite / JSON Serializado

Frontend Móvil y Stand: HTML5, CSS3 (Tailwind CSS) y Vanilla JavaScript (ES6+)

📐 Arquitectura de Flujo

[ Celular del Visitante ] 
    │ 
    ▼ (Petición HTTP POST JSON)
[ API Servidor Python ] ─── (Escribe localmente) ───► [ Base de Datos ]
    │
    ▼ (Notificación de Evento WebSocket)
[ Pantalla Stand / Dashboard ] ───► Reacción visual instantánea


✨ Características Principales

UX Cero Fricción: Formulario de carga ultra-rápido optimizado para conexiones móviles débiles.

Filtrado Inteligente de Cursos: Los cursos se filtran dinámicamente según el CFP seleccionado por el usuario:

CFP N°11: Programación Web, Diseño Web, Diseño Gráfico, Marketing Digital.

CFP N°27: Programación, Programación con IA, Productividad con IA, Marketing Digital.

Pantalla Stand Reactiva: Un monitor en el stand escucha el servidor por WebSockets y muestra un saludo personalizado con confeti cada vez que alguien se registra.

Dashboard de Administración: Panel privado para monitorear métricas, visualizar inscriptos en tiempo real y exportar la base de datos completa a un archivo CSV para futuras campañas de marketing.

Tolerancia a Fallos (Modo Offline): Diseñado para funcionar en la nube o localmente (localhost) en una red local cerrada del stand si el internet del predio falla por completo.

🚀 Guía de Instalación y Uso (Desarrollo Local)

1. Clonar el repositorio

git clone https://github.com/sergiogimenezclass/Acreditacion-Express.git
cd Acreditacion-Express


2. Configurar el Entorno Virtual (Python)

# Crear entorno virtual
python -m venv venv

# Activar entorno virtual
# En Windows:
venv\Scripts\activate
# En macOS/Linux:
source venv/bin/activate


3. Instalar Dependencias

(Ejemplo para FastAPI)

pip install -r requirements.txt


4. Ejecutar el Servidor

uvicorn main:app --reload --host 0.0.0.0 --port 8080


El servidor estará disponible en la red local bajo la dirección IP de tu máquina (ej. http://192.168.1.150:8080).

📅 Plan de Trabajo para Alumnos (Hitos de Desarrollo)

Hito 1 (Base de Datos): Modelado de tablas y lógica de persistencia en SQLite usando Python.

Hito 2 (API Backend & WS): Configuración de endpoints HTTP POST y canales WebSocket.

Hito 3 (Maquetación UX): Diseño adaptativo de la app móvil (con JS para el filtrado dinámico) y la interfaz para el televisor.

Hito 4 (Dashboard & Exportación): Programación de la tabla de control del administrador y el generador CSV.

Hito 5 (Integración y Pruebas): Simulacro de carga concurrente y pruebas del plan de contingencia offline.
