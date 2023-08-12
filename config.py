import os
import subprocess

from libqtile import bar, layout, widget, hook, extension
from libqtile.layout.columns import Columns
from libqtile.layout.stack import Stack
from libqtile.layout.floating import Floating
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from libqtile.config import (
    Click,
    Drag,
    DropDown,
    Group,
    Key,
    Match,
    ScratchPad,
    Screen
)

from colors import gruvbox
from bar2 import bar

mod = "mod4"
terminal = guess_terminal()

# ██╗  ██╗███████╗██╗   ██╗██████╗ ██╗███╗   ██╗██████╗ ███████╗
# ██║ ██╔╝██╔════╝╚██╗ ██╔╝██╔══██╗██║████╗  ██║██╔══██╗██╔════╝
# █████╔╝ █████╗   ╚████╔╝ ██████╔╝██║██╔██╗ ██║██║  ██║███████╗
# ██╔═██╗ ██╔══╝    ╚██╔╝  ██╔══██╗██║██║╚██╗██║██║  ██║╚════██║
# ██║  ██╗███████╗   ██║   ██████╔╝██║██║ ╚████║██████╔╝███████║
# ╚═╝  ╚═╝╚══════╝   ╚═╝   ╚═════╝ ╚═╝╚═╝  ╚═══╝╚═════╝ ╚══════╝

keys = [
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
    
    # Toggle floating and fullscreen
    Key([mod], "f", lazy.window.toggle_fullscreen(),
        desc="Toggle fullscreen mode"),
    Key([mod, "shift"], "space", lazy.window.toggle_floating(),
        desc="Toggle fullscreen mode"),

    # Dmenu
    Key([mod], "p", lazy.run_extension(extension.DmenuRun(
        font="JetBrainsMono Nerd Font",
        fontsize="12",
        dmenu_command="dmenu_run",
        dmenu_prompt=">_",
        dmenu_height=10,
        dmenu_lines=15,
        background=gruvbox['bg'],
        foreground=gruvbox['gray'],
        selected_background=gruvbox['bg1'],
        selected_foreground=gruvbox['blue'],
))),
]

#  ██████╗ ██████╗  ██████╗ ██╗   ██╗██████╗ ███████╗
# ██╔════╝ ██╔══██╗██╔═══██╗██║   ██║██╔══██╗██╔════╝
# ██║  ███╗██████╔╝██║   ██║██║   ██║██████╔╝███████╗
# ██║   ██║██╔══██╗██║   ██║██║   ██║██╔═══╝ ╚════██║
# ╚██████╔╝██║  ██║╚██████╔╝╚██████╔╝██║     ███████║
#  ╚═════╝ ╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═╝     ╚══════╝                                            

groups = [
    Group(
        '1',
        label="一",
        matches=[
            Match(wm_class='firefox'),
            Match(wm_class='brave'),
            Match(wm_class='qutebrowser')
        ],
        layout="stack"
    ),
    Group('2', label="二", layout="monadtall"),
    Group('3', label="三", layout="columns"),
    Group(
        '4',
        label="四",
        matches=[
            Match(wm_class="whatsdesk")
        ],
        layout="stack"
    ),
    Group(
        '5',
        label="五",
        layout="stack"
    ),
    Group('6', label="六", matches=[
          Match(wm_class="thunderbird")], layout="monadtall"),
    Group('7', label="七", layout="monadtall"),
    Group('8', label="八", layout="monadtall"),
    Group('9', label="九", layout="monadtall"),
]


for i in groups:
    keys.extend([
        # mod1 + letter of group = switch to group
        Key([mod], i.name, lazy.group[i.name].toscreen(),
            desc="Switch to group {}".format(i.name)),

        Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            desc="move focused window to group {}".format(i.name)),
    ])
                    
groups.append(
    ScratchPad(
        'scratchpad',
        [
            DropDown(
                'mixer',
                'pavucontrol',
                width=0.4,
                height=0.6,
                x=0.3,
                y=0.1,
                opacity=1
            ),
        ]
    )
)

keys.extend([
    Key(["control"], "1", lazy.group['scratchpad'].dropdown_toggle('term')),
    Key(["control"], "2", lazy.group['scratchpad'].dropdown_toggle('mixer')),
    Key(["control"], "3", lazy.group['scratchpad'].dropdown_toggle('pomodoro')),
    Key(["control"], "4", lazy.group['scratchpad'].dropdown_toggle('blueman')),
])
        
# ██╗      █████╗ ██╗   ██╗ ██████╗ ██╗   ██╗████████╗███████╗
# ██║     ██╔══██╗╚██╗ ██╔╝██╔═══██╗██║   ██║╚══██╔══╝██╔════╝
# ██║     ███████║ ╚████╔╝ ██║   ██║██║   ██║   ██║   ███████╗
# ██║     ██╔══██║  ╚██╔╝  ██║   ██║██║   ██║   ██║   ╚════██║
# ███████╗██║  ██║   ██║   ╚██████╔╝╚██████╔╝   ██║   ███████║
# ╚══════╝╚═╝  ╚═╝   ╚═╝    ╚═════╝  ╚═════╝    ╚═╝   ╚══════╝

layouts = [
    Columns(
        border_normal=gruvbox['bg1'],
        border_focus=gruvbox['red'],
        border_width=2,
        border_normal_stack=gruvbox['bg1'],
        border_focus_stack=gruvbox['red'],
        border_on_single=2,
        margin=8,
        margin_on_single=10,
    ),
    Stack(
        border_normal=gruvbox['bg1'],
        border_focus=gruvbox['red'],
        border_width=2,
        num_stacks=1,
        margin=10,
    ),
]

floating_layout = Floating(
    border_normal=gruvbox['bg1'],
    border_focus=gruvbox['red'],
    border_width=2,
    float_rules=[
        *Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)

mouse = [
    Drag(
        [mod], 
        "Button1", 
        lazy.window.set_position_floating(), 
        start=lazy.window.get_position()
    ),
    Drag(
        [mod], 
        "Button3", 
        lazy.window.set_size_floating(), 
        start=lazy.window.get_size()
    ),
    Click(
        [mod], 
        "Button2", 
        lazy.window.bring_to_front()
    ),
]

widget_defaults = dict(
    font='JetBrainsMono Nerd Font',
    fontsize=12,
    padding=10,
    background=gruvbox['bg'],
)

extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar,
        wallpaper='~/Documents/wallpapers/red-samurai-wallpaper.png',
        wallpaper_mode='stretch',
    ),
    Screen(
        wallpaper='~/Documents/wallpapers/red-samurai-wallpaper.png',
        wallpaper_mode='stretch',
    ),
    Screen(
        wallpaper='~/Documents/wallpapers/red-samurai-wallpaper.png',
        wallpaper_mode='stretch',
    ),
]

dgroups_key_binder = None
dgroups_app_rules = []
follow_mouse_focus = False
bring_front_click = ''
cursor_warp = False
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True
auto_minimize = True
wmname = "LG3D"


# ██╗  ██╗ ██████╗  ██████╗ ██╗  ██╗███████╗
# ██║  ██║██╔═══██╗██╔═══██╗██║ ██╔╝██╔════╝
# ███████║██║   ██║██║   ██║█████╔╝ ███████╗
# ██╔══██║██║   ██║██║   ██║██╔═██╗ ╚════██║
# ██║  ██║╚██████╔╝╚██████╔╝██║  ██╗███████║
# ╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚══════╝

# Runs the autostart script
@hook.subscribe.startup_once
def autostart():
    home=os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.Popen([home])
