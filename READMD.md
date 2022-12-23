# Flask 安裝與設定

```
.
├── apps
│   ├── Module                     # 評論處理 & 爬蟲
│   │   ├── Filter.py              # 比對和結果分析
│   │   ├── InputProcess.py        # 處理一開始要傳入的資料庫跟文本(評論)
│   │   ├── PythonApplication1.py  # 評論處理主程式
│   │   ├── SensitiveMap.py        # 建立詞彙森林(tree結構)DFA算法
│   │   ├── __init__.py
│   │   └── main.py                # 爬蟲
│   ├── data
│   │   ├── badwords.txt
│   │   ├── negativewords.txt
│   │   ├── positivewords.py
│   │   └── text.py                # 爬取的留言
│   └── minimalapp
│       ├── static
│       │   ├── css
│       │   │   ├── style.css       # index.html
│       │   │   └── style_page2.css # result.html
│       │   ├── js
│       │   │   ├── move.js
│       │   │   └── script.js
│       │   └── pic
│       ├── templates
│       │   ├── index.html
│       │   └── result.html
│       ├── __init__.py
│       └── app.py                  # Flask 應用程式主程式
│
└── venv
```

## 安裝

- [python](https://python.org/downloads)
- [Visual Stdio Code](https://code.visualstudio.com/)

## 環境架設

1. 在任意目錄之下

- Windows(PowerShell)

```bash=
$ PowerShell Set-ExecutionPolicy RemoteSigned
```

報錯:

```bash=
$ PowerShell Set-ExecutionPolicy RemoteSigned CurrentUser
Set-ExecutionPolicy : Windows PowerShell 已成功更新您的執行原則，但是該設定已被定義範圍更特定的原則覆寫。由於覆
寫的緣故，您的殼層將會保留它目前 Bypass 的有效執行原則。輸入
"Get-ExecutionPolicy -List" 可檢視您的執行原則設定。如需詳細資訊，請參閱 "Get-Help Set-ExecutionPolicy"。
位於 線路:1 字元:1
+ Set-ExecutionPolicy RemoteSigned CurrentUser
+ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : PermissionDenied: (:) [Set-ExecutionPolicy], SecurityException
    + FullyQualifiedErrorId : ExecutionPolicyOverride,Microsoft.PowerShell.Commands.SetExecutionPolicyCommand
```

[解決方法](https://github.com/jiwenxing/qimage-win/issues/14)：  
使用管理員身份運行 powershell，在命令下執行下面 2 條命令即可。然後重新以管理員權限運行 qImage.exe

```bash=
Set-ExecutionPolicy "RemoteSigned" -Scope Process -Confirm:$false
Set-ExecutionPolicy "RemoteSigned" -Scope CurrentUser -Confirm:$false
```

2. 建立工作目錄

```bash=
mkdir [資料夾名稱]            # 建立
cd [資料夾名稱]               # 移動
py -m venv venv             # 建立虛擬環境
venv\Scripts\Activate.ps1   # 啟動虛擬環境
```

3. 安裝 Flask

```bash=
(venv) $ pip install flask
```

### Visual Stdio Code 環境設定

1. 安裝 Python 擴充套件

```
延伸模組 -> Python
```

2. 安裝程式庫

```bash=
(venv) $ pip install flake8 black isort mypy
```

3. 設定程式庫

```
左下角齒輪 -> 設定 -> 工作區(WorkSpace)
```

#### 設定 flake8

搜尋欄輸入，勾選

```
Python > Linting: Enabled
```

![](https://i.imgur.com/ux4I6HY.png)

搜尋欄輸入，**停用**

```
Python > Linting: Pylint Enabled
```

![](https://i.imgur.com/LwclBJL.png)

搜尋欄輸入，勾選

```
Python > Linting: Flake8 Enabled
```

![](https://i.imgur.com/dCt4eBO.png)

搜尋欄輸入

```=
Flake8 Args          # 搜尋這行
--max-line-length=88 # 點新增項目輸入這行
```

![](https://i.imgur.com/6vBaBPX.png)

#### 設定 black

搜尋欄輸入, 更改為 black

```
Python > Formatting: Provider
```

![](https://i.imgur.com/oWwtLya.png)

搜尋欄輸入，勾選

```
Editor: Format On Save
```

![](https://i.imgur.com/ycbt1Po.png)

#### 設定 isort

搜尋欄輸入，點選 `在 setting.json 編輯`

```
Editor: Code Actions On Save
```

setting.json

```json
"editor.codeActionOnSave": {
    "source,organizeImports": True  // 新增這行
}
```

#### 設定 mypy

搜尋欄輸入，勾選

```
Python > Linting: Mypy Enabled
```

![](https://i.imgur.com/uL2gFSb.png)

#### 最終 .vscode/setting.json 內容

```json=
{
  "python.linting.pylintEnabled": false,
  "python.linting.flake8Enabled": true,
  "python.linting.flake8Args": [
    "--max-line-length=88"
  ],
  "python.formatting.provider": "black",
  "editor.formatOnSave": true,
  "editor.codeActionsOnSave": {
    "source.organizeImports": true
  },
  "python.linting.mypyEnabled": true
}

```
