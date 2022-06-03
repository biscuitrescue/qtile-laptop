import os
from libqtile import layout
from libqtile.config import Group, Key, Match, ScratchPad, DropDown
from libqtile.command import lazy
from keys import keys

myTerm = "kitty"
mod = "mod4"
mod1 = "mod1"
mod2 = "control"
mod3 = "shift"
home = os.path.expanduser('~')
groups = [
    Group("1", label=""),
    Group("2", label="", spawn="vivaldi-stable",
        matches=[
            Match(wm_class=["Vivaldi-stable"]),
            Match(wm_class=["Icecat"]),
            Match(wm_class=["LibreWolf"]),
            Match(wm_class=["Brave-browser"]),
        ]
          ),


    Group("3", label="", layout="zoomy",
        matches=[
            Match(wm_class=["Zathura"]),
            Match(wm_class=["Evince"]),
        ]
          ),

    Group("4", label="",
        matches=[
            Match(wm_class=["discord"]),
            Match(wm_class=["Mailspring"]),
            Match(wm_class=["Session"]),
        ]
          ),

    Group("5", label="",
        matches=[
            Match(wm_class=["Firefox"]),
            Match(wm_class=["firefox"]),
            Match(wm_class=["Mplayer"]),
        ]
          ),

    Group("6", label="",
        matches=[
            Match(wm_class=["pcmanfm"]),
            Match(wm_class=["qBittorrent"]),
        ]
          ),

    Group("7", label="",
        matches=[
            Match(wm_class=["pavucontrol"]),
        ]
          ),

    Group("8", label="",
          ),

    Group("9", label="", layout="max",
        matches=[
            Match(wm_class=["zoom"]),
            Match(wm_class=["Microsoft Teams - Preview"]),
        ]
          ),

    Group("0", label="",
        matches=[
            Match(wm_class=["Virt-manager"]),
            Match(wm_class=["VirtualBox Manager"]),
        ]
          ),

    Group('f', label='',
        # matches=[
        #     Match(wm_class=["Signal Beta"]),
        # ]
          ),
]
for i in groups:
    keys.extend([
        Key([mod], i.name, lazy.group[i.name].toscreen(),
            desc="Switch to group {}".format(i.name)),
        Key([mod, "shift"], i.name,
            lazy.window.togroup(i.name, switch_group=False),
            desc="Switch to & move focused window to group {}".format(i.name)),
        Key([mod1, "shift"], i.name,
            lazy.window.togroup(i.name, switch_group=True),
            desc="Switch to & move focused window to group {}".format(i.name)),
    ])

# ScratchPad

groups.append(ScratchPad('Scratchpad', [
    DropDown("sig", "signal-desktop-beta", height=0.6,
             width=0.5, x=0.25, y=0.2, opacity=1),
    DropDown("term", "kitty",
             # width=0.8, height=0.6,
             # x=0.1, y=0, opacity=1),
             width=0.75, height=0.9,
             x=0.125, y=0.05, opacity=1),
    DropDown("editor", "emacs",
             # width=0.9, height=0.85,
             # x=0.05, y=0.15, opacity=1),
             width=0.9, height=0.9,
             x=0.05, y=0.05, opacity=1),
    DropDown("fmger", "thunar",
             width=0.6, height=0.85,
             x=0.2, y=0.075, opacity=1),
    DropDown("spotify", "spotify", height=0.75, opacity=1,
             width=0.7, x=0.15, y=0.125),
    DropDown("fm", 'kitty -e ranger',
             width=0.7, height=0.85,
             x=0.15, y=0.075, opacity=1),
    DropDown("hitop", 'kitty -e htop',
             width=0.7, height=0.85,
             x=0.15, y=0.075, opacity=1),
    DropDown("dc", 'kitty -e gord',
             width=0.7, height=0.85,
             x=0.15, y=0.075, opacity=1),
    DropDown("top", 'kitty -e btop',
             width=0.7, height=0.85,
             x=0.15, y=0.075, opacity=1),
]))

keys.extend([
    Key([mod, 'shift'], "v",
        lazy.group['Scratchpad'].dropdown_toggle('sig')),
    Key([mod], "p",
        lazy.group['Scratchpad'].dropdown_toggle('term')),
    Key([mod], "o",
        lazy.group['Scratchpad'].dropdown_toggle('editor')),
    Key([mod, "shift"], "s",
        lazy.group['Scratchpad'].dropdown_toggle("spotify")),
    Key([mod, "shift"], "d",
        lazy.group['Scratchpad'].dropdown_toggle("dc")),
    Key(['control'], 'space',
        lazy.group['Scratchpad'].dropdown_toggle('fm')),
    Key([mod1], 'space',
        lazy.group['Scratchpad'].dropdown_toggle('top')),
    Key([mod1, 'shift'], 'space',
        lazy.group['Scratchpad'].dropdown_toggle('hitop')),
    Key([mod, 'shift'], 'space',
        lazy.group['Scratchpad'].dropdown_toggle('fmger')),
])
