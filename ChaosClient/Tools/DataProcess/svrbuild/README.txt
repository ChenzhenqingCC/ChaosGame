一.安装vbp

二.服务器release版本构建
cd dir
set PATH=%PATH%;C:\Program Files (x86)\VisBuildPro8
VisBuildCmd ServerBuild.bld %ZONE%=1 %VERSION%=1.2.3.4

二.服务器开发版本策划资源热更新
cd dir
set PATH=%PATH%;C:\Program Files (x86)\VisBuildPro8
VisBuildCmd HotfixRes.bld