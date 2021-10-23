#!/usr/bin/env python3

# Standard libraries.
from __future__ import annotations

# External dependencies.
import markdown


# Same as `markdown.Markdown`.
# Adds `Meta` attribute for typehint purposes.
class MarkdownStub(markdown.Markdown):
    # The `meta` extension creates `Meta` attribute.
    Meta: dict[str, list[str]]
    # The `references` attribute is not in typeshed.
    references: dict[str, tuple[str, str | None]]
