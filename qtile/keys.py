import os
from libqtile.config import Click, Drag, KeyChord, Key 
from libqtile.command import lazy
from libqtile.lazy import lazy

mod = "mod4"
mod1 = "mod1"
mod2 = "control"
mod3  = "shift"
home = os.path.expanduser('~')
Term2 = "alacritty"
myTerm = "kitty"

# if qtile.core.name=='x11':
#     launcher="dmenu_run -i -h 25 -p 'RUN:'"
# elif qtile.core.name=='wayland':
    # launcher="bemenu-run -i -H 30 --fn 'Space mono for powerline 11' --nb '#2e3440' --nf '#ffffff' --hb '#aaeedd' --hf '#000000' --sb '#aaeedd' --sf '#000000' -p 'RUN:' --tb '#aaeedd' --tf '#000000' --fb '#000000' --ff '#aaeedd'"

# a=subprocess.Popen('echo $HOME', shell=True, stdout=subprocess.PIPE)
# user=a.communicate()[0].decode().strip()

@lazy.function
def window_to_prev_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i - 1].name)

@lazy.function
def window_to_next_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i + 1].name)

#############################################
############ SHORTCUTS ######################
#############################################


keys = [
    Key([], "F4", lazy.spawn("launcher")),
    Key([mod], "d", lazy.spawn("dmenu_run -i -h 25 -p 'RUN'")),


##################################################
################# MEDIA CONTROLS #################
##################################################

# INCREASE/DECREASE/MUTE VOLUME
    # Key([], "XF86AudioMute", lazy.spawn("amixer -q set Master toggle")),
    # Key([], "XF86AudioLowerVolume", lazy.spawn("amixer -q set Master 5%-")),
    # Key([], "XF86AudioRaiseVolume", lazy.spawn("amixer -q set Master 5%+")),

    Key([], "XF86AudioMute", lazy.spawn("pamixer -t")),
    Key([], "XF86AudioMicMute", lazy.spawn("mictoggle")),
    Key([], "XF86AudioLowerVolume", lazy.spawn("pamixer -d 5")),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("pamixer -i 5")),

    Key([], "XF86AudioPlay", lazy.spawn("playerctl play-pause")),
    Key([], "XF86AudioNext", lazy.spawn("playerctl next")),
    Key([], "XF86AudioPrev", lazy.spawn("playerctl previous")),
    Key([], "XF86AudioStop", lazy.spawn("playerctl stop")),
    Key([], "XF86MonBrightnessUp", lazy.spawn("light -A 5")),
    Key([], "XF86MonBrightnessDown", lazy.spawn("light -U 5")),
    # Key([], "XF86MonBrightnessUp", lazy.spawn("xbacklight -inc 5")),
    # Key([], "XF86MonBrightnessDown", lazy.spawn("xbacklight -dec 5")),



    # Switch between windows in current stack pane
###################################################
################  SWITCH LAYOUT ###################
###################################################

# TOGGLE FLOATING LAYOUT
    Key([mod, "control"], "a", lazy.window.toggle_floating()),

    # CHANGE FOCUS
    Key([mod], "Up", lazy.layout.up()),
    Key([mod], "Down", lazy.layout.down()),
    Key([mod], "Left", lazy.layout.left()),
    Key([mod], "Right", lazy.layout.right()),
    Key([mod], "k", lazy.layout.up()),
    Key([mod], "j", lazy.layout.down()),
    Key([mod], "period",lazy.layout.grow(), lazy.layout.increase_nmaster()),
    Key([mod], "comma", lazy.layout.shrink(), lazy.layout.decrease_nmaster()),
    Key([mod], "n", lazy.layout.normalize()),
    Key([mod], "w", lazy.window.toggle_fullscreen()),
    Key([mod], "h", lazy.layout.decrease_ratio()),
    Key([mod], "l", lazy.layout.increase_ratio()),

# FLIP LAYOUT FOR MONADTALL/MONADWIDE
    Key([mod, "shift"], "f", lazy.layout.flip()),

# MOVE WINDOWS UP OR DOWN MONADTALL/MONADWIDE LAYOUT
    Key([mod, "shift"], "Up", lazy.layout.shuffle_up()),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up()),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down()),
    Key([mod, "shift"], "Down", lazy.layout.shuffle_down()),
    Key([mod, "shift"], "Left", lazy.layout.swap_left()),
    Key([mod, "shift"], "Right", lazy.layout.swap_right()),
    Key([mod], "s", lazy.layout.next()),

