from blog.models import users, posts


# authenticate
# authenticate(username,email):
def authenticate(**kwargs):
    username = kwargs.get("username")
    email = kwargs.get("email")
    user_data = [user for user in users if user["username"] == username and user["email"] == email]
    return user_data


session = {}  # user:django


def login_required(fn):
    def wrapper(*args, **kwargs):
        if "user" in session:
            return fn(*args,**kwargs)
        else:
              print("u must login")
    return wrapper


@login_required
def loged_user():
    username=session.get("user")
    userId=[user["id"]for user in users if user["username"] == username][0]
    return userId




class SigninView:
    def post(self, *args, **kwargs):
        username = kwargs.get("username")
        email = kwargs.get("email")
        user = authenticate(username="django", email="django@gmail.com")
        if user:
            print("success")
            session["user"] = username
        else:
            print("invalid credentials")

@login_required
def logout(*args, **kwargs):
    session.pop("user")

class PostListView:
    @login_required
    def get(self, *args, **kwargs):
        return posts


class MyPostView:
    @login_required
    def get(self,*args, **kwargs):
        userid=loged_user()
        qs=[post for post in posts if post["userId"]==userid]
        return qs


class PostCreateView():
    @login_required
    def post(self,*args,**kwargs):
        userId=loged_user()
        title=kwargs.get("title")
        body=kwargs.get("body")
        data={

             "userId":userId,
             "title":title,
             "body":body

        }
        posts.append(data)
        print("post created successfully")

class Postdetailsview():
    @login_required
    def get(self,*args,**kwargs):
     post_id=kwargs.get("post_id")
     qs=[p for p in posts if p.get("id")==post_id]
     return qs

    def put(self,id=None,*args,**kwargs):
     print(id)
     post=[p for p in posts if p.get("id")==id][0]
     title=kwargs.get("title")
     body=kwargs.get("body")
     post["title"]=title
     post["body"]=body
     print(post)





log=SigninView()
log.post(username="django",email="django@gmail.com")
pst=PostCreateView()
pst.post(title="mypost",body="this is my new post")
mp=MyPostView()
print(mp.get())
detail=Postdetailsview()
print(detail.get(post_id=10))
detail.put(id=10,title="my new post",body="this is my post")




