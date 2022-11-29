from fastapi import FastAPI, status, Response, UploadFile
import databases
import db
import validate
from typing import Union

app = FastAPI()
database = databases.Database('sqlite+aiosqlite:///bills.db')

@app.on_event('startup')
async def startup():
    await database.connect()

@app.on_event('shutdown')
async def shutdown():
    await database.disconnect()

@app.post('/upload/', status_code=status.HTTP_201_CREATED)
async def upload_bills(file: UploadFile, response: Response):
    try:
        csv_lines = str(await file.read(), 'utf-8').split('\n')[1:] # splitting by newline and skipping header
        parsed_csv = await validate.validate_csv(csv_lines)

        queries = tuple(map(db.bills.insert().values, parsed_csv))
        for query in queries:
            await database.execute(query)

        return { 'filename': file.filename }
    except Exception as e:
        response.status_code = status.HTTP_400_BAD_REQUEST

@app.get('/get_bills', status_code=status.HTTP_200_OK)
async def get_bills(org: Union[str, None] = None, name: Union[str, None] = None):
    query = db.bills.select()

    if (org is not None):
        query = query.where(db.bills.c.client_org == org)

    if (name is not None):
        query = query.where(db.bills.c.client_name == name)

    r = await database.fetch_all(query)

    return { 'data': r }
