import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException


# 指定したXpathの値を取得
def get_value(driver, xpath):
    try:
        target_element = driver.find_element(By.XPATH, xpath)
        return target_element.text
    except NoSuchElementException:
        print('要素が見つかりませんでした')
        sys.exit(1)


def main():
    # Chromiumのオプションを設定
    chrome_options = Options()
    chrome_options.binary_location = "/usr/bin/chromium"  # Chromiumのバイナリパス
    chrome_options.add_argument("--headless")  # ヘッドレスモードを有効にする コンテナのブラウザにはGUIが無いから
    chrome_options.add_argument("--no-sandbox")  # サンドボックスを無効にする セキュリティ制限を避けるため

    # WebDriverを起動
    driver = webdriver.Chrome(options=chrome_options)

    # yahooを開く
    driver.get("https://www.yahoo.co.jp/")

    # タイトルを取得して出力
    print(driver.title)

    # 主張ニュースのタイトルを取得
    for i in range(0, 8):
        # 要素の指定
        news_title_xpath = '//*[@id="tabpanelTopics1"]/div/div[1]/ul/li[' + str(i+1) + ']/article/a/div/div/h1/span'
        # 指定要素より値を取得(関数を使用)
        news_title= get_value(driver, news_title_xpath)
        # 取得した値をコンソールに出力
        print(news_title)


if __name__ == "__main__":
    main()
