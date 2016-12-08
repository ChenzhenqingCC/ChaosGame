@echo off
set "mapid=terrain_9999"
set mapname=terrain_0100
set maptype=arena
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

set "mapid=terrain_9999"
set mapname=terrain_0200
set maptype=dark
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

set "mapid=terrain_9999"
set mapname=terrain_0300
set maptype=desert
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

set "mapid=terrain_9999"
set mapname=terrain_0500
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

set "mapid=terrain_9999"
set mapname=terrain_0800
set maptype=lava
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

set "mapid=terrain_9999"
set mapname=terrain_1100
set maptype=main
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

set "mapid=terrain_9999"
set mapname=terrain_6000
set maptype=snow
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

set "mapid=terrain_9999"
set mapname=terrain_8000
set maptype=stageselect
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

set "mapid=terrain_9999"
set mapname=terrain_9800
set maptype=stsm
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

set "mapid=terrain_9999"
set mapname=terrain_9900
set maptype=swamp
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