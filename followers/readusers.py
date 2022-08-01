from json import *
with open("users.json") as f:
    data=load(f)
print(len(data))

# followers of id 2

followers_user=[len(user["followers"]) for user in data if user["id"]==2]
print(followers_user)

# users with most followers
print(max(data,key=lambda user:len(user["followers"])))

# akhil-followings

all_users=[user ["id"]for user in data]
my_followings_list=[user["following"]for user in data if user["id"]==1]
my_followings=my_followings_list.pop()
print(all_users)
print(my_followings)

# suggestion

to_flw=[user for user in all_users if user not in my_followings]
print(to_flw)

# better_to_follow=set(all_users-set(my_followings))
# print(better_to_follow)

# print(dir(set))




