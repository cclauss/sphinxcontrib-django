import pytest

try:
    from phonenumber_field.modelfields import PhoneNumberField  # noqa: F401

    PHONENUMBER = True
except ModuleNotFoundError:
    # In case phonenumber is not used, pass
    PHONENUMBER = False


@pytest.mark.sphinx("html", testroot="docstrings")
def test_model_field(app, do_autodoc):
    actual = do_autodoc(
        app, "attribute", "dummy_django_app.models.SimpleModel.dummy_field"
    )
    print(actual)
    assert actual == [
        "",
        ".. py:attribute:: SimpleModel.dummy_field",
        "   :module: dummy_django_app.models",
        "",
        "   Type: :class:`~django.db.models.CharField`",
        "",
        "   Very verbose name of dummy field. This should help you",
        "",
    ]


@pytest.mark.sphinx("html", testroot="docstrings")
def test_foreignkey(app, do_autodoc):
    actual = do_autodoc(app, "attribute", "dummy_django_app.models.SimpleModel.file")
    print(actual)
    assert actual == [
        "",
        ".. py:attribute:: SimpleModel.file",
        "   :module: dummy_django_app.models",
        "",
        "   Type: :class:`~django.db.models.ForeignKey` to "
        ":class:`~dummy_django_app.models.FileModel`",
        "",
        "   File (related name: :attr:`~dummy_django_app.models.FileModel.simple_models`)",
        "",
    ]


@pytest.mark.sphinx("html", testroot="docstrings")
def test_foreignkey_id(app, do_autodoc):
    actual = do_autodoc(app, "attribute", "dummy_django_app.models.SimpleModel.file_id")
    print(actual)
    assert actual == [
        "",
        ".. py:attribute:: SimpleModel.file_id",
        "   :module: dummy_django_app.models",
        "",
        "   Internal field, use :class:`~dummy_django_app.models.SimpleModel.file` instead.",
        "",
    ]


@pytest.mark.sphinx("html", testroot="docstrings")
def test_foreignkey_string(app, do_autodoc):
    actual = do_autodoc(
        app,
        "attribute",
        "dummy_django_app.models.AbstractModel.simple_model",
    )
    print(actual)
    assert actual == [
        "",
        ".. py:attribute:: AbstractModel.simple_model",
        "   :module: dummy_django_app.models",
        "",
        "   Type: :class:`~django.db.models.ForeignKey` to :class:`~SimpleModel`",
        "",
        "   Simple model "
        "(related name: :attr:`~dummy_django_app.models.SimpleModel.abstractmodel`)",
        "",
    ]


@pytest.mark.sphinx("html", testroot="docstrings")
def test_reverse_foreignkey(app, do_autodoc):
    actual = do_autodoc(
        app,
        "attribute",
        "dummy_django_app.models.FileModel.simple_models",
    )
    print(actual)
    assert actual == [
        "",
        ".. py:attribute:: FileModel.simple_models",
        "   :module: dummy_django_app.models",
        "",
        "   Type: Reverse :class:`~django.db.models.ForeignKey` from "
        ":class:`~dummy_django_app.models.SimpleModel`",
        "",
        "   All simple models of this file model "
        "(related name of :attr:`~dummy_django_app.models.SimpleModel.file`)",
        "",
    ]


@pytest.mark.sphinx("html", testroot="docstrings")
def test_manytomany_field(app, do_autodoc):
    actual = do_autodoc(
        app,
        "attribute",
        "dummy_django_app.models.SimpleModel.childrenB",
    )
    print(actual)
    assert actual == [
        "",
        ".. py:attribute:: SimpleModel.childrenB",
        "   :module: dummy_django_app.models",
        "",
        "   Type: :class:`~django.db.models.ManyToManyField` to "
        ":class:`~dummy_django_app.models.ChildModelB`",
        "",
        "   ChildrenB "
        "(related name: :attr:`~dummy_django_app.models.ChildModelB.simple_models`)",
        "",
    ]


@pytest.mark.sphinx("html", testroot="docstrings")
def test_reverse_manytomany_field(app, do_autodoc):
    actual = do_autodoc(
        app,
        "attribute",
        "dummy_django_app.models.ChildModelB.simple_models",
    )
    print(actual)
    assert actual == [
        "",
        ".. py:attribute:: ChildModelB.simple_models",
        "   :module: dummy_django_app.models",
        "",
        "   Type: Reverse :class:`~django.db.models.ManyToManyField` from "
        ":class:`~dummy_django_app.models.SimpleModel`",
        "",
        "   All simple models of this child model b "
        "(related name of :attr:`~dummy_django_app.models.SimpleModel.childrenB`)",
        "",
    ]


@pytest.mark.sphinx("html", testroot="docstrings")
def test_reverse_onetoone_field(app, do_autodoc):
    actual = do_autodoc(
        app, "attribute", "dummy_django_app.models.ChildModelA.simple_model"
    )
    print(actual)
    assert actual == [
        "",
        ".. py:attribute:: ChildModelA.simple_model",
        "   :module: dummy_django_app.models",
        "",
        "   Type: Reverse :class:`~django.db.models.OneToOneField` from "
        ":class:`~dummy_django_app.models.SimpleModel`",
        "",
        "   The simple model of this child model a "
        "(related name of :attr:`~dummy_django_app.models.SimpleModel.childA`)",
        "",
    ]


@pytest.mark.sphinx("html", testroot="docstrings")
def test_model_manager_fields(app, do_autodoc):
    actual = do_autodoc(
        app, "attribute", "dummy_django_app.models.SimpleModel.custom_objects"
    )
    print(actual)
    assert actual == [
        "",
        ".. py:attribute:: SimpleModel.custom_objects",
        "   :module: dummy_django_app.models",
        "   :value: <dummy_django_app.models.SimpleModelManager object>",
        "",
        "   Custom model manager",
        "",
        "   Django manager to access the ORM",
        "   Use ``SimpleModel.objects.all()`` to fetch all objects.",
        "",
    ]


@pytest.mark.sphinx("html", testroot="docstrings")
def test_file_field(app, do_autodoc):
    actual = do_autodoc(app, "attribute", "dummy_django_app.models.FileModel.upload")
    print(actual)
    assert actual == [
        "",
        ".. py:attribute:: FileModel.upload",
        "   :module: dummy_django_app.models",
        "",
        "   Type: :class:`~django.db.models.FileField`",
        "",
        "   Upload",
        "",
    ]


if PHONENUMBER:

    @pytest.mark.sphinx("html", testroot="docstrings")
    def test_phonenumber_field(app, do_autodoc):
        actual = do_autodoc(
            app, "attribute", "dummy_django_app.models.PhoneNumberModel.phone_number"
        )
        print(actual)
        assert actual == [
            "",
            ".. py:attribute:: PhoneNumberModel.phone_number",
            "   :module: dummy_django_app.models",
            "",
            "   Type: :class:`~phonenumber_field.modelfields.PhoneNumberField`",
            "",
            "   Phone number",
            "",
        ]