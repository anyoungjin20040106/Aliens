from fastapi import FastAPI,Form
from tool import Explorer,Alien,AlienTable,ExplorerTable,ExplorerUpdate,AlienUpdate,KoreanCol

app=FastAPI()

@app.get("/explorers")
def index():
    explorer=ExplorerTable()
    df=explorer.select()
    result={'data':[]}
    for row in df.values:
        result['data'].append(dict(zip(df.columns,row)))
    return result

@app.get("/explorers/{explorer_id}")
def index(explorer_id:int):
    explorer=ExplorerTable()
    df=explorer.select(explorer_id)
    return dict(zip(df.columns,df.values[0] if bool(len(df)) else['']*len(df.columns)))

@app.get("/aliens")
def index():
    alien=AlienTable()
    df=alien.select()
    result={'data':[]}
    for row in df.values:
        result['data'].append(dict(zip(df.columns,row)))
    return result

@app.get("/aliens/{alien_id}")
def index(alien_id:int):
    alien=AlienTable()
    df=alien.select(alien_id)
    return dict(zip(df.columns,df.values[0] if bool(len(df)) else ['']*len(df.columns)))

@app.post("/aliens")
def insert(alien:Alien=Form(...)):
    table=AlienTable()
    return {"msg":table.insert(alien)}

@app.post("/explorers")
def insert(explorer:Explorer=Form(...)):
    table=ExplorerTable()
    return {"msg":table.insert(explorer)}

@app.put("/aliens/{alien_id}")
def update(alien_id: int,alien:AlienUpdate=Form(...)):
    table=AlienTable()
    table.update(str(alien_id),alien)
    return {"msg":table.insert(alien)}

@app.put("/explorers/{explorer_id}")
def update(explorer_id: int,explorer:ExplorerUpdate=Form(...)):
    table=ExplorerTable()
    table.update(str(explorer_id),explorer)
    return {"msg":table.insert(explorer)}

@app.delete("/aliens/{alien_id}")
def delete(alien_id: int):
    table=AlienTable()
    return {"msg":table.delete(alien_id)}

@app.delete("/explorers/{explorer_id}")
def delete(explorer_id: int):
    table=ExplorerTable()
    return {"msg":table.delete(explorer_id)}

@app.get("/filed")
def filed():
    pass