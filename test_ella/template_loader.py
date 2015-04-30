from unittest import TestCase

from django.template import TemplateDoesNotExist

from nose import tools


templates = {}


class GlobalMemTemplateLoader(object):
    is_usable = True

    def __init__(self, *args, **kwargs):
        pass

    def __call__(self, template_name, template_dirs=None):
        return self.load_template(template_name, template_dirs)

    def load_template(self, template_name, template_dirs=None):
        "Dummy template loader that returns templates from templates dictionary."
        try:
            return templates[template_name], template_name
        except KeyError as e:
            raise TemplateDoesNotExist(e)

    def load_template_source(self, template_name, template_dirs=None):
        return self.load_template(template_name, template_dirs)


class TestDummyTemplateLoader(TestCase):

    def tearDown(self):
        global templates
        templates = {}

    def test_simple(self):
        loader = GlobalMemTemplateLoader()
        templates['anything.html'] = 'Something'
        source, name = loader.load_template_source('anything.html')
        tools.assert_equals('anything.html', name)
        tools.assert_equals('Something', source)

    def test_empty(self):
        loader = GlobalMemTemplateLoader()
        tools.assert_raises(TemplateDoesNotExist, loader.load_template_source, 'anything.html')
