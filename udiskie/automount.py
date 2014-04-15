"""
Udiskie automounter daemon.
"""

__all__ = ['AutoMounter']


class AutoMounter(object):

    """
    Automatically mount newly added media.
    """

    def __init__(self, mounter):
        self._mounter = mounter
        mounter.udisks.connect_all(self)

    def device_added(self, udevice):
        self._mounter.add(udevice)

    def media_added(self, udevice):
        self._mounter.add(udevice)

    def device_changed(self, old_state, new_state):
        """
        Check whether is_external changed, then mount
        """
        # udisks2 sometimes adds empty devices and later updates them so
        # the is_external becomes true:
        if not old_state.is_external and new_state.is_external:
            self._mounter.add(new_state)

