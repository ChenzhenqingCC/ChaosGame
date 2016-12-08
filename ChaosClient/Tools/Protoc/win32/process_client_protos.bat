protoc -I=..\..\Server\protocol --cpp_out=..\..\Test\Classes\Proto ..\..\Server\protocol\cs_protocol.proto
protoc -I=..\..\Server\Data --cpp_out=..\..\Test\Classes\GameData ..\..\Server\Data\gameconfig.proto
protoc -I=..\..\Server\Data --cpp_out=..\..\Test\Classes\GameData ..\..\Server\Data\square.proto
protoc -I=..\..\Server\Data --cpp_out=..\..\Test\Classes\GameData ..\..\Server\Data\formation.proto
protoc -I=..\..\Server\Data --cpp_out=..\..\Test\Classes\GameData ..\..\Server\Data\weight.proto
protoc -I=..\..\Server\Data --cpp_out=..\..\Test\Classes\GameData ..\..\Server\Data\character.proto
protoc -I=..\..\Server\Data --cpp_out=..\..\Test\Classes\GameData ..\..\Server\Data\skill.proto
protoc -I=..\..\Server\Data --cpp_out=..\..\Test\Classes\GameData ..\..\Server\Data\stage.proto
protoc -I=..\..\Server\Data --cpp_out=..\..\Test\Classes\GameData ..\..\Server\Data\battle_show.proto

xcopy ..\..\Server\Data\gameconfig.db ..\..\Test\Resources\GameData /D /Y
xcopy ..\..\Server\Data\square ..\..\Test\Resources\GameData\square /D /I /E /Y
xcopy ..\..\Server\Data\formation ..\..\Test\Resources\GameData\formation /D /I /E /Y
xcopy ..\..\Server\Data\weight ..\..\Test\Resources\GameData\weight /D /I /E /Y
xcopy ..\..\Server\Data\character ..\..\Test\Resources\GameData\character /D /I /E /Y
xcopy ..\..\Server\Data\skill ..\..\Test\Resources\GameData\skill /D /I /E /Y
xcopy ..\..\Server\Data\stage ..\..\Test\Resources\GameData\stage /D /I /E /Y
xcopy ..\..\Server\Data\battle_show ..\..\Test\Resources\GameData\battle_show /D /I /E /Y