from quickmachotkey import quickHotKey, mask
from quickmachotkey.constants import kVK_ANSI_O, kVK_F18, cmdKey, controlKey, optionKey, shiftKey


@quickHotKey(virtualKey=kVK_F18, modifierMask=mask())
def handle_pause() -> None:
    print("pause music")


@quickHotKey(virtualKey=kVK_ANSI_O, modifierMask=mask(cmdKey, controlKey, optionKey, shiftKey))
def handle_play() -> None:
    print("play music")


def main():
    from AppKit import NSApplication  # type:ignore[import]
    from PyObjCTools import AppHelper  # type:ignore[import]
    NSApplication.sharedApplication()
    AppHelper.runEventLoop()
