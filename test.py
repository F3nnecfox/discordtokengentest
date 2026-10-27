import nodriver as uc
import requests
import asyncio


async def main():
    email="hirazoke@miho.uk"
    username="aoshdaoisdou183198d"
    global_name="tamatama"
    password="1145148101919"
    
    browser = await uc.start(headless=True)
    tab = await browser.get("https://discord.com/register")
    await tab.wait(5)
    print("hello")
    cookies = await browser.cookies.get_all()
    cf_clearance = next((c for c in cookies if c.name == "cf_clearance"), None)
    if cf_clearance:
        print("Pass!")
        hcaptchKeys = await tab.evaluate(
            """
            const hcapcha = (fetch("/api/v9/auth/register",
                {
                    "fingerprint": ((fetch("api/v9/experiments")).json()).fingerprint,
                    "email": email,
                    "username": username,
                    "global_name": global_name,
                    "password": password,
                    "invite":"null",
                    "consent":"true",
                    "date_of_birth":"2000-1-01",
                    "gift_code_sku_id":"null",
                    "promotional_email_opt_in":"false"
                })).json();
            """,
            await_promise=True)
    else:
        print("NoCF")
if __name__ == '__main__':
    uc.loop().run_until_complete(main())



#XInstallationID=(requests.get("https://discord.com/api/v9/apex/experiments",params={"surface": "2"}).json())["installation"]





#JSON
#{"fingerprint":"1563584986076938403.icFG2-tV160uVqJ2yQqiOOpoIts","email":"kyarogya@miho.uk","username":"kyarogya1112","global_name":"kyarogya","password":"259533kaoru","invite":null,"consent":true,"date_of_birth":"2000-12-06","gift_code_sku_id":null,"promotional_email_opt_in":false}



