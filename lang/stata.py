import time
from talon.voice import  Context, Key, Str, press

from ..utils import is_filetype

FILETYPES = (".do")

ctx = Context("stata", func=is_filetype(FILETYPES))


ctx.keymap(
    {
        "execute": [Key("shift+cmd+d")],

        # commands for commenting
        "slashy":[Key("/ / /")],
        "comment start":[Key("/ *")],
        "comment end":[Key("* /")],
        "section break":[Key("* * * - - - - - - - - - - - - - - - - - - - - - - - - - - * * *")],
    }
)
