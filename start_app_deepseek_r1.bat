@echo off
chcp 65001 > nul
title AI小说生成器 - DeepSeek-R1版本

echo.
echo ========================================
echo     AI自动小说生成器 - DeepSeek-R1版本
echo ========================================
echo.
echo 正在启动服务器...
echo 使用模型: DeepSeek-R1 (免费)
echo 服务商: OpenRouter
echo 端口: 60001
echo.

REM 检查Python环境
python --version >nul 2>&1
if errorlevel 1 (
    echo 错误: 未找到Python，请先安装Python
    pause
    exit /b 1
)

REM 检查虚拟环境
if exist "venv\Scripts\activate.bat" (
    echo 激活虚拟环境...
    call venv\Scripts\activate.bat
) else (
    echo 警告: 未找到虚拟环境，使用系统Python
)

REM 安装依赖
echo 检查并安装依赖包...
pip install -r requirements.txt --quiet

REM 启动Flask应用
echo.
echo 启动DeepSeek-R1模型服务...
echo 访问地址: http://localhost:60001/bingte
echo 按 Ctrl+C 停止服务
echo.

python apps/app-deepseek-r1.py

echo.
echo 服务已停止
pause
