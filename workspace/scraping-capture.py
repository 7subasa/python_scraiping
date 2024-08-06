import os
import time
from PIL import Image
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException


# 指定したXpathの値をクリック
def click(driver, xpath):
    try:
        target_element = driver.find_element(By.XPATH, xpath)
        target_element.click()
    except NoSuchElementException:
        print('要素が見つかりませんでした')


# スクリーンショット
def capture(driver, filename):
    try:
        driver.save_screenshot(filename)
    except:
        print('キャプチャに失敗')


# ページ全体のキャプチャ
def capture_full_page(driver, filename):
    original_size = driver.get_window_size()
    body = driver.find_element(By.TAG_NAME, 'body')
    body_size = body.size
    driver.set_window_size(body_size['width'], body_size['height'])

    # スクロールしてキャプチャ
    total_height = driver.execute_script('return document.body.scrollHeight')
    driver.set_window_size(body_size['width'], total_height)
    capture(driver, filename)

    driver.set_window_size(original_size['width'], original_size['height'])


# 文字入力
def input_text(driver, xpath, value):
    try:
        target_element = driver.find_element(By.XPATH, xpath)
        target_element.send_keys(value)
    except NoSuchElementException:
        print('要素が見つかりませんでした')


def main():
    # Chromiumのオプションを設定
    chrome_options = Options()
    chrome_options.binary_location = "/usr/bin/chromium"  # Chromiumのバイナリパス
    chrome_options.add_argument("--headless")  # ヘッドレスモードを有効にする コンテナのブラウザにはGUIが無いから
    chrome_options.add_argument("--no-sandbox")  # サンドボックスを無効にする セキュリティ制限を避けるため
    chrome_options.add_argument("--disable-dev-shm-usage")  # 共有メモリの使用を無効にする
    chrome_options.add_argument("--disable-gpu")  # GPUの使用を無効にする
    chrome_options.add_argument("--remote-debugging-port=9222")  # リモートデバッグポートを設定

    # WebDriverを起動
    driver = webdriver.Chrome(options=chrome_options)

    # 対象ページを開く
    driver.get("URL")

    # ログイン処理
    input_text(driver, xpath='//*[@id="user_email"]', value='')
    input_text(driver, xpath='//*[@id="user_password"]', value='')

    # ログインボタンをクリック
    click(driver, xpath='//*[@id="new_user"]/div[4]/button')

    # 対象のボタン分処理
    for key, xpath in capture_xpaths.items():
        # タイトルを取得して出力
        print(driver.title)

        # 要素をクリック
        click(driver, xpath)
        # スクリーンショットのファイル名を生成
        filename = os.path.join(SAVE_DIR, f'{driver.title}-{key}.png')
        # スクリーンショットを保存
        capture_full_page(driver, filename)
        print(f'キャプチャを保存: {filename}')

    # ブラウザを終了
    driver.quit()

if __name__ == "__main__":

    # キャプチャの保存場所
    SAVE_DIR = 'captures'
    if not os.path.exists(SAVE_DIR):
        os.makedirs(SAVE_DIR)

    # キャプチャを取るためXpath
    capture_xpaths = {
        1: '//*[@id="page_top"]/a',
    }

    main()

