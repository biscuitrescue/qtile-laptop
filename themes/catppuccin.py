import os
from libqtile.config import Screen 
from libqtile import layout, bar, widget, hook
from qtile_extras import widget
from qtile_extras.widget.decorations import RectDecoration
from qtile_extras.bar import Bar

colours =  [
    ["#00000000"],      # Colour 0
    ["#1e1e2e"],        # Colour 1
    ["#f28fad"],        # Colour 2
    ["#abe9b3"],        # Colour 3
    ["#fae3b0"],        # Colour 4
    ["#d6acff"],        # Colour 5
    ["#f5c2e7"],        # Colour 6
    ["#89DCEB"],        # Colour 7
    ["#F2779C"],        # Colour 8
    ["#b5e8e0"],        # Colour 9
    ["#ff6e6e"]]        # Colour 10

decor = {
    "decorations": [
        RectDecoration(use_widget_background=True, radius=11, filled=True, padding_y=0,)
    ],
    "padding": 10,
}
decor2 = {
    "decorations": [
        RectDecoration(use_widget_background=True, radius=11, filled=True, padding_y=0)
    ],
    "padding": 10,
}

xx=16
xf="operator mono book"
default=[
    widget.GroupBox(
        font="jetbrainsmono nerd font",
        fontsize=25,
        background="#1e1e2e99",
        margin_y=4,
        margin_x=5,
        padding_y=9,
        padding_x=2,
        borderwidth=7,
        inactive=colours[6],
        active=colours[3],
        rounded=True,
        highlight_color=colours[4],
        highlight_method="text",
        this_current_screen_border=colours[10],
        block_highlight_text_color=colours[1],
        **decor,
    ),
    widget.Sep(
        padding=8,
        linewidth=0,
    ),
    widget.CurrentLayoutIcon(
        custom_icon_paths=[os.path.expanduser("~/.config/qtile/icons")],
        scale=0.4,
        background="#1e1e2e99",
        **decor,
    ),

    widget.Sep(
        padding=8,
        linewidth=0,
    ),

    widget.Spacer(),

    widget.Sep(
        padding=8,
        linewidth=0,
    ),
    widget.CPU(
        background=colours[9],
        foreground=colours[1],
        format=' {load_percent}%',
        font=xf,
        fontsize=xx,
        **decor,
        ),
    widget.Sep(
        padding=8,
        linewidth=0,
    ),
    widget.Memory(
        background=colours[4],
        font=xf,
        fontsize=xx,
        foreground=colours[1],
        measure_mem='G',
        measure_swap='G',
        format='{MemUsed: .2f} GB',
        **decor,
    ),
    widget.Sep(
        padding=8,
        linewidth=0,
    ),
    widget.Memory(
        measure_mem='G',
        background=colours[6],
        font=xf,
        fontsize=xx,
        foreground=colours[1],
        measure_swap='G',
        format='{SwapUsed: .2f} GB',
        **decor,
    ),
    widget.Sep(
        padding=8,
        linewidth=0,
    ),
    widget.PulseVolume(
        mouse_callbacks={'Button3': lambda: qtile.cmd_spawn("pavucontrol")},
        foreground=colours[1],
        update_interval=0.001,
        font=xf,
        fontsize=xx,
        background=colours[3],
        **decor2
    ),
    # widget.Sep(
    #     padding=8,
    #     linewidth=0,
    # ),
    # widget.CheckUpdates(
    #     font=xf,
    #     fontsize=xx,
    #     background=colours[2],
    #     foreground=colours[1],
    #     distro='Gentoo_eix',
    #     display_format=" {updates}",
    #     colour_have_updates=colours[1],
    #     no_update_string='N/A',
    #     update_interval=60,
    #     **decor2,
    # ),
    widget.Sep(
        padding=8,
        linewidth=0,
    ),
    widget.Clock(
        background=colours[5],
        foreground=colours[1],
        format=' %d %b, %a',
        font=xf,
        fontsize=xx,
        **decor,
    ),
    widget.Sep(
        padding=8,
        linewidth=0,
    ),
    widget.Clock(
        background=colours[2],
        foreground=colours[1],
        font=xf,
        fontsize=xx,
        format=' %I:%M %p',
        **decor,
    ),
    widget.Sep(
        padding=8,
        linewidth=0,
    ),
    widget.Systray(
        background=colours[0],
        foreground=colours[4],
        icon_size=20,
        padding=4,
    ),
    widget.Sep(
        padding=8,
        linewidth=0,
    ),
]
if len(os.listdir("/sys/class/power_supply"))==0:
    default.append(
        widget.CapsNumLockIndicator(
            fontsize=xx,
            font=xf,
            foreground=colours[1],
            background=colours[7],
            **decor,
        )
    )
else:
    default.append(
        widget.Battery(
            fontsize=xx,
            font=xf,
            foreground=colours[1],
            low_percentage=0.3,
            low_background=colours[10],
            background=colours[7],
            low_foreground=colours[1],
            update_interval=1,
            charge_char='',
            discharge_char='',
            format='{char} {percent:2.0%}',
            **decor,
        ),
    )

screens = [
    Screen(
    bottom=bar.Bar(
        default,
        34,
        background=colours[0],
        foreground=colours[1],
        opacity=1,
        margin=[4,6,8,6],
    ),
    ),
]