# myapp/tests/test_models.py
import pytest
from leilao.models import MyModel

@pytest.mark.django_db
def test_my_model_creation():
    instance = MyModel.objects.create(name="test")
    assert instance.name == "test"
