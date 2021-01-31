## Django Rest Framework(DRF) practice Repository
### 
- User<br>
  @permission_classes([AllowAny])
  - ```[POST] /signup``` ✔ : create_user 👉 자동 encrypt
  - ```[POST] /login``` ✔ : jwt
- Post <br>
  @permission_classes([IsAuthenticated])
  - ```[GET] /post``` ✔
  - ```[GET] /post/<int:post_id>``` ✔
  - ```[PUT] /post/<int:post_id>``` ✔
  - ```[DELETE] post/<int:post_id>``` ✔
- Comment<br>
  @permission_classes([IsAuthenticated])
  - ```[GET] /post/comment``` ✔
  - ```[POST] /post/comment``` ✔
  - ```[PUT] /post/comment/<int:comment_id>``` ✔
  - ```[PUT] /post/comment/<int:comment_id>``` ✔
  
