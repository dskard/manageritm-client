import pytest
import uuid

from deepdiff import DeepDiff
from manageritm_client import ManagerITMProxyClient, ManagerITMCommandClient


class TestClient:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self):
        self.base_uri = "https://localhost:5000"

    @pytest.fixture(scope="function")
    def client(self, requests_mock):
        self.client_id = str(uuid.uuid4())
        requests_mock.post(
            f"{self.base_uri}/client/proxy",
            status_code=200,
            json={"client_id": self.client_id},
        )
        # not sure why this mock doesn't prevent the
        # client's __del__() function from failing
        # requests_mock.get(
        #    f"{self.base_uri}/{self.client_id}/status",
        #    status_code=200,
        #    json={'status': None}
        # )
        client = ManagerITMProxyClient(self.base_uri)
        client.client()

        yield client

        client._client_id = None
        del client

    def test_proxy_client_default_ports(self, requests_mock):
        """user can create a proxy client without setting ports"""

        # setup expected data and mocks
        expected_request_data = {}
        expected_response_status = 200
        expected_response_data = {"client_id": str(uuid.uuid4())}
        mock = requests_mock.post(
            f"{self.base_uri}/client/proxy",
            status_code=expected_response_status,
            json=expected_response_data,
        )
        requests_mock.get(
            f"{self.base_uri}/{expected_response_data['client_id']}/status",
            status_code=200,
            json={"status": None},
        )

        # call the function under test
        client = ManagerITMProxyClient(self.base_uri)
        actual_response_data = client.client()

        # check that we sent the correct request to the server
        history = mock.request_history[0]
        assert history.method == "POST"
        assert DeepDiff(history.json(), expected_request_data) == {}

        # check that we return the correct data we get from the server
        assert actual_response_data == expected_response_data
        assert client._uri == self.base_uri
        assert client._client_id == expected_response_data["client_id"]

    def test_proxy_client_set_port(self, requests_mock):
        """user can create proxy client, setting port"""

        # setup expected data and mocks
        expected_request_data = {"port": 5200}
        expected_response_status = 200
        expected_response_data = {
            "client_id": str(uuid.uuid4()),
            "port": expected_request_data["port"],
            "webport": 5201,
        }
        mock = requests_mock.post(
            f"{self.base_uri}/client/proxy",
            status_code=expected_response_status,
            json=expected_response_data,
        )
        requests_mock.get(
            f"{self.base_uri}/{expected_response_data['client_id']}/status",
            status_code=200,
            json={"status": None},
        )

        # call the function under test
        client = ManagerITMProxyClient(self.base_uri)
        actual_response_data = client.client(port=expected_request_data["port"])

        # check that we sent the correct request to the server
        history = mock.request_history[0]
        assert history.method == "POST"
        assert DeepDiff(history.json(), expected_request_data) == {}

        # check that we return the correct data we get from the server
        assert actual_response_data == expected_response_data
        assert client._uri == self.base_uri
        assert client._client_id == expected_response_data["client_id"]

    def test_proxy_client_set_webport(self, requests_mock):
        """user can create proxy client, setting web port"""

        # setup expected data and mocks
        expected_request_data = {"webport": 5201}
        expected_response_status = 200
        expected_response_data = {
            "client_id": str(uuid.uuid4()),
            "port": 5200,
            "webport": expected_request_data["webport"],
        }
        mock = requests_mock.post(
            f"{self.base_uri}/client/proxy",
            status_code=expected_response_status,
            json=expected_response_data,
        )
        requests_mock.get(
            f"{self.base_uri}/{expected_response_data['client_id']}/status",
            status_code=200,
            json={"status": None},
        )

        # call the function under test
        client = ManagerITMProxyClient(self.base_uri)
        actual_response_data = client.client(webport=expected_request_data["webport"])

        # check that we sent the correct request to the server
        history = mock.request_history[0]
        assert history.method == "POST"
        assert DeepDiff(history.json(), expected_request_data) == {}

        # check that we return the correct data we get from the server
        assert actual_response_data == expected_response_data
        assert client._uri == self.base_uri
        assert client._client_id == expected_response_data["client_id"]

    def test_proxy_client_set_all_ports(self, requests_mock):
        """user can create proxy, sending port and webport"""

        # setup expected data and mocks
        expected_request_data = {"port": 5200, "webport": 5201}
        expected_response_status = 200
        expected_response_data = {
            "client_id": str(uuid.uuid4()),
            "port": expected_request_data["port"],
            "webport": expected_request_data["webport"],
        }
        mock = requests_mock.post(
            f"{self.base_uri}/client/proxy",
            status_code=expected_response_status,
            json=expected_response_data,
        )
        requests_mock.get(
            f"{self.base_uri}/{expected_response_data['client_id']}/status",
            status_code=200,
            json={"status": None},
        )

        # call the function under test
        client = ManagerITMProxyClient(self.base_uri)
        actual_response_data = client.client(
            port=expected_request_data["port"], webport=expected_request_data["webport"]
        )

        # check that we sent the correct request to the server
        history = mock.request_history[0]
        assert history.method == "POST"
        assert DeepDiff(history.json(), expected_request_data) == {}

        # check that we return the correct data we get from the server
        assert actual_response_data == expected_response_data
        assert client._uri == self.base_uri
        assert client._client_id == expected_response_data["client_id"]

    def test_command_client_default_environment(self, requests_mock):
        """user can create command client with the default environment"""

        # setup expected data and mocks
        expected_request_data = {}
        expected_status = 200
        expected_response_data = {"client_id": str(uuid.uuid4())}
        mock = requests_mock.post(
            f"{self.base_uri}/client/command",
            status_code=expected_status,
            json=expected_response_data,
        )
        requests_mock.get(
            f"{self.base_uri}/{expected_response_data['client_id']}/status",
            status_code=200,
            json={"status": None},
        )

        # call the function under test
        client = ManagerITMCommandClient(self.base_uri)
        actual_response_data = client.client()

        # check that we sent the correct request to the server
        history = mock.request_history[0]
        assert history.method == "POST"
        assert DeepDiff(history.json(), expected_request_data) == {}

        # check that we return the correct data we get from the server
        assert actual_response_data == expected_response_data
        assert client._uri == self.base_uri
        assert client._client_id == expected_response_data["client_id"]

    def test_command_client_set_env(self, requests_mock):
        """user can create command client with user specified environment"""

        # setup expected data and mocks
        expected_request_data = {"env": {"VARIABLE": "VALUE"}}
        expected_response_status = 200
        expected_response_data = {
            "client_id": str(uuid.uuid4()),
        }
        mock = requests_mock.post(
            f"{self.base_uri}/client/command",
            status_code=expected_response_status,
            json=expected_response_data,
        )
        requests_mock.get(
            f"{self.base_uri}/{expected_response_data['client_id']}/status",
            status_code=200,
            json={"status": None},
        )

        # call the function under test
        client = ManagerITMCommandClient(self.base_uri)
        actual_response_data = client.client(env=expected_request_data["env"])

        # check that we sent the correct request to the server
        history = mock.request_history[0]
        assert history.method == "POST"
        assert DeepDiff(history.json(), expected_request_data) == {}

        # check that we return the correct data we get from the server
        assert actual_response_data == expected_response_data
        assert client._uri == self.base_uri
        assert client._client_id == expected_response_data["client_id"]

    def test_command_client_set_additional_env(self, requests_mock):
        """user can create command client with user modified environment"""

        # setup expected data and mocks
        expected_request_data = {"additional_env": {"VARIABLE": "VALUE"}}
        expected_response_status = 200
        expected_response_data = {
            "client_id": str(uuid.uuid4()),
        }
        mock = requests_mock.post(
            f"{self.base_uri}/client/command",
            status_code=expected_response_status,
            json=expected_response_data,
        )
        requests_mock.get(
            f"{self.base_uri}/{expected_response_data['client_id']}/status",
            status_code=200,
            json={"status": None},
        )

        # call the function under test
        client = ManagerITMCommandClient(self.base_uri)
        actual_response_data = client.client(
            additional_env=expected_request_data["additional_env"]
        )

        # check that we sent the correct request
        history = mock.request_history[0]
        assert history.method == "POST"
        assert DeepDiff(history.json(), expected_request_data) == {}

        # check that we return the correct data we get from the server
        assert actual_response_data == expected_response_data
        assert client._uri == self.base_uri
        assert client._client_id == expected_response_data["client_id"]

    @pytest.mark.parametrize(
        "exit_status",
        [
            0,
            -1,
            1,
            None,
        ],
        ids=[
            "exited_successfully",
            "exited_with_error",
            "error_starting",
            "running",
        ],
    )
    def test_start(self, requests_mock, exit_status, client):
        """user can start a client's process"""

        # setup expected data and mocks
        expected_response_status = 200
        expected_response_data = {"status": exit_status}
        mock = requests_mock.post(
            f"{self.base_uri}/{self.client_id}/start",
            status_code=expected_response_status,
            json=expected_response_data,
        )

        # call the function under test
        actual_response_data = client.start()

        # check that we sent the correct request
        history = mock.request_history[0]
        assert history.method == "POST"

        # check that we return the correct data we get from the server
        assert actual_response_data == expected_response_data

    @pytest.mark.parametrize(
        "exit_status",
        [
            0,
            -1,
            1,
            None,
        ],
        ids=[
            "exited_successfully",
            "exited_with_error",
            "error_starting",
            "running",
        ],
    )
    def test_status(self, requests_mock, exit_status, client):
        """user can start get the status of a client's process"""

        # setup expected data and mocks
        expected_response_status = 200
        expected_response_data = {"status": exit_status}
        mock = requests_mock.get(
            f"{self.base_uri}/{self.client_id}/status",
            status_code=expected_response_status,
            json=expected_response_data,
        )

        # call the function under test
        actual_response_data = client.status()

        # check that we sent the correct request
        history = mock.request_history[0]
        assert history.method == "GET"

        # check that we return the correct data we get from the server
        assert actual_response_data == expected_response_data

    @pytest.mark.parametrize(
        "exit_status",
        [
            0,
            -1,
            1,
            None,
        ],
        ids=[
            "exited_successfully",
            "exited_with_error",
            "error_starting",
            "running",
        ],
    )
    def test_stop(self, requests_mock, exit_status, client):
        """user can start stop a client's process"""

        # setup expected data and mocks
        expected_response_status = 200
        expected_response_data = {"status": exit_status}
        mock = requests_mock.post(
            f"{self.base_uri}/{self.client_id}/stop",
            status_code=expected_response_status,
            json=expected_response_data,
        )

        # call the function under test
        actual_response_data = client.stop()

        # check that we sent the correct request
        history = mock.request_history[0]
        assert history.method == "POST"

        # check that we return the correct data we get from the server
        assert actual_response_data == expected_response_data
