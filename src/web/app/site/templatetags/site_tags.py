from django import template
from django.utils.safestring import mark_safe
from django.conf import settings
from django.urls import reverse_lazy

register = template.Library()


@register.simple_tag
def version_text():
    return mark_safe(f'<span class="navbar-text">v{settings.APP_VERSION}</span>')


# this template tag displays the username from profile
# used in navbar.html
@register.simple_tag(takes_context=True)
def user_display_name(context):
    user = context['user']
    profile = Profile.objects.get(user=user.id)
    return profile.user_display_name


# returns badge colour for username background
# used in navbar.html
@register.simple_tag(takes_context=True)
def user_badge_colour(context):
    user = context['user']
    if user.is_staff:
        return 'badge-primary'
    return 'badge-primary'


@register.simple_tag(takes_context=True)
def user_is_you(context, username):
    you = context['user']
    if you.username == username:
        return mark_safe(username + ' <span class="badge badge-pill badge-info">you</span>')
    return username


# returns the menu state (active) depending on route
# used in navbar.html
@register.simple_tag
def menu_state(menu, path):
    if menu in path:
        return 'active'
    return ''


@register.simple_tag
def page_selected(page, path):
    if page in path:
        return 'selected'
    return ''


# returns the help_page according to the current url
# used in navbar.html help link
@register.simple_tag(takes_context=True)
def help_page(context):

    request = context['request']
    url_name = request.resolver_match.url_name

    base_route = '/static/site/help/sum/user'
    page = 'index.html'

    # this dictionary consists of the url_names as given by the name field
    # in the various urls.py files for each application and the target
    # page in the help. It is used to open the help page that corresponds to
    # the current loaded page.
    #
    # The target is a page like "batch.html" and it's possible to add link to
    # a specific chapter with the # like "connection.html#login"
    #
    help_targets = {
      "home": "index.html",
    }
    if url_name in help_targets:
        page = help_targets[url_name]

    return f"{base_route}/{page}"


# returns the help_page according to the current url
# used in navbar.html help link
@register.simple_tag(takes_context=True)
def admin_help_page(context):

    request = context['request']
    url_name = request.resolver_match.url_name

    base_route = '/static/site/help/adm/admin'
    page = 'index.html'

    # this dictionary consists of the url_names as given by the name field
    # in the various urls.py files for each application and the target
    # page in the help. It is used to open the help page that corresponds to
    # the current loaded page.
    #
    # The target is a page like "batch.html" and it's possible to add link to
    # a specific chapter with the # like "connection.html#login"
    #
    help_targets = {
      "home": "index.html",
    }
    if url_name in help_targets:
        page = help_targets[url_name]

    return f"{base_route}/{page}"




