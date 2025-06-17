import logging
from utils.logger import get_logger

LOGGER = get_logger(__name__, logging.DEBUG)

class TestExampleFixture:

        # @classmethod
        # def setup_class(cls):
        #     """
        #     Setup class
        #     :return:
        #     """
        #     # arrange (Initial Data)
        #     API_KEY = "30733d7aefa87b3bd3752797f6b378cb6de16720"
        #     LOGGER.info('Setup class')
        #     cls.header_API = {
        #         "Authorization": "Bearer {}".format(API_KEY),
        #     }
        #     LOGGER.debug("HEADER API: %s", cls.header_API)

        def setup_method(self):
            pass
            # act (test)
            # LOGGER.info('1er Test: %s', self.header_API)
            # # assert (validation)
            # assert self.header_API

        def test_one(self):
            pass
            #LOGGER.info('Test one')

        def test_two(self):
            pass
            #LOGGER.info('Test two')

        def test_three(self):
            LOGGER.info('Test three')

        def teardown_method(self):
            LOGGER.info('Teardown method')

        # @classmethod
        # def teardown_class(cls):
        #     LOGGER.info('Teardown class')