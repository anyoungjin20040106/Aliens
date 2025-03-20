import sqlite3
from pydantic import BaseModel
import pandas as pd
from abc import ABC, abstractmethod

#한국어 칼럼
class KoreanColumn:
    @staticmethod
    def explorer():
        return ['아이디','이름','계급','소속 함선','종족']
    
    @staticmethod
    def alien():
        return ['아이디','이름','종족','출신행성','소속']

#영어 칼럼
class EnglishColumn:
    @staticmethod
    def explorer():
        return ['id','name','rank','assignment','species']
    
    @staticmethod
    def alien():
        return ['id','name','species','homeworld','affiliation']

#탐험가 클래스
class Explorer(BaseModel):
    id:int
    name:str
    rank:str
    assignment:str
    species:str
#외계인 클래스
class Alien(BaseModel):
    id:int
    name:str
    species:str
    homeworld:str
    affiliation:str
class DB(ABC):
    @property
    def path():
        return 'aliens.db'
    @abstractmethod
    def select(self, id=''):
        """SELECT 구현 (자식 클래스 필수 구현)"""
        pass
    @abstractmethod
    def insert(self, obj):
        """INSERT 구현 (자식 클래스 필수 구현)"""
        pass
    @abstractmethod
    def update(self, obj):
        """UPDATE 구현 (자식 클래스 필수 구현)"""
        pass
    @abstractmethod
    def delete(self, id=''):
        """DELETE 구현 (자식 클래스 필수 구현)"""
        pass

class AlienTable(DB):
    def select(self,id=''):
        con=sqlite3.connect(super().path)
        try:
            df=pd.read_sql_query(f"SELECT * FROM alien WHERE id=?",con,params=(id,)) if bool(id)else pd.read_sql_query(f"SELECT * FROM alien",con)
            con.close()
            return df if bool(len(df)) else "해당 아이디가 존재하지 않습니다"
        except:
            return None
    def delete(self, id=''):
        con=sqlite3.connect(super().path)
        try:
            if id=="":
                return "인자좀 넣어라"
            cursor=con.cursor()
            if not bool(len(self.select(id))):
                return '해당 아이디가 존재하지 않습니다'
            cursor.execute("delete FROM alien WHERE id=?",(id))
            con.commit()
            con.close()
            return "삭제 완료"
        except Exception as e:
            return f'예외 사항 : {e}'
    def update(self, alien:Alien):
        con=sqlite3.connect(super().path)
        try:
            if alien.id=="":
                return "인자좀 넣어라"
            cursor=con.cursor()
            if not bool(len(self.select(alien.id))):
                return '해당 아이디가 존재하지 않습니다'
            cursor.execute(f"update set affiliation='{alien.affiliation}', species='{alien.species}', homeworld='{alien.homeworld}', name='{alien.name}' alien WHERE id=?",(alien.id))
            con.commit()
            con.close()
            return "수정 완료"
        except Exception as e:
            return f'예외 사항 : {e}'
    def insert(self,alien:Alien):
        con=sqlite3.connect("aliens.db")
        cursor=con.cursor()
        try:
            cursor.execute("INSERT INTO alien VALUES(?,?,?,?,?)",(alien.id,alien.name,alien.species,alien.homeworld,alien.affiliation))
            con.commit()
            con.close()
            return  "추가되었습니다"
        except sqlite3.IntegrityError:
            con.close()
            return "이미 존재하는 아이디 입니다"
        except Exception as e:
            con.close()
            return f"예외 상황 발생 : {e}","color"
    
class ExplorerTable(DB):
    def select(self,id=''):
        con=sqlite3.connect('aliens.db')
        try:
            df=pd.read_sql_query(f"SELECT * FROM explorer WHERE id=?",con,params=(id,)) if bool(id)else pd.read_sql_query(f"SELECT * FROM explorer",con)
            con.close()
            return pd.read_sql()
        except:
            return None
    def insert(self,explorer:Explorer):
        con=sqlite3.connect("aliens.db")
        cursor=con.cursor()
        try:
            cursor.execute("INSERT INTO explorer VALUES(?,?,?,?,?)",(explorer.id,explorer.name,explorer.rank,explorer.assignment,explorer.species))
            con.commit()
            con.close()
            return "추가되었습니다"
        except sqlite3.IntegrityError:
            con.close()
            return "이미 존재하는 아이디 입니다"
        except Exception as e:
            con.close()
            return f"예외 상황 발생 : {e}"
    def delete(self, id=''):
        con=sqlite3.connect(super().path)
        try:
            if id=="":
                return "인자좀 넣어라"
            cursor=con.cursor()
            if not bool(len(self.select(id))):
                return '해당 아이디가 존재하지 않습니다'
            cursor.execute("delete FROM explorer WHERE id=?",(id))
            con.commit()
            con.close()
            return "삭제 완료"
        except Exception as e:
            return f'예외 사항 : {e}'
    def update(self,explorer:Explorer):
        con=sqlite3.connect(super().path)
        try:
            if explorer.id=="":
                return "인자좀 넣어라"
            cursor=con.cursor()
            if not bool(len(self.select(explorer.id))):
                return '해당 아이디가 존재하지 않습니다'
            cursor.execute(f"update set assignment='{explorer.assignment}', species='{explorer.species}', rank='{explorer.rank}', name='{explorer.name}' explorer WHERE id=?",(explorer.id))
            con.commit()
            con.close()
            return "수정 완료"
        except Exception as e:
            return f'예외 사항 : {e}'