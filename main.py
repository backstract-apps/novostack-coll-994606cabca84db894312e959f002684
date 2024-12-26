from fastapi import FastAPI
from database import engine
import models
import uvicorn
from routes import router

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title='Backstract Generated APIs - novostack-coll-994606cabca84db894312e959f002684',debug=False,docs_url='/happy-chandrasekhar-e0b195c0c36c11efb4b70242ac12000399/docs',openapi_url='/happy-chandrasekhar-e0b195c0c36c11efb4b70242ac12000399/openapi.json')

app.include_router(router, prefix='/happy-chandrasekhar-e0b195c0c36c11efb4b70242ac12000399/api', tags=['APIs v1'])

def main():
    uvicorn.run('main:app', host='127.0.0.1', port=8008, reload=True)

if __name__ == '__main__':
    main()