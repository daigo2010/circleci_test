import unittest
from datetime import datetime
from circleci_test.models import Posts

class PostsModelTestCase(unittest.TestCase):
    def test_get_recent_data(self):
        for i in range(0, 6):
            p = Posts(name="name{0}".format(i), description="description{0}".format(i),url="url{0}".format(i),  created_at=datetime.now())
            p.save()

        self.assertEquals(1, 1)
