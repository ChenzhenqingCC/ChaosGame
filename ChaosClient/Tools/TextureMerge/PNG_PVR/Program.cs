using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.IO;
using System.Diagnostics;

namespace PNG_PVR
{
    static class TP_CONST
    {
        public const int MAX_SIZE = 2048;
        public const string FORMAT_PNG = "png";
        public const string FORMAT_PVR = "pvr2ccz";
        public const string OPT_RGBA4444 = "RGBA4444";
        public const string OPT_RGBA8888 = "RGBA8888";
        public const string OPT_RGBA5551 = "RGBA5551";
    }

    class Program
    {
        static void Main(string[] args)
        {
            string  inputPath = args[0];
            string outputPath = args[1];
            if (inputPath  == null)
            {
                Print("ERROR: inputpath is null~!");
            }
            if (outputPath == null)
            {
                Print("ERROR: outputPath is null~!");
            }
            DirectoryInfo inputFolder = new DirectoryInfo(inputPath);
            FileInfo[] files = inputFolder.GetFiles();
            foreach (FileInfo file in files)
            {
                if (file.Extension != ".png")
                {
                    continue;
                }
                string inputFilePath = file.FullName;
                string fileName = file.Name;
                CallTexturePacker(inputFilePath, outputPath, fileName.Substring(0,fileName.IndexOf('.')));
            }
            DirectoryInfo outputFolder = new DirectoryInfo(outputPath);
            FileInfo[] afterFiles = outputFolder.GetFiles();
            foreach (FileInfo afterFile in afterFiles)
            {
                if (afterFile.Extension != ".ccz")
                {
                    afterFile.Delete();
                }
            }
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
                                                                 string outPutName)
        {
            //DirectoryInfo checkPath = new DirectoryInfo(inputPath);
            //if (!checkPath.Exists)
            //{
            //    Print("ERROR:CallTexturePacker - InputPath is not exist!");
            //    return false;
            //}
            //else
            //{
            //    char lastChar = inputPath[inputPath.Length - 1];
            //    if (lastChar != '/' || lastChar != '\\')
            //    {
            //        inputPath += "\\";
            //    }
            //}
            DirectoryInfo checkPath = new DirectoryInfo(outputPath);
        
            if (!checkPath.Exists)
            {
                Print("OutPutPath is not exist!");
                Print("OutPutPath Create....");
                Directory.CreateDirectory(outputPath);
            }
            string extName = ".pvr.ccz";
            string command = " --max-size " + TP_CONST.MAX_SIZE + " "
                                           + "--texture-format " + TP_CONST.FORMAT_PVR + " "
                                           + "--size-constraints AnySize "
                                           + "--opt " + TP_CONST.OPT_RGBA4444+ " "
                                           + "--border-padding 0 "
                                           + "--dither-fs-alpha "
                                           + "--disable-rotation "
                                           + "--trim-mode None ";
            command += "--data " + outputPath + "/" + outPutName + ".plist ";
            command += "--sheet " + outputPath + "/" + outPutName + extName + " ";
            command += inputPath;
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
        /// 简化输出打印信息
        /// </summary>
        /// <param name="printStr"></param>
        public static void Print(string printStr)
        {
            Console.WriteLine(printStr);
        }

    }
}
