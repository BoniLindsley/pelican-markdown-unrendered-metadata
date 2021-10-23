#!/usr/bin/env python3

# Standard libraries.
import typing

# Internal modules.
import test_pelican_markdown_unrendered_metadata.phill.markdown
from pelican_markdown_unrendered_metadata import (
    markdown_metadata_in_heading as extension_module,
)


class MarkdownStub(
    test_pelican_markdown_unrendered_metadata.phill.markdown.MarkdownStub
):
    def __init__(self, *args: typing.Any, **kwargs: typing.Any) -> None:
        kwargs.setdefault("extensions", [extension_module.Extension()])
        super().__init__(*args, **kwargs)


class TestHeadingMetaProcessor:
    def test_run_removes_h1_and_set_title(self) -> None:
        md = MarkdownStub()
        output = md.convert("# Hello, world!")
        assert output == ""
        assert md.Meta == {"title": ["Hello, world!"]}

    def test_run_ignores_other_h1(self) -> None:
        md = MarkdownStub()
        output = md.convert("# Hello, world!\n# Hi!")
        assert output == "<h1>Hi!</h1>"
        assert md.Meta == {"title": ["Hello, world!"]}

    def test_run_ignores_h1_if_not_at_start(self) -> None:
        md = MarkdownStub()
        output = md.convert("Hello, world!\n# Hi!")
        assert output == "<p>Hello, world!</p>\n<h1>Hi!</h1>"
        assert md.Meta == {}

    def test_run_ignores_other_headings(self) -> None:
        md = MarkdownStub()
        output = md.convert("## Hi!")
        assert output == "<h2>Hi!</h2>"
        assert md.Meta == {}

    def test_run_ignores_other_metadata(self) -> None:
        md = MarkdownStub()
        md.Meta = {"footnote": ["Goodbye, world!"]}
        output = md.convert("# Hello, world!")
        assert output == ""
        assert md.Meta == {
            "footnote": ["Goodbye, world!"],
            "title": ["Hello, world!"],
        }

    def test_run_ignores_empty_tree(self) -> None:
        md = MarkdownStub()
        output = md.convert("")
        assert output == ""
        assert md.Meta == {}


class TestExtension:
    def test_registers_processor(self) -> None:
        md = MarkdownStub()
        treeprocessors = list(md.treeprocessors)
        assert any(
            isinstance(processor, extension_module.HeadingMetaProcessor)
            for processor in treeprocessors
        ), treeprocessors


def test_make_extension_detected_by_markdown() -> None:
    MarkdownStub(extensions=[extension_module.__name__])
