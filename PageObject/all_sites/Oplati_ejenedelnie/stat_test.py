# import test_OD
import test_CC
import test_LZ
import test_DF
import test_DFF
import test_LZLP

import unittest
from unittest import TestSuite
from unittest import TestResult

def load_tests (loader, tests, pattern):
    suite = TestSuite()
    for test_class in (test_OD, test_CC, test_LZ, test_DF, test_LZLP, test_DFF):
        tests = loader.loadTestsFromTestCase(test_class)
        suite.addTest(tests)

    return suite

if __name__ == '__main__':
    unittest.main()
