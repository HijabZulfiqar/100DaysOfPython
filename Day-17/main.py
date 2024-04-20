class User:
   def __init__(self,  userId,username,password):

       self.id =userId;
       self.Username =username
       self.Password =password;
       self.following=0
       self.followers=0

   def follow(self,user):
      user.followers+=1
      self.following+=1


user_1 = User(211370188,"Hijab",11222)
user_2 = User(211370160,"Ammar",2002)
print(user_1.id)
# user_1.getUsername()
user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)
# print(user_1.Username)
# print(user_1.Password)
# print(user_1)
# user_1.username = 'Hijab'
# print(user_1.username)

