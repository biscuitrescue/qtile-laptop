import os
from libqtile.config import Screen 
from libqtile import layout, bar, widget, hook
from qtile_extras import widget
from qtile_extras.widget.decorations import RectDecoration
from qtile_extras.bar import Bar

colors =  [
        ["#00000000"],     # color 0
        ["#2e3440"], # color 1
        ["#adefd1"], # color 2
        ["#f8baaf"], # color 3
        ["#FF7696"], # color 4
        ["#f3f4f5"], # color 5
        ["#ffb18f"], # color 6
        ["#aec597"], # color 7
        ["#B591B0"], # color 8
        ["#0ee9af"], # color 9
        ["#5aec97"], # color 8
        ["#ff6e6e"]] # color 9

decor = {
    "decorations": [
        RectDecoration(use_widget_background=True, radius=12, filled=True, padding_y=0,)
    ],
    "padding": 15,
}

xx=14
xf="novamono for powerline bold"
default=[
    widget.Clock(
        font=xf,
        fontsize=xx,
        foreground=colors[1],
        background=colors[4],
        format='  %d %b, %A ',
        **decor,
    ),
    widget.Sep(
        background=colors[0],
        padding=10,
        linewidth=0,
    ),
    widget.Memory(
        background=colors[10],
        foreground=colors[1],
        font=xf,
        fontsize=xx,
        measure_mem='G',
        measure_swap='G',
        format='{MemUsed: .2f} GB',
        **decor,
    ),
    widget.Sep(
        background=colors[0],
        padding=10,
        linewidth=0,
    ),
    widget.CurrentLayout(
        background=colors[3],
        foreground=colors[1],
        font=xf,
        fontsize=xx,
        **decor,
    ),
    widget.CurrentLayoutIcon(
        custom_icon_paths=[os.path.expanduser("~/.config/qtile/icons")],
        scale=0.45,
        padding=0,
        background=colors[0],
    ),

    widget.Spacer(),

    widget.GroupBox(
        font="space mono for powerline",
        fontsize=15,
        margin_y=4,
        margin_x=4,
        padding_y=5,
        padding_x=4,
        borderwidth=7,
        inactive=colors[11],
        active=colors[6],
        rounded=True,
        highlight_color=colors[0],
        highlight_method="text",
        this_current_screen_border=colors[10],
        block_highlight_text_color=colors[1],
        background=colors[1],
        **decor,
    ),

    widget.Spacer(),

    widget.Systray(
        background=colors[0],
        foreground=colors[8],
        icon_size=20,
        padding=4,
    ),
    widget.Sep(
        background=colors[0],
        padding=10,
        linewidth=0,
    ),
    widget.PulseVolume(
        background=colors[2],
        foreground=colors[1],
        font=xf,
        fontsize=xx,
        mouse_callbacks={'Button3': lambda: qtile.cmd_spawn("pavucontrol")},
        update_interval=0.001,
        **decor
    ),
    widget.Sep(
        background=colors[0],
        padding=10,
        linewidth=0,
    ),
    widget.CPU(
        background=colors[9],
        foreground=colors[1],
        format=' {load_percent}%',
        font=xf,
        fontsize=xx,
        **decor
    ),
    widget.Sep(
        background=colors[0],
        padding=10,
        linewidth=0,
    ),
    widget.Memory(
        background=colors[6],
        foreground=colors[1],
        font=xf,
        fontsize=xx,
        measure_mem='G',
        measure_swap='G',
        format='{SwapUsed: .2f} GB',
        **decor,
    ),
    widget.Sep(
        background=colors[0],
        padding=10,
        linewidth=0,
    ),
    widget.Clock(
        background=colors[4],
        foreground=colors[1],
        font=xf,
        fontsize=xx,
        format='%I:%M %p',
        **decor
    ),
    widget.Sep(
        background=colors[0],
        padding=10,
        linewidth=0,
    ),
]

if len(os.listdir("/sys/class/power_supply"))==0:
    default.append(
        widget.CapsNumLockIndicator(
            fontsize=xx,
            font=xf,
            foreground=colors[1],
            background=colors[9],
            **decor,
        )
    )
else:
    default.append(
        widget.Battery(
            fontsize=xx,
            font=xf,
            foreground=colors[1],
            low_percentage=0.3,
            low_background=colors[11],
            background=colors[10],
            low_foreground=colors[1],
            update_interval=1,
            charge_char='',
            discharge_char='',
            format='{char} {percent:2.0%}',
            **decor,
        ),
    )

screens = [
    Screen(
    top=bar.Bar(
        default,
        36,
        background=colors[0],
        foreground=colors[1],
        margin=[8,6,4,6],
    ),
    ),
]
