Minitwit
=========
### 전공동아리 GRAM - Minitwit 

## Technical Stack

### Main
- Python
- Flask

### Database
- MongoDB 

### API Documentation
- Flasgger (미구현)

### Authorization
- Json Web Token (JWT)

### host
- local or AWS

## Api
- REST API
  - blueprint + Flask-restful

### 1. 로그인 및 회원가입 구현 & 여러 account 기능들 구현
  - signup
  - login
  - Token을 DB로 관리해주고, 독립된 Token 하나만을 사용하는 기능은 미구현

### 2. 게시물 구현. + Comments, tags
  - post 작성
  - 모든 post 보는 기능
  - commend 작성
  - tag 추가

### 3. Followers, Following
  - Follow
  - 팔로워, 팔로잉 조회
  - 팔로우 끊기
  이 부분에서는 데이터베이스를 효율적으로 구조화해서 사용하면 보다 쿼리문을 깔끔하게 사용할 수 있을 것 같다.
