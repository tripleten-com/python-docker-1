def test_bind_volume(container, volume):
    binds: list[str] = container.attrs["HostConfig"]["Binds"]
    if not binds:
        raise AssertionError(
            "Make sure that a volume is specified for the container with the application."
        )

    assert any(bind.startswith(volume.name) for bind in binds), (
        f"Make sure the `{volume.name}` volume is linked to the container with the application."
    )


def test_ports(container, volume):
    expected_internal_port = "8080/tcp"

    port_bindings: dict[str, list] = container.attrs["HostConfig"]["PortBindings"]
    if expected_internal_port not in port_bindings:
        raise AssertionError(
            "Make sure that an internal port is specified for the container with the application correctly."
        )

    expected_external_port = "8080"
    actual_external_port = port_bindings[expected_internal_port][0]["HostPort"]

    assert actual_external_port == expected_external_port, (
        "Make sure that an external port is specified for the container with the application correctly."
    )


def test_required_env(container):
    expected_value = "DJANGO_SECRET_KEY"

    env_variables: list[str] = container.attrs["Config"]["Env"]
    assert any(env.startswith(expected_value) for env in env_variables), (
        f"Make sure the `{expected_value}` environment variable is specified with no default value "
        f"when starting the container."
    )