#########################################
############### BSPWM ###################
#########################################
    Key([mod], "Down", lazy.layout.down()),
    Key([mod], "Up", lazy.layout.up()),
    Key([mod], "Left", lazy.layout.left()),
    Key([mod], "Right", lazy.layout.right()),
    Key([mod, "shift"], "Down", lazy.layout.shuffle_down()),
    Key([mod, "shift"], "Up", lazy.layout.shuffle_up()),
    Key([mod, "shift"], "Left", lazy.layout.shuffle_left()),
    Key([mod, "shift"], "Right", lazy.layout.shuffle_right()),
    Key([mod, "mod1"], "Down", lazy.layout.flip_down()),
    Key([mod, "mod1"], "Up", lazy.layout.flip_up()),
    Key([mod, "mod1"], "Left", lazy.layout.flip_left()),
    Key([mod, "mod1"], "Right", lazy.layout.flip_right()),
    Key([mod, "control"], "Down", lazy.layout.grow_down()),
    Key([mod, "control"], "Up", lazy.layout.grow_up()),
    Key([mod, "shift"], "l", lazy.layout.grow_left()),
    Key([mod, "shift"], "m", lazy.layout.grow_right()),
    Key([mod, "shift"], "n", lazy.layout.normalize()),
    # Key([mod], "z", lazy.layout.toggle_split()),
    Key([mod], "z", lazy.spawn("killall zoom")),

    Key([mod], "b", lazy.hide_show_bar()),
    Key([mod], "Tab", lazy.next_layout()),
    Key([mod], "a", lazy.prev_layout()),
    Key([mod], "q", lazy.window.kill()),
    Key([mod, "shift"], "q", lazy.shutdown()),
    Key([mod], "c", lazy.restart()),
    Key([mod], "r", lazy.spawncmd()),
    Key([mod, "shift"], "x", lazy.spawn("poweroff")),
##############################################
############## SCREENSHOTS ###################
##############################################

    Key(["shift"], "Print", lazy.spawn("clip")),
    Key(["control"], "Print", lazy.spawn("vmcrop")),
    Key([mod], "Print", lazy.spawn("crop")),
    Key([], "Print", lazy.spawn("shot")),

#####################3#########################
############## APPLICATIONS ###################
###############################################

    Key([mod], "space", lazy.spawn(Term2)),
    Key([mod, "shift"], "a", lazy.spawn("i3lock -c 000000")),
    Key([mod], "KP_Subtract", lazy.spawn("i3lock -c 00000000")),
    Key([mod], "KP_Add", lazy.spawn("lock")),
    Key([mod], "Return", lazy.spawn(myTerm)),
    Key([mod], "KP_Enter", lazy.spawn(myTerm)),
    Key([mod], "z", lazy.spawn(myTerm+" -e fish")),
    Key([mod], "v", lazy.spawn("pavucontrol")),
    Key([], "F9", lazy.spawn("pavucontrol")),
    Key([mod, "shift"], 'd', lazy.spawn('dunstop')),

    KeyChord([mod], "i",[
        Key([], "f", lazy.spawn("firefox")),
        Key([], "v", lazy.spawn("vivaldi-stable")),
        Key([], "b", lazy.spawn("brave")),
        Key([], "l", lazy.spawn("librewolf")),
    ]),
### EDITORS
    KeyChord([mod], "e",[
        Key([], "e", lazy.spawn("emacs")),
        Key([], "v", lazy.spawn("vscodium")),
        Key([], "k", lazy.spawn("kitty -e nvim")),
    ]),
### XSS-LOCK
    KeyChord([mod], "t",[
        Key([], "x", lazy.spawn("killall xss-lock")),
        Key([], "r", lazy.spawn("xss-lock --transfer-sleep-lock -- i3lock -c 00000000 --nofork")),
            ]),
### DMSCRIPTS
    KeyChord([mod], "x",[
        Key([], "c", lazy.spawn("bash /home/karttikeya/dmscripts/dmconf")),
        Key([], "x", lazy.spawn("powermenu")),
        Key([], "p", lazy.spawn("bash /home/karttikeya/dmscripts/dmpy")),
        Key([], "f", lazy.spawn("bash /home/karttikeya/dmscripts/dmfeh")),
            ]),

### REDSHIFT
    KeyChord([mod], "r",[
        Key([], "1", lazy.spawn("redshift -O 6000")),
        Key([], "2", lazy.spawn("redshift -O 5000")),
        Key([], "3", lazy.spawn("redshift -O 4500")),
        Key([], "4", lazy.spawn("redshift -O 4250")),
        Key([], "5", lazy.spawn("redshift -O 4000")),
        Key([], "6", lazy.spawn("redshift -O 3500")),
        Key([], "x", lazy.spawn("redshift -x")),
            ]),
    ]


mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

