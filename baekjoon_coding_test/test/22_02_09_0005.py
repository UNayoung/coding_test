class Friend:
    def __init__(self, email):
        self.email = email
        self.friends = []

    def add_friendship(self, friend):
        self.friends.append(friend)
        friend.friends.append(self)

    def can_be_connected(self, friend):
        answer = False
        def search(search_class):
            for i in search_class.friends:
                if i.email == friend.email:
                    answer = True
                    return
                search(i)
        search(self)
        return answer


if __name__ == "__main__":
    a = Friend("A")
    b = Friend("B")
    c = Friend("C")

    a.add_friendship(b)
    b.add_friendship(c)

    print(a.can_be_connected(c))