def test_working_directory(image):
    expected_value = "/app"

    actual_value = image.attrs["Config"]["WorkingDir"]
    assert actual_value == expected_value, (
        'Check that the Dockerfile has the working directory set as specified.'
    )


def test_cmd(image):
    expected_value = ['gunicorn', '--bind', '0.0.0.0:8080', 'simple_project.wsgi']

    actual_value = image.attrs["Config"]["Cmd"]
    assert actual_value == expected_value, (
        'Check that the command to run in the Dockerfile is set as specified.'
    )
