"""Shared configuration objects."""

from dataclasses import dataclass


@dataclass(frozen=True)
class AppConfig:
    page_title: str = "GitCamiloHub"
    page_icon: str = "🚀"
    layout: str = "wide"
    sidebar_state: str = "expanded"


class CatalogSingleton:
    """Singleton that exposes reusable catalog data for the UI."""

    _instance: "CatalogSingleton | None" = None

    def __new__(cls) -> "CatalogSingleton":
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._repos = [
                "mi-app-web",
                "api-rest",
                "microservicio-auth",
                "data-pipeline",
                "frontend-react",
            ]
            cls._instance._branches = [
                "main",
                "develop",
                "feature/nueva-ui",
                "hotfix/bug-99",
                "release/2.0",
            ]
        return cls._instance

    @property
    def repositories(self) -> list[str]:
        return list(self._repos)

    @property
    def branches(self) -> list[str]:
        return list(self._branches)
