import time
from talon.voice import  Context, Key, Str, press

from ..utils import is_filetype, normalise_keys, surround

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


surrounders = normalise_keys(
    {
        "comment out": (False, surround("/*", "*/")),
    }
)
