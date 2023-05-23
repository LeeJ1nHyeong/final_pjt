### commit할 때마다 변경사항 commit message로 써놓기!!!

## 사전 준비

### 1) Back-End(Django)

1.   final-pjt-back 폴더 이동 후 venv 설치 및  활성화

     ```bash
     (폴더 미이동 시) cd final-pjt-back
     python -m venv venv
     source venv/Scripts/activate
     ```

2.   requirement 설치

     ```bash
     pip install -r requirements.txt
     (작업 중 설치 파일 추가 시) pip freeze > requirements.txt
     ```

3.   (필요 시) migrate 진행

     ```bash
     python manage.py makemigrations
     python manage.py migrate
     ```

4.   서버 켜기

     ```bash
     python manage.py runserver
     ```



### 2) Front-End(Vue)

1.   final-pjt-front 폴더 이동 후 node_modules 설치

     ```bash
     (폴더 미이동 시) cd final-pjt-front
     npm install
     ```

2.   서버 켜기

     ```bash
     npm run serve
     ```



## 개발일지

#### 23-05-15

*   프로젝트 구상(컴포넌트 뷰 등)
*   전체적인 웹 틀 만들기
*   API 활용하여 카카오 맵 웹 화면 구현 테스트

#### 23-05-16

*   HomeView → Carousel 구현 시도(제대로 구현되지 않아 수정 필요)
*   로그인 화면, 회원가입 화면 구현(router-link 활용하여 회원가입 클릭 시 화면 이동도 성공, 기능은 아직 추가X)
*   API 활용하여 정기예금 자료 요청 테스트 → 성공하여 정기적금도 시도 예정

#### 23-05-17

*   정기예금, 정기적금, 환율 model 생성 및 api 데이터 요청
*   정기예금, 정기적금 json 파일에 Nested Relationship 적용(Depositoptions, SavingOptions)
*   환율계산기 View 구현(최소한의 화면만 구현, 기능은 아직 X)
*   기타 CSS 약간 수정
*   로그인, 회원가입 기능 구현
     *   회원가입 기능, 비밀번호 변경은 토큰이 잘 받아지는 것 확인
     *   로그인은 현재 axioserror가 발생하여 원인을 찾아봐야함
     *   AllowAny상태에서 게시물 전체 조회, 게시물 생성에 대해 permission IsAuthenticated 데코레이터를 적용하여 headers에 Token을 정상적으로 기입했음에도 인증이 되지 않는 문제 발생

#### 23-05-18

*   로그인, 회원가입 관련 디버깅
     * 게시물 전체 조회, 게시물 생성(해결완료) -> settings에서 'DEFAULT_AUTHENTICATION_CLASSES'를 추가하지 않아 발생한 문제였음
     * 로그인, 회원가입(해결완료) -> 교안을 참고한 결과 payload후 mutations에서 id 변수명을 username으로 해야 정상적으로 진행되는 걸 알게 됨
     * 커뮤니티 게시판 진입 시 로그인되지 않으면 팝업이 생기게 하고 싶지만 뜨지 않음(해결중)
     * User model 성별(gender), 나이(age), 거주지(residence) 속성 추가

*   금융상품비교 화면 구현
     *   axios 요청으로 전체 금융상품 조회하여 화면에 올리기는 성공
     *   특정 금융상품명 클릭 시 상세 조회 페이지로 넘어가기 성공 -> 상세 내용 화면에 나타내기 (완료)
     *   백엔드에서 특정 상품 상세조회를 만들지 않아 제작해야함 -> 코드 작성 및 테스트 (완료)
     *   은행별 금융상품 조회 기능 구현 (완료)

*   지도
     * 광역시/도 선택 시, 해당 광역시/도에 맞는 행정구역이 나오게 구현 성공

*   환율
     * api로 받은 환율 데이터 목록 화면에 구현하기(예정)

*   기타
     * 진희가 만든 코드랑 일부분 합치기 -> App.vue(NavBar, FootBar 적용 포함), HomeView.vue, LoginView.vue, SignupView.vue merge 완료

#### 23-05-19

