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
    
# 탐험가(Explorer) 데이터 모델
class Explorer(BaseModel):
    id: int
    name: str
    rank: str
    assignment: str
    species: str

# 외계인(Alien) 데이터 모델
class Alien(BaseModel):
    id: int
    name: str
    species: str
    homeworld: str
    affiliation: str

# 탐험가(Explorer) 업데이트용 모델
class ExplorerUpdate (BaseModel):
    name: str
    rank: str
    assignment: str
    species: str

# 외계인(Alien) 업데이트용 모델
class AlienUpdate (BaseModel):
    name: str
    species: str
    homeworld: str
    affiliation: str

# 데이터베이스 인터페이스 추상 클래스
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
                return '해당 아이디가 존재하지 않습니다'
            cursor.execute("UPDATE alien SET affiliation=?, species=?, homeworld=?, name=? WHERE id=?",
                           (alien.affiliation, alien.species, alien.homeworld, alien.name, id))
            con.commit()
            con.close()
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
            return "추가됐습니다"
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
class ID(BaseModel):
    id:int