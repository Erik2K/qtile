import os
import subprocess

from libqtile import bar, hook, extension
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
    # Move window focus
    Key([mod], "h", lazy.layout.left()),
    Key([mod], "l", lazy.layout.right()),
    Key([mod], "j", lazy.layout.down()),
    Key([mod], "k", lazy.layout.up()),
    Key([mod], "space", lazy.layout.next()),
    
    # Move window
    Key([mod, "shift"], "h", lazy.layout.shuffle_left()),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right()),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down()),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up()),
    
    # Grow window
    Key([mod, "control"], "h", lazy.layout.grow_left()),
    Key([mod, "control"], "l", lazy.layout.grow_right()),
    Key([mod, "control"], "j", lazy.layout.grow_down()),
    Key([mod, "control"], "k", lazy.layout.grouw_up()),
    
    # Reset all window sizes
    Key([mod], "n", lazy.layout.normalize()),
    
    # Toggle fullscreen window
    Key([mod], "f", lazy.window.toggle_fullscreen()),
    
    # Toggle floating window
    Key([mod, "shift"], "space", lazy.window.toggle_floating()),
    
    #  Kill focused window
    Key([mod], "w", lazy.window.kill()),
    
    # Move screen focus
    Key([mod], "Right", lazy.next_screen()),
    
    # Split stack layout
    Key([mod, "shift"], "Return", lazy.layout.toggle_split()),

    # Toggle layouts
    Key([mod], "Tab", lazy.next_layout()),

    # Launch terminal
    Key([mod], "Return", lazy.spawn(terminal)),

    # Launch dmenu
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
    
    # Reload qtile config
    Key([mod, "control"], "r", lazy.reload_config()),
]

#  ██████╗ ██████╗  ██████╗ ██╗   ██╗██████╗ ███████╗
# ██╔════╝ ██╔══██╗██╔═══██╗██║   ██║██╔══██╗██╔════╝
# ██║  ███╗██████╔╝██║   ██║██║   ██║██████╔╝███████╗
# ██║   ██║██╔══██╗██║   ██║██║   ██║██╔═══╝ ╚════██║
# ╚██████╔╝██║  ██║╚██████╔╝╚██████╔╝██║     ███████║
#  ╚═════╝ ╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═╝     ╚══════╝                                            

groups = [
    Group(
        "1",
        label="",
        layout="columns",
        matches=[Match(wm_class=["Alacritty", "Alacritty"])],
    ),
    Group(
        "2",
        label="󰨞",
        layout="columns",   
        matches=[Match(wm_class=["code", "Code"])],
    ),
    Group(
        "3",
        label="",
        layout="columns",
        matches=[Match(wm_class=["google-chrome", "Google-chrome"])],
    ),
    Group(
        "4",
        label="",
        layout="columns",
    ),
    Group(
        "5",
        label="󰡨",
        layout="columns",
    ),
    Group(
        "6",
        label="󰙯",
        layout="columns",
        matches=[Match(wm_class=["discord", "discord"])],
    ),
    Group(
        "7",
        label="",
        layout="columns",
        matches=[Match(wm_class=["spotify", "Spotify"])],
    ),
    Group(
        "8",
        label="",
        layout="columns",
    ),
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
                'net',
                'alacritty -e "nmtui"',
                width=0.4,
                height=0.6,
                x=0.3,
                y=0.1,
                opacity=1
            ),
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
    Key([mod,"control"], "1", lazy.group['scratchpad'].dropdown_toggle('net')),
    Key([mod, "control"], "2", lazy.group['scratchpad'].dropdown_toggle('mixer')),
])
        
# ██╗      █████╗ ██╗   ██╗ ██████╗ ██╗   ██╗████████╗███████╗
# ██║     ██╔══██╗╚██╗ ██╔╝██╔═══██╗██║   ██║╚══██╔══╝██╔════╝
# ██║     ███████║ ╚████╔╝ ██║   ██║██║   ██║   ██║   ███████╗
# ██║     ██╔══██║  ╚██╔╝  ██║   ██║██║   ██║   ██║   ╚════██║
# ███████╗██║  ██║   ██║   ╚██████╔╝╚██████╔╝   ██║   ███████║
# ╚══════╝╚═╝  ╚═╝   ╚═╝    ╚═════╝  ╚═════╝    ╚═╝   ╚══════╝

layouts = [
    Columns(
        border_normal=gruvbox['bg'],
        border_focus=gruvbox['bg3'],
        border_width=2,
        border_normal_stack=gruvbox['bg'],
        border_focus_stack=gruvbox['bg3'],
        border_on_single=2,
        margin=8,
        margin_on_single=10,
    ),
    Stack(
        border_normal=gruvbox['bg'],
        border_focus=gruvbox['bg3'],
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
        wallpaper='~/.config/qtile/wallpapers/red-samurai-wallpaper.png',
        wallpaper_mode='stretch',
    ),
    Screen(
        wallpaper='~/.config/qtile/wallpapers/red-samurai-wallpaper.png',
        wallpaper_mode='stretch',
    ),
    Screen(
        wallpaper='~/.config/qtile/wallpapers/red-samurai-wallpaper.png',
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
