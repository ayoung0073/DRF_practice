## Django Rest Framework(DRF) practice Repository
### 
- User<br>
  @permission_classes([AllowAny]) 설정
  - ```[POST] /signup``` ✔ : create_user 👉 자동 encrypt
  - ```[POST] /login``` ✔ : JWT
- Post 
  - ```[GET] /post``` ✔
  - ```[GET] /post/<int:post_id>``` ✔
  - ```[PUT] /post/<int:post_id>``` ✔
  - ```[DELETE] post/<int:post_id>``` ✔
- Comment
  - ```[GET] /post/comments``` ✔
  - ```[POST] /post/<int:post_id>/comments/<int:comment_id>``` 
  
