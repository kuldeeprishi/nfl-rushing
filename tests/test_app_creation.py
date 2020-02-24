# encoding: utf-8
# pylint: disable=missing-docstring
import pytest

from app import config_by_name, create_app


def test_create_app():
    try:
        create_app()
    except SystemExit:
        pass


@pytest.mark.parametrize("config_name", ["prod", "dev", "qa", "test"])
def test_create_app_passing_config_name(monkeypatch, config_name):
    if config_name == "prod":
        production_config = config_by_name[config_name]
        monkeypatch.setattr(production_config, "SECRET_KEY", "secret")
    create_app(config_name=config_name)


@pytest.mark.parametrize("config_name", ["prod", "dev", "qa", "test"])
def test_create_app_passing_FLASK_CONFIG_env(monkeypatch, config_name):
    monkeypatch.setenv("FLASK_CONFIG", config_name)
    if config_name == "production":
        production_config = config_by_name[config_name]
        monkeypatch.setattr(production_config, "SECRET_KEY", "secret")
    create_app()


def test_create_app_with_conflicting_config(monkeypatch):
    monkeypatch.setenv("ENV", "prod")
    with pytest.raises(AssertionError):
        create_app("development")


def test_create_app_with_non_existing_config():
    with pytest.raises(KeyError):
        create_app("non-existing-config")


def test_create_app_with_broken_import_config():
    config_by_name["broken-import-config"] = "broken-import-config"
    with pytest.raises(ImportError):
        create_app("broken-import-config")
    del config_by_name["broken-import-config"]
