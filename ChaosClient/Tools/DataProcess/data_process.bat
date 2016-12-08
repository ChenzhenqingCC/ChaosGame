####################################################################################
#	Convert all data to be used by game
####################################################################################
#ui data
call UITexturePack.bat

#map data
FileListGen ../../Client/Output data/map/background/bg_8000_01 .png_.plist_.pvr.ccz_.pkm tex resources-
FileListGen ../../Client/Output data/map/background/bg_01 .png_.plist_.pvr.ccz_.pkm tex resources-
FileListGen ../../Client/Output data/map/background/bg_03 .png_.plist_.pvr.ccz_.pkm tex resources-
FileListGen ../../Client/Output data/map/background/bg_square .png_.plist_.pvr.ccz_.pkm tex resources-
FileListGen ../../Client/Output data/map/background/bg_04 .png_.plist_.pvr.ccz_.pkm tex resources-
FileListGen ../../Client/Output data/map/background/bg_05 .png_.plist_.pvr.ccz_.pkm tex resources-
FileListGen ../../Client/Output data/map/background/bg_06 .png_.plist_.pvr.ccz_.pkm tex resources-
FileListGen ../../Client/Output data/map/texture/grass .png_.plist_.pvr.ccz_.pkm tex resources-
FileListGen ../../Client/Output data/map/texture/main .png_.plist_.pvr.ccz_.pkm tex resources-
FileListGen ../../Client/Output data/map/texture/stsm .png_.plist_.pvr.ccz_.pkm tex resources-
FileListGen ../../Client/Output data/map/texture/dark .png_.plist_.pvr.ccz_.pkm tex resources-
FileListGen ../../Client/Output data/map/texture/stageselect .png_.plist_.pvr.ccz_.pkm tex resources-
FileListGen ../../Client/Output data/map/texture/desert .png_.plist_.pvr.ccz_.pkm tex resources-
FileListGen ../../Client/Output data/map/texture/swamp .png_.plist_.pvr.ccz_.pkm tex resources-
FileListGen ../../Client/Output data/map/texture/lava .png_.plist_.pvr.ccz_.pkm tex resources-
FileListGen ../../Client/Output data/map/texture/city .png_.plist_.pvr.ccz_.pkm tex resources-
FileListGen ../../Client/Output data/map/texture/arena .png_.plist_.pvr.ccz_.pkm tex resources-
FileListGen ../../Client/Output data/map/texture/island .png_.plist_.pvr.ccz_.pkm tex resources-
FileListGen ../../Client/Output data/map/texture/ice .png_.plist_.pvr.ccz_.pkm tex resources-
FileListGen ../../Client/Output data/map/texture/redplateau .png_.plist_.pvr.ccz_.pkm tex resources-

# char and effect data(auto generate)
ResConverter effect ..\..\..\ChaosArt\res\effect_editor_publish\comeff ..\..\Client\Output\data\obj\ccb\comeff
call ResConverter_bat
ResConverter effect ..\..\..\ChaosArt\res\effect_editor_publish\mireff ..\..\Client\Output\data\obj\ccb\mireff
call ResConverter_bat
ResConverter effect ..\..\..\ChaosArt\res\effect_editor_publish\miseff ..\..\Client\Output\data\obj\ccb\miseff
call ResConverter_bat
ResConverter effect ..\..\..\ChaosArt\res\effect_editor_publish\skieff ..\..\Client\Output\data\obj\ccb\skieff
call ResConverter_bat
rd /s /q ..\..\Client\Output\data\obj\spine
md ..\..\Client\Output\data\obj\spine
ResConverter spine ..\..\..\ChaosArt\res\char_editor ..\..\Client\Output\data\obj\spine
call ResConverter_bat
ResConverter spine ..\..\..\ChaosArt\res\item_editor ..\..\Client\Output\data\obj\spine
call ResConverter_bat
del .\ResConverter_bat.bat /Q /F
pause
