#!/usr/bin/env python3

# Internal modules.
from pelican.plugins import (  # type: ignore[import]
    markdown_unrendered_metadata as markdown_plugin,
)
import pelican.settings  # type: ignore[import]


class TestRegister:
    def test_auto_detected_by_pelican_as_namespace_plugin(self) -> None:
        pelican_object = pelican.Pelican(
            pelican.settings.DEFAULT_CONFIG.copy()
        )
        assert markdown_plugin in pelican_object.plugins

    def test_pelican_detects_with_shortname(self) -> None:
        config = pelican.settings.DEFAULT_CONFIG.copy()
        config["PLUGINS"] = ["markdown_unrendered_metadata"]
        pelican_object = pelican.Pelican(config)
        assert markdown_plugin in pelican_object.plugins

    def test_pelican_detects_with_fullname(self) -> None:
        config = pelican.settings.DEFAULT_CONFIG.copy()
        config["PLUGINS"] = [markdown_plugin.__name__]
        pelican_object = pelican.Pelican(config)
        assert markdown_plugin in pelican_object.plugins
