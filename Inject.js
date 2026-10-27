
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
