import pytest
import mock
import argparse

from pre_commit_hooks.regex import main

@mock.patch('argparse.ArgumentParser.parse_args', return_value=argparse.Namespace(
    critical='True',
    custom_message='We dont talk about this',
    filenames=['/file/one', '/file/two/'],
    pattern='(?:fight club)')
)
@mock.patch("builtins.print")
@mock.patch("builtins.open", new_callable=mock.mock_open, read_data=b"I like fight club")
def test_matching_a_critical_rule_twice(m_open, m_print, m_argparse):
    assert main(['test']) == 1

@mock.patch('argparse.ArgumentParser.parse_args', return_value=argparse.Namespace(
    critical=None,
    custom_message='He-Who-Must-Not-Be-Named',
    filenames=['/file/one'],
    pattern='(?:Voldemort)')
)
@mock.patch("builtins.print")
@mock.patch("builtins.open", new_callable=mock.mock_open, read_data=b"Tell me about Voldemort")
def test_matching_a_non_critical_rule(m_open, m_print, m_argparse):
    assert main(['arguments']) == 0

@mock.patch('argparse.ArgumentParser.parse_args', return_value=argparse.Namespace(
    critical='True',
    custom_message='You are not allowed to say that',
    filenames=['/file/one', '/file/two'],
    pattern='(?:the f word)')
)
@mock.patch("builtins.print")
@mock.patch("builtins.open", new_callable=mock.mock_open, read_data=b"Just a SFW sentence")
def test_non_matching_rule(m_open, m_print, m_argparse):
    assert main(['arguments']) == 0
