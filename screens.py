import os
from libqtile.config import Screen 
from libqtile import layout, bar, widget, hook
from qtile_extras import widget
from qtile_extras.widget.decorations import RectDecoration
from qtile_extras.bar import Bar

colours =  [
        ["#00000000"],     # color 0
        ["#282a36"], # color 1
        ["#adefd1"], # color 2
        ["#f8baaf"], # color 3
        ["#FF6e6e"], # color 4
        ["#f3f4f5"], # color 5
        ["#ffb18f"], # color 6
        ["#7AEEAA"], # color 7
        ["#B591B0"], # color 8
        ["#50fa7b"], # color 9
        ["#8be9fd"], # color 10
        ["#ff5555"]] # color 10


decor = {
    "decorations": [
        RectDecoration(use_widget_background=True, radius=13, filled=True, padding_y=0,)
    ],
    "padding": 3,
}
decor2 = decor.copy()
decor2["padding"] = 10

xx=16
xf="ubuntumono nerd font bold"
default=[
    widget.GroupBox(
        font=xf,
        fontsize=25,
        background="#282c3485",
        foreground=colours[5],
        margin_y=4,
        margin_x=5,
        padding_y=9,
        padding_x=4,
        borderwidth=7,
        inactive=colours[11],
        active=colours[6],
        rounded=True,
        highlight_color=colours[4],
        highlight_method="text",
        this_current_screen_border=colours[9],
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
        background="#282c3485",
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
        background=colours[10],
        foreground=colours[1],
        format='   {load_percent}% ',
        font=xf,
        fontsize=xx,
        **decor,
        ),
    widget.Sep(
        padding=8,
        linewidth=0,
    ),
    widget.Memory(
        background=colours[7],
        font=xf,
        fontsize=xx,
        foreground=colours[1],
        measure_mem='G',
        measure_swap='G',
        format='  {MemUsed: .2f} GB ',
        **decor,
    ),
    widget.Sep(
        padding=8,
        linewidth=0,
    ),
    widget.Memory(
        measure_mem='G',
        foreground=colours[1],
        font=xf,
        fontsize=xx,
        background=colours[3],
        measure_swap='G',
        format='  {SwapUsed: .2f} GB ',
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
        background=colours[2],
        **decor2
    ),
    widget.Sep(
        padding=8,
        linewidth=0,
    ),
    widget.CheckUpdates(
        colour_have_updates=colours[1],
        font=xf,
        fontsize=xx,
        colour_no_updates=colours[1],
        display_format='  {updates} ',
        no_update_string='  N/A ',
        update_interval=1,
        background=colours[4],
        **decor,
    ),
    widget.Sep(
        padding=8,
        linewidth=0,
    ),
    widget.Clock(
        background=colours[8],
        foreground=colours[1],
        format='   %d %b, %a ',
        font=xf,
        fontsize=xx,
        **decor,
    ),
    widget.Sep(
        padding=8,
        linewidth=0,
    ),
    widget.Clock(
        background=colours[6],
        foreground=colours[1],
        font=xf,
        fontsize=xx,
        format='  %I:%M %p ',
        **decor,
    ),
    widget.Sep(
        padding=8,
        linewidth=0,
    ),
    widget.Systray(
        background=colours[0],
        foreground=colours[8],
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
            background=colours[9],
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
            low_background=colours[11],
            background=colours[9],
            low_foreground=colours[1],
            update_interval=1,
            charge_char=' ',
            discharge_char='',
            format=' {char} {percent:2.0%} ',
            **decor,
        ),
    )

screens = [
    Screen(
    top=bar.Bar(
        default,
        35,
        background=colours[0],
        foreground=colours[1],
        margin=[8,6,4,6],
    ),
    ),
]
