# sf-task-slack
Pushes Salesforce tasks to Slack.

This is a very rough script that takes a Salesforce user's tasks and posts their RelatedTo URLs to a Slack channel/message.
All of the login/API info needs to be hardcoded in.
Currently using launchd (or cron) to schedule the task to run weekly.

##Requirements
[Simple Salesforce](https://github.com/heroku/simple-salesforce)
[Slacker](https://github.com/os/slacker)