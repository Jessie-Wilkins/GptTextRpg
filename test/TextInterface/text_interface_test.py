from unittest import mock
import pytest
from GptTextRpg.TextInterface.text_interface import TextInterface

def test_render_text_will_render_string_input_without_formatting():
    interface_render = TextInterface()

    rendered_text = interface_render.RenderText("This is text rendered in a particular format")

    assert rendered_text == "This is text rendered in a particular format"

def test_render_text_will_render_multi_line_text():
    interface_render = TextInterface()
    rendered_text = interface_render.RenderText("This is text rendered in a particular format", "And so is this one")
    assert rendered_text == "This is text rendered in a particular format\nAnd so is this one"

def test_user_input_will_accept_user_input():
    with mock.patch('builtins.input', return_value='walk forward'):

        interface_render = TextInterface()
        user_input = interface_render.UserInput()

        assert user_input == 'walk forward'

