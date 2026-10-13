# cyber-security-study

记录学习网络安全过程中用过的脚本

## 目录

| 目录 | 内容 |
| --- | --- |
| `CTF/crypto/` | 密码学相关脚本：JWT 密钥爆破、RC4、RSA（小 e / 完整流程）、TEA 分组密码 |
| `渗透测试基础/` | 网络编程与渗透基础工具：TCP/UDP 客户端与服务端、TCP 代理、netcat 实现、SSH 远程命令执行 |
| `py基础语法/` | Python 基础语法练习：函数、类、列表/字典、循环、异常处理、模块导入 |

## 说明

- `CTF/crypto/JWT爆破密钥.py` 依赖字典文件 `rockyou.txt`（约 139 MB）。该文件超出 GitHub 单文件 100 MB 限制，因此未纳入仓库，运行前请自行准备字典。
- `渗透测试基础/` 中的脚本仅用于本地授权环境下的学习与测试。

## 环境

部分脚本依赖第三方库：

```bash
pip install pycryptodome paramiko
```

- `pycryptodome` — `CTF/crypto/` 下的 RSA 相关脚本
- `paramiko` — `渗透测试基础/ssh_cmd.py`
