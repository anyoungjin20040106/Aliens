'''
이 과제는 제가 가르치고 있는 학생인 중학생(특징 2000년생을 아저씨 아줌마라고 생각함)이랑 같이 풀었습니다
이 중학생은 SQL을 할줄몰라서 
제가 DB를 다루는 클래스,
한국어 칼럼을 가져오는 클래스,
그리고 입력모델이 있는 tool모듈을 만들었고
또한 웹과 fastapi의 연동이 흔해 빠져서 싫어하고 
unity와 fastapi의 연동은 특별해서 도전적이라 좋아하기 때문에
(저도 제 학생의 생각의 동의합니다)
웹에다가 fastapi를 연동하지 않고 유니티에다가 fastapi를 연동하기로 했습니다
'''
import sqlite3
from pydantic import BaseModel
import pandas as pd
from abc import ABC, abstractmethod

#DB 필드명 한국어 칼럼
class KoreanCol:
    @staticmethod
    def Alien():
        return ['아이디 ','이름 ','종족 ','출신 행성 ','소속 ']
    @staticmethod
    def Explorer():
        return ['아이디 ','이름 ','계급 ','소속 함선 ','종족 ']
    
# 탐험가 데이터를 표현하는 틀
class Explorer(BaseModel):
    id: int            # 탐험가 고유 번호
    name: str          # 이름
    rank: str          # 계급 (ex. 선장, 부선장 등)
    assignment: str    # 어떤 함선에 배정됐는지
    species: str       # 종족

# 외계인 데이터를 표현하는 틀
class Alien(BaseModel):
    id: int            # 외계인 고유 번호
    name: str          # 이름
    species: str       # 종족
    homeworld: str     # 출신 행성
    affiliation: str   # 소속 (어디 조직에 소속됐는지)

# 업데이트할 때 쓸 데이터 틀 (id는 수정 안 하니까 없음)
class ExplorerUpdate(BaseModel):
    name: str
    rank: str
    assignment: str
    species: str

class AlienUpdate(BaseModel):
    name: str
    species: str
    homeworld: str
    affiliation: str

# 데이터베이스 클래스들의 틀
class DB(ABC):

    @abstractmethod
    def select(self, id=''):
        """SELECT 기능 (각 자식 클래스에서 구현)"""
        pass

    @abstractmethod
    def insert(self, obj):
        """INSERT 기능 (각 자식 클래스에서 구현)"""
        pass

    @abstractmethod
    def update(self, id:str, obj):
        """UPDATE 기능 (각 자식 클래스에서 구현)"""
        pass

    @abstractmethod
    def delete(self, id=''):
        """DELETE 기능 (각 자식 클래스에서 구현)"""
        pass

# Alien 테이블을 관리하는 클래스
class AlienTable(DB):
    def select(self, id=''):
        """Alien 테이블에서 데이터를 조회"""
        con = sqlite3.connect('aliens.db')
        try:
            df = pd.read_sql_query("SELECT * FROM alien WHERE id=?", con, params=(id,)) if id!='' else pd.read_sql_query("SELECT * FROM alien", con)
            con.close()
            return df
        except:
            return None
    
    def delete(self, id=''):
        """Alien 테이블에서 특정 ID의 데이터를 삭제"""
        con = sqlite3.connect('aliens.db')
        try:
            if not id:
                return "인자좀 넣어라"
            cursor = con.cursor()
            if not len(self.select(id)):
                print('해당 아이디가 존재하지 않습니다')
                return '해당 아이디가 존재하지 않습니다'
            cursor.execute("DELETE FROM alien WHERE id=?", (id,))
            con.commit()
            con.close()
            print("삭제 완료")
            return "삭제 완료"
        except Exception as e:
            print(f'예외 사항 : {e}')
            return f'예외 사항 : {e}'
    
    def update(self, id:str,alien: AlienUpdate):
        """Alien 테이블에서 특정 ID의 데이터를 수정"""
        con = sqlite3.connect('aliens.db')
        try:
            cursor = con.cursor()
            if not len(self.select(id)):
                con.close()
                print('해당 아이디가 존재하지 않습니다')
                return '해당 아이디가 존재하지 않습니다'
            cursor.execute("UPDATE alien SET affiliation=?, species=?, homeworld=?, name=? WHERE id=?",
                           (alien.affiliation, alien.species, alien.homeworld, alien.name, id))
            con.commit()
            con.close()
            print("수정 완료")
            return "수정 완료"
        except Exception as e:
            return f'예외 사항 : {e}'
    
    def insert(self, alien: Alien):
        """Alien 테이블에 데이터를 추가"""
        con = sqlite3.connect("aliens.db")
        cursor = con.cursor()
        try:
            cursor.execute("INSERT INTO alien VALUES(?,?,?,?,?)", (alien.id, alien.name, alien.species, alien.homeworld, alien.affiliation))
            con.commit()
            con.close()
            return "추가 완료"
        except sqlite3.IntegrityError:
            con.close()
            return "이미 존재하는 아이디 입니다"
        except Exception as e:
            con.close()
            return f"예외 상황 발생 : {e}"

# Explorer 테이블을 관리하는 클래스
class ExplorerTable(DB):
    def select(self, id=''):
        """Explorer 테이블에서 데이터를 조회"""
        con = sqlite3.connect('aliens.db')
        try:
            df = pd.read_sql_query("SELECT * FROM explorer WHERE id=?", con, params=(id,)) if id!='' else pd.read_sql_query("SELECT * FROM explorer", con)
            con.close()
            return df
        except:
            return None
    
    def insert(self, explorer: Explorer):
        """Explorer 테이블에 데이터를 추가"""
        con = sqlite3.connect("aliens.db")
        cursor = con.cursor()
        try:
            cursor.execute("INSERT INTO explorer VALUES(?,?,?,?,?)", (explorer.id, explorer.name, explorer.rank, explorer.assignment, explorer.species))
            con.commit()
            con.close()
            return "추가 완료"
        except sqlite3.IntegrityError:
            con.close()
            return "이미 존재하는 아이디 입니다"
        except Exception as e:
            con.close()
            return f"예외 상황 발생 : {e}"
    
    def delete(self, id=''):
        """Explorer 테이블에서 특정 ID의 데이터를 삭제"""
        con = sqlite3.connect('aliens.db')
        try:
            if not id:
                return "인자좀 넣어라"
            cursor = con.cursor()
            if not len(self.select(id)):
                return '해당 아이디가 존재하지 않습니다'
            cursor.execute("DELETE FROM explorer WHERE id=?", (id,))
            con.commit()
            con.close()
            return "삭제 완료"
        except Exception as e:
            return f'예외 사항 : {e}'
    
    def update(self, id:str,explorer: ExplorerUpdate):
        """Explorer 테이블에서 특정 ID의 데이터를 수정"""
        con = sqlite3.connect('aliens.db')
        try:
            cursor = con.cursor()
            if not len(self.select(id)):
                return '해당 아이디가 존재하지 않습니다'
            cursor.execute("UPDATE explorer SET assignment=?, species=?, rank=?, name=? WHERE id=?",
                           (explorer.assignment, explorer.species, explorer.rank, explorer.name,id))
            con.commit()
            con.close()
            return "수정 완료"
        except Exception as e:
            return f'예외 사항 : {e}'
