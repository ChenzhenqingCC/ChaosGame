using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Diagnostics;

namespace TextureMerge
{
    static class TP_CONST
    {
         public const int MAX_SIZE = 2048;
         public const string FORMAT_PNG = "png";
         public const string FORMAT_PVR  = "pvr2ccz";
         public const string OPT_RGBA4444 = "RGBA4444";
         public const string OPT_RGBA8888 = "RGBA8888";
    }

    static class SINGLE_PNG_TO_PVR
    {
        public const int MAX_SIZE = 2048;
        public const string FORMAT_PVR = "pvr2ccz";
        public const string OPT_RGBA8888 = "pvr2ccz";
    }


    class Program
    {
        //输入参数为: 1.需要合并纹理的文件路径(注1),2.合并纹理后输出的路径
        //合并文件的路径例子为 X:\...\总图片文件夹\图片类型名(如UI)\合并图片文件夹名如(minigame_4png)\
        //输出路径为:X:\...\总图片文件夹
        //需要合并图片的文件夹名结构为:名字_压缩类型.如:minigame_4png
        //类型说明:
        //4png: RGBA4444 png
        //4pvr:  RGBA4444 pvr.ccz
        //8png: RGBA8888 png
        //8pvr:  RGBA8888 pvr.ccz
        //那么最终合成的大图就是minigame.png/minigame.pvr.ccz
        //注1:多个输入路径用,间隔
        static void Main(string[] args)
        {
            string[] inputPathArr = GetInputFolder(args[0]);
            string outPutPath  = args[1];
            foreach (string inputPath in inputPathArr)
            {
                string[] inputInfoList = CheckInputPath(inputPath);
                if (inputInfoList == null)
                {
                    Print("ERROR: Main -- InputInfoList is null!");
                    Console.ReadKey();
                    return;
                }
                //将输入路径反转,获得相应的参数.
                //反转的参数为:合并图片文件名,上层类型名,总输出文件夹
                Array.Reverse(inputInfoList);
                if (!CheckOutputPath(outPutPath,inputInfoList[2]))
                {
                    Print("ERROR: Main - Check your output path! It's wrong!");
                    Console.ReadKey();
                    return;
                }
                string outputName = inputInfoList[1].Substring(0,inputInfoList[1].LastIndexOf('_'));
                string outPutFmtStr = inputInfoList[1].Substring(inputInfoList[1].IndexOf('_')+1);
                CallTexturePacker(inputPath,outPutPath,outputName,GetMergeFormat(outPutFmtStr),GetMergeOpt(outPutFmtStr));
            }
            Console.ReadKey();
        }

        /// <summary>
        /// 将输入的参数变为实际可以操作的文件夹路径
        /// </summary>
        /// <param name="inputPaths"></param>
        /// <returns></returns>
        public static string[] GetInputFolder(string inputPaths)
        {
            char[] delimiter = {','};
            string[] inputPathArr = inputPaths.Split(delimiter);
            return inputPathArr;
        }

