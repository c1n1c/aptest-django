# -*- coding: utf-8 -*-

from django.utils import unittest


class ContentTagsTest(unittest.TestCase):
    '''Test for page content tags converting.'''

    def test_decode_tags(self):
        from aptest.forms import decode_content_tags

        # bold tag
        self.assertEqual(decode_content_tags('****'), '<b></b>')
        self.assertEqual(decode_content_tags('********'), '<b></b><b></b>')
        self.assertEqual(decode_content_tags('**text1**'), '<b>text1</b>')

        # italic tag
        self.assertEqual(decode_content_tags(r'\\\\'), '<i></i>')
        self.assertEqual(decode_content_tags(r'\\\\\\\\'), '<i></i><i></i>')
        self.assertEqual(decode_content_tags(r'\\text1\\'), '<i>text1</i>')

        # href tag
        self.assertEqual(decode_content_tags('((/ ))'), '<a href="/"></a>')
        self.assertEqual(decode_content_tags('(( / 1 ))'), '<a href="/">1</a>')
        self.assertEqual(decode_content_tags('((/url1/ name1))'), '<a href="/url1/">name1</a>')

        # mix tags
        self.assertEqual(decode_content_tags(r'**\\((/ 1))\\**'), '<b><i><a href="/">1</a></i></b>')

    def test_encode_tags(self):
        from aptest.forms import encode_content_tags

        # bold tag
        self.assertEqual(encode_content_tags('<b>1</b>'), '**1**')
        self.assertEqual(encode_content_tags('<b></b><b></b>'), '********')
        self.assertEqual(encode_content_tags('<b><></b>'), '**<>**')

        # italic tag
        self.assertEqual(encode_content_tags('<i>1</i>'), r'\\1\\')
        self.assertEqual(encode_content_tags('<i></i><i></i>'), r'\\\\\\\\')
        self.assertEqual(encode_content_tags('<i><></i>'), r'\\<>\\')

        # href tag
        self.assertEqual(encode_content_tags('<a href="/">1</a>'), '((/ 1))')
        self.assertEqual(encode_content_tags('<a href="/"></a><a href="/"></a>'), '((/ ))((/ ))')
        self.assertEqual(encode_content_tags('<a href="/url1/">name1</a>'), '((/url1/ name1))')

        # mix tags
        self.assertEqual(encode_content_tags('<b><i><a href="/">1</a></i></b>'), r'**\\((/ 1))\\**')
