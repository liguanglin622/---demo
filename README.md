# 梅间一卦

## 发布到公网（GitHub Pages）

GitHub Pages 发布后，任何人都可以通过手机 Wi-Fi 或移动网络访问 HTTPS 链接。当前工作流只发布 `index.html` 页面，不公开提供本地手机预览服务器或其他项目文件。

1. 本项目使用的公开仓库是 [`liguanglin622/---demo`](https://github.com/liguanglin622/---demo)。
2. 在终端进入本项目目录：

   ```bash
   cd "$HOME/Desktop/机器人行业需要我/梅花易数"
   git add index.html README.md start_mobile.py 手机访问.command .github/workflows/deploy-pages.yml
   git commit -m "Update Plum Blossom divination site"
   git push -u origin main
   ```

   如果 Git 还没有关联远程仓库，先运行：

   ```bash
   git remote add origin https://github.com/liguanglin622/---demo.git
   ```

   GitHub 首次认证时按终端或浏览器提示完成登录，不要把密码或访问令牌发给别人。
3. 在仓库的 **Settings → Pages → Build and deployment** 中，将 **Source** 设为 **GitHub Actions**。
4. 打开仓库的 **Actions** 页面，等待 `Deploy static site to GitHub Pages` 执行成功。
5. 公网地址通常是 <https://liguanglin622.github.io/---demo/>。将此 HTTPS 链接发给访客即可；首次部署可能需要几分钟。

仓库设为公开，意味着仓库中的源文件可被其他人浏览。Pages 工作流只会把 `index.html` 发布为网站内容。以后修改网页并推送到 `main`，GitHub Actions 会自动重新发布。

## 在手机上打开

1. 电脑和手机连接同一个 Wi-Fi。
2. 在 Finder 中双击 `手机访问.command`。如果 macOS 提示确认，请选择“打开”。
3. 保持弹出的终端窗口运行；窗口会显示手机访问地址，例如 `http://192.168.1.23:8766/`。
4. 在手机浏览器输入该地址即可。电脑休眠、服务窗口关闭或切换 Wi-Fi 后，地址可能无法访问。

如果 macOS 防火墙询问是否允许 Python 接受网络连接，请允许私人网络连接。

也可以在终端进入项目目录后运行：

```bash
python3 start_mobile.py
```

## 说明

- 此预览服务绑定到本机所有网络接口，可供同一局域网访问；它只提供本目录中的静态网页，不处理或保存提交数据。
- 若希望离开当前 Wi-Fi 后仍可访问，需要将网页部署到 HTTPS 静态网站托管服务。局域网地址不能从互联网直接访问。
- 主页面为 `index.html`，可离线直接查看；跨设备访问需启动上述服务。
