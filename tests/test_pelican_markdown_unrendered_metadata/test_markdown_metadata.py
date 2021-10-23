#!/usr/bin/env python3

# Internal modules.
from test_pelican_markdown_unrendered_metadata.phill.markdown import (
    MarkdownStub,
)
from pelican_markdown_unrendered_metadata import markdown_metadata


class TestExtension:
    def test_accepted_by_markdown(self) -> None:
        MarkdownStub(extensions=[markdown_metadata.Extension()])

    def test_reset_sets_meta_to_new_dict(self) -> None:
        md = MarkdownStub(extensions=[markdown_metadata.Extension()])
        md.reset()
        assert md.Meta == {}
