from tempest import test
from oslo_log import log as logging
from tempest import config

LOG = logging.getLogger(__name__)
CONF = config.CONF

class TestBlazar(test.BaseTestCase):

    def test_enforcement_url(self):
        """ Test blazar call to portal for usage enforcement.
        
        Blazar calls out to portal for enforcement checks. Portal whitelists
        certain auth_urls. Check that request is sent with the correct headers.     
        """
        pass

    def test_lease_email(self):
        pass
    