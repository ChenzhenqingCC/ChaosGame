rd /s /q ..\..\Client\Output
md ..\..\Client\Output
xcopy /Y /Q /R /E \\192.168.1.251\share\publish\pc_pub\*.* ..\..\Client\Output\
xcopy /Y /Q /R /E \\192.168.1.251\share\publish\pc\*.* ..\..\Client\Output\
