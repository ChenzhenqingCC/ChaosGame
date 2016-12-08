############################################################
#	ui ccb data process
############################################################

#copy ccbi
xcopy /Y /Q /R /E /exclude:exclude_normal.txt ..\..\..\ChaosArt\res\ui_editor_publish\*.ccbi ..\..\Client\Output\data\ccb\
