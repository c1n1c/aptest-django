# -*- coding: utf-8 -*-

from django.template import Library

from aptest.models import Page


register = Library()


@register.inclusion_tag('page-tree.html')
def page_tree(page=None):
    '''Render pages subtree for given page or all pages tree.'''

    context = {
        'pages': page.get_descendants() if page else Page.objects.all()
    }

    return context
