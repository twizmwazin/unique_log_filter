import unittest
from logging import makeLogRecord

from unique_log_filter import UniqueLogFilter


class TestUniqueLogFilter(unittest.TestCase):
    def test_filter_unique_messages(self):
        log_filter = UniqueLogFilter()
        record1 = makeLogRecord({"msg": "Test message 1"})
        record2 = makeLogRecord({"msg": "Test message 2"})
        record3 = makeLogRecord({"msg": "Test message 1"})  # Duplicate message

        self.assertTrue(log_filter.filter(record1))  # First occurrence should pass
        self.assertTrue(log_filter.filter(record2))  # Different message should pass
        self.assertFalse(log_filter.filter(record3))  # Duplicate should be filtered out


if __name__ == "__main__":
    unittest.main()
