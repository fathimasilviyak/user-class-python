# A class with no data
# class User:
#     pass
#
# initialize attribute values separately for each object
# user_1 = User()
# user_1.id = "001"
# user_1.username = "Anu"
#
# user_2 = User()
# user_2.id = "002"
# user_2.username = "Rani"
#
# print(user_1.username)

# initialize attribute values using constructor
class User:
    def __init__(self, id, username):
        self.user_id = id
        self.use_name = username
        self.followers = 0
        self.following = 0

    def change_id(self):
        self.user_id += "user"
        return self.user_id

    def follow(self, user):
        user.followers += 1
        self.following += 1


user_1 = User("001", "Asin")
user_2 = User("002", "Amrin")

# print(user_1.user_id)
# print(user_2.use_name)
# print(user_1.followers)
#
# print(user_1.change_id())

user_1.follow(user_2)
print(f"User_1 followers: {user_1.followers}")
print(f"User_1 following: {user_1.following}")
print(f"User_2 followers: {user_2.followers}")
print(f"User_2 following: {user_2.following}")