@echo off
chcp 65001 >nul
echo =====================================
echo TU-8 Framework - GitHub 发布助手
echo =====================================
echo.
echo 本脚本将_public_release文件夹发布到GitHub
echo.

set REPO_NAME=tu-8-ai-security-framework
set REPO_DESC=AI系统安全架构参考框架 - A framework for AI system stability, core-layer protection, and knowledge evolution.

echo [1/4] 检查GitHub CLI...
gh --version >nul 2>&1
if errorlevel 1 (
    echo [错误] 未安装GitHub CLI
    echo 请先安装: winget install GitHub.cli
    echo 或访问: https://cli.github.com/
    pause
    exit /b 1
)

echo [2/4] 检查登录状态...
gh auth status >nul 2>&1
if errorlevel 1 (
    echo [错误] 未登录GitHub
    echo 请运行: gh auth login
    pause
    exit /b 1
)

echo [3/4] 创建仓库...
gh repo create %REPO_NAME% --public --description "%REPO_DESC%" --source "_public_release" --push --remote origin 2>nul
if errorlevel 1 (
    echo [提示] 仓库可能已存在，尝试推送...
    cd _public_release
    git init
    git add -A
    git commit -m "Initial commit: TU-8 AI Security Architecture Reference Framework v1.0"
    git branch -M main
    git remote add origin https://github.com/YOUR_USERNAME/%REPO_NAME%.git
    git push -u origin main
    cd ..
) else (
    echo [成功] 仓库创建并推送完成
)

echo [4/4] 打开仓库页面...
start https://github.com/YOUR_USERNAME/%REPO_NAME%

echo.
echo =====================================
echo 完成！请检查仓库页面确认内容
echo =====================================
pause