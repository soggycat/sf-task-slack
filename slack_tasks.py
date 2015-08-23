#!/usr/bin/env python
from simple_salesforce import Salesforce
from slacker import Slacker

# Salesforce setup
# set up username, password, token, whether environment is a sandbox, and instance url
user = # Salesforce username (string)
pswd = # Salesforce password (string)
token = # Salesforce security token (string)
sandbox_bool = # boolean for whether or not it is a Sandbox
instance_url = # Salesforce instance url (string)

# create a Salesforce object
sf = Salesforce(username = user, password = pswd, security_token = token, sandbox = sandbox_bool)

# Slack setup
slack_key = #Slack API key (string)
slack_channel = # Slack channel or message "#channel_name" or "@message_recipient"
slack_bot_name = # name of Slack bot (string)
# create a Slack object
slack = Slacker(slack_key)

# query tasks
tasks = sf.query_all("SELECT WhatId FROM Task WHERE Owner.Id='Owner ID goes here'") # Salesforce query for Tasks.

# set for WhatId
id_set = set()

# post Salesforce Task URLs to Slack
for item in tasks['records']:
  id_set.add(item['WhatId'])
slack.chat.post_message(slack_channel, 'Here is your weekly list of dupe report links!\n', username=slack_bot_name)
for item in id_set:
  #send to slack
  slack.chat.post_message(slack_channel, instance_url + item, username=slack_bot_name)