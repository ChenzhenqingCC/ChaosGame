#! /bin/sh

CURRENT_PATH=`dirname $0`
LANSTR=
if [ $1 -eq 1 ];then
  LANSTR=
elif [ $1 -eq 2 ];then
  LANSTR=/loc/vnm
fi

CCB_PATH=$CURRENT_PATH/../../../ChaosArt/res$LANSTR/ui_editor
TEMP_OUT=$CURRENT_PATH/out
OUT=$CURRENT_PATH/../../../ChaosArt/res$LANSTR/ui_editor_publish

#export P4CONFIG=$CURRENT_PATH/p4.configfile
export P4CLIENT=chaos_ccb_pub
export P4PASSWD=maple123
export P4PORT=192.168.1.251:1999
export P4USER=chenzhenqing
chmod 777 $CURRENT_PATH/p4
P4OUTPATH=//$P4CLIENT/ChaosArt/res$LANSTR/ui_editor_publish

echo ！！！！！！！！！！！！Get New Version of UI editor！！！！！！！！！！！！
$CURRENT_PATH/p4 sync //$P4CLIENT/ChaosArt/res$LANSTR/ui_editor/...#head
$CURRENT_PATH/p4 sync -f $P4OUTPATH/...#head

publishFiles(){
   for i in $1/* 
   do
    if [ -d $i ];then
       mkdir ${i/$CCB_PATH/$TEMP_OUT}
       publishFiles $i
    else
      fileName=`basename $i`
      if [[ $fileName =~ \.ccb$ ]]
      then
        echo "--- publish >>$fileName<<"
        fileNameWithoutExt=${fileName%\.ccb}
        filedir=${i%/*}
	outdir=${filedir/$CCB_PATH/$TEMP_OUT}
        $CURRENT_PATH/ccbpublish -o $outdir/$fileNameWithoutExt".ccbi" $i
      fi
    fi
   done
}

addFiles(){
   for i in $1/* 
   do
    if [ -d $i ];then
       addFiles $i
    else
      fileName=`basename $i`
      if [[ $fileName =~ \.ccbi$ ]]
      then
      	filedir=${i%/*}
	outdir=${filedir/$OUT/$P4OUTPATH}
	$CURRENT_PATH/p4 add -d -f -c default $outdir/$fileName
      fi
    fi
   done
}

addAndEditFiles(){
   for i in $1/* 
   do
    if [ -d $i ];then
       addAndEditFiles $i
    else
      fileName=`basename $i`
      if [[ $fileName =~ \.ccbi$ ]]
      then
        filedir=${i%/*}
	 outdir=${filedir/$TEMP_OUT/$OUT}
	 p4dir=${filedir/$TEMP_OUT/$P4OUTPATH}
	 srcDir=$filedir/$fileName
	 tagDir=$outdir/$fileName
	 subDir=$p4dir/$fileName
	 if [ -f $tagDir ]; then
		diff $srcDir $tagDir
		if [[ $? = 0 ]];then
    			echo $tagDir not modified
		else
    			echo $tagDir modified
			$CURRENT_PATH/p4 edit -c default $subDir
		fi
	 else
		$CURRENT_PATH/p4 add -d -f -c default $subDir
		$CURRENT_PATH/p4 reopen -c default -t binary $subDir
	 fi
      fi
    fi
   done
}

deleteFiles(){
   for i in $1/* 
   do
    if [ -d $i ];then
       deleteFiles $i
    else
      fileName=`basename $i`
      if [[ $fileName =~ \.ccbi$ ]]
      then
        fileNameWithoutExt=${fileName%\.ccb}
        filedir=${i%/*}
	outdir=${filedir/$OUT/$TEMP_OUT}
	p4dir=${filedir/$OUT/$P4OUTPATH}
	srcDir=$filedir/$fileName
	tagDir=$outdir/$fileName
	subDir=$p4dir/$fileName
	if [ -f $tagDir ]; then
		echo $tagDir exists
	else
		echo $tagDir not exists
		$CURRENT_PATH/p4 delete -c default -v $subDir
	fi
      fi
    fi
   done
}

echo ！！！！！！！！！！！！make temp out flower！！！！！！！！！！！！
if [ -d $TEMP_OUT ];then
    echo "Clean temp files..."
    rm -rf $TEMP_OUT
fi

mkdir $TEMP_OUT

echo ！！！！！！！！！！！！publish ccb files！！！！！！！！！！！！

publishFiles $CCB_PATH

echo ！！！！！！！！！！！！reconcile ccbi files！！！！！！！！！！！！
addAndEditFiles $TEMP_OUT
deleteFiles $OUT

echo ！！！！！！！！！！！！remove temp out flower！！！！！！！！！！！！
if [ -d $OUT ];then
    echo "Clean out files..."
    rm -rf $OUT
fi

mkdir $OUT

echo ！！！！！！！！！！！！move ccbi files！！！！！！！！！！！！

mv $TEMP_OUT/* $OUT/

rm -rf $TEMP_OUT

echo ！！！！！！！！！！！！submit ccbi files！！！！！！！！！！！！
#$CURRENT_PATH/p4 submit -f revertunchanged -d ccbAutoPublish
