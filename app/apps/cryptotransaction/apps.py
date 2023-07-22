from django.apps import AppConfig


class DemoConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "app.apps.cryptotransaction"

    def ready(self) -> None:
        # Without this import, admin panel will not include this app
        from app.apps.cryptotransaction.web import admin  # noqa: F401 (unused-import)
