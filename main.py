from hook import webhook_url
while True:
   cnt = input("Message to send? : ")
   def_hook = hook.webhook_url()
   webhook = DiscordWebhook(url=def_hook, content=cnt)
   response = webhook.execute()
