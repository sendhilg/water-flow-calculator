import pytest

from water_flow.flow import Flow


@pytest.fixture(scope='session', autouse=True)
def flow(request):
    return Flow()
