from tempest import test


class TestExampleCase(test.BaseTestCase):
    def test_example_create_server(self):
        credentials = self.os_primary.credentials
        username = credentials.username
        user_id = credentials.user_id
        password = credentials.password
        tenant_id = credentials.tenant_id