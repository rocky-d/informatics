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
Write-Output "targetPth: $targetPth"

# 获取源文件所在目录
$targetDir = [System.IO.Path]::GetDirectoryName($targetPth)
Write-Output "targetDir: $targetDir"

# 获取源文件名，不包含后缀名
$targetNam = [System.IO.Path]::GetFileNameWithoutExtension($targetPth)
Write-Output "targetNam: $targetNam"

# 获取源文件后缀名，不包含“.”
$targetExt = [System.IO.Path]::GetExtension($targetPth).Substring(1)
Write-Output "targetExt: $targetExt"

# 获取主项目目录
$mainDir = "C:\rocky_d\code\informatics"
Write-Output "mainDir: $mainDir"

# 获取子项目目录
$subDir = "$mainDir\code\$targetExt"
Write-Output "subDir: $subDir"
$subSrcDir = "$subDir\src"
Write-Output "subSrcDir: $subSrcDir"
$subOutDir = "$subDir\out"
Write-Output "subOutDir: $subOutDir"

# 添加临时环境变量PATH变量
$tmpEnvPath = "$mainDir;$subDir;$subSrcDir;$subOutDir;$targetDir;"
Write-Output "tmpEnvPath: $tmpEnvPath"
$env:PATH = "$tmpEnvPath$env:PATH"

# 切换当前工作目录
Set-Location $targetDir
Write-Output "Get-Location: $(Get-Location)"

# Clear-Host
Write-Output "-------------------------"

if ($targetExt -eq "c") {
    # 编译c源文件
    gcc -o "$subOutDir\$targetNam.exe" $targetPth
    # 运行输出文件
    . "$subOutDir\$targetNam.exe"
} elseif ($targetExt -eq "cpp") {
    # 运行cpp源文件
} elseif ($targetExt -eq "go") {
    # 运行go源文件
} elseif ($targetExt -eq "java") {
    # 运行java源文件
} elseif ($targetExt -eq "js") {
    # 运行js源文件
} elseif ($targetExt -eq "kt") {
    # 运行kt源文件
} elseif ($targetExt -eq "lua") {
    # 运行lua源文件
} elseif ($targetExt -eq "py") {
    # 设置PYTHONPATH环境变量
    $env:PYTHONPATH = $subSrcDir
    # 运行py源文件
    python $targetPth
    # 删除PYTHONPATH环境变量
    $env:PYTHONPATH = ""
} elseif ($targetExt -eq "rs") {
    # 运行rs源文件
} elseif ($targetExt -eq "ts") {
    # 运行ts源文件
} else {
    # 不支持的源文件类型
    Write-Error "Unsupported file type: $targetExt"
}

# 切换回原目录
Set-Location $mainDir

# 删除临时环境变量PATH变量
$env:PATH = $env:PATH.Replace($tmpEnvPath, "")
