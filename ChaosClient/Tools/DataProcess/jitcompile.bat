rd /s /q .\..\..\Client\Output\data\export_obj
md .\..\..\Client\Output\data\export_obj
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\booter.lua .\..\..\Client\Output\data\export_obj\booter.obj
md .\..\..\Client\Output\data\export_obj\libraries
md .\..\..\Client\Output\data\export_obj\libraries\base
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\libraries\base\List.lua .\..\..\Client\Output\data\export_obj\libraries\base\List.obj
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\libraries\base\Math.lua .\..\..\Client\Output\data\export_obj\libraries\base\Math.obj
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\libraries\base\String.lua .\..\..\Client\Output\data\export_obj\libraries\base\String.obj
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\libraries\base\Tween.lua .\..\..\Client\Output\data\export_obj\libraries\base\Tween.obj
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\libraries\base\Util.lua .\..\..\Client\Output\data\export_obj\libraries\base\Util.obj
md .\..\..\Client\Output\data\export_obj\libraries\behavior
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\libraries\behavior\Behavior.lua .\..\..\Client\Output\data\export_obj\libraries\behavior\Behavior.obj
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\libraries\behavior\BehaviorDefines.lua .\..\..\Client\Output\data\export_obj\libraries\behavior\BehaviorDefines.obj
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\libraries\behavior\BehaviorGroup.lua .\..\..\Client\Output\data\export_obj\libraries\behavior\BehaviorGroup.obj
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\libraries\behavior\BehaviorObject.lua .\..\..\Client\Output\data\export_obj\libraries\behavior\BehaviorObject.obj
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\libraries\behavior\Operation.lua .\..\..\Client\Output\data\export_obj\libraries\behavior\Operation.obj
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\libraries\behavior\OperationDefines.lua .\..\..\Client\Output\data\export_obj\libraries\behavior\OperationDefines.obj
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\libraries\behavior\OperationGroup.lua .\..\..\Client\Output\data\export_obj\libraries\behavior\OperationGroup.obj
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\libraries\behavior\OperationObject.lua .\..\..\Client\Output\data\export_obj\libraries\behavior\OperationObject.obj
md .\..\..\Client\Output\data\export_obj\libraries\cinematics
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\libraries\cinematics\Cinema.custom.lua .\..\..\Client\Output\data\export_obj\libraries\cinematics\Cinema.custom.obj
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\libraries\cinematics\Cinema.dialog.lua .\..\..\Client\Output\data\export_obj\libraries\cinematics\Cinema.dialog.obj
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\libraries\cinematics\Cinema.environment.lua .\..\..\Client\Output\data\export_obj\libraries\cinematics\Cinema.environment.obj
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\libraries\cinematics\Cinema.event.lua .\..\..\Client\Output\data\export_obj\libraries\cinematics\Cinema.event.obj
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\libraries\cinematics\Cinema.input.lua .\..\..\Client\Output\data\export_obj\libraries\cinematics\Cinema.input.obj
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\libraries\cinematics\Cinema.screen.lua .\..\..\Client\Output\data\export_obj\libraries\cinematics\Cinema.screen.obj
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\libraries\cinematics\Cinema.sound.lua .\..\..\Client\Output\data\export_obj\libraries\cinematics\Cinema.sound.obj
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\libraries\cinematics\Cinema.trigger.lua .\..\..\Client\Output\data\export_obj\libraries\cinematics\Cinema.trigger.obj
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\libraries\cinematics\CinemaData.lua .\..\..\Client\Output\data\export_obj\libraries\cinematics\CinemaData.obj
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\libraries\cinematics\Cinematics.layer.lua .\..\..\Client\Output\data\export_obj\libraries\cinematics\Cinematics.layer.obj
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\libraries\cinematics\Cinematics.lua .\..\..\Client\Output\data\export_obj\libraries\cinematics\Cinematics.obj
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\libraries\cinematics\Cinematics.timeline.lua .\..\..\Client\Output\data\export_obj\libraries\cinematics\Cinematics.timeline.obj
md .\..\..\Client\Output\data\export_obj\libraries\cinematics\custom
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\libraries\cinematics\custom\fade.lua .\..\..\Client\Output\data\export_obj\libraries\cinematics\custom\fade.obj
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\libraries\cinematics\custom\story.lua .\..\..\Client\Output\data\export_obj\libraries\cinematics\custom\story.obj
md .\..\..\Client\Output\data\export_obj\libraries\cocos2dx
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\libraries\cocos2dx\AudioEngine.lua .\..\..\Client\Output\data\export_obj\libraries\cocos2dx\AudioEngine.obj
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\libraries\cocos2dx\CCBReaderLoad.lua .\..\..\Client\Output\data\export_obj\libraries\cocos2dx\CCBReaderLoad.obj
md .\..\..\Client\Output\data\export_obj\libraries\data
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\libraries\data\Database.lua .\..\..\Client\Output\data\export_obj\libraries\data\Database.obj
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\libraries\data\persistence.lua .\..\..\Client\Output\data\export_obj\libraries\data\persistence.obj
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\libraries\data\TableData.lua .\..\..\Client\Output\data\export_obj\libraries\data\TableData.obj
md .\..\..\Client\Output\data\export_obj\libraries\draw
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\libraries\draw\BatchSprite.lua .\..\..\Client\Output\data\export_obj\libraries\draw\BatchSprite.obj
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\libraries\draw\CCBNode.lua .\..\..\Client\Output\data\export_obj\libraries\draw\CCBNode.obj
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\libraries\draw\FileData.lua .\..\..\Client\Output\data\export_obj\libraries\draw\FileData.obj
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\libraries\draw\ImeButton.lua .\..\..\Client\Output\data\export_obj\libraries\draw\ImeButton.obj
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\libraries\draw\Input.lua .\..\..\Client\Output\data\export_obj\libraries\draw\Input.obj
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\libraries\draw\LineSprite.lua .\..\..\Client\Output\data\export_obj\libraries\draw\LineSprite.obj
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\libraries\draw\Map.lua .\..\..\Client\Output\data\export_obj\libraries\draw\Map.obj
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\libraries\draw\NetData.lua .\..\..\Client\Output\data\export_obj\libraries\draw\NetData.obj
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\libraries\draw\Node.lua .\..\..\Client\Output\data\export_obj\libraries\draw\Node.obj
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\libraries\draw\PackageData.lua .\..\..\Client\Output\data\export_obj\libraries\draw\PackageData.obj
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\libraries\draw\PiechartSprite.lua .\..\..\Client\Output\data\export_obj\libraries\draw\PiechartSprite.obj
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\libraries\draw\ProgressData.lua .\..\..\Client\Output\data\export_obj\libraries\draw\ProgressData.obj
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\libraries\draw\RendererTexture.lua .\..\..\Client\Output\data\export_obj\libraries\draw\RendererTexture.obj
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\libraries\draw\ScrollView.lua .\..\..\Client\Output\data\export_obj\libraries\draw\ScrollView.obj
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\libraries\draw\ShakeObject.lua .\..\..\Client\Output\data\export_obj\libraries\draw\ShakeObject.obj
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\libraries\draw\SoapSprite.lua .\..\..\Client\Output\data\export_obj\libraries\draw\SoapSprite.obj
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\libraries\draw\Spine.lua .\..\..\Client\Output\data\export_obj\libraries\draw\Spine.obj
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\libraries\draw\Sprite.lua .\..\..\Client\Output\data\export_obj\libraries\draw\Sprite.obj
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\libraries\draw\StreakSprite.lua .\..\..\Client\Output\data\export_obj\libraries\draw\StreakSprite.obj
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\libraries\draw\TableList.lua .\..\..\Client\Output\data\export_obj\libraries\draw\TableList.obj
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\libraries\draw\Text.lua .\..\..\Client\Output\data\export_obj\libraries\draw\Text.obj
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\libraries\draw\TextAtlas.lua .\..\..\Client\Output\data\export_obj\libraries\draw\TextAtlas.obj
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\libraries\draw\View.lua .\..\..\Client\Output\data\export_obj\libraries\draw\View.obj
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\libraries\draw\View3D.lua .\..\..\Client\Output\data\export_obj\libraries\draw\View3D.obj
md .\..\..\Client\Output\data\export_obj\libraries\event
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\libraries\event\DelayCall.lua .\..\..\Client\Output\data\export_obj\libraries\event\DelayCall.obj
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\libraries\event\Event.lua .\..\..\Client\Output\data\export_obj\libraries\event\Event.obj
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\libraries\event\EventFactory.lua .\..\..\Client\Output\data\export_obj\libraries\event\EventFactory.obj
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\libraries\event\EventSystem.lua .\..\..\Client\Output\data\export_obj\libraries\event\EventSystem.obj
md .\..\..\Client\Output\data\export_obj\libraries\network
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\libraries\network\Network.lua .\..\..\Client\Output\data\export_obj\libraries\network\Network.obj
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\libraries\network\protobuf.lua .\..\..\Client\Output\data\export_obj\libraries\network\protobuf.obj
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\libraries\network\Remote.lua .\..\..\Client\Output\data\export_obj\libraries\network\Remote.obj
md .\..\..\Client\Output\data\export_obj\libraries\scene
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\libraries\scene\DataObject.lua .\..\..\Client\Output\data\export_obj\libraries\scene\DataObject.obj
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\libraries\scene\Object.lua .\..\..\Client\Output\data\export_obj\libraries\scene\Object.obj
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\libraries\scene\Scene.lua .\..\..\Client\Output\data\export_obj\libraries\scene\Scene.obj
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\libraries\scene\System.lua .\..\..\Client\Output\data\export_obj\libraries\scene\System.obj
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\libraries\scene\Window.lua .\..\..\Client\Output\data\export_obj\libraries\scene\Window.obj
md .\..\..\Client\Output\data\export_obj\libraries\scope
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\libraries\scope\Scope.lua .\..\..\Client\Output\data\export_obj\libraries\scope\Scope.obj
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\libraries\scope\ScopeData.lua .\..\..\Client\Output\data\export_obj\libraries\scope\ScopeData.obj
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\libraries\scope\ScopeStack.lua .\..\..\Client\Output\data\export_obj\libraries\scope\ScopeStack.obj
md .\..\..\Client\Output\data\export_obj\libraries\sequence
md .\..\..\Client\Output\data\export_obj\libraries\sequence\clip
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\libraries\sequence\clip\Clip.allornone.lua .\..\..\Client\Output\data\export_obj\libraries\sequence\clip\Clip.allornone.obj
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\libraries\sequence\clip\Clip.branch.lua .\..\..\Client\Output\data\export_obj\libraries\sequence\clip\Clip.branch.obj
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\libraries\sequence\clip\Clip.call.lua .\..\..\Client\Output\data\export_obj\libraries\sequence\clip\Clip.call.obj
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\libraries\sequence\clip\Clip.effect.lua .\..\..\Client\Output\data\export_obj\libraries\sequence\clip\Clip.effect.obj
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\libraries\sequence\clip\Clip.group.lua .\..\..\Client\Output\data\export_obj\libraries\sequence\clip\Clip.group.obj
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\libraries\sequence\clip\Clip.jump.lua .\..\..\Client\Output\data\export_obj\libraries\sequence\clip\Clip.jump.obj
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\libraries\sequence\clip\Clip.label.lua .\..\..\Client\Output\data\export_obj\libraries\sequence\clip\Clip.label.obj
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\libraries\sequence\clip\Clip.net.lua .\..\..\Client\Output\data\export_obj\libraries\sequence\clip\Clip.net.obj
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\libraries\sequence\clip\Clip.stock.lua .\..\..\Client\Output\data\export_obj\libraries\sequence\clip\Clip.stock.obj
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\libraries\sequence\clip\Clip.wait.lua .\..\..\Client\Output\data\export_obj\libraries\sequence\clip\Clip.wait.obj
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\libraries\sequence\Sequence.lua .\..\..\Client\Output\data\export_obj\libraries\sequence\Sequence.obj
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\libraries\sequence\SequenceClip.lua .\..\..\Client\Output\data\export_obj\libraries\sequence\SequenceClip.obj
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\libraries\sequence\SequenceMgr.lua .\..\..\Client\Output\data\export_obj\libraries\sequence\SequenceMgr.obj
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\libraries\sequence\SequenceQueue.lua .\..\..\Client\Output\data\export_obj\libraries\sequence\SequenceQueue.obj
md .\..\..\Client\Output\data\export_obj\libraries\sound
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\libraries\sound\Sound.lua .\..\..\Client\Output\data\export_obj\libraries\sound\Sound.obj
md .\..\..\Client\Output\data\export_obj\libraries\task_protocol
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\libraries\task_protocol\TaskFunc.lua .\..\..\Client\Output\data\export_obj\libraries\task_protocol\TaskFunc.obj
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\libraries\task_protocol\TaskProtocol.lua .\..\..\Client\Output\data\export_obj\libraries\task_protocol\TaskProtocol.obj
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\main.lua .\..\..\Client\Output\data\export_obj\main.obj
md .\..\..\Client\Output\data\export_obj\modules
md .\..\..\Client\Output\data\export_obj\modules\loading
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\modules\loading\LoadingMask.lua .\..\..\Client\Output\data\export_obj\modules\loading\LoadingMask.obj
md .\..\..\Client\Output\data\export_obj\modules\movement
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\modules\movement\Action.lua .\..\..\Client\Output\data\export_obj\modules\movement\Action.obj
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\modules\movement\Movement.lua .\..\..\Client\Output\data\export_obj\modules\movement\Movement.obj
md .\..\..\Client\Output\data\export_obj\modules\stage
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\modules\stage\World.lua .\..\..\Client\Output\data\export_obj\modules\stage\World.obj
md .\..\..\Client\Output\data\export_obj\modules\ui
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\modules\ui\MessageBox.lua .\..\..\Client\Output\data\export_obj\modules\ui\MessageBox.obj
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\modules\ui\SimpleChar.lua .\..\..\Client\Output\data\export_obj\modules\ui\SimpleChar.obj
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\modules\ui\ToolTip.Item.lua .\..\..\Client\Output\data\export_obj\modules\ui\ToolTip.Item.obj
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\modules\ui\ToolTip.lua .\..\..\Client\Output\data\export_obj\modules\ui\ToolTip.obj
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\modules\ui\UIPanel.lua .\..\..\Client\Output\data\export_obj\modules\ui\UIPanel.obj
md .\..\..\Client\Output\data\export_obj\modules\user
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\modules\user\User.activity.lua .\..\..\Client\Output\data\export_obj\modules\user\User.activity.obj
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\modules\user\User.actor.lua .\..\..\Client\Output\data\export_obj\modules\user\User.actor.obj
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\modules\user\User.hero.lua .\..\..\Client\Output\data\export_obj\modules\user\User.hero.obj
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\modules\user\User.item.lua .\..\..\Client\Output\data\export_obj\modules\user\User.item.obj
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\modules\user\User.playrecord.lua .\..\..\Client\Output\data\export_obj\modules\user\User.playrecord.obj
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\modules\user\User.stage.lua .\..\..\Client\Output\data\export_obj\modules\user\User.stage.obj
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\modules\user\User.tower.lua .\..\..\Client\Output\data\export_obj\modules\user\User.tower.obj
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\project.lua .\..\..\Client\Output\data\export_obj\project.obj
md .\..\..\Client\Output\data\export_obj\scenes
md .\..\..\Client\Output\data\export_obj\scenes\battle
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\scenes\battle\BattleData.lua .\..\..\Client\Output\data\export_obj\scenes\battle\BattleData.obj
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\scenes\battle\BattleNode.lua .\..\..\Client\Output\data\export_obj\scenes\battle\BattleNode.obj
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\scenes\battle\BattleScene.lua .\..\..\Client\Output\data\export_obj\scenes\battle\BattleScene.obj
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\scenes\battle\BattleVerify.lua .\..\..\Client\Output\data\export_obj\scenes\battle\BattleVerify.obj
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\scenes\battle\BulletTime.lua .\..\..\Client\Output\data\export_obj\scenes\battle\BulletTime.obj
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\scenes\battle\Camera.lua .\..\..\Client\Output\data\export_obj\scenes\battle\Camera.obj
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\scenes\battle\CameraFollow.lua .\..\..\Client\Output\data\export_obj\scenes\battle\CameraFollow.obj
md .\..\..\Client\Output\data\export_obj\scenes\battle\camp
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\scenes\battle\camp\Camp.lua .\..\..\Client\Output\data\export_obj\scenes\battle\camp\Camp.obj
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\scenes\battle\camp\Camp.player.lua .\..\..\Client\Output\data\export_obj\scenes\battle\camp\Camp.player.obj
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\scenes\battle\camp\Camp.spawn.lua .\..\..\Client\Output\data\export_obj\scenes\battle\camp\Camp.spawn.obj
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\scenes\battle\camp\Spot.instant.lua .\..\..\Client\Output\data\export_obj\scenes\battle\camp\Spot.instant.obj
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\scenes\battle\camp\Spot.lua .\..\..\Client\Output\data\export_obj\scenes\battle\camp\Spot.obj
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\scenes\battle\camp\Spot.time.lua .\..\..\Client\Output\data\export_obj\scenes\battle\camp\Spot.time.obj
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\scenes\battle\camp\Wave.lua .\..\..\Client\Output\data\export_obj\scenes\battle\camp\Wave.obj
md .\..\..\Client\Output\data\export_obj\scenes\battle\char
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\scenes\battle\char\Char.lua .\..\..\Client\Output\data\export_obj\scenes\battle\char\Char.obj
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\scenes\battle\char\Char.player.lua .\..\..\Client\Output\data\export_obj\scenes\battle\char\Char.player.obj
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\scenes\battle\char\CharAttrs.lua .\..\..\Client\Output\data\export_obj\scenes\battle\char\CharAttrs.obj
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\scenes\battle\char\CharBehaviors.birth.lua .\..\..\Client\Output\data\export_obj\scenes\battle\char\CharBehaviors.birth.obj
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\scenes\battle\char\CharBehaviors.death.lua .\..\..\Client\Output\data\export_obj\scenes\battle\char\CharBehaviors.death.obj
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\scenes\battle\char\CharBehaviors.lua .\..\..\Client\Output\data\export_obj\scenes\battle\char\CharBehaviors.obj
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\scenes\battle\char\CharBehaviors.move.lua .\..\..\Client\Output\data\export_obj\scenes\battle\char\CharBehaviors.move.obj
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\scenes\battle\char\CharBehaviors.search.lua .\..\..\Client\Output\data\export_obj\scenes\battle\char\CharBehaviors.search.obj
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\scenes\battle\char\CharBehaviors.select.lua .\..\..\Client\Output\data\export_obj\scenes\battle\char\CharBehaviors.select.obj
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\scenes\battle\char\CharBehaviors.skill.lua .\..\..\Client\Output\data\export_obj\scenes\battle\char\CharBehaviors.skill.obj
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\scenes\battle\char\CharColor.lua .\..\..\Client\Output\data\export_obj\scenes\battle\char\CharColor.obj
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\scenes\battle\char\CharTop.lua .\..\..\Client\Output\data\export_obj\scenes\battle\char\CharTop.obj
md .\..\..\Client\Output\data\export_obj\scenes\battle\cinema
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\scenes\battle\cinema\Cinema.camera.lua .\..\..\Client\Output\data\export_obj\scenes\battle\cinema\Cinema.camera.obj
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\scenes\battle\cinema\Cinema.camp.lua .\..\..\Client\Output\data\export_obj\scenes\battle\cinema\Cinema.camp.obj
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\scenes\battle\cinema\Cinema.char.lua .\..\..\Client\Output\data\export_obj\scenes\battle\cinema\Cinema.char.obj
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\scenes\battle\cinema\Cinema.dialog.lua .\..\..\Client\Output\data\export_obj\scenes\battle\cinema\Cinema.dialog.obj
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\scenes\battle\cinema\Cinema.story.lua .\..\..\Client\Output\data\export_obj\scenes\battle\cinema\Cinema.story.obj
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\scenes\battle\cinema\Cinema.team.lua .\..\..\Client\Output\data\export_obj\scenes\battle\cinema\Cinema.team.obj
md .\..\..\Client\Output\data\export_obj\scenes\battle\drop
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\scenes\battle\drop\Drop.coin.lua .\..\..\Client\Output\data\export_obj\scenes\battle\drop\Drop.coin.obj
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\scenes\battle\drop\Drop.item.lua .\..\..\Client\Output\data\export_obj\scenes\battle\drop\Drop.item.obj
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\scenes\battle\drop\Drop.lua .\..\..\Client\Output\data\export_obj\scenes\battle\drop\Drop.obj
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\scenes\battle\drop\Drop.red.lua .\..\..\Client\Output\data\export_obj\scenes\battle\drop\Drop.red.obj
md .\..\..\Client\Output\data\export_obj\scenes\battle\effect
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\scenes\battle\effect\ConnectCCB.lua .\..\..\Client\Output\data\export_obj\scenes\battle\effect\ConnectCCB.obj
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\scenes\battle\effect\ScreenMask.lua .\..\..\Client\Output\data\export_obj\scenes\battle\effect\ScreenMask.obj
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\scenes\battle\Field.lua .\..\..\Client\Output\data\export_obj\scenes\battle\Field.obj
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\scenes\battle\Sfx.lua .\..\..\Client\Output\data\export_obj\scenes\battle\Sfx.obj
md .\..\..\Client\Output\data\export_obj\scenes\battle\skill
md .\..\..\Client\Output\data\export_obj\scenes\battle\skill\buff
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\scenes\battle\skill\buff\Buff.attr.lua .\..\..\Client\Output\data\export_obj\scenes\battle\skill\buff\Buff.attr.obj
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\scenes\battle\skill\buff\Buff.eot.lua .\..\..\Client\Output\data\export_obj\scenes\battle\skill\buff\Buff.eot.obj
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\scenes\battle\skill\buff\Buff.hate.lua .\..\..\Client\Output\data\export_obj\scenes\battle\skill\buff\Buff.hate.obj
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\scenes\battle\skill\buff\Buff.lash.lua .\..\..\Client\Output\data\export_obj\scenes\battle\skill\buff\Buff.lash.obj
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\scenes\battle\skill\buff\Buff.lua .\..\..\Client\Output\data\export_obj\scenes\battle\skill\buff\Buff.obj
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\scenes\battle\skill\buff\Buff.mod.lua .\..\..\Client\Output\data\export_obj\scenes\battle\skill\buff\Buff.mod.obj
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\scenes\battle\skill\buff\Buff.repel.lua .\..\..\Client\Output\data\export_obj\scenes\battle\skill\buff\Buff.repel.obj
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\scenes\battle\skill\buff\Buff.shift.lua .\..\..\Client\Output\data\export_obj\scenes\battle\skill\buff\Buff.shift.obj
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\scenes\battle\skill\buff\Buff.state.lua .\..\..\Client\Output\data\export_obj\scenes\battle\skill\buff\Buff.state.obj
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\scenes\battle\skill\buff\Buff.transform.lua .\..\..\Client\Output\data\export_obj\scenes\battle\skill\buff\Buff.transform.obj
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\scenes\battle\skill\ColdWindSfx.lua .\..\..\Client\Output\data\export_obj\scenes\battle\skill\ColdWindSfx.obj
md .\..\..\Client\Output\data\export_obj\scenes\battle\skill\effect
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\scenes\battle\skill\effect\Effect.buff.lua .\..\..\Client\Output\data\export_obj\scenes\battle\skill\effect\Effect.buff.obj
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\scenes\battle\skill\effect\Effect.chain.lua .\..\..\Client\Output\data\export_obj\scenes\battle\skill\effect\Effect.chain.obj
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\scenes\battle\skill\effect\Effect.heal.lua .\..\..\Client\Output\data\export_obj\scenes\battle\skill\effect\Effect.heal.obj
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\scenes\battle\skill\effect\Effect.hurt.lua .\..\..\Client\Output\data\export_obj\scenes\battle\skill\effect\Effect.hurt.obj
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\scenes\battle\skill\effect\Effect.lua .\..\..\Client\Output\data\export_obj\scenes\battle\skill\effect\Effect.obj
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\scenes\battle\skill\effect\Effect.missile.lua .\..\..\Client\Output\data\export_obj\scenes\battle\skill\effect\Effect.missile.obj
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\scenes\battle\skill\effect\Effect.shadow.lua .\..\..\Client\Output\data\export_obj\scenes\battle\skill\effect\Effect.shadow.obj
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\scenes\battle\skill\effect\Effect.state.lua .\..\..\Client\Output\data\export_obj\scenes\battle\skill\effect\Effect.state.obj
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\scenes\battle\skill\effect\Effect.summon.lua .\..\..\Client\Output\data\export_obj\scenes\battle\skill\effect\Effect.summon.obj
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\scenes\battle\skill\Energy.lua .\..\..\Client\Output\data\export_obj\scenes\battle\skill\Energy.obj
md .\..\..\Client\Output\data\export_obj\scenes\battle\skill\missile
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\scenes\battle\skill\missile\Missile.follow.lua .\..\..\Client\Output\data\export_obj\scenes\battle\skill\missile\Missile.follow.obj
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\scenes\battle\skill\missile\Missile.lua .\..\..\Client\Output\data\export_obj\scenes\battle\skill\missile\Missile.obj
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\scenes\battle\skill\missile\Missile.wave.lua .\..\..\Client\Output\data\export_obj\scenes\battle\skill\missile\Missile.wave.obj
md .\..\..\Client\Output\data\export_obj\scenes\battle\skill\mod
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\scenes\battle\skill\mod\Mod.hurt.lua .\..\..\Client\Output\data\export_obj\scenes\battle\skill\mod\Mod.hurt.obj
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\scenes\battle\skill\mod\Mod.lua .\..\..\Client\Output\data\export_obj\scenes\battle\skill\mod\Mod.obj
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\scenes\battle\skill\mod\Mod.reeffect.lua .\..\..\Client\Output\data\export_obj\scenes\battle\skill\mod\Mod.reeffect.obj
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\scenes\battle\skill\mod\Mod.shield.lua .\..\..\Client\Output\data\export_obj\scenes\battle\skill\mod\Mod.shield.obj
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\scenes\battle\skill\mod\Mod.stealhp.lua .\..\..\Client\Output\data\export_obj\scenes\battle\skill\mod\Mod.stealhp.obj
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\scenes\battle\skill\RemainSfx.lua .\..\..\Client\Output\data\export_obj\scenes\battle\skill\RemainSfx.obj
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\scenes\battle\skill\Result.lua .\..\..\Client\Output\data\export_obj\scenes\battle\skill\Result.obj
md .\..\..\Client\Output\data\export_obj\scenes\battle\skill\skill
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\scenes\battle\skill\skill\Skill.camp.lua .\..\..\Client\Output\data\export_obj\scenes\battle\skill\skill\Skill.camp.obj
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\scenes\battle\skill\skill\Skill.channeling.lua .\..\..\Client\Output\data\export_obj\scenes\battle\skill\skill\Skill.channeling.obj
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\scenes\battle\skill\skill\Skill.instant.lua .\..\..\Client\Output\data\export_obj\scenes\battle\skill\skill\Skill.instant.obj
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\scenes\battle\skill\skill\Skill.lua .\..\..\Client\Output\data\export_obj\scenes\battle\skill\skill\Skill.obj
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\scenes\battle\skill\skill\Skill.passive.lua .\..\..\Client\Output\data\export_obj\scenes\battle\skill\skill\Skill.passive.obj
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\scenes\battle\skill\SuperTrumpSfx.lua .\..\..\Client\Output\data\export_obj\scenes\battle\skill\SuperTrumpSfx.obj
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\scenes\battle\skill\Target.lua .\..\..\Client\Output\data\export_obj\scenes\battle\skill\Target.obj
md .\..\..\Client\Output\data\export_obj\scenes\battle\story
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\scenes\battle\story\Story.lua .\..\..\Client\Output\data\export_obj\scenes\battle\story\Story.obj
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\scenes\battle\story\StoryDialog.lua .\..\..\Client\Output\data\export_obj\scenes\battle\story\StoryDialog.obj
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\scenes\battle\story\StoryTouch.lua .\..\..\Client\Output\data\export_obj\scenes\battle\story\StoryTouch.obj
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\scenes\battle\story\StoryUI.lua .\..\..\Client\Output\data\export_obj\scenes\battle\story\StoryUI.obj
md .\..\..\Client\Output\data\export_obj\scenes\battle\team
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\scenes\battle\team\Team.lua .\..\..\Client\Output\data\export_obj\scenes\battle\team\Team.obj
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\scenes\battle\team\Team.player.lua .\..\..\Client\Output\data\export_obj\scenes\battle\team\Team.player.obj
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\scenes\battle\team\TeamBehaviors.lua .\..\..\Client\Output\data\export_obj\scenes\battle\team\TeamBehaviors.obj
md .\..\..\Client\Output\data\export_obj\scenes\battle\UI
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\scenes\battle\UI\Bottle.lua .\..\..\Client\Output\data\export_obj\scenes\battle\UI\Bottle.obj
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\scenes\battle\UI\CharStatus.lua .\..\..\Client\Output\data\export_obj\scenes\battle\UI\CharStatus.obj
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\scenes\battle\UI\CharUI.lua .\..\..\Client\Output\data\export_obj\scenes\battle\UI\CharUI.obj
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\scenes\battle\UI\EnergyBar.lua .\..\..\Client\Output\data\export_obj\scenes\battle\UI\EnergyBar.obj
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\scenes\battle\UI\FloatText.lua .\..\..\Client\Output\data\export_obj\scenes\battle\UI\FloatText.obj
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\scenes\battle\UI\FocusFireCDText.lua .\..\..\Client\Output\data\export_obj\scenes\battle\UI\FocusFireCDText.obj
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\scenes\battle\UI\HpBar.lua .\..\..\Client\Output\data\export_obj\scenes\battle\UI\HpBar.obj
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\scenes\battle\UI\MainHpBar.lua .\..\..\Client\Output\data\export_obj\scenes\battle\UI\MainHpBar.obj
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\scenes\battle\UI\MainUI.lua .\..\..\Client\Output\data\export_obj\scenes\battle\UI\MainUI.obj
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\scenes\battle\UI\MapClickUI.lua .\..\..\Client\Output\data\export_obj\scenes\battle\UI\MapClickUI.obj
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\scenes\battle\UI\NaviMap.lua .\..\..\Client\Output\data\export_obj\scenes\battle\UI\NaviMap.obj
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\scenes\battle\UI\ResultLose.lua .\..\..\Client\Output\data\export_obj\scenes\battle\UI\ResultLose.obj
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\scenes\battle\UI\ResultWin.lua .\..\..\Client\Output\data\export_obj\scenes\battle\UI\ResultWin.obj
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\scenes\battle\UI\SkillCDText.lua .\..\..\Client\Output\data\export_obj\scenes\battle\UI\SkillCDText.obj
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\scenes\battle\UI\SkillFrame.lua .\..\..\Client\Output\data\export_obj\scenes\battle\UI\SkillFrame.obj
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\scenes\battle\UI\Util.lua .\..\..\Client\Output\data\export_obj\scenes\battle\UI\Util.obj
md .\..\..\Client\Output\data\export_obj\scenes\debug_menu
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\scenes\debug_menu\DebugMenu.lua .\..\..\Client\Output\data\export_obj\scenes\debug_menu\DebugMenu.obj
md .\..\..\Client\Output\data\export_obj\scenes\map_editor
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\scenes\map_editor\MapEditor.lua .\..\..\Client\Output\data\export_obj\scenes\map_editor\MapEditor.obj
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\scenes\map_editor\MapViewer.lua .\..\..\Client\Output\data\export_obj\scenes\map_editor\MapViewer.obj
md .\..\..\Client\Output\data\export_obj\scenes\model_viewer
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\scenes\model_viewer\ModelViewer.lua .\..\..\Client\Output\data\export_obj\scenes\model_viewer\ModelViewer.obj
md .\..\..\Client\Output\data\export_obj\scenes\square
md .\..\..\Client\Output\data\export_obj\scenes\square\activity
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\scenes\square\activity\ActivityPanel.lua .\..\..\Client\Output\data\export_obj\scenes\square\activity\ActivityPanel.obj
md .\..\..\Client\Output\data\export_obj\scenes\square\environment
md .\..\..\Client\Output\data\export_obj\scenes\square\hero
md .\..\..\Client\Output\data\export_obj\scenes\square\herocenter
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\scenes\square\herocenter\HeroBag.lua .\..\..\Client\Output\data\export_obj\scenes\square\herocenter\HeroBag.obj
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\scenes\square\herocenter\HeroCenter.lua .\..\..\Client\Output\data\export_obj\scenes\square\herocenter\HeroCenter.obj
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\scenes\square\herocenter\StarupResult.lua .\..\..\Client\Output\data\export_obj\scenes\square\herocenter\StarupResult.obj
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\scenes\square\herocenter\StarupSourceInfo.lua .\..\..\Client\Output\data\export_obj\scenes\square\herocenter\StarupSourceInfo.obj
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\scenes\square\herocenter\Tab.charinfo.lua .\..\..\Client\Output\data\export_obj\scenes\square\herocenter\Tab.charinfo.obj
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\scenes\square\herocenter\Tab.levelup.lua .\..\..\Client\Output\data\export_obj\scenes\square\herocenter\Tab.levelup.obj
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\scenes\square\herocenter\Tab.skill.lua .\..\..\Client\Output\data\export_obj\scenes\square\herocenter\Tab.skill.obj
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\scenes\square\herocenter\Tab.upgrade.lua .\..\..\Client\Output\data\export_obj\scenes\square\herocenter\Tab.upgrade.obj
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\scenes\square\herocenter\UpgradeResult.lua .\..\..\Client\Output\data\export_obj\scenes\square\herocenter\UpgradeResult.obj
md .\..\..\Client\Output\data\export_obj\scenes\square\hero_bag
md .\..\..\Client\Output\data\export_obj\scenes\square\item
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\scenes\square\item\ItemBag.lua .\..\..\Client\Output\data\export_obj\scenes\square\item\ItemBag.obj
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\scenes\square\item\ItemSell.lua .\..\..\Client\Output\data\export_obj\scenes\square\item\ItemSell.obj
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\scenes\square\item\ItemUse.lua .\..\..\Client\Output\data\export_obj\scenes\square\item\ItemUse.obj
md .\..\..\Client\Output\data\export_obj\scenes\square\levelselect
md .\..\..\Client\Output\data\export_obj\scenes\square\lineup
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\scenes\square\lineup\CharInfo.lua .\..\..\Client\Output\data\export_obj\scenes\square\lineup\CharInfo.obj
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\scenes\square\lineup\HeroCard.lua .\..\..\Client\Output\data\export_obj\scenes\square\lineup\HeroCard.obj
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\scenes\square\lineup\HeroSlot.lua .\..\..\Client\Output\data\export_obj\scenes\square\lineup\HeroSlot.obj
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\scenes\square\lineup\Lineup.lua .\..\..\Client\Output\data\export_obj\scenes\square\lineup\Lineup.obj
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\scenes\square\lineup\Lineup.readyforbattle.lua .\..\..\Client\Output\data\export_obj\scenes\square\lineup\Lineup.readyforbattle.obj
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\scenes\square\lineup\Lineup.withcharinfo.lua .\..\..\Client\Output\data\export_obj\scenes\square\lineup\Lineup.withcharinfo.obj
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\scenes\square\lineup\LineupMode.lua .\..\..\Client\Output\data\export_obj\scenes\square\lineup\LineupMode.obj
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\scenes\square\SquareBuilding.lua .\..\..\Client\Output\data\export_obj\scenes\square\SquareBuilding.obj
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\scenes\square\SquareData.lua .\..\..\Client\Output\data\export_obj\scenes\square\SquareData.obj
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\scenes\square\SquareScene.lua .\..\..\Client\Output\data\export_obj\scenes\square\SquareScene.obj
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\scenes\square\SquareTouch.lua .\..\..\Client\Output\data\export_obj\scenes\square\SquareTouch.obj
md .\..\..\Client\Output\data\export_obj\scenes\square\stageselect
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\scenes\square\stageselect\Block.lua .\..\..\Client\Output\data\export_obj\scenes\square\stageselect\Block.obj
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\scenes\square\stageselect\StageInfo.lua .\..\..\Client\Output\data\export_obj\scenes\square\stageselect\StageInfo.obj
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\scenes\square\stageselect\StageOverview.lua .\..\..\Client\Output\data\export_obj\scenes\square\stageselect\StageOverview.obj
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\scenes\square\stageselect\StageSelect.lua .\..\..\Client\Output\data\export_obj\scenes\square\stageselect\StageSelect.obj
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\scenes\square\stageselect\StageSelectWorld.lua .\..\..\Client\Output\data\export_obj\scenes\square\stageselect\StageSelectWorld.obj
md .\..\..\Client\Output\data\export_obj\scenes\square\tower
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\scenes\square\tower\BoxWithToolTip.lua .\..\..\Client\Output\data\export_obj\scenes\square\tower\BoxWithToolTip.obj
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\scenes\square\tower\FloorList.lua .\..\..\Client\Output\data\export_obj\scenes\square\tower\FloorList.obj
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\scenes\square\tower\Lineup.readyfortower.lua .\..\..\Client\Output\data\export_obj\scenes\square\tower\Lineup.readyfortower.obj
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\scenes\square\tower\Tower.lua .\..\..\Client\Output\data\export_obj\scenes\square\tower\Tower.obj
md .\..\..\Client\Output\data\export_obj\scenes\square\UI
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\scenes\square\UI\Reward.lua .\..\..\Client\Output\data\export_obj\scenes\square\UI\Reward.obj
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\scenes\square\UI\RewardToolTip.lua .\..\..\Client\Output\data\export_obj\scenes\square\UI\RewardToolTip.obj
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\scenes\square\UI\ScenarioList.lua .\..\..\Client\Output\data\export_obj\scenes\square\UI\ScenarioList.obj
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\scenes\square\UI\SettingUI.lua .\..\..\Client\Output\data\export_obj\scenes\square\UI\SettingUI.obj
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\scenes\square\UI\SquareMainUI.lua .\..\..\Client\Output\data\export_obj\scenes\square\UI\SquareMainUI.obj
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\scenes\square\UI\SquareMenu.lua .\..\..\Client\Output\data\export_obj\scenes\square\UI\SquareMenu.obj
.\..\..\Client\scripting\lua\luajit\LuaJIT-2.0.1\x86_bin\luajit -b .\..\..\Client\Output\data\export\scenes\square\UI\SquareResource.lua .\..\..\Client\Output\data\export_obj\scenes\square\UI\SquareResource.obj
md .\..\..\Client\Output\data\export_obj\table
md .\..\..\Client\Output\data\export_obj\table\appearance
