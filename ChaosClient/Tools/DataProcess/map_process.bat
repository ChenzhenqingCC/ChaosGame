@echo off
set "mapid=terrain_0101 terrain_0102 terrain_0103 terrain_0104 terrain_0105 terrain_0106 terrain_0107 terrain_0108 terrain_0109 terrain_0110"
set mapname=terrain_0100
set maptype=grass
set inputTypePath=..\..\..\ChaosArt\res\map_editor\texture\%maptype%
set outputTypePath=..\..\Client\Output\data\map\texture\%maptype%
set inputPath=..\..\..\ChaosArt\res\map_editor\texture\%mapname%\tile
set outputPath=..\..\Client\Output\data\map\texture\%mapname%\tile
for %%a in (%mapid%) do (md ..\..\Client\Output\data\map\%%a&del /F /Q ..\..\Client\Output\data\map\%%a\%%a.tmx&xcopy /Y /Q /R ..\..\..\ChaosArt\res\map_editor\%%a\%%a.tmx ..\..\Client\Output\data\map\%%a\)
md %outputTypePath%
del /F /Q %cd%\%outputTypePath%\%maptype%.plist
del /F /Q %cd%\%outputTypePath%\%maptype%.png
del /F /Q %cd%\%outputTypePath%\%maptype%.pvr.ccz
TexturePacker --max-size 4096 --allow-free-size --size-constraints POT --force-squared --texture-format png --opt RGBA8888 --data %cd%/%outputTypePath%/%maptype%.plist --format cocos2d --sheet %cd%/%outputTypePath%/%maptype%.png %cd%/%inputTypePath%
rd /s /q %outputPath%
ResConverter map %inputPath% %outputPath%
call ResConverter_bat
del .\ResConverter_bat.bat /Q /F
pause