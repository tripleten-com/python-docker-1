import pytest
import docker

from docker import errors

LOCAL_IMAGE_NAME = "simple_django"
VOLUME_NAME = "simple_django_volume"


@pytest.fixture
def client():
    client = docker.from_env()
    return client


@pytest.fixture
def image(client):
    try:
        image = client.images.get(LOCAL_IMAGE_NAME)
        return image
    except errors.ImageNotFound:
        raise AssertionError(
            f"Make sure you've built the ` {LOCAL_IMAGE_NAME}` image"
        )


@pytest.fixture
def container(client):
    containers = client.containers.list(filters={"ancestor": LOCAL_IMAGE_NAME}, limit=1)  # take the very last container
    if not containers:
        raise AssertionError(
            f"Make sure you are running the container from the ` {LOCAL_IMAGE_NAME}` image"
        )

    return containers[0]


@pytest.fixture
def volume(client):
    try:
        volume = client.volumes.get(VOLUME_NAME)
        return volume
    except errors.NotFound:
        raise AssertionError(
            f"Make sure you've created the ` {VOLUME_NAME}` volume"
        )
