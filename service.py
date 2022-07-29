import xbmc
import xbmcaddon
import xbmcvfs


def main():
    logWrite('Starting adrocorder service')
    monitor = xbmc.Monitor()

    while not monitor.abortRequested():
        logWrite('monitoring for abortRequested')
        updateBookings()
        epgUpdateDelta = int(xbmcaddon.Addon('script.anezl.adrocorder').getSetting('epgUpdateDelta')) * 3600 - 900
        logWrite(f'Waiting for {epgUpdateDelta} seconds ({epgUpdateDelta/3600} hours)')
        if monitor.waitForAbort(epgUpdateDelta):
            break

def updateBookings():
    addonID = xbmcaddon.Addon('script.anezl.adrocorder')
    recorderScript = xbmcvfs.translatePath(addonID.getAddonInfo('path') + 'addon.py')
    logWrite(f'trying to run script: {recorderScript}')
    xbmc.executebuiltin(f"RunScript(script.anezl.adrocorder, updateBookings)")


def logWrite(stuff2Log):
    xbmc.log(str(stuff2Log), level=xbmc.LOGINFO)

if __name__ == "__main__":
    main()