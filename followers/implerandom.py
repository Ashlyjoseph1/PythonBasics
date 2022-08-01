import random
all_users=["a","b","c","d","e"]
def get_user():
    random.shuffle((all_users))
    return all_users[:3]
print(get_user())

# django
# web fundamental
