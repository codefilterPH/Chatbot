from wagtail.contrib.modeladmin.options import (
    ModelAdmin,
    ModelAdminGroup,
    modeladmin_register
)

from .models import *


class OpenAIKeySettings(ModelAdmin):
    """About admin."""
    model = OpenAIKey
    base_url_path = 'api'
    menu_label = 'API KEY'  # ditch this to use verbose_name_plural from model
    menu_icon = 'pick'  # change as required
    menu_order = 100  # will put in 3rd place (000 being 1st, 100 2nd)
    add_to_settings_menu = True  # or True to add your model to the Settings sub-menu
    exclude_from_explorer = False  # or True to exclude pages of this type from Wagtail's explorer view
    add_to_admin_menu = False  # or False to exclude your model from the menu
    list_display = ('name', 'key')
    list_filter = ('name', 'key')
    search_fields = ('name','key')


modeladmin_register(OpenAIKeySettings)