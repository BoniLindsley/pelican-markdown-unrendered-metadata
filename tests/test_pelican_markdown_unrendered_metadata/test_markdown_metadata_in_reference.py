#!/usr/bin/env python3

# Standard libraries.
from __future__ import annotations
import typing

# External dependencies.
import markdown

# Internal modules.
import test_pelican_markdown_unrendered_metadata.phill.markdown
from pelican_markdown_unrendered_metadata import (
    markdown_metadata_in_reference as extension_module,
)


class MarkdownStub(
    test_pelican_markdown_unrendered_metadata.phill.markdown.MarkdownStub
):
    def __init__(self, *args: typing.Any, **kwargs: typing.Any) -> None:
        kwargs.setdefault("extensions", [extension_module.Extension()])
        super().__init__(*args, **kwargs)


class TestIsMetaReference:
    def test_true_for_prefix_in_key_and_hash_with_value_in_value(
        self,
    ) -> None:
        assert extension_module.is_meta_reference(
            "abc", ("#", "two"), "ab"
        )

    def test_false_for_non_prefix_key(self) -> None:
        assert not extension_module.is_meta_reference(
            "Hi", ("#", "#"), "Hello"
        )

    def test_false_for_prefix_key_as_key(self) -> None:
        assert not extension_module.is_meta_reference(
            "Hi", ("#", "#"), "Hi"
        )

    def test_false_for_non_hash_url(self) -> None:
        assert not extension_module.is_meta_reference(
            "Hi", ("?", "#"), "H"
        )

    def test_false_for_reference_without_title(self) -> None:
        assert not extension_module.is_meta_reference(
            "Hi", ("?", None), "H"
        )


class TestReferenceMetaProcessor:
    def test_run_moves_prefix_references_to_meta(self) -> None:
        md = MarkdownStub()
        output = md.convert("[//pelican/title]: # (Hello, world!)")
        assert output == ""
        assert md.references == {}
        assert md.Meta == {"title": ["Hello, world!"]}

    def test_run_uses_case_insensitive_keys(self) -> None:
        md = MarkdownStub()
        md.convert("[//PeLiCaN/TiTlE]: # (Hello, world!)")
        assert md.Meta == {"title": ["Hello, world!"]}

    def test_run_ignores_empty_references(self) -> None:
        md = MarkdownStub()
        output = md.convert("[//pelican/]:")
        assert output == "<p>[//pelican/]:</p>"
        assert md.references == {}
        assert md.Meta == {}


class TestExtension:
    def test_registers_processor(self) -> None:
        md = MarkdownStub()
        postprocessors = list(md.postprocessors)
        assert any(
            isinstance(
                processor, extension_module.ReferenceMetaProcessor
            )
            for processor in postprocessors
        ), postprocessors


def test_make_extension_detected_by_markdown() -> None:
    MarkdownStub(extensions=[extension_module.__name__])
