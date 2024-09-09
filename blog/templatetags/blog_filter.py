import markdown
from django import template
from django.utils.safestring import mark_safe
from pygments.formatters import HtmlFormatter
from markdown.extensions.codehilite import CodeHiliteExtension

register = template.Library()


@register.filter
def sub(value, arg):
    return value - arg

@register.filter
def tags_to_string(tags):
    if tags:
        return ' '.join(f'#{tag.name}' for tag in tags)
    return ''

@register.filter
def mark(value):
    #extensions = ["nl2br", "fenced_code", "codehilite", "tables", "sane_lists", "toc", "def_list", "attr_list"]
    #extensions = ["nl2br","fenced_code"]#, CodeHiliteExtension(pygments_formatter=CustomHtmlFormatter)]
    extensions = ["nl2br", "fenced_code"]
    #extensions = [CodeHiliteExtension(pygments_formatter=CustomHtmlFormatter)]
    #result = markdown.markdown(value, extensions=extensions)
    result = markdown.markdown(value, extensions=extensions)
    result = mark_safe(result)
    return result


class CustomHtmlFormatter(HtmlFormatter):
    def __init__(self, lang_str='', **options):
        super().__init__(**options)
        # lang_str has the value {lang_prefix}{lang}
        # specified by the CodeHilite's options
        self.lang_str = lang_str

    def _wrap_code(self, source):
        yield 0, f'<code class="{self.lang_str}">'
        yield from source
        yield 0, '</code>'
