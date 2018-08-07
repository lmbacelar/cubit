import pytest
from mixer.backend.django import mixer
pytestmark = pytest.mark.django_db

class TestMake:
    def test_creation(self):
        obj = mixer.blend('inventory.Make')
        assert obj.pk == 1, 'Should create a Make instance'

    def test_string_representation(self):
        obj = mixer.blend('inventory.Make', name='Agilent')
        assert str(obj) == 'Agilent', 'Should be represented by name'


class TestMakeModel:
    def test_creation(self):
        obj = mixer.blend('inventory.MakeModel', make__name='Agilent')
        assert obj.pk == 1, 'Should create a MakeModel instance'

    def test_string_representation(self):
        obj = mixer.blend('inventory.MakeModel', make__name='Agilent', model= '3458A')
        assert str(obj) == 'Agilent 3458A', 'Should be represented by make name and model'


class TestItem:
    def test_creation(self):
        obj = mixer.blend('inventory.Item', make_model__make__name='Agilent', make_model__model='3458A')
        assert obj.pk == 1, 'Should create a Item instance'

    def test_name_with_description(self):
        obj = mixer.blend('inventory.Item', make_model__make__name='Agilent',
                                            make_model__model='3458A',
                                            description='Dummy Item')
        assert obj.name == 'Dummy Item', 'Name should be item description when present'

    def test_name_without_description(self):
        obj = mixer.blend('inventory.Item', make_model__make__name='Agilent',
                                            make_model__model='3458A',
                                            make_model__name='Dummy Model',
                                            description='')
        assert obj.name == 'Dummy Model', 'Name should be model name when description not present'

    def test_absolute_url(self):
        obj = mixer.blend('inventory.Item')
        assert obj.get_absolute_url() == '/inventory/items/1/'

    def test_string_representation(self):
        obj = mixer.blend('inventory.Item', make_model__make__name='Agilent',
                                            make_model__model='3458A',
                                            reference='XPTO')
        assert str(obj) == 'XPTO: Agilent 3458A', 'Should be represented by reference: make_model'
