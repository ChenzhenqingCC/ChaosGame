set LAN=tha
rd /s /q ..\..\Client\Output\data\obj\ccb\comeff\texture\work
md ..\..\Client\Output\data\obj\ccb\comeff\texture\work
xcopy /Y /Q /R /E ..\..\..\ChaosArt\res\loc\%LAN%\effect_editor\comeff\texture\comefftitle ..\..\Client\Output\data\obj\ccb\comeff\texture\work\comefftitle\
TexturePacker --texture-format png --allow-free-size --size-constraints POT --force-squared --enable-rotation --opt RGBA8888 --data ..\..\Client\Output\loc\%LAN%\data\obj\ccb\comeff\texture/comefftitle.plist --format cocos2d --sheet ..\..\Client\Output\loc\%LAN%\data\obj\ccb\comeff\texture/comefftitle.png ..\..\Client\Output\data\obj\ccb\comeff\texture\work
rd /s /q ..\..\Client\Output\data\obj\ccb\comeff\texture\work
pause