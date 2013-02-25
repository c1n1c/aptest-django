# -*- coding: utf-8 -*-

from django.views.generic import *

from django.http import Http404

from forms import PageEditForm
from models import Page


__all__ = ('HomeView', 'PageView', 'PageAddView', 'PageEditView')


class HomeView(TemplateView):
    '''Home root view.'''

    template_name = 'home.html'


class PagePathMixin(object):
    '''Page views mixin for getting page from url path.'''

    context_object_name = 'page'
    queryset = Page.objects.root_nodes()

    RAISE_404 = False  # raise 404 error if page not exists

    def get_context_data(self, **kwargs):
        context = super(PagePathMixin, self).get_context_data(**kwargs)

        context.update(self.kwargs)

        return context

    def get_page_from_path(self):
        '''Get page instance by url path and store it in context.'''

        path = self.kwargs.get('path') or ''
        page = None

        for name in path.strip('/').split('/'):
            pages = page.children.all() if page else self.get_queryset()

            try:
                page = pages.get(name=name)
            except Page.DoesNotExist:
                if self.RAISE_404:
                    raise Http404(u'Страница "%s" не существует.' % name)
                else:
                    self.kwargs['page_not_exist'] = name
                    break

        self.kwargs[self.context_object_name] = page

        return page


class PageView(PagePathMixin, DetailView):
    '''Show page by url path.'''

    template_name = 'page.html'

    def get_object(self, queryset=None):
        return self.get_page_from_path()


class PageAddView(PagePathMixin, CreateView):
    '''Add new page as child for url path.'''

    form_class = PageEditForm
    template_name = 'page-add.html'

    def get_form_kwargs(self):
        kwargs = super(PageAddView, self).get_form_kwargs()

        kwargs['instance'] = Page(parent=self.get_page_from_path())

        return kwargs

    def get_initial(self):
        return {'name': self.request.GET.get('name', u'')}

    def get_success_url(self):
        return self.object.get_absolute_url()


class PageEditView(PagePathMixin, UpdateView):
    '''Edit existing page by url path.'''

    form_class = PageEditForm
    template_name = 'page-edit.html'

    def get_object(self, queryset=None):
        return self.get_page_from_path()

    def get_success_url(self):
        return self.object.get_absolute_url()
