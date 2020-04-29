from django import forms
from django.forms.formsets import formset_factory
from django.test import TestCase

from ..templatetags import admin2_tags
from ..views import IndexView
from .models import TagsTestsModel


class TagsTestForm(forms.Form):
    visible_1 = forms.CharField()
    visible_2 = forms.CharField()
    invisible_1 = forms.HiddenInput()


TagsTestFormSet = formset_factory(TagsTestForm)


class TagsTests(TestCase):

    def setUp(self):
        self.instance = TagsTestsModel()

    def test_admin2_urlname(self):
        self.assertEqual(
            "admin2:None_None_index",
            admin2_tags.admin2_urlname(IndexView, "index")
        )

    def test_model_verbose_name_as_model_class(self):
        self.assertEqual(
            TagsTestsModel._meta.verbose_name,
            admin2_tags.model_verbose_name(TagsTestsModel)
        )

    def test_model_verbose_name_as_model_instance(self):
        self.assertEqual(
            self.instance._meta.verbose_name,
            admin2_tags.model_verbose_name(self.instance)
        )

    def test_model_verbose_name_plural_as_model_class(self):
        self.assertEqual(
            TagsTestsModel._meta.verbose_name_plural,
            admin2_tags.model_verbose_name_plural(TagsTestsModel)
        )

    def test_model_verbose_name_plural_as_model_instance(self):
        self.assertEqual(
            self.instance._meta.verbose_name_plural,
            admin2_tags.model_verbose_name_plural(self.instance)
        )

    def test_model_field_verbose_name_autogenerated(self):
        self.assertEqual(
            'field1',
            admin2_tags.model_attr_verbose_name(self.instance, 'field1')
        )

    def test_model_field_verbose_name_overridden(self):
        self.assertEqual(
            'second field',
            admin2_tags.model_attr_verbose_name(self.instance, 'field2')
        )

    def test_model_method_verbose_name(self):
        self.assertEqual(
            'Published recently?',
            admin2_tags.model_attr_verbose_name(self.instance, 'was_published_recently')
        )

    def test_formset_visible_fieldlist(self):
        formset = TagsTestFormSet()
        self.assertEqual(
            admin2_tags.formset_visible_fieldlist(formset),
            [u'Visible 1', u'Visible 2']
        )

    def test_verbose_name_for(self):
        app_verbose_names = {
            u'app_one_label': 'App One Verbose Name',
        }
        self.assertEqual(
            "App One Verbose Name",
            admin2_tags.verbose_name_for(app_verbose_names, 'app_one_label')
        )