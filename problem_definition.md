# 🖖 스타트렉 스토리텔링 기반 과제: "스타플릿 데이터 위기!"
<img src="https://images.unsplash.com/photo-1501532358732-8b50b34df1c4?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D" alt="Sample Image" width="300">

---

## 🚀 우주력 2300년, 스타플릿의 새로운 도전

광활한 은하계를 탐험하는 **유나이티드 페더레이션 오브 플래닛(United Federation of Planets, UFP)**, 그리고 그 탐사의 최전선에 있는 **스타플릿(Starfleet)**.

스타플릿의 함선들은 우주의 미지의 영역을 개척하며, 새로운 생명체와 문명을 찾아 나아가고 있다. 하지만 이 거대한 사명을 수행하는 데 있어, 예상치 못한 문제가 발생했다.

**스타플릿의 데이터 관리 시스템이 한계를 맞이한 것이다.**

---

## 🖖 문제의 시작: USS 엔터프라이즈의 긴급 통신

> "스타플릿 본부 응답하라. 여기는 USS 엔터프라이즈.  
> 방금 막 새로운 외계 생명체를 발견했지만, 데이터 관리 시스템이 다운되었다.  
> 현재 우리가 수집한 정보를 저장할 방법이 없다. 반복한다. 데이터 관리 시스템이 다운되었다!"
> 
> — **캡틴 제임스 T. 커크 (James T. Kirk)**

스타플릿 본부는 즉시 상황을 분석했다.  
함선들은 하루에도 수십 개의 새로운 종족과 조우하고, 수많은 승무원이 함선 간 배치를 받고 있다. 그러나 기존의 시스템은 이를 관리하기엔 너무 오래되었고, 데이터가 제대로 저장되지 않아 **중요한 탐사 정보가 유실될 위험**에 처해 있었다.

이대로 가면 **은하계 탐사의 역사적 순간들을 기록하지 못할 수도 있다!**

---

## 🖖 미션: 스타플릿 데이터 관리 시스템(SDMS) 구축

스타플릿 최고 데이터 엔지니어인 당신에게 **중대한 임무**가 주어졌다.  
바로 **새로운 데이터 관리 시스템을 구축하는 것!**

당신은 **FastAPI**를 사용하여 **탐험가(Explorer)와 외계 생명체(Alien)의 정보를 효율적으로 관리할 수 있는 API**를 만들어야 한다.  
이를 통해 USS 엔터프라이즈뿐만 아니라, 보이저(Voyager), 디파이언트(Defiant) 등 **모든 스타플릿 함선들이 안전하고 체계적으로 데이터를 기록할 수 있도록 해야 한다.**

---

## 🖖 시스템 요구 사항

### 1. 데이터 모델링: 새로운 생명체와 탐험가를 등록하라!

먼저, 데이터베이스를 설계해야 한다.  
스타플릿은 다음과 같은 정보를 관리할 수 있어야 한다.

### 📌 탐험가(Explorer) 정보
- `id` (고유번호)  
- `name` (이름)  
- `rank` (계급 – 예: 대위, 부함장, 엔지니어 등)  
- `assignment` (소속 함선 – 예: USS 엔터프라이즈, USS 보이저 등)  
- `species` (종족 – 예: 인간, 벌칸, 안도리안 등)  

### 📌 외계 생명체(Alien) 정보
- `id` (고유번호)  
- `name` (이름)  
- `species` (종족)  
- `homeworld` (출신 행성)  
- `affiliation` (소속 – 예: 클링온 제국, 로뮬런 스타 엠파이어 등)  

---

### 2. API 구축: 데이터를 손쉽게 관리하라!

FastAPI를 활용하여 두 가지 주요 엔드포인트를 만들어야 한다.

#### ✅ `/aliens` 엔드포인트
- `POST /aliens/` : 새로운 외계 생명체 등록
- `GET /aliens/` : 모든 외계 생명체 조회
- `GET /aliens/{alien_id}` : 특정 외계 생명체 정보 조회
- `PUT /aliens/{alien_id}` : 외계 생명체 정보 수정
- `DELETE /aliens/{alien_id}` : 외계 생명체 삭제

#### ✅ `/explorers` 엔드포인트
- `POST /explorers/` : 새로운 탐험가 등록
- `GET /explorers/` : 모든 탐험가 조회
- `GET /explorers/{explorer_id}` : 특정 탐험가 정보 조회
- `PUT /explorers/{explorer_id}` : 탐험가 정보 수정
- `DELETE /explorers/{explorer_id}` : 탐험가 삭제

---

### 3. 초기 데이터: 스타플릿의 기록을 보존하라!

#### 📌 탐험가 예시 (Explorers Table)
| ID | Name         | Rank     | Assignment         | Species  |
|----|-------------|---------|-------------------|---------|
| 1  | James T. Kirk  | Captain | USS Enterprise | Human   |
| 2  | Spock        | Commander | USS Enterprise | Vulcan  |
| 3  | Jean-Luc Picard | Captain | USS Enterprise-D | Human   |
| 4  | Kathryn Janeway | Captain | USS Voyager | Human   |
| 5  | Worf         | Lieutenant | USS Defiant | Klingon |

#### 📌 외계 생명체 예시 (Aliens Table)
| ID | Name       | Species     | Homeworld        | Affiliation |
|----|-----------|------------|-----------------|-------------|
| 1  | Kahless   | Klingon     | Qo'noS          | Klingon Empire |
| 2  | Sarek     | Vulcan      | Vulcan          | Federation |
| 3  | Tal'Aura  | Romulan     | Romulus         | Romulan Empire |
| 4  | Neelix    | Talaxian    | Talax           | Independent |
| 5  | Gorn Commander | Gorn  | Gornar          | Gorn Hegemony |

---

## 🖖 엔딩: 미래를 위한 데이터 시스템을 완성하라!

이제 당신에게는 단 한 가지의 목표가 있다.  
바로 **스타플릿의 데이터를 안전하게 저장하고 관리할 차세대 시스템을 구축하는 것!**

> "우리는 미지의 세계를 탐험하며, 새로운 생명체와 문명을 찾아 나아간다. 하지만 우리가 그들의 기록을 남기지 못한다면, 우리의 탐사는 의미가 없을 것이다."
> 
> — **캡틴 장 뤽 피카드 (Jean-Luc Picard)**

당신이 구축할 시스템은 앞으로 수십 년간 스타플릿이 새로운 문명과 조우할 때마다 사용될 것이다.  
이제 **스타플릿 데이터 관리 시스템(SDMS)**을 완성하라! 🚀


#### Reference to https://github.com/rumbarum/fastapi-book-example 
