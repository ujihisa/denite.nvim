# ============================================================================
# FILE: base.py
# AUTHOR: Shougo Matsushita <Shougo.Matsu at gmail.com>
# License: MIT license
# ============================================================================

from pynvim import Nvim

from denite.base.kind import Base as _Base


class Base(_Base):
    def __init__(self, vim: Nvim) -> None:
        super().__init__(vim)
