import unittest

from amazon_test import AmazonHomeTests, AmazonSearchTests, AmazonItemTests

loader = unittest.TestLoader()
suite = unittest.TestSuite()

# add tests to the test suite
suite.addTests(loader.loadTestsFromModule(AmazonHomeTests))
suite.addTests(loader.loadTestsFromModule(AmazonSearchTests))
suite.addTests(loader.loadTestsFromModule(AmazonItemTests))

# initialize a runner, pass it your suite and run it
runner = unittest.TextTestRunner(verbosity=2)
result = runner.run(suite)
