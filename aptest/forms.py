# -*- coding: utf-8 -*-

from django.forms import ModelForm

from django.conf import settings

from models import Page

import re


# tags converting rules for page content
CONTENT_DECODE_RULES = {
    re.compile(ur'\*\*((?:(?!\*\*).)*?)\*\*'): ur'<b>\1</b>',  # **[text]** -> <b>[text]</b>
    re.compile(ur'\\\\((?:(?!\\\\).)*?)\\\\'): ur'<i>\1</i>',  # \\[text]\\ -> <i>[text]</i>
    re.compile(ur'\(\( ?(/(?:%s)?) ((?:(?!\)\)).)*?) ?\)\)' % settings.PAGE_PATH_RE): ur'<a href="\1">\2</a>',  # (([url] [name])) -> <a href="[url]">[name]</a>
}
CONTENT_ENCODE_RULES = {
    re.compile(ur'<b>((?:(?!</b>).)*?)</b>'): ur'**\1**',  # <b>[text]</b> -> **[text]**
    re.compile(ur'<i>((?:(?!</i>).)*?)</i>'): ur'\\\\\1\\\\',  # <i>[text]</i> -> \\[text]\\
    re.compile(ur'<a href="(/(?:%s)?)">((?:(?!</a>).)*?)</a>' % settings.PAGE_PATH_RE): ur'((\1 \2))',  # <a href="[url]">[name]</a> -> (([url] [name]))
}


def decode_content_tags(content):
    '''Convert tags to html.'''

    for pattern, repl in CONTENT_DECODE_RULES.iteritems():
        content = re.sub(pattern, repl, content)

    return content

def encode_content_tags(content):
    '''Convert tags from html.'''

    for pattern, repl in CONTENT_ENCODE_RULES.iteritems():
        content = re.sub(pattern, repl, content)

    return content


class PageEditForm(ModelForm):
    '''Page add/edit form with content tags auto converting.'''

    class Meta:
        model = Page
        fields = ('name', 'title', 'content')

    def __init__(self, *args, **kwargs):
        initial = kwargs.setdefault('initial', {})
        instance = kwargs.get('instance')

        if instance:
            initial['content'] = encode_content_tags(instance.content)

        super(PageEditForm, self).__init__(*args, **kwargs)

    def clean_content(self):
        content = self.cleaned_data.get('content', u'')

        return decode_content_tags(content)
