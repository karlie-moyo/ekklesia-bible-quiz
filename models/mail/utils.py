#!/usr/bin/env python3
"""mailsender utility function's module"""
from jinja2 import Template
from jinja2.exceptions import TemplateSyntaxError, TemplateAssertionError


def render_template(body, **kwargs) -> str:
    """Uses Jinja2 to merge data to html template"""
    try:
        result = Template(body).render(**kwargs)
    except TemplateSyntaxError as exc:
        raise SyntaxError(str(exc))
    except TemplateAssertionError as exc:
        raise SyntaxError(str(exc))

    return result
