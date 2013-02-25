# -*- coding: utf-8 -*-

from django.db.models import *

from django.conf import settings
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator

from mptt.models import MPTTModel, TreeForeignKey


class Page(MPTTModel):
    '''Page model with mptt-tree implementation.'''

    name = CharField(max_length=50, verbose_name=u'Имя', validators=[
        RegexValidator(settings.PAGE_NAME_RE, u'Имя страницы содержит недопустимые символы.'),
    ])

    title = CharField(max_length=50, verbose_name=u'Название')
    content = TextField(verbose_name=u'Текст', blank=True)

    parent = TreeForeignKey('self', blank=True, null=True, related_name='children', verbose_name=u'Родитель')

    class Meta:
        unique_together = ('parent', 'name')
        verbose_name = u'Страница'
        verbose_name_plural = u'Страницы'

    class MPTTMeta:
        order_insertion_by = ('name',)

    def __unicode__(self):
        return u'%s' % self.name

    def get_absolute_url(self):
        '''Build page absolute url.'''

        parent_url = self.parent.get_absolute_url() if self.parent else '/'

        return '%s%s/' % (parent_url, self.name)

    def validate_unique(self, exclude=None):
        '''Validate page name unique for one parent.'''

        if Page.objects.exclude(pk=self.pk).filter(parent=self.parent, name=self.name).exists():
            raise ValidationError({'name': [u'Страница с таким именем уже существует.']})

        super(Page, self).validate_unique(exclude)
