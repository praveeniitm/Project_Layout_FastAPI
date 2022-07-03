# This is the file, from where service/application will start.



from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

from app.api.endpoints.api import api_router
import uvicorn


app = FastAPI(title = "Project name")

app.include_router(api_router)

if __name__ = '__main__':
  uvicorn.run(app,host = 0.0.0.0, port=8000)
