import os

from tempest import config
from tempest.test_discover import plugins


class ChiTempestPlugin(plugins.TempestPlugin):
    def load_tests(self):
        base_path = os.path.split(os.path.dirname(os.path.abspath(__file__)))[0]
        test_dir = "chi_tempest_plugin/tests"
        full_test_dir = os.path.join(base_path, test_dir)
        return full_test_dir, base_path

    def register_opts(self, conf):
        pass

    def get_opt_lists(self):
        pass

    def get_service_clients(self):
        blazar_dashboard_config = config.service_client_config("blazardashboard")
        params_blazar_dashboard = {
            "name": "blazar_dashboard_extra",
            "service_version": "blazar_dashboard.v1",
            "module_path": "chi_tempest_plugin.services.blazardashboardclient",
            "client_names": [
                "BlazarDashboardClient",
            ],
        }
        params_blazar_dashboard.update(blazar_dashboard_config)
        return [
            params_blazar_dashboard,
        ]
