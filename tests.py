import unittest
import feedparser
import re

class Test(unittest.TestCase):

    def setUp(self):
        self.good_feed = 'http://feeds.gawker.com/lifehacker/full'
        self.missing_feed = 'http://missing.example.com'

    def test_live_feed(self):
        f = feedparser.parse(self.good_feed)

        self.assertEquals(0, f['bozo'])

    def test_missing_feed(self):
        f = feedparser.parse(self.missing_feed)

        self.assertEquals(1, f['bozo'])
        self.assertTrue('bozo_exception' in f)
        self.assertRegexpMatches(
            str(f['bozo_exception']),
            r'^.+?Name or service not known',
        )


if __name__ == '__main__':
    unittest.main()
