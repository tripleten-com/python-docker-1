def test_environment_variables_are_used(settings):
    expected_value = "django-insecure-j_89af+30&&4qm*8z9_(^zz8p4-ho8z_m6ylm0s$h!-p@on1_^"
    assert settings.SECRET_KEY == expected_value, (
        "Убедитесь, что в `simple_project/settings.py` значение переменной `SECRET_KEY` "
        "настраивается с помощью переменной окружения"
    )
