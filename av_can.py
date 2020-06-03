import feedparser
from twilio.rest import Client
# Twilio user information
account_sid = #"Twilio Account SID here"
auth_token = #"Twilio auth token here"


# Get the RSS feed from Avalanche Canada for desired forecast region
news_feed = feedparser.parse('https://www.avalanche.ca/api/forecasts/kootenay-boundary.rss')
entry = news_feed.entries[0]

# print (entry.keys())

# Get part of RSS feed that we want
bulletin = entry.summary

# Convert RSS to string
bulletin = str(bulletin)

# Use .replace() to make message more readable and remove html syntax, probably a better way to do this
new_bulletin = bulletin.replace('<h1>','')\
                       .replace('<article>','')\
                       .replace('</h1>','')\
                       .replace('<article><header>Avalanche Bulletin - Kootenay-Boundary</h1><p><b>Date Issued:</b><time datetime=','')\
                       .replace('<p>','')\
                       .replace('</p>','')\
                       .replace('</div>','')\
                       .replace('</section>','')\
                       .replace('<header>','')\
                       .replace('<b>','')\
                       .replace('</b>','')\
                       .replace('<time','')\
                       .replace('</time>','')\
                       .replace('</header>','')\
                       .replace('<section>','')\
                       .replace('>','')\
                       .replace('<table','')\
                       .replace('<thead>','')\
                       .replace('<tr>','')\
                       .replace('<thead','')\
                       .replace('<tr','')\
                       .replace('</th','')\
                       .replace('<th','')\
                       .replace('tyle="border-spacing:0px; border-color: black; border-collapse: collapse;','')\
                       .replace('style="background-color: #ddeefa','')\
                       .replace('</tr','')\
                       .replace('<tbody','')\
                       .replace('<td','')\
                       .replace('</td','')\
                       .replace('style="background-color: #f79218"','')\
                       .replace('style="background-color: #fff300"','')\
                       .replace('style="background-color: #f79218"','')\
                       .replace('style="background-color: #f79218"','')\
                       .replace('Date Issued: datetime="','')\
                       .replace('Valid Until: ','')\
                       .replace('style="background-color: #aebfac"','')\
                       .replace('style="background-color: #d1d9a3"','')\
                       .replace('</tbodyead','')\
                       .replace('</table','')\
                       .replace(' ','')\
                       .replace('<caption','')

# Limit size of outgoing message (InReach allows only 160 char per messages)
# Could break message up into 160 character chunks and send multiple messages
outgoing = new_bulletin[385:545]

# Print message
print(outgoing)

# Check length of outgoing
print(len(outgoing))
print(len(new_bulletin))

# Send message to phone using Twilio
client = Client(account_sid, auth_token)
message = client.messages.create(
                            body = #[this is the message you want to send],
                            from_ = #[from phone number here],
                            to= # [message recipient phone number]
                        )
print(message.sid)
print("Message sent to " + message.to)
print("Complete")