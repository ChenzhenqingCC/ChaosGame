############################################################
#	icon data process
############################################################

# clear icon
rd /s /q ..\..\Client\Output\data\obj\icon
md ..\..\Client\Output\data\obj\icon

#copy icons
xcopy /Y /Q /R /E /exclude:exclude_normal.txt ..\..\..\ChaosArt\res\icons ..\..\Client\Output\data\obj\icon

# navimap batch
TexturePacker --allow-free-size --size-constraints POT --texture-format png --opt RGBA8888 --data ..\..\Client\Output\data\obj\icon\navi_work\ui_battle_navicon.plist --format cocos2d --sheet ..\..\Client\Output\data\obj\icon\navi_work\ui_battle_navicon.png ..\..\Client\Output\data\obj\icon\navi
rd /s /q ..\..\Client\Output\data\obj\icon\navi
md ..\..\Client\Output\data\obj\icon\navi
xcopy /Y /Q /R /E ..\..\Client\Output\data\obj\icon\navi_work\*.* ..\..\Client\Output\data\obj\icon\navi
rd /s /q ..\..\Client\Output\data\obj\icon\navi_work
