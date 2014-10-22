import posting

posting.post_blog(1, "blog1")
posting.post_blog(2, "blog2")
posting.post_blog(3, "blog3")
posting.post_blog(4, "blog4")

posting.post_comment(1, "com1", "hello")
posting.post_comment(1, "com2", "goodbye")
posting.post_comment(2, "com1", "this is cool")
posting.post_comment(3, "com1", "yay databases")
posting.post_comment(4, "com1", "bacon avocado chipotle on a roll")

print posting.get_blog(1)
print posting.get_blog(1)
print posting.get_blog(1)
print posting.get_blog(1)

print posting.get_comment(1)
print posting.get_comment(2)
print posting.get_comment(3)
print posting.get_comment(4)
