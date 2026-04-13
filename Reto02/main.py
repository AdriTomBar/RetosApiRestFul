from fastapi import FastAPI
from pydantic import BaseModel

from futboldata import FutbolData

futbol = FutbolData()
app = FastAPI(
    title="FutbolApi",
    description="ApiRestFul para la gestión de futbol",
    version="0.0.1",
    contact={
        "name":"Adrian Tomas",
        "url":"http://www.mastermind.ac"
    },
    license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    }
)

class Partido(BaseModel):
    id : int
    anyio : int
    fase: str
    equipolocal: str
    goleslocales: int
    golesvisitante: int
    equipovisitante: str
    estaequipoanfitrion: int



@app.get("/partidos")
async def get_partidos(total: int = 10, skip: int = 0):
    return await futbol.get_partidos(skip,total)

@app.get("/todospartidos")
async def get_todospartidos():
    return await futbol.get_allIPartidos()

@app.get("/partidos/{partido_id}")
async def get_partido(partido_id: int):
    return await futbol.get_partido(partido_id)

@app.get("/partidosequipo/{equipo_id}")
async def get_partidoequipo(equipo_id: str):
    return await futbol.get_partidoequipo(equipo_id)

@app.post("/partidos")
async def get_partidoequipo(equipo_id: str):
    return await futbol.get_partidoequipo(equipo_id)

@app.post("/partidos")
async def write_partido(partido: Partido):
    return await futbol.write_partido(partido)

@app.put("/partidos/{partido_id}")
async def update_partido(partido_id: int, partido: Partido):
    return await futbol.update_partido(partido_id, partido)

@app.delete("/partidos/{partido_id}")
async def delete_partido(partido_id: int):
    return await futbol.delete_partido(partido_id)