#POST /api/v9/auth/register HTTP/3
#Host: discord.com
#User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:157.0) Gecko/20100101 Firefox/157.0
#Accept: */*
#Accept-Language: ja,en-US;q=0.9,en;q=0.8
#Accept-Encoding: gzip, deflate, br, zstd
#Content-Type: application/json
#X-Captcha-Key: P1_eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.haJwZACjZXhwzmrfS52ncGFzc2tlecUIM24GQVGD_mBnI5CjvY5YvGghHaME2i2rpvmHPwopS9Lg1HnI27aTCSDgOLHc9ovmOKVS9YeFdjBt12kOufn4ApZzhiPIBraEPefymn1Th95On14pjjR-sKV9SHwA9tqkOE4YvVskdKeT02y65ag_R762F5P0PRzYQfj-8YUminoPom9GMe9Q-Q0IhrbwPccEAXiVVpyEQLXA4CQHU1HejGanvR-u7ijXs71uMWMC8Rj3_HNfBPjK0s2MeH_-LlEaGDZ6vEPDHUfA5CKEnm4tVPyx_IfJtR4HQ0sLgJuAJ0BeZMLotjgrxvKXovmVNYAOpPV11W28T-npf68TERsV0rN_5a1eaxOhAAE9dBqaBJvMq0GC6JmpkMKr5OZkzBNJSH4jkStsdRZV78ISxq8vStpVM4tUl-GD8gwTC8Xfo4hIEqJBUD_CKZoc4OTn68hMMbWKmo78XUM4uBH0MJrQE0R1hg4ONGxn0sTrjdet5meCAnQAKECaJCTOgf_GLWTL0sVtYtitchuzC88qyBXyp4UgAUXgYDRWsqghCOxHO8ORdhhX4_ch61RCReR_SAz8QvVnQzMz8nnly9C2NQ_Ods9lvyQqQK5s3rn2hcAQVU1Y8tzK0stWdVjh1DT2842dTfk-q3vkdRM2r7NTygWkQLVGxdmuWCSXzrhLKCuTA2PC5ZFWMYJTI25demgur6OCgOmUMBMGetM8IFfHTzrJzRe7tiYYPBimI39RG1MkThEUEUqXvEDV4nNektbE-x2fAE3ZDQd4RsgP9e_BL27H0uLf8Q3W0eLDtlOhDk-YqQ5jXDsMZbR-TbBgc89GdcuslpyBrRJfWiXF0kkrrg3UytF2lRmjhEP1uSIF-tZo1C0d7sk9plLFNDNwtdBVgWVYHg4ZZz-UNR5JAf7sY25sJpG6fGhHpzQ8molaw9j16ToCyWC9G2G2PcE5kWJLyQTG5e5djHnNQgQEf_TOlYVSx5a11LC6M1JZ__ZRABxwtLviNMY9wnRGxZmvn1WkCg9CRgt4wLNW9ZVOIWYEwRWfksExuv2-9wlQMrMZiqKDTwvDAfgMhC91VNPHPjqUnQrLcLUBOkw4VB5BrrnQEKzkRXQnKmmnHbTXWaNrDbig1pf6mR4FaPu3c42OySGpH-ba8i43_fbXQgxOprXAtARJYBkJ_npSrdVBnupS1-fNKoADUwsUxA_HU4bKbXgrrlBATHNFdwDmT21Fots7wR3Gcw2Ol_FmSqIaUW_2p1RVZnxr9fyUQhZdt_p2rEqESJBlNg1nObz98hy9zeWjYU3DBYuyPL-qoL1bxVVvhQcCOKtqMr0LGNfix9R01Fgm3g1bWVFW6Mwtmacz5-d5V9uIuYXsGvHRhTkGMkdD6t4_GqTUYAg1ViNLiwzJU7tXxusAhsy3FSFA1i79K3aTkVCKDSg762obsJGHi4Cy6xhf15iLLZvX8HXuzysKG3HptM42StG86TQsqrEu3-C3Y59dKv1FnYwHWZVrx6KEoYZDCcQTlEllrXlzPr-bnQHbZvwo24k4ok3bqEZPwJvAWznZ-r1xL-NXfDkm0IGiJrq82WU0TjYG1A5CFqYDHIw2TVL4x9mOChpVQd53VpE7N7FS60whvy6a3aJ1EcRHASOc3rJeGVC6TIeXDWbFCi5bmAKHnQQh3eemldBs-A0s247Kl1fLvJZeUtduuki8KlZhFoVBa5OI9YJIaoFQ_a0qk2jVegp2hz3rIy7cUuKxxwGax_zW6IVSE-u6Jkb_RlaY1LFYAxSNfp7-bkl4ywmEhFt30X6yQmrr-vcD6ohxS_X_JXfIuhNZStehCWmYhn1zgUarXidYp1qwpuBWZxG8igPF7FYqkcK8ml2FbM0gThSI7IJdAkWKgu_DITA5saqwGqSyO5Xqok3gCdoKA06o9neIvtJbURPL5CUjhWjOeQIGsKukQf8zsSJGz9xvFP6f3z4TWopmqcQxMoEnmAh9cDhilJGKWdtPfKfnmgnceaNSKp-UvRTf2reEYfekIi4_SiEtZ7iSs6mGKolgPxmLJAJHgHEXrY1qM1DUU_fhY7PIOY2NDl24GHY_hPe1B0JaEyDGSGViOJYhIUBh5cD1_NIo44IX6wIvmY1WI76FTLXkoWVv-xPqmB_daaNHl7keoec99o_3j5R3-h_p4POsfjAI-UD158WiWJcguddNRtaPVpx5fHhgyL91EgkxIV5CsU2M5i-yu0j8wJkWJ-z8PV0Qr6T1x7cTnmNGQQK-w-LbVV9IZcYjn9fiDnQbLbad7rycesFo6m_h6icmJRdYBonwZNEvqHLAzEjmH15FTC4_2bM9dsTS2TKqAnquvje1AOv5SYN18mN7nXAVQl_kGYj6JsPaeD_rvNG5xJiCIdXcKX7wOoVDejFj45RW9wKKDzWboisnmGCvjhJg0fEfJqzXFqoKJOmF2chk0-hOUmD1HUI81kJKxHYLmv1QGea_EKU7ZCEsQJqrTYnB3I9XKxQdL5-7ox0Kmr_MdyRpBCWGc19bbT1TSNGZHyyG26eE9axyettGPjcKSSZWUlfEOoMSh0BVXVSpRkTEtaDWfY3M0XF43W7jBsUXBnHqSlhTVsj0iXTkTTpunLIf4Vpb7n5ga_ZAD6m_FUINqwN25ehH-SG9FMnb0CDbImp7Vr4dpgpRdDbkkj0d_p4rCwI5dWFr5r0ai1dbmH_TncDSQ7AJWlWD2Rw3D7penEkzdtmSXy_NrSxbXDivJg3AxBgIuleRKR5d4tGOOv-wBqzn3t2f7Q11LByL2y7Lxby74I-3hz80FzDJomtyp2UzMTVjOGOoc2hhcmRfaWTOFZnkVA.xNKUukelClKoMSeTAN99iJq5NbSjps4644kuikjFmfg
#X-Captcha-Rqtoken: Im1oOWQ5UVQyS3lQa2RYZDduRGpCa0diZDdwTEZvK2VWSlY2c3U0VGZ3OHlJNEl6b0hXeFh2UEtGTnE0d1NEMlFCY0NZdlE9PVpWSGNXZVJEbzByd1ZINnci.at9K6Q.ZSbdcjahwZEH28LAZmY-Bn75QIY
#X-Captcha-Session-Id: 2131e198-3355-46a5-ad17-35ab912c783d
#X-Super-Properties: eyJvcyI6IkxpbnV4IiwiYnJvd3NlciI6IkZpcmVmb3giLCJkZXZpY2UiOiIiLCJkZXZpY2VfbW9kZWxfbmFtZSI6IiIsInN5c3RlbV9sb2NhbGUiOiJqYSIsImhhc19jbGllbnRfbW9kcyI6ZmFsc2UsImJyb3dzZXJfdXNlcl9hZ2VudCI6Ik1vemlsbGEvNS4wIChYMTE7IExpbnV4IHg4Nl82NDsgcnY6MTU3LjApIEdlY2tvLzIwMTAwMTAxIEZpcmVmb3gvMTU3LjAiLCJicm93c2VyX3ZlcnNpb24iOiIxNTcuMCIsIm9zX3ZlcnNpb24iOiIiLCJyZWZlcnJlciI6IiIsInJlZmVycmluZ19kb21haW4iOiIiLCJyZWZlcnJlcl9jdXJyZW50IjoiaHR0cHM6Ly9kaXNjb3JkLmNvbS8iLCJyZWZlcnJpbmdfZG9tYWluX2N1cnJlbnQiOiJkaXNjb3JkLmNvbSIsInJlbGVhc2VfY2hhbm5lbCI6InN0YWJsZSIsImNsaWVudF9idWlsZF9udW1iZXIiOjY0OTM4OSwiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbCwiY2xpZW50X2xhdW5jaF9pZCI6ImNhNGQwMGEwLTdmYzEtNDA2MS1iN2E1LTFhNjg2ZjliMTI0YSIsImxhdW5jaF9zaWduYXR1cmUiOiJkZDNmNjgyZC1jMzQ1LTQ0ZGItODA1NC1mNTIwNzA5MTczODkiLCJjbGllbnRfYXBwX3N0YXRlIjoidW5mb2N1c2VkIn0=
#X-Fingerprint: 1563584986076938403.icFG2-tV160uVqJ2yQqiOOpoIts
#X-Installation-ID: 1511996558919602211.F9Qwy9R0OlR9q7fCtz7YkSa-KpM
#X-Discord-Locale: ja
#X-Discord-Timezone: Asia/Tokyo
#X-Debug-Options: bugReporterEnabled
#Content-Length: 283
#Origin: https://discord.com
#Alt-Used: discord.com
#Connection: keep-alive
#Referer: https://discord.com/register
#Cookie: __dcfduid=d0db40b05fe711f1af7fe95865e47a1a; __sdcfduid=d0db40b15fe711f1af7fe95865e47a1ae047a0df205b566eb4cc3b6bdc573f907be6b01861440035e9ba70c88b9838ea; cf_clearance=OrXd2ncQHXDI.NN0sT6YO8UJ1eoq88XtWDwpIDSzgMo-1793018147-1.2.1.1-NBRgFGUwTayGcJy76wtbGFpN.Xvc1k85OvGCwfa7ZeNUBr2GZOBm2uso1r2gVclTZNCysxh4EuBTFbaMRWpnNpBPGh8F2zkEZrcgRcblWeYd5uSLjCYT6cAOBBIIpl9LtfDKcBASTBar_miMryysv8h5Gc0vTE7oriTrYYtqn1gCAeSq_R9xRslzAa9VZehf5fSRwkbehp1bfNNZW7jEiCbAIS_uGiWL8_MYErR7PZ40sTHwCPcOggU192vnJvSsJQf3aFAS6mshKcN3A7rWsCf3IwrcIau9rpraU6wghU3EEkoW_EEPl6tLDwObSW6G1O8R_5b8ZTj_x5Fqn24_0onTrRtH6F.XYuZBkCWVnsw; OptanonConsent=isGpcEnabled=0&datestamp=Mon+Oct+26+2026+21%3A35%3A47+GMT%2B0900+(%E6%97%A5%E6%9C%AC%E6%A8%99%E6%BA%96%E6%99%82)&version=202501.2.0&browserGpcFlag=0&isIABGlobal=false&hosts=&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1&consentId=fd44c6dc-2d62-4499-95a3-ff02e41e270d&interactionCount=0&isAnonUser=1&AwaitingReconsent=false; _ga_Q149DFWHT7=GS2.1.s1793018147$o4$g0$t1793018153$j54$l0$h0; _ga=GA1.1.178034111.1780558473; _ga_YL03HBJY7E=GS2.1.s1789812828$o3$g0$t1789812833$j55$l0$h0; _gcl_au=1.1.1879046586.1789808970; dbind=755dba7c-0ea7-4473-bab1-e210f2af1c14; locale=ja; _cfuvid=lmeZiFqDTpW9Yq8ireU6c8.wUyqPaPoOupAhAyV6RDo-1793018146.4398134-1.0.1.1-6VAqLVmsMJTnOl4cL1gbEbHWkPpeU5O.FPlcePBD7Ro; __cf_bm=0WFAtuWnnBkXyJT_uDHDmBVKlTb98aVw2bADFpetRjA-1793018600.8167074-1.0.1.1-GaiYzhqizfMlm8qpsm8V473n0JMblJOwQUpFXz0Mso5xs0P.j.yr3qxvC7ZjFaoLgiy9X7tG6njXcNoyle.GWhpibP_o4g43gcVCDRXAVHL0YtbMLPhWU1l548_kbCfz
#Sec-Fetch-Dest: empty
#Sec-Fetch-Mode: cors
#Sec-Fetch-Site: same-origin
#Pragma: no-cache
#Cache-Control: no-cache
#TE: trailers

#JSON
#{"fingerprint":"1563584986076938403.icFG2-tV160uVqJ2yQqiOOpoIts","email":"kyarogya@miho.uk","username":"kyarogya1112","global_name":"kyarogya","password":"259533kaoru","invite":null,"consent":true,"date_of_birth":"2000-12-06","gift_code_sku_id":null,"promotional_email_opt_in":false}
