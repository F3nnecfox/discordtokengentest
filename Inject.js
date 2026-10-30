
    email=""
    username=""
    global_name=""
    password=""
    const hcapcha = (await fetch("/api/v9/auth/register",
                {
                    "fingerprint": ((await fetch("api/v9/experiments")).json()).fingerprint,
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
https://api.hcaptcha.com/checksiteconfig?v=3b71cbe0d677f40e17dc54f11aed7a067d3e1066&host=discord.com&sitekey=a9b5fb07-92ff-493f-86fe-352a2803b3df&sc=1&swa=1&spst=0