*   로그인/로그아웃 및 회원가입 기능 구현하기
     * User model 추가한 속성 바탕으로 회원가입 구현하기 -> 토큰 발급 확인 완료, 새로 추가된 속성(gender, age, residence)의 값이 DB에 저장되지 않는 현상 확인
     * AxiosError 발생 시(회원가입이 안될 시) 회원가입이 되지 않았다는 알림 및 사유 출력하기
       -> 조건별로 알림 문구 뜨게 만들어야 될 듯(아이디 최소 길이, 비밀번호 최소 길이 등)
     * 로그인이 안되어 있으면 로그인 링크만, 로그인이 되어있으면 로그아웃 및 프로필 링크만 뜨게 만들기 (완료)
     * 로그인이 안 된 상태에서 금융상품조회, 환율, 지도, 게시판 링크 클릭 시 '로그인이 필요한 서비스입니다.' 팝업 출력 후 로그인 페이지 이동 구현
          * router-link에서는 @click으로 이벤트가 발생하지 않아 검색해본 결과 @click.native를 붙여야 하는 것을 알게 됨
          * 미로그인 상태에서 HomeView에 있는 버튼 클릭 시 로그인 페이지 이동의 경우 router-link 태그가 아닌 button 태그로 설정해야 작동되는 것을 확인
          * 구현은 성공 했지만 간헐적으로 에러페이지가 반짝였다가 로그인 페이지로 이동하는 현상 발생 
          * 네비게이션 가드를 활용해야 할 듯

*   지도
     * 광역시/도, 시/군/구, 은행명에 해당하는 지도 검색 결과 구현하기(예정) 
          * MapSearchInput에서 얻은 키워드들을 KakaoMap으로 props하는데에는 성공
          * 이 props한 키워드들로 카카오맵 api 가이드 참고하여 구현 시도할 것

*   환율
     * api로 받은 환율 데이터 목록 화면(실시간 환율)에 구현하기 (완료) -> 예쁘게 배치해야함
     * 환율계산기 구현하기(예정)

#### 23-05-20

*   금융상품조회
     * 정기적금 api 요청 완료
     * Tab기능 추가(정기예금 tab, 정기적금 tab)

*   환율
     * 비영업일(주말, 공휴일 등)의 경우 데이터 자료가 없는 것을 확인 -> 금요일 또는 공휴일 이전 영업일 날짜로 바꿔서 요청해야함

*   게시판
     * 게시글 CRUD 구현 완료
     * 생성된 게시글이 없을 시 axioserror 발생하는 현상 발견
     * 댓글 CRUD 구현(예정)

#### 23-05-21

*   회원가입
     * 회원가입이 안된 상태에서 성별, 나이, 거주지 정보가 저장되지 않음
          -> 회원가입 후 프로필 페이지에서 해당 정보 입력할 수 있게 구현해야 될 듯

*   금융상품조회
     * 각 상품 별 옵션 출력 성공(게시할 내용들 정리 해야함)

*   게시판
     * 게시글이 없을 때 빈 화면으로 만들기 성공('게시글이 없습니다' 문구 추가할 예정)
          -> 같은 방법으로 댓글도 그럴 예정
     * 댓글 작성자 출력 시도 중 IntegrityError 발생(문제 해결)
          -> views.py에서 serializer.save() 진행 시 user=request.user를 추가하지 않았었음
     * 댓글 CRUD 구현 완료

*   프로필
     * 진희가 만들어 놓은 ProfileVue merge
     * 프로필 model 제작 및 생성, 조회, 수정 기능 구현

#### 23-05-22

*   환율
     * ~~간단한 계산기 기능 구현 완료 (환율별로 비율 환산해서 계산하려면 api 자료가 와야함)~~
     * input 사이에 자리바꾸기 버튼 만들기 (완료)
     * 환율계산기 구현 완료(JPY 등 100 화폐단위당 환율은 계산 따로 해줘야함)

*   금융상품조회
     * 관심상품(팔로우)기능 추가 예정(등록한 관심상품 리스트를 프로필 화면에 구현할 예정)
     * 각 상품별 옵션 정리하기(완료)

*   지도
     * 기능 구현 반드시 완료하기 (데이터 추출 성공)
          -> 가공해서 리스트 보기 좋게 만들면 됨 (완료)

