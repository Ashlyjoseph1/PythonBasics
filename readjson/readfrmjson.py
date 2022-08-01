from json import *

with open("blog.json","r") as f:
     data=load(f)
print(data)


user_posts=[post for post in data if post["userId"]==1]
print(len(user_posts))

# no of likes for postId=3
like_cunt=[ len(post["liked_by"]) for post in data if post["postId"]==3]
print(like_cunt)

# no of posts liked by  postId=2
like_cunt_user=len([post for post in data if 2 in  post["liked_by"]])
print(like_cunt_user)

# most liked post

print(max(data,key=lambda post:len(post["liked_by"])))

# least liked post

print(min(data,key=lambda post:len(post["liked_by"])))


