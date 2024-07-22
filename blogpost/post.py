class Post:
    def __init__(self,post) -> None:
        self.id = post["id"]
        self.body = post["body"]
        self.date = post["date"]
        self.image = post["image"]
        self.title = post["title"]
        self.author = post["author"]
        self.subtitle = post["subtitle"]
