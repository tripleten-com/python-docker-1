def test_bind_volume(container, volume):
    binds: list[str] = container.attrs["HostConfig"]["Binds"]
    if not binds:
        raise AssertionError(
            "Убедитесь, что для контейнера с приложением, указан том."
        )

    assert any(bind.startswith(volume.name) for bind in binds), (
        f"Убедитесь, что к контейнеру с приложением, привязан том `{volume.name}`."
    )


def test_ports(container, volume):
    expected_internal_port = "8080/tcp"

    port_bindings: dict[str, list] = container.attrs["HostConfig"]["PortBindings"]
    if expected_internal_port not in port_bindings:
        raise AssertionError(
            "Убедитесь, что для контейнера с приложением верно указан внутренний порт."
        )

    expected_external_port = "8080"
    actual_external_port = port_bindings[expected_internal_port][0]["HostPort"]

    assert actual_external_port == expected_external_port, (
        "Убедитесь, что для контейнера с приложением верно указан внешний порт."
    )


def test_required_env(container):
    expected_value = "DJANGO_SECRET_KEY"

    env_variables: list[str] = container.attrs["Config"]["Env"]
    assert any(env.startswith(expected_value) for env in env_variables), (
        f"Убедитесь, что при запуске контейнера указана переменная окружения `{expected_value}` "
        f"без значения по умолчанию."
    )
