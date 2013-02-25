# -*- coding: utf-8 -*-

from django.contrib import admin

from mptt.admin import MPTTModelAdmin

from models import Page


class PageAdmin(MPTTModelAdmin):
    '''Page model admin settings.'''

    list_display = ('name', 'title', 'parent')
    list_filter = ('parent',)
    ordering = ('name',)
    search_fields = ('title',)


admin.site.register(Page, PageAdmin)
