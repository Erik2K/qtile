from libqtile.bar import Bar

from libqtile.widget.groupbox import GroupBox
from libqtile.widget.clock import Clock
from libqtile.widget.spacer import Spacer
from libqtile.widget.textbox import TextBox
from libqtile.widget.battery import Battery
from libqtile.widget.pulse_volume import PulseVolume


from colors import gruvbox
from unicodes import right_arrow, left_arrow

bar = Bar([
    TextBox(
        '󰣇',
        background=gruvbox['red'],
        foreground=gruvbox['fg'],
        fontsize=28,
    ),
    
    right_arrow(gruvbox['bg1'], gruvbox['red']),
    
    GroupBox(
        font='JetBrainsMono Nerd Font Mono',
        fontsize=27,
        padding_x=3,
        padding_y=5,
        rounded=False,
        center_aligned=True,
        disable_drag=True,
        borderwidth=3,
        highlight_method="line",
        active=gruvbox["fg"],
        inactive=gruvbox["fg"],
        highlight_color=gruvbox["bg1"],
        this_current_screen_border=gruvbox["red"],
        this_screen_border=gruvbox["red"],
        other_screen_border=gruvbox["red"],
        other_current_screen_border=gruvbox["red"],
        background=gruvbox["bg1"],
        foreground=gruvbox["fg"],
    ),
    
    right_arrow(gruvbox['bg'], gruvbox['bg1']),

    Spacer(length=1210),
    
    left_arrow(gruvbox['bg'], gruvbox['dark-yellow']),
    
    PulseVolume(
        fmt="󰕾 {}",
        fontsize=14,
        foreground=gruvbox["bg"],
        background=gruvbox["dark-yellow"],
        padding=10,
    ),
    
    left_arrow(gruvbox['dark-yellow'], gruvbox['dark-blue']),

    Battery(
        format='󰁿 {percent:2.0%}',
        foreground=gruvbox['fg'],
        background=gruvbox['dark-blue'],
        fontsize=14,
    ),

    left_arrow(gruvbox['dark-blue'], gruvbox['fg']),

    Clock(
        format=' %a %d %b %H:%M',
        background=gruvbox['fg'],
        foreground=gruvbox['bg'],
        fontsize=14,
    ),
],
    30,
    margin=[6, 10, 6, 10],
    border_width=[0, 0, 0, 0],
)