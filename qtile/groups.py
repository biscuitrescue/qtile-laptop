import os
from libqtile import layout
from libqtile.config import Group, KeyChord, Key, Match, ScratchPad, DropDown
from libqtile.command import lazy
from libqtile.lazy import lazy
from keys import keys

mod = "mod4"
mod1 = "mod1"
mod2 = "control"
mod3  = "shift"
home = os.path.expanduser('~')
groups= [
    Group("1",
          label="",
          ),

    Group("2",
          label="",
          spawn="brave-bin",
          matches=[Match(wm_class=["Vivaldi-stable"]),
                   Match(wm_class=["Icecat"]),
                   Match(wm_class=["Brave-browser"]),
                   ],
          ),

    Group("3",
          label="",
          layout="zoomy",
          matches=[Match(wm_class=["Zathura"]),
                   Match(wm_class=["Evince"]),
                   ],
          ),

    Group("4",
          label="",
          matches=[Match(wm_class=["discord"]),
                   ],
          ),

    Group("5",
          label="",
          matches=[Match(wm_class=["Firefox"]),
                   Match(wm_class=["firefox"]),
                   Match(wm_class=["Mplayer"]),
                   ],
          ),

    Group("6",
          label="",
          matches=[Match(wm_class=["pcmanfm"]),
                   Match(wm_class=["qBittorrent"]),
                   ],
          ),

    Group("7",
          label="",
          matches=[Match(wm_class=["pavucontrol"]),
                   ],
          ),

    Group("8",
          label="",
          matches=[Match(wm_class=["VSCodium"]),
                   ],
          ),

    Group("9",
          label="",
          layout="max",
          matches=[Match(wm_class=["zoom"]),
                   Match(wm_class=["Microsoft Teams - Preview"]),
                   ],
          ),

    Group("0",
          label="",
          matches=[Match(wm_class=["Virt-manager"]),
                   Match(wm_class=["VirtualBox Manager"]),
                   ],
          ),
    Group('f',
          label='',
          matches=[Match(wm_class=["Signal Beta"]),
                   ]
          ),
]
for i in groups:
    keys.extend([
        Key([mod], i.name, lazy.group[i.name].toscreen(),
            desc="Switch to group {}".format(i.name)),
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name, switch_group=False),
            desc="Switch to & move focused window to group {}".format(i.name)),
        Key([mod1, "shift"], i.name, lazy.window.togroup(i.name, switch_group=True),
            desc="Switch to & move focused window to group {}".format(i.name)),
    ])



### ScratchPad

groups.append(ScratchPad('Scratchpad',[
    DropDown("sig", "signal-desktop", height=0.6, width=0.5, x=0.25, y=0.225,
             opacity=1),
    DropDown("term", "kitty", height=0.6, opacity=1),
    DropDown("editor", "emacs",
             x=0.05, y=0.35, width=0.9, height=0.65, opacity=1,
             on_focus_lost_hide=True),
    DropDown("fmger", "thunar", height=0.7, opacity=1,
             width=0.7, x=0.15, y=0.10 ),
    DropDown("spotify", "spotify", height=0.7, opacity=0.9,
             width=0.7, x=0.15, y=0.15 ),
    DropDown("fm", 'kitty -e ranger', height=0.7, opacity=1,
             width=0.7, x=0.15, y=0.125),
    DropDown("hitop", 'kitty -e htop', height=0.7, opacity=1,
             width=0.7, x=0.15, y=0.125),
    DropDown("dc", 'kitty -e gord', height=0.7, opacity=1,
             width=0.7, x=0.15, y=0.125),
    DropDown("top", 'kitty -e btop', height=0.7, opacity=1,
             width=0.7, x=0.15, y=0.125),
]))

keys.extend([
    Key([mod, 'shift'], "v", lazy.group['Scratchpad'].dropdown_toggle('sig')),
    Key([mod], "p", lazy.group['Scratchpad'].dropdown_toggle('term')),
    Key([mod], "o", lazy.group['Scratchpad'].dropdown_toggle('editor')),
    Key([mod, "shift"], "s", lazy.group['Scratchpad'].dropdown_toggle("spotify")),
    Key([mod, "shift"], "d", lazy.group['Scratchpad'].dropdown_toggle("dc")),
    Key(['control'], 'space', lazy.group['Scratchpad'].dropdown_toggle('fm')),
    Key([mod1], 'space', lazy.group['Scratchpad'].dropdown_toggle('top')),
    Key([mod1, 'shift'], 'space', lazy.group['Scratchpad'].dropdown_toggle('hitop')),
    Key([mod, 'shift'], 'space', lazy.group['Scratchpad'].dropdown_toggle('fmger')),
])
border=dict(
    border_focus="#aaeedd",
    border_normal="#4c566a"
)

layouts = [
    layout.Tile(
        margin=8,
        border_width=2,
        ratio=0.55,
        shift_windows=True,
        **border
    ),
    layout.MonadWide(
        margin=15,
        border_width=2,
        ratio=0.55,
        **border
    ),
    layout.Zoomy(
        columnwidth=350,
        margin=8,
    ),
    layout.Max(),

]

