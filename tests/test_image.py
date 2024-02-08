def test_working_directory(image):
    expected_value = "/app"

    actual_value = image.attrs["Config"]["WorkingDir"]
    assert actual_value == expected_value, (
        'Проверьте, что в Dockerfile рабочая директория установлена согласно заданию.'
    )


def test_cmd(image):
    expected_value = ['gunicorn', '--bind', '0.0.0.0:8080', 'simple_project.wsgi']

    actual_value = image.attrs["Config"]["Cmd"]
    assert actual_value == expected_value, (
        'Проверьте, что в Dockerfile команда для запуска установлена согласно заданию.'
    )
