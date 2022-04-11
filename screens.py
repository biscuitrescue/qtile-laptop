import os
from libqtile.config import Screen 
from libqtile import layout, bar, widget, hook

colours =  [
    ["#D8DEE9"],      # Colour 0
    ["#2e3440"],        # Colour 1
    ["#ff8b92"],        # Colour 2
    ["#c3e88d"],        # Colour 3
    ["#ffe585"],        # Colour 4
    ["#c792ea"],        # Colour 5
    ["#f5c2e7"],        # Colour 6
    ["#82aaff"],        # Colour 7
    ["#F2779C"],        # Colour 8
    ["#81A1C1"],        # Colour 9
    ["#ff6e6e"]]        # Colour 10

xx=16
xf="operatormono nerd font medium"
default=[
    widget.GroupBox(
        font="operator mono medium",
        fontsize=17,
        background=colours[1],
        margin_y=3,
        margin_x=5,
        padding_y=3,
        padding_x=2,
        borderwidth=8,
        inactive=colours[9],
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
        foreground=colours[3],
        text=" | ",
        font=xf,
    ),
    widget.PulseVolume(
        mouse_callbacks={'Button3': lambda: qtile.cmd_spawn("pavucontrol")},
        foreground=colours[3],
        update_interval=0.001,
        font=xf,
        fontsize=xx,
    ),
    widget.TextBox(
        foreground=colours[2],
        text=" | ",
        font=xf,
    ),
    widget.Clock(
        foreground=colours[2],
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
        foreground=colours[7],
        text=" | ",
        font=xf,
    ),
]
if len(os.listdir("/sys/class/power_supply"))==0:
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
                foreground=colours[7],
                format='{char} {percent:2.0%}',
            ),
            widget.TextBox(
                foreground=colours[7],
                text=" |",
                font=xf,
            ),
        ]
    )

screens = [
    Screen(
    top=bar.Bar(
        default,
        34,
        background=colours[1],
        foreground=colours[1],
        opacity=0.9,
        margin=[8,60,12,60],
    ),
    ),
]
