import os
from libqtile.config import Screen
from libqtile import bar, widget
from libqtile import qtile

colours = [
    ["#D8DEE9"],        # Colour 0
    ["#282a36"],        # Colour 1
    ["#F2779C"],        # Colour 2
    ["#50fa7b"],        # Colour 3
    ["#f1fa8c"],        # Colour 4
    ["#d6acff"],        # Colour 5
    ["#ff79c6"],        # Colour 6
    ["#8be9fd"],        # Colour 7
    ["#ff6e6e"],        # Colour 8
    ["#a4ffff"],        # Colour 9
    ["#ff5555"]         # Colour 10
]

xx = 16
xf = "operatormono nerd font medium"
default = [
    widget.GroupBox(
        font="operator mono medium",
        fontsize=17,
        background=colours[1],
        margin_y=3,
        margin_x=5,
        padding_y=3,
        padding_x=2,
        borderwidth=8,
        inactive=colours[5],
        active=colours[3],
        rounded=True,
        highlight_color=colours[4],
        highlight_method="block",
        this_current_screen_border=colours[8],
        block_highlight_text_color=colours[1],
    ),
    widget.Sep(
        padding=8,
        linewidth=0,
    ),
    widget.CurrentLayoutIcon(
        custom_icon_paths=[os.path.expanduser("~/.config/qtile/icons")],
        scale=0.5,
        background=colours[1],
    ),

    widget.Spacer(),

    widget.Systray(
        foreground=colours[4],
        icon_size=20,
        padding=4,
    ),
    widget.TextBox(
        foreground=colours[9],
        text=" | ",
        font=xf,
    ),
    widget.CPU(
        foreground=colours[9],
        format=' {load_percent}%',
        font=xf,
        fontsize=xx,
    ),
    widget.TextBox(
        foreground=colours[4],
        text=" | ",
        font=xf,
    ),
    widget.Memory(
        font=xf,
        fontsize=xx,
        foreground=colours[4],
        measure_mem='G',
        measure_swap='G',
        format='{MemUsed: .2f} GB',
    ),
    widget.TextBox(
        foreground=colours[6],
        text=" | ",
        font=xf,
    ),
    widget.Memory(
        measure_mem='G',
        font=xf,
        fontsize=xx,
        foreground=colours[6],
        measure_swap='G',
        format='{SwapUsed: .2f} GB',
    ),
    widget.TextBox(
        foreground=colours[7],
        text=" | ",
        font=xf,
    ),
    widget.PulseVolume(
        mouse_callbacks={'Button3': lambda: qtile.cmd_spawn("pavucontrol")},
        foreground=colours[7],
        update_interval=0.001,
        font=xf,
        fontsize=xx,
    ),
    widget.TextBox(
        foreground=colours[8],
        text=" | ",
        font=xf,
    ),
    widget.Clock(
        foreground=colours[8],
        format=' %d %b, %a',
        font=xf,
        fontsize=xx,
    ),
    widget.TextBox(
        foreground=colours[5],
        text=" | ",
        font=xf,
    ),
    widget.Clock(
        foreground=colours[5],
        font=xf,
        fontsize=xx,
        format=' %I:%M %p',
    ),
    widget.TextBox(
        foreground=colours[3],
        text=" | ",
        font=xf,
    ),
]
if len(os.listdir("/sys/class/power_supply")) == 0:
    default.append(
        widget.CapsNumLockIndicator(
            fontsize=xx,
            font=xf,
            foreground=colours[1],
            background=colours[7],
        )
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
                discharge_char='',
                foreground=colours[3],
                format='{char} {percent:2.0%}',
            ),
            widget.TextBox(
                foreground=colours[3],
                text=" |",
                font=xf,
            ),
        ]
    )

screens = [
    Screen(
        top=bar.Bar(
            default,
            32,
            background=colours[1],
            foreground=colours[1],
            # opacity=0.9,
            margin=[10, 80, 8, 80],
        ),
    ),
]
