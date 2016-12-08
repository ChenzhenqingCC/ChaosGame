last_version_file="/Users/plutopapa/polar_workplace/CandyCarrier/Client/PolarClient/Build/version/last_version"

for client_version in `cat $last_version_file`
do
    echo "$client_version" 
    break
done

proto_version_file="/Users/plutopapa/polar_workplace/CandyCarrier/Client/PolarClient/Build/version/proto_version"

for proto_version in `cat $proto_version_file`
do
    echo "$proto_version" 
    break
done

version_str=PolarClient-$proto_version.0.$client_version
echo $version_str

project_path="/Volumes/POLAR项目组$/Candy/Develop/"$(date +"%Y-%m-%d")


echo "make Publish root dir : $project_path"


mkdir $project_path
mkdir $project_path"/"$version_str
mkdir $project_path"/"$version_str"/IOS"




echo "copying ipa..."
cp /Users/plutopapa/polar_workplace/PolarClient.ipa $project_path"/"$version_str"/IOS/PolarClient.ipa" && ( echo Success ) || ( echo Failed;exit 2 )

#if [ "$do_encrypt" == "true" ];
#then
#	echo "encrypt";
	#cp /Users/plutopapa/polar_workplace/PolarClient.ipa $project_path"/PolarClientVersion/IOS/PolarClient_encrypt.ipa";
#else
	#echo 2;
	#cp /Users/plutopapa/polar_workplace/PolarClient.ipa $project_path"/PolarClientVersion/IOS/PolarClient.ipa";
#fi;


echo "-----------DONE----------"

