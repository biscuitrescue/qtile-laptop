import os
from libqtile.config import Screen
from libqtile import layout, bar, widget, hook
from qtile_extras import widget
from qtile_extras.widget.decorations import RectDecoration
from qtile_extras.bar import Bar

colours =  [
    ["#D8DEE9"],      # Colour 0
    ["#181f21"],        # Colour 1
    ["#ef7d7d"],        # Colour 2
    ["#9bdead"],        # Colour 3
    ["#f4d67a"],        # Colour 4
    ["#C9CBFF"],        # Colour 5
    ["#f5c2e7"],        # Colour 6
    ["#8ccf7e"],        # Colour 7
    ["#d6acff"],        # Colour 8
    ["#6da4cd"],        # Colour 9
    ["#e06e6e"]]        # Colour 10

decor = {
    "decorations": [
        RectDecoration(
            use_widget_background=True,
            radius=9,
            filled=True,
            padding_y=7,
        )
    ],
    "padding": 10,
}

xx=17
xf="ubuntumono nerd font bold"
default=[
    widget.GroupBox(
        font="ubuntumono nerd font bold",
        fontsize=25,
        background=colours[1],
        margin_y=4,
        margin_x=5,
        padding_y=3,
        padding_x=2,
        borderwidth=8,
        inactive=colours[9],
        active=colours[5],
        rounded=True,
        highlight_color=colours[4],
        highlight_method="text",
        this_current_screen_border=colours[3],
        block_highlight_text_color=colours[1],
    ),
    widget.Sep(
        padding=2,
        linewidth=0,
    ),
    widget.CurrentLayoutIcon(
        custom_icon_paths=[os.path.expanduser("~/.config/qtile/icons")],
        scale=0.45,
        background=colours[1],
    ),

    widget.Spacer(),

    widget.Systray(
        icon_size=20,
        padding=4,
    ),
    widget.TextBox(
        foreground=colours[9],
        text="|",
        font=xf,
    ),
    widget.CPU(
        background=colours[9],
        foreground=colours[1],
        format='  {load_percent}%',
        font=xf,
        fontsize=xx,
        **decor,
    ),
    widget.TextBox(
        foreground=colours[4],
        text="|",
        font=xf,
    ),
    widget.Memory(
        font=xf,
        fontsize=xx,
        background=colours[4],
        foreground=colours[1],
        measure_mem='G',
        measure_swap='G',
        format='  {MemUsed: .2f} GB',
        **decor,
    ),
    widget.TextBox(
        foreground=colours[6],
        text="|",
        font=xf,
    ),
    widget.Memory(
        measure_mem='G',
        font=xf,
        fontsize=xx,
        foreground=colours[1],
        background=colours[6],
        measure_swap='G',
        format=' {SwapUsed: .2f} GB',
        **decor,
    ),
    widget.TextBox(
        foreground=colours[3],
        text="|",
        font=xf,
    ),
    widget.PulseVolume(
        mouse_callbacks={'Button3': lambda: qtile.cmd_spawn("pavucontrol")},
        background=colours[3],
        foreground=colours[1],
        update_interval=0.001,
        font=xf,
        fontsize=xx,
        **decor,
    ),
    widget.TextBox(
        foreground=colours[8],
        text="|",
        font=xf,
    ),
    widget.Clock(
        foreground=colours[1],
        background=colours[8],
        format='  %d %b, %a',
        font=xf,
        fontsize=xx,
        **decor,
    ),
    widget.TextBox(
        foreground=colours[5],
        text="|",
        font=xf,
    ),
    widget.Clock(
        foreground=colours[1],
        background=colours[5],
        font=xf,
        fontsize=xx,
        format='  %I:%M %p',
        **decor,
    ),
    widget.TextBox(
        foreground=colours[7],
        text="|",
        font=xf,
    ),
]
if len(os.listdir("/sys/class/power_supply"))==0:
    default.extend(
        [
            widget.CapsNumLockIndicator(
                fontsize=xx,
                font=xf,
                foreground=colours[1],
                background=colours[7],
                **decor,
            ),
            widget.TextBox(
                foreground=colours[7],
                text="|",
                font=xf,
            ),
        ]
    )
else:
    default.extend(
        [
            widget.Battery(
                fontsize=xx,
                font=xf,
                low_percentage=0.3,
                low_background=colours[10],
                low_foreground=colours[1],
                update_interval=1,
                charge_char='',
                discharge_char=' ',
                background=colours[7],
                format='{char}  {percent:2.0%}',
                foreground=colours[1],
                **decor,
            ),
            widget.TextBox(
                foreground=colours[7],
                text="|",
                font=xf,
            ),
        ]
    )

screens = [
    Screen(
    top=bar.Bar(
        default,
        44,
        background=colours[1],
        foreground=colours[1],
        opacity=0.95,
        margin=[8,30,12,30],
    ),
    ),
]
