from tempest.lib.common import rest_client

class BlazarDashboardClient(rest_client.RestClient):
    def __init__(self, auth_provider, service, region, **kwargs):
        super().__init__(auth_provider, service, region, **kwargs)