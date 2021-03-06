from libqtile import layout
from libqtile.config import Match
from typing import List  # noqa: F401
from keys import keys
from groups import groups
from screens import screens
# 96cdfb
# d6acff
border = dict(
    border_focus="#7EA6FA",
    border_normal="#4c566a",
    border_width=2,
)
layouts = [
    layout.Tile(
        margin=8,
        ratio=0.55,
        border_on_single=False,
        shift_windows=True,
        **border
    ),
    # layout.Bsp(
    #     fair=False,
    #     margin=8,
    #     shift_windows=True,
    #     **border
    # ),
    layout.TreeTab(
        font="jetbrainsmono nerd font mono",
        fontsize=15,
        sections=["Qtile"],
        section_fontsize=16,
        border_width=3,
        bg_color="282d3e",
        active_bg="c678dd",
        active_fg="000000",
        inactive_bg="a9a1e1",
        inactive_fg="1c1f24",
        padding_left=10,
        padding_x=0,
        padding_y=8,
        section_top=20,
        section_bottom=20,
        level_shift=8,
        vspace=5,
        panel_width=240
    ),
    layout.Max(),

]
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
        Match(wm_class='Todogtk.py'),
        Match(wm_class='Signal Beta'),  # ssh-askpass
        Match(title='branchdialog'),  # gitk
        Match(wm_class='Gpower.py'),
        Match(title='pinentry'),  # GPG key password entry
    ])

auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True
auto_minimize = True
wmname = "LG3D"
