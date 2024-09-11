param (
    [string]$pth
)

# 将当前命令行编码设置为UTF-8
$OutputEncoding = [console]::InputEncoding = [console]::OutputEncoding = New-Object System.Text.UTF8Encoding

# 判断源文件targetPth是否存在，如果不存在则退出脚本
if (-not (Test-Path $pth)) {
    Write-Error "Not existing file path: $pth"
    exit
}

# 将targetPth转换为绝对路径
$targetPth = (Get-Item $pth).FullName
# Write-Output "targetPth: $targetPth"

# 获取源文件所在目录
$targetDir = [System.IO.Path]::GetDirectoryName($targetPth)
# Write-Output "targetDir: $targetDir"

# 获取源文件名，不包含后缀名
$targetNam = [System.IO.Path]::GetFileNameWithoutExtension($targetPth)
# Write-Output "targetNam: $targetNam"

# 获取源文件后缀名，不包含“.”
$targetExt = [System.IO.Path]::GetExtension($targetPth).Substring(1)
# Write-Output "targetExt: $targetExt"

# 获取主项目目录
$mainDir = "C:\rocky_d\code\informatics"
# Write-Output "mainDir: $mainDir"
# $scriptsDir = "$mainDir\scripts"
# Write-Output "scriptsDir: $scriptsDir"

# 获取子项目目录
$subDir = "$mainDir\code\$targetExt"
# Write-Output "subDir: $subDir"
$subSrcDir = "$subDir\src"
# Write-Output "subSrcDir: $subSrcDir"
$subOutDir = "$subDir\out"
# Write-Output "subOutDir: $subOutDir"

# 添加临时环境变量PATH变量
$tmpEnvPath = "$subDir;"
# Write-Output "tmpEnvPath: $tmpEnvPath"
$env:PATH = "$tmpEnvPath$env:PATH"

# 切换当前工作目录
$originalDir = Get-Location
# Write-Output "originalDir: $originalDir"
Set-Location $targetDir
# Write-Output "Get-Location: $(Get-Location)"

# Clear-Host
# Write-Output "-------------------------"

try {
    if ($targetExt -eq "c") {
        # 设置输出文件路径
        $resultPth = "$subOutDir\$targetNam.exe"
        # 编译源文件
        gcc -o $resultPth $targetPth
        # 运行输出文件
        . $resultPth
    }
    elseif ($targetExt -eq "cpp") {
        # 设置输出文件路径
        $resultPth = "$subOutDir\$targetNam.exe"
        # 编译源文件
        g++ -o $resultPth $targetPth
        # 运行输出文件
        . $resultPth
    }
    elseif ($targetExt -eq "cs") {
        # 设置输出文件路径
        $resultPth = "$subOutDir\$targetNam.exe"
        # 编译源文件
        & "C:\Program Files (x86)\Microsoft Visual Studio\2022\BuildTools\MSBuild\Current\Bin\Roslyn\csc.exe" -out:$resultPth $targetPth
        # 运行输出文件
        . $resultPth
    }
    elseif ($targetExt -eq "go") {
        # 设置输出文件路径
        $resultPth = "$subOutDir\$targetNam.exe"
        # 编译源文件
        go build -o $resultPth $targetPth
        # 运行输出文件
        . $resultPth
    }
    elseif ($targetExt -eq "java") {
        # 运行java源文件
    }
    elseif ($targetExt -eq "js") {
        # 运行js源文件
    }
    elseif ($targetExt -eq "kt") {
        # 运行kt源文件
    }
    elseif ($targetExt -eq "lua") {
        # 设置LUA_PATH环境变量
        $env:LUA_PATH = $subSrcDir
        # 运行lua源文件
        lua53 $targetPth
        # 删除LUA_PATH环境变量
        $env:LUA_PATH = ""
    }
    elseif ($targetExt -eq "py") {
        # 设置PYTHONPATH环境变量
        $env:PYTHONPATH = $subSrcDir
        # 运行py源文件
        python $targetPth
        # 删除PYTHONPATH环境变量
        $env:PYTHONPATH = ""
    }
    elseif ($targetExt -eq "rs") {
        # 设置输出文件路径
        $resultPth = "$subOutDir\$targetNam.exe"
        # 编译源文件
        rustc -o $resultPth $targetPth
        # 运行输出文件
        . $resultPth
    }
    elseif ($targetExt -eq "ts") {
        # 运行ts源文件
    }
    else {
        # 不支持的源文件类型
        Write-Error "Unsupported file type: $targetExt"
    }
}
finally {
    # 切换回原目录
    Set-Location $originalDir
    # 删除临时环境变量PATH变量
    $env:PATH = $env:PATH.Replace($tmpEnvPath, "")
}
