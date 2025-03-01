# 六十甲子本地抽签工具

这是一个用于本地抽取和显示六十甲子签诗的 Python 工具。图片来自台北新莊地藏庵。本工具仅适用于 macOS 系统。

## 图片位置
60个图片保存在 images/ 目录下

## 功能

- 心里默念或抽一个六十甲子签
- 输入数字或六十甲子，抽取六十甲子签诗。
- 在命令行中显示对应的签诗图片。

## 安装要求

### 系统要求

- **macOS**：本工具仅在 macOS 上测试通过。

### 依赖工具

- **iTerm2**：确保你在使用 iTerm2 终端。
- **imgcat**：用于在命令行中显示图片。

### imgcat 安装步骤

1. **下载`imgcat`脚本**：

   - 从[iTerm2 官方文档](https://iterm2.com/documentation-images.html)下载`imgcat`脚本。

2. **保存并设置权限**：

   - 将`imgcat`脚本保存到`/usr/local/bin`目录。
   - 在终端运行以下命令以给予执行权限：
     ```bash
     chmod +x /usr/local/bin/imgcat
     ```

3. **确保路径正确**：
   - 确保`/usr/local/bin`在你的`PATH`环境变量中。如果不在，请在`~/.bash_profile`或`~/.zshrc`中添加：
     ```bash
     export PATH="/usr/local/bin:$PATH"
     ```
   - 重新加载配置文件：
     ```bash
     source ~/.bash_profile
     ```
     或
     ```bash
     source ~/.zshrc
     ```

## 使用方法

1. **运行抽签工具**：
   - 在 iTerm2 中运行`chouqian.py`脚本：
     ```bash
     python3 chouqian.py
     ```
   - 脚本将抽取相应签诗，并在命令行中显示对应的图片。

## 图片来源

图片来自台北新莊地藏庵的六十甲子签诗集。
