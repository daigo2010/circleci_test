import unittest
from datetime import datetime
from circleci_test.models import Posts

class PostsModelTestCase(unittest.TestCase):
    def test_get_recent_data(self):
        for i in range(0, 6):
            p = Posts(name="name{0}".format(i), description="description{0}".format(i),url="url{0}".format(i),  created_at=datetime.now())
            p.save()

        posts = Posts.objects.get_recent_data()

        self.assertEquals(len(posts), 5)
        self.assertEquals(posts[0].name, "name5")
        self.assertEquals(posts[1].name, "name4")
        self.assertEquals(posts[2].name, "name3")
        self.assertEquals(posts[3].name, "name2")
        self.assertEquals(posts[4].name, "name1")
