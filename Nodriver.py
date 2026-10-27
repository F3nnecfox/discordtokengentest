import nodriver

async def main():
    browser = await nodriver.start()
    base_url = "https://quotes.toscrape.com"
    page = await browser.get(base_url)
    await page.close()
if __name__ == '__main__':
    nodriver.loop().run_until_complete(main())
