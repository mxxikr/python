from slack_cleaner2 import *
import os
### User Token Scope ###
# channels:history
# channels:read
# chat:write
# files:read
# files:write
# groups:history
# groups:read
# im:history
# im:read
# mpim:history
# mpim:read
# users:read

slack_token = os.environ.get('A_SLACK_TOKEN')
s = SlackCleaner(slack_token)

# list of users
s.users

# list of all kind of channels
s.conversations

# delete all messages in channels
for msg in s.c['D01FNCYBY1Z'].msgs(with_replies=True):
    msg.delete(replies=True, files=True, as_user=True)
    print(f"{msg} 삭제 완료")
  # delete messages, its files, and all its replies (thread)

### bash 
# slack-cleaner2 --token='' --message --mpdirect='' --user='*' --perform --user