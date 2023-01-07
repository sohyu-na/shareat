오픈SW플랫폼 맛집추천 웹 어플리케이션 팀 프로젝트 [어서오소 ]
#  SharEat 
: Web pages to share your favorite restaurant with others <br>

## 1. Introduction of pages
### [ 메인 화면 ]

<img width="960" alt="메인홈" src="https://user-images.githubusercontent.com/79395147/211154816-5a7333a2-74a4-4127-89cc-d47b613d6a8e.png">

- 홈 화면과 맛집 리스트 화면의 기능을 동시에 구현
- 회원가입 및 로그인 화면으로 바로 이동 가능
- 맛집 등록 화면으로 바로 이동 가능
- 가게 리스트
- 가게의 별점을 바로 확인 가능
- 사진을 클릭하면 해당 맛집의 상세 페이지로 바로 이동 가능 
<br>

  ( 가게 정렬 및 페이징 )
- 카테고리 별 정렬: 한식, 중식, 일식, 양식, 아시아, 남미, 디저트, 주점, 기타
- 최신순 정렬: 최근에 등록된 가게 순으로 정렬 가능 
- 평점순 정렬: 리뷰에서 등록한 가게의 평점을 내림차순 정렬
- 카테고리+ 최신순 정렬 가능 / 카테고리+ 평점순 정렬 가능
- 페이징: 한 페이지 당 3X3

### [ 가게 정보 조회화면 ]
<img width="960" alt="가게 상세정보 조회" src="https://user-images.githubusercontent.com/79395147/211155092-3fdbcc1c-ce96-4d06-a991-b04ab25fcb40.png">

- 대표메뉴 조회화면 과 리뷰 조회화면으로 바로 이동 가능
- 레이더 차트(Extra Credit)를 통해 맛집의 맛, 가성비, 서비스, 분위기,  위생 점수를 한 눈에 파악 가능
- 별점과 재방문 희망률을 통해 손님의 평가를 파악 가능
- 가게 정보와 사진 및 예약 페이지로 연결되는 링크 첨부 

찜하기 버튼을 통해 해당 가게를 내가 찜한 맛집에 추가

### [ 가게 대표메뉴 조회화면 ]
<img width="960" alt="대표메뉴 조회 화면" src="https://user-images.githubusercontent.com/79395147/211155244-fee0fcaf-9c83-451c-96b9-5a33f36d9d84.png">

- 가게의 대표메뉴의 음식명, 사진, 가격, 알러지와 비건 여부를 알려줌
- '대표메뉴 수정하기' 버튼을 통해 대표메뉴 수정화면으로 바로 이동 가능

### [ 가게 리뷰 조회화면 ]
<img width="960" alt="리뷰 조회" src="https://user-images.githubusercontent.com/79395147/211155363-9800baf3-989e-40f9-9ecf-02cf80762838.png">

- 리뷰 작성자의 닉네임, 점수, 작성 날짜, 리뷰 사진, 리뷰 내용을 제공
- 해당 리뷰가 도움이 된다고 느꼈으면 사용할 수 있는 동의 버튼(Extra Credit) 제공 
- 리뷰에 동의한 사람 수를 알려줌
- '리뷰 등록하기' 버튼을 통해 맛집 리뷰 등록화면으로 바로 이동 가능

### [ 회원가입 & 로그인 & 로그아웃 ]
<img width="947" alt="로그인" src="https://user-images.githubusercontent.com/79395147/211155418-1d2dd438-b3b6-47f5-8f67-b0475d53162f.png">
- 로그인 페이지에서 회원가입 페이지로 바로 이동 가능

<img width="947" alt="로그아웃" src="https://user-images.githubusercontent.com/79395147/211155424-d5022f01-fa0c-47bd-a320-3897bd36249e.png">
- logout 버튼을 통해 바로 로그아웃 가능

<img width="938" alt="로그인 화면" src="https://user-images.githubusercontent.com/79395147/211155430-cbdb5f17-2fe6-45ab-9119-65a470278902.png">
- 회원가입 시 입력한 아이디와 비밀번호를 통해 로그인

<img width="960" alt="회원가입" src="https://user-images.githubusercontent.com/79395147/211155463-06c0ccbb-757a-4102-a039-40f7a7106cfc.png">
- 본인이 직접 아이디 와 비밀번호를 설정
- 이미 등록된 아이디일 경우 중복임을 알려줌
- 이름, 성별, 생년월일을 입력