        /// <summary>
        ///  调用TexturePacker 去合并大图
        /// 仅仅做文件路径和格式是否存在检查,不做路径逻辑检查
        /// </summary>
        /// <param name="inputPath"></param>
        /// <param name="outputPath"></param>
        /// <param name="mergeName"></param>
        /// <param name="formatType"></param>
        /// <param name="optType"></param>
        /// <returns></returns>
        public static bool CallTexturePacker(string inputPath, 
                                                                 string outputPath, 
                                                                 string outPutName,
                                                                 string formatType,
                                                                 string optType)
        {
            DirectoryInfo checkPath = new DirectoryInfo(inputPath);
            if (!checkPath.Exists)
            {
                Print("ERROR:CallTexturePacker - InputPath is not exist!");
                return false ;
            }
            else
            {
                char lastChar = inputPath[inputPath.Length - 1];
                if (lastChar != '/' || lastChar != '\\')
                {
                    inputPath += "\\";
                }
            }
            checkPath = new DirectoryInfo(outputPath);
            if (!checkPath.Exists)
            {
                Print("ERROR:CallTexturePacker - OutPutPath is not exist!");
                return false;
            }
            string extName = "";
            switch (formatType)
            {
                case TP_CONST.FORMAT_PNG:
                    extName = "png";
                    break;
                case TP_CONST.FORMAT_PVR:
                    extName = "pvr.ccz";
                    break;
                default:
                    Print("ERROR:CallTexturePacker -- Output formatType is ERROR! Type:" + formatType);
                    break;
            }
            switch (optType)
            {
                case TP_CONST.OPT_RGBA4444:
                case TP_CONST.OPT_RGBA8888:
                    break;
                default:
                    Print("ERROR:CallTexturePacker -- Output optType is ERROR! Type:" + optType);
                    break;
            }

            string command=  "--max-size " + TP_CONST.MAX_SIZE + " "
                                           + "--texture-format " + formatType + " "
                                           + "--size-constraints NPOT "   
                                           + "--opt " + optType  
                                           + "--dither-none-nn ";
            command += "--data " + outputPath + "/" + outPutName + ".plist ";
            command += "--sheet " + outputPath + "/" + outPutName + extName;
            command += inputPath ;
            Process p = new Process();
            p.StartInfo.FileName = "TexturePacker";
            p.StartInfo.Arguments = command;
            p.StartInfo.UseShellExecute = false;
            p.StartInfo.RedirectStandardInput = true;
            p.StartInfo.RedirectStandardOutput = true;
            p.StartInfo.RedirectStandardError = true;
            p.StartInfo.CreateNoWindow = false;
            p.Start();
            string error = p.StandardError.ReadToEnd();
            if (error != "")
            {
                Print("ERROR:CallTexturePacker--" + error);
            }
            else
            {
                Print(p.StandardOutput.ReadToEnd());
            }
            p.WaitForExit();
            return true;
        }

        /// <summary>
        /// 检查输入路径是否正确
        /// </summary>
        /// <param name="inputPath"></param>
        /// <returns></returns>
        public static string[] CheckInputPath(string inputPath)
        {
            //合并文件的路径例子为 X:\...\总图片文件夹\图片类型名(如UI)\合并图片文件夹名如(minigame_4png)\
            char lastChar = inputPath[inputPath.Length - 1];
            if (lastChar != '\\')
            {
                inputPath += "\\";
            }
            char[] delimiter = { '\\' };
            string[] delimPath = inputPath.Split(delimiter);
            if (delimPath.Length < 4)
            {
                Print("ERROR: CheckInputPath - Input path is error! Check it! inputPath:" + inputPath);
                return null;
            }
            return delimPath;
        }

        /// <summary>
        ///  检查输出文件夹是否合法
        /// </summary>
        /// <param name="outputPath"></param>
        /// <param name="topOutputFolder"></param>
        /// <returns></returns>
        public static bool CheckOutputPath(string outputPath,string topOutputFolder)
        {
            char[] delimiter = { '\\' };
            string[] delimPath = outputPath.Split(delimiter);
            if (delimPath[delimPath.Length - 1] != topOutputFolder)
            {
                return false;
            }
            return true;
        }

        /// <summary>
        /// 获得导出合并图片的opt
        /// </summary>
        /// <param name="fmtOptStr"></param>
        /// <returns></returns>
        public static string GetMergeOpt(string fmtOptStr)
        {
            //描述导出图片的字符串应该类似为:4png
            char optStr = fmtOptStr[0];
            switch (optStr)
            {
            case '4':
                    return TP_CONST.OPT_RGBA4444;
            case '8':
                return TP_CONST.OPT_RGBA8888;
            }
            return null;
        }

        /// <summary>
        /// 获得导出合并图片的format
        /// </summary>
        /// <param name="fmOptStr"></param>
        /// <returns></returns>
        public static string GetMergeFormat(string fmOptStr)
        {
            string optStr = fmOptStr.Substring(1);
            switch (optStr)
            {
            case "png":
                    return TP_CONST.FORMAT_PNG;
            case "pvr":
                    return TP_CONST.FORMAT_PVR;
            }
            return null;
        }

        /// <summary>
        /// 简化输出打印信息
        /// </summary>
        /// <param name="printStr"></param>
        public static void Print(string printStr)
        {
            Console.WriteLine(printStr);
        }
    }
    
}
