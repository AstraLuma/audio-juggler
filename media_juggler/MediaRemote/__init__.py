"""
https://stackoverflow.com/questions/61003379/how-to-get-currently-playing-song-on-mac-swift
https://iphonedevwiki.net/index.php/MediaRemote.framework
"""

import objc as _objc            # type:ignore[import]
from warnings import catch_warnings as _catch

with _catch():
    # There's a deprecation warning on this asking me to use the "new metadata
    # system", but this system is undocumented and given issues like
    # https://github.com/ronaldoussoren/objective.metadata/issues/6 not really
    # ready for third-party use yet, so we're just going to squash the warning
    # for now.

    __bundle__ = _objc.initFrameworkWrapper(
        __name__,
        frameworkIdentifier='com.apple.MediaRemote',
        frameworkPath=_objc.pathForFramework(
            "/System/Library/PrivateFrameworks/MediaRemote.framework"
        ),
        globals=globals(),
    )
