############################################################
#	ui ccb data process
############################################################
# clear data/ccb
rd /s /q ..\..\Client\Output\data\ccb
md ..\..\Client\Output\data\ccb

#copy ccbi
xcopy /Y /Q /R /E /exclude:exclude_normal.txt ..\..\..\ChaosArt\res\ui_editor_publish\*.ccbi ..\..\Client\Output\data\ccb\

#copy font
md ..\..\Client\Output\data\ccb\font
xcopy /Y /Q /R /E /exclude:exclude_normal.txt ..\..\..\ChaosArt\res\ui_editor\font\*.ttf ..\..\Client\Output\data\ccb\font\

#copy number/bmfont
md ..\..\Client\Output\data\ccb\number
xcopy /Y /Q /R /E /exclude:exclude_normal.txt ..\..\..\ChaosArt\res\ui_editor\number\*.png ..\..\Client\Output\data\ccb\number\
xcopy /Y /Q /R /E /exclude:exclude_normal.txt ..\..\..\ChaosArt\res\ui_editor\number\*.fnt ..\..\Client\Output\data\ccb\number\
md ..\..\Client\Output\data\ccb\bmfont
xcopy /Y /Q /R /E /exclude:exclude_normal.txt ..\..\..\ChaosArt\res\ui_editor\bmfont\*.png ..\..\Client\Output\data\ccb\bmfont\
xcopy /Y /Q /R /E /exclude:exclude_normal.txt ..\..\..\ChaosArt\res\ui_editor\bmfont\*.fnt ..\..\Client\Output\data\ccb\bmfont\

#make texture/.. 
ResConverter ui ..\..\..\ChaosArt\res\ui_editor ..\..\Client\Output\data\ccb
call ResConverter_bat
