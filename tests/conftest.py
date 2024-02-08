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
            f"Убедитесь, что вы собрали образ `{LOCAL_IMAGE_NAME}`"
        )


@pytest.fixture
def container(client):
    containers = client.containers.list(filters={"ancestor": LOCAL_IMAGE_NAME}, limit=1)  # берём самый последний контейнер
    if not containers:
        raise AssertionError(
            f"Убедитесь, что вы запустили контейнер из образа `{LOCAL_IMAGE_NAME}`"
        )

    return containers[0]


@pytest.fixture
def volume(client):
    try:
        volume = client.volumes.get(VOLUME_NAME)
        return volume
    except errors.NotFound:
        raise AssertionError(
            f"Убедитесь, что вы создали том `{VOLUME_NAME}`"
        )
