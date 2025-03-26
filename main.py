from fastapi import FastAPI, Form,APIRouter
from tool import Explorer, Alien, AlienTable, ExplorerTable, ExplorerUpdate, AlienUpdate, KoreanCol

# FastAPI 인스턴스 생성 (여기가 서버의 시작점!)
app = FastAPI(title="Starfleet Data Management System",
              description="이 시스템은 **탐험가와 외계인의 정보를 효율적으로 관리하기 위한 API**입니다."
              )
explorers_router = APIRouter(prefix="/explorers", tags=["explorers"])
aliens_router = APIRouter(prefix="/aliens", tags=["aliens"])
# =====================[ 탐험가 관련 API ]=====================

# ▶ 모든 탐험가 정보 가져오기 (GET /explorers)
@explorers_router.get("/")
def index():
    explorer = ExplorerTable()
    df = explorer.select()
    result = {'data': []}
    for row in df.values:
        result['data'].append(dict(zip(df.columns, row)))
    return result

# ▶ 특정 탐험가 정보 가져오기 (GET /explorers/{explorer_id})
@explorers_router.get("/{explorer_id}")
def index(explorer_id: int):
    explorer = ExplorerTable()
    df = explorer.select(explorer_id)
    return dict(zip(df.columns, df.values[0] if bool(len(df)) else [''] * len(df.columns)))

# ▶ 탐험가 추가하기 (POST /explorers)
@explorers_router.post("/")
def insert(explorer: Explorer = Form(...)):
    table = ExplorerTable()
    return {"msg": table.insert(explorer)}

# ▶ 탐험가 정보 수정하기 (PUT /explorers/{explorer_id})
@explorers_router.put("/{explorer_id}")
def update(explorer_id: int, explorer: ExplorerUpdate):
    table = ExplorerTable()
    return {"msg": table.update(str(explorer_id), explorer)}

# ▶ 탐험가 삭제하기 (DELETE /explorers/{explorer_id})
@explorers_router.delete("/{explorer_id}")
def delete(explorer_id: int):
    table = ExplorerTable()
    result = table.delete(explorer_id)
    print(f"결과 : {result}")
    return {"msg": result}


# =====================[ 외계인 관련 API ]=====================

# ▶ 모든 외계인 정보 가져오기 (GET /aliens)
@aliens_router.get("/")
def index():
    alien = AlienTable()
    df = alien.select()
    result = {'data': []}
    for row in df.values:
        result['data'].append(dict(zip(df.columns, row)))
    return result

# ▶ 특정 외계인 정보 가져오기 (GET /aliens/{alien_id})
@aliens_router.get("/{alien_id}")
def index(alien_id: int):
    alien = AlienTable()
    df = alien.select(alien_id)
    return dict(zip(df.columns, df.values[0] if bool(len(df)) else [''] * len(df.columns)))

# ▶ 외계인 추가하기 (POST /aliens)
@aliens_router.post("/")
def insert(alien: Alien = Form(...)):
    table = AlienTable()
    return {"msg": table.insert(alien)}

# ▶ 외계인 정보 수정하기 (PUT /aliens/{alien_id})
@aliens_router.put("/{alien_id}")
def update(alien_id: int, alien: AlienUpdate):
    table = AlienTable()
    return {"msg": table.update(str(alien_id), alien)}

# ▶ 외계인 삭제하기 (DELETE /aliens/{alien_id})
@aliens_router.delete("/{alien_id}")
def delete(alien_id: int):
    table = AlienTable()
    return {"msg": table.delete(alien_id)}


# =====================[ 기타 기능 API ]=====================

# ▶ 테이블 종류에 따른 한글 컬럼명 가져오기 (GET /key/{kind})
@app.get("/key/{kind}")
def Key(kind: str):
    return {"key": KoreanCol.Alien() if kind == "aliens" else KoreanCol.Explorer()}

# ▶ 특정 ID가 존재하는지 확인 (GET /ishasuser/{kind}/{id})
@app.get("/ishasuser/{kind}/{id}")
def Key(kind: str, id: int):
    table: AlienTable | ExplorerTable
    if kind == 'aliens':
        table = AlienTable()
    else:
        table = ExplorerTable()
    df = table.select(str(id))
    return {"msg": '존재' if bool(len(df)) else '해당 아이디가 존재하지 않습니다'}

app.include_router(explorers_router)
app.include_router(aliens_router)