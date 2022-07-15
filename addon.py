import xbmc
import xbmcaddon
import xbmcvfs


def main():
    monitor = xbmc.Monitor()

    while not monitor.abortRequested():
        updateBookings()
        if monitor.waitForAbort(3*60*60):
            break

def updateBookings():
    addonID = xbmcaddon.Addon('script.anezl.adrocorder')
    recorderScript = xbmcvfs.translatePath(addonID.getAddonInfo("path" + "/addon.py"))
    xbmc.executebuiltin("XBMC.RunScript(recorderScript, updateBookings)")


if __name__ == "__main__":
    main()