*   프로필
     * 프로필 추가 및 수정 기능 구현 예정
     * 금융상품 알고리즘 제작하여 나열할 예정(3개 정도를 랜덤으로, 카테고리는 지역, 소득금액 등 예정)

*   기타
     * 진희가 만든 코드랑 merge 진행하기
          * ~~Home~~
          * ~~금융상품~~
          * 환율
          * ~~지도~~
          * 커뮤니티
          * 프로필

#### 23-05-23

*   계정관련
     * 로그인해야 접근 가능하게 만들기(네비게이션 가드)

*   금융상품
     * ~~세전, 세후이자 계산식 세우기~~(완료)
     * 카테고리별 검색 추가하기 (가입방식만 추가할 생각)
     * 금융상품 추천 알고리즘 제작

*   프로필
     * 기본정보화면 구현
     * 관심상품 목록
     * 작성한 게시글

*   기타
     * 제출용 README.md 제작(계획서, ERD 등 포함시키기)


---------------------------------------------

## 해결해야할 과제

#### 로그인/회원가입 관련

* 네비게이션 가드 활용하여 비로그인 상태일때 로그인 화면 전환
* 성별, 나이, 거주지 DB 저장 안되는 문제
     -> profile model을 따로 만들어 외래키 활용하여 데이터 저장해야 할듯
* 비로그인 상태에서 로그인 페이지 이동 시 간헐적으로 반짝이는 에러 페이지 문제 -> 네비게이션 가드 사용하면 없어질 것으로 추정
* ~~아이디 저장 체크박스 클릭 시 이 후 로그인 화면으로 와도 아이디가 남아있게 만들기~~ (후순위로 미룸)
* AxiosError 발생 시(회원가입이 안될 시) 회원가입이 되지 않았다는 알림 및 사유 출력하기
     -> 조건별로 알림 문구 뜨게 만들어야 될 듯(아이디 최소 길이, 비밀번호 최소 길이 등)
* 회원 탈퇴 기능
* 관리자 계정
* (가능하다면?) 소셜 로그인

#### 금융상품비교

* ~~정기적금 api 불러오기~~
* 상세페이지에서 관심 상품 등록 기능 구현(프로필의 팔로우랑 같은 기능)
* ~~예치 기간별 금리 및 세전/세후이자 계산하여 리스트에 나열~~
* ~~예쁘게 배치하기~~ (merge 완료)

#### 환율

* ~~환율 계산기 제작~~
* ~~비영업일에 환율 데이터 불러오는 방법 찾아보기~~(평일 발표라서 후순위로 미룸)
* JPY 등 100 화폐단위로 계산하는 부분 계산 적용하기

#### ~~지도~~

* ~~광역시/도, 시/군/구, 은행명에 해당하는 지도 검색 결과 구현하기(리스트 나열 정리만 하면 됨)~~

#### 커뮤니티

* ~~게시판 및 댓글 CRUD~~
     * ~~게시글 생성~~
     * ~~전체 게시글 조회~~
     * ~~특정 게시글 상세 조회~~
     * ~~특정 게시글 수정~~
     * ~~특정 게시글 삭제~~
     * ~~특정 게시글 댓글 조회~~
     * ~~특정 게시글 댓글 생성~~
     * ~~특정 게시글 댓글 수정~~
     * ~~특정 게시글 댓글 삭제~~
     * ~~댓글 작성자 출력하게 만들기~~
* 비로그인시 게시글 작성 불가 상태로 만들기(로그인 페이지로 이동하게 만들기)

#### 프로필

* 유저 프로필 리스트 나열
* 유저 관심상품 등록 리스트 구현
* (가능하다면?) 상품 추천 알고리즘 제작

#### 기타

* View 및 Component 폴더 정리 (가능하다면 modules도 정리하여 폴더 제작하기)
* 진희가 만든 코드와 합치기
     * ~~Home~~
     * ~~금융상품~~(230522)
     * 환율
     * ~~지도~~(230522)
     * 커뮤니티
     * 프로필
* ~~남은 기간 만들 수 있는 기능 생각해보기~~ (현재 할 수 있는 기능들부터 완성하기로 함)
* CSS
* 발표 PPT 제작