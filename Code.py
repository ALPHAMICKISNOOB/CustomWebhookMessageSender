from webhook_url import webhook_url
while True:
   content = input("Message to send? : ")
   webhook = webhook_url
   webhook = DiscordWebhook(url=webhook, content=)
   response = webhook.execute()
