import asyncio
import nodriver as uc

async def main():
    browser = await uc.start(headless=True)

    page = await browser.get("https://google.com")

    await page.sleep(3)

    cookies = await page.get_cookies()

    if cookies:
        print(f"Cookieあり: {len(cookies)}個")
        for cookie in cookies:
            print(f"{cookie.name} = {cookie.value}")
    else:
        print("Cookieなし")

    browser.stop()

asyncio.run(main())
