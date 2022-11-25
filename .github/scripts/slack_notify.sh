curl -X POST -d \
"payload={
	'channel': '$SLACK_CHANNEL',
	'text': '$SLACK_MESSAGE'
}" \
$SLACK_WEBHOOK
