import xbmc

if xbmc.getCondVisibility("System.HasNetwork"):
    xbmc.executebuiltin("XBMC.RunScript(Q:/scripts/cortanaPlayerCount/getnews.py)")
    xbmc.executebuiltin("XBMC.RunScript(Q:/scripts/cortanaPlayerCount/playercount.py)")
else:
    xbmc.log("Network not available, getting player count and news failed!", xbmc.LOGNOTICE)
