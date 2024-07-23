from tempest import test
from oslo_log import log as logging
from tempest import config

LOG = logging.getLogger(__name__)
CONF = config.CONF

class TestBlazarDashboard(test.BaseTestCase):


    # project/leases/computehost/extras.json
    # project/leases/network/extras.json
    
    def test_host_extra_properties(self):
        pass
    
    def test_network_extra_properties(self):
        pass        