### [ 맛집 등록 화면 ]
<img width="960" alt="맛집 등록" src="https://user-images.githubusercontent.com/79395147/211155398-b42a2dff-6310-4a33-a802-ead29aa326da.png">
- 공유를 원하는 맛집의 상호명, 전화번호, 주소, 사이트, 영업시간, 주차 및 예약 가능 여부, 카테고리, 가격대 와 식당의 사진을 입력

### [ 맛집 수정 화면 ]
<img width="960" alt="맛집 수정" src="https://user-images.githubusercontent.com/79395147/211155394-1d034f6e-b73d-4765-85c9-1fb689bdf00d.png">
- 이미 등록되어 있는 맛집의 정보들 중 원하는 부분을 선택해서 수정 가능

### [ 대표메뉴 등록화면 ]
<img width="960" alt="대표 메뉴 등록 " src="https://user-images.githubusercontent.com/79395147/211155388-51b7ec7b-8f14-4688-a5b3-bba4fcc524d2.png">
- 대표메뉴의 이름, 가격, 알러지 와 비건 여부 및 사진을 등록

### [ 대표메뉴 추가 및 삭제 ]
<img width="941" alt="대표 메뉴 수정" src="https://user-images.githubusercontent.com/79395147/211155386-f2e08532-604d-430c-9d98-d3187e6a4be0.png">
- 대표메뉴 추가하기로 재등록 가능
- 등록한 대표메뉴 삭제 가능

### [ 맛집 리뷰 등록화면 ]
<img width="960" alt="리뷰 등록" src="https://user-images.githubusercontent.com/79395147/211155379-f5c4face-1702-4893-a9a2-b879534d07df.png">
- 0점부터 5점 중 원하는 점수를 줄 수 있음
- 맛, 가성비, 서비스, 위생, 분위기 중 리뷰 작성자가 마음에 든 부분을 선택 가능
- 재방문 의사 선택이 가능
- 상세 리뷰 작성 및 사진 첨부 가능 
- 리뷰 작성 시 닉네임 직접 작성 가능, 작성하지 않을 시 익명으로 등록됨

### [ 내가 찜한 맛집 화면 ]
<img width="960" alt="내가 찜한 맛집" src="https://user-images.githubusercontent.com/79395147/211155374-39d3d260-4369-4777-80c4-48f7e121c487.png">
- 찜하기 버튼을 통해 내가 찜한 맛집에 추가 가능
- 홈 화면에서와 마찬가지로 가게의 이름, 카테고리, 별점을 메인에서 확인 가능
- 맛집의 사진을 클릭하면 해당 맛집의 상세 페이지로 바로 이동 가능

## 2. Development environment
- FrontEnd : HTML / CSS / JS
- BackEnd : Python / Flask / Firebase

## 3. Configuration of database
<img width="831" alt="db1" src="https://user-images.githubusercontent.com/79395147/211157341-568d2d58-e576-419e-a8a2-3a2d42d9d883.png">
<img width="791" alt="db2" src="https://user-images.githubusercontent.com/79395147/211157347-ed2846e1-b0a1-4790-8780-317519afa014.png">
<img width="835" alt="db3" src="https://user-images.githubusercontent.com/79395147/211157348-43028672-5576-44fa-b64f-7b3f837eaad0.png">
<img width="826" alt="db4" src="https://user-images.githubusercontent.com/79395147/211157350-e1a8b030-615c-4361-a3d0-a3d3510aea90.png">

## 4. 기술 블로그 Link
- 개념: https://gmlwo810.tistory.com/105
- 팁/디버깅: https://gmlwo810.tistory.com/106
- 가이드: https://aj-tech.tistory.com/2
- 해설1: https://velog.io/@ccomi/%EC%9B%B9-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%ED%95%91-%EB%82%B4%EA%B0%80-%EC%B0%9C%ED%95%9C-%EB%A7%9B%EC%A7%91-%EA%B5%AC%ED%98%84
-해설2: https://velog.io/@sha0809/%EC%9B%B9-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D-%EB%A0%88%EC%9D%B4%EB%8D%94-%EC%B0%A8%ED%8A%B8-%EA%B5%AC%ED%98%84

