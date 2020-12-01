# import test_alabama
# import test_alaska
# import test_alberta
# import test_arkansas
# import test_britishcolumbia
# import test_california
# import test_colorado
# import test_connecticut
# import test_delawere
# import test_florida
# import test_georgia
# import test_hawaii
# import test_idaho
# import test_illinois
# import test_indiana
# import test_iowa
# import test_kansas
# import test_kentucky
# import test_louisiana
# import test_maine
# import test_manitoba
# import test_maryland
# import test_massachusetts
# import test_michigan
# import test_minnesota
# import test_mississippi
# import test_missouri
# import test_montana
# import test_rhodeisland
# import test_nebraska
# import test_nevada
# import test_newbrunswick
# import test_newhampshire
# import test_newjersey
# import test_newmexico
# import test_newyork
# import test_northcarolina
# import test_northdakota
# import test_ohio
# import test_oklohoma
# import test_ontario
# import voronka_rs #arizona
# import test_oregon
# import test_pennsylvania
# import test_southcarolina
# import test_southdakota
# import test_tennessee
import test_texas
# import test_utah
# import test_vermont
# import test_virginia
# import test_washington
# import test_washingtondc
# import test_westvirginia
# import test_wisconsin
# import test_wyoming


import unittest
from unittest import TestSuite

def load_tests (loader, tests, pattern):
    suite = TestSuite()
    for test_class in (test_alabama, test_alaska, test_arkansas, test_alberta, test_britishcolumbia,
                       test_california, test_colorado, test_connecticut, test_delawere, test_florida, test_georgia,
                       test_hawaii,
                       test_idaho, test_illinois, test_indiana, test_iowa, test_kansas,
                       test_kentucky,
                       test_louisiana, test_manitoba, test_maryland, test_maine, test_massachusetts,
                       test_michigan, test_minnesota, test_mississippi, test_missouri,
                       test_montana, test_rhodeisland, test_nebraska, test_nevada, test_newbrunswick,
                       test_newhampshire, test_newjersey,
                       test_newmexico, test_newyork, test_northcarolina, test_northdakota,
                       test_ohio, test_oklohoma, test_ontario, test_oregon, test_pennsylvania, test_southcarolina,
                       test_southdakota, test_tennessee, test_texas,
                       test_utah, test_vermont,
                       test_virginia, test_washington, test_washingtondc, test_westvirginia, test_wisconsin,
                       test_wyoming, voronka_rs):
        tests = loader.loadTestsFromTestCase(test_class)
        suite.addTest(tests)

    return suite


unittest.main()
