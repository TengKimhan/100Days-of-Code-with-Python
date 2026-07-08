class User:
    def __init__(self, user_id, username):
        # constructor
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0
        
    def follow(self, user):
        user.followers += 1
        self.following += 1
        
user1 = User(1, "kimhan")
user2 = User(2, "Jack")
user1.follow(user2)

print(f"User 1 followers expect 0: {user1.followers}")
print(f"User 1 following expect 1: {user1.following}")
print(f"User 2 followers expect 1: {user2.followers}")
print(f"User 2 following expect 0: {user2.following}")