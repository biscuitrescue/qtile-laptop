from libqtile import layout
from libqtile.config import Match
from typing import List  # noqa: F401
from keys import keys
from groups import groups, layouts
from screens import screens

border = dict(
    border_focus="#8ec07c",
    border_normal="#4c566a",
    border_width=2,
)
dgroups_key_binder = None
dgroups_app_rules = []  # type: List
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    **border,
    float_rules=[
        *layout.Floating.default_float_rules,
        Match(wm_class='confirmreset'),  # gitk
        Match(wm_class='Blueman-manager'),
        Match(wm_class='Tor Browser'),
        Match(wm_class='makebranch'),  # gitk
        Match(wm_class='maketag'),  # gitk
        Match(wm_class='ssh-askpass'),  # ssh-askpass
        Match(wm_class='Tk'),  # ssh-askpass
        Match(wm_class='Signal Beta'),  # ssh-askpass
        Match(title='branchdialog'),  # gitk
        Match(title='pinentry'),  # GPG key password entry
    ])

auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True
auto_minimize = True
wmname = "LG3D"
