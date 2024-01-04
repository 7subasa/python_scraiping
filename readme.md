
## 事前準備
1. **Dockerのインストール**: Dockerを公式サイトからダウンロードしてインストールします。
2. **Docker Desktopのインストール**: Docker Desktopを公式サイトからダウンロードしてインストールします。
3. **VSCode拡張機能のインストール**:
   - [Dev Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers): VSCodeの拡張機能マーケットプレイスからインストールします。

## Pythonの開発環境を構築
1. 任意のフォルダを作成し、コマンドプロンプトでそのフォルダを開きます（`mkdir`や`cd`コマンドを使用）。
2. 以下のコマンドを実行して、Pythonの開発環境をクローンします。
   ```bash
   git clone https://github.com/7subasa/python_scraiping.git
   ```
3. 以下のコマンドを実行して、リモートリポジトリを削除します。
   ```bash
   git remote remove origin
   ```
4. Docker Desktopアプリを起動します。
5. クローンしたPython開発環境をVSCodeで開きます。
6. VSCodeでターミナルを起動します。
7. 以下のコマンドを実行してコンテナを起動します。
   ```bash
   docker-compose up -d
   ```
8. VSCodeの左下にある `><` アイコンをクリックします。
9. 「Attach to Running Container...」をクリックします。
10. `/python3_container` をクリックします。
11. ディレクトリを開くよう指示されたら `workspace/` を指定します。
12. 以上で開発環境のセットアップが完了です。

## Pythonプログラムの実行
例として、`Hello.py`を実行します。
1. 左のワークスペースにある `Hello.py` を開きます。
2. `F5` キーを押すか、メニューから「Run > Start Debugging」をクリックして実行します。
3. 初回実行時にはConfigurationを聞かれるので、「Python File」を選択します。
4. コンソールに「Hello」が表示されるはずです。

これを応用して、`FirstScraiping.py`も実行してみてください。

**トラブルシューティング**:
もし正常に動作しない場合は、使用しているPythonが切り替わっている可能性があります。VSCodeの右下にあるベルの横の数字の部分をクリックし、「Python 3.10.13」を指定して再度実行してください。

