# WazzUp???

- Aggregate message streams
- Provide proactive and reactive observational filter based on explicit and implied content
- Provide explicit and autonomous reply to message streams where approved by the user

## Architecture

### Content Hosts (external)

- not all provide notifcations, searching, or API access

- Slack
- Discord
- Twitter
- WeChat
- Line
- Zoom
- Skype
- Teams
- Signal
- WhatsApp
- Facebook Messenger
- Email
- Document upload (in-house message host)
- Snail mail (just a wrapper around document upload)
- SMS
- RSS
- Webhooks
- Google
- Bing
- YouTube
- ChatGPT
- Bard
- AppleMusic
- News
- NYT

### Message Host Interface Layer

- message host webhooks: listen for new messages that user has subscribed to
- message host API: explicitly query for new messages
- message sender API: send messages to other users/channels

- organic interface with semi-structured headless browser agent: for sites that don't have an API or webhooks
    **Must access the sites on the users device** to avoid copyright issues and storing their credentials.
- API-specific interface: for sites that have an API

### Information Organization Layer

- use multiple semantic indexes like
  - what is this about? (emb)
  - who is this about? (entity extraction with heavier wieght on character-level similarity)
  - what is the source? (source extraction, KG matching)
  - whendid this happen? (date extraction if possible, assign a small weight to date accessed. but the heaviest weight is on the date the information source generated the content)
  - where did this happen? (geolocation extraction and geo-based similarity. also give some weight to semanticly similar items)
  - what is the sentiment? (sentiment analysis)
  - why is this important? (topic modeling)
- additional user defined semantic index prompts

- Each piece ofcontent is saved onthe users device after we have computed all the embeddings and other stuff on the server.

### Reactive User Interface Layer

1. Event is triggered by a new message or a time interval (or a user input statement, in the case of responsive)
2. The agent determines whether to respond to the event based on the user's preferences
3. If respond,
   1. The agent generates a response based on the user's preferences
   2. This kicks off another event, returning to step 1
4. Otherwise,
   1. the agent does nothing

Test cases:
- Hey Alice has been trying to reach you. She said she's going to be late.

### Responsive User Interface Layer

1. user types question / comment
2. this triggers an event
3. we pass a override flag to force at least one response
4. application does RAG (retrieval augmented generation) to find the most relevant content and generate a response
   1. can include snippets from the content (ideally, the entirety of one or more)

Test Cases:
- Is anyone going to the party tonight?
- Did i get billed for any subscriptions this month?

### Predictive User Interface Layer

1. The agent sets an arbitrary time interval to reconsider whether it should generate a response (step 2 of Reactive User Interface Layer)
   1. This may vary by topic over the day/week/month/year, eg, in the evening, check all the todods and ask how the day went

Test Cases:
- How was your day?
- What didyou think about the movie?

## Code Organization

### Schema

MessageHost:
- url
- logo
- name
- description
- abilities: MessageHostAbility[]

MessageHostAbility:
- listenForNewContent: boolean
- queryForContent: boolean
- sendContent: boolean

User:
- profile: Profile...
- account: Account...

Profile:
- name
- preferred contact methods: ContactMethod[] // ordered by preference
- demographics: Demographics...
- psychographics: Psychographics...
- preferences: JSONB
- notes

Account:
- clerk_auth_id
- stripe_customer_id
- admin_notes
- created_at: Date
- last_updated_at: Date
- banned_at?: Date

- messages_sent: Message[]
- message_stream_privileges: MessageStreamPrivilege[]

ContactMethod:
- host: MessageHost
- value: string
- verified: boolean

MessageStreamPrivilege:
- user: User
- read: boolean
- write: boolean
- admin: boolean

MessageSream:
- messageStreamPrivilege: MessageStreamPrivilege[]
- messages: Message[]
- archived: boolean // whenits archived the information in that chat is still there bu. if you want to delte the information, delete the convo, then you'll have to upload the info again

Message:
- content: string
- author: User
- created_at: Date
- updated_at: Date
- read_at?: Date
- deleted_at?: Date
- archived_at?: Date
- reported?: boolean
- report?: MessageReport
- stream: MessageStream

MessageReport:
- reported_on: Date
- report_reason: string
- reported_by: User
- report_user_notes: string
- report_admin_notes: string

### Services

- chat service: for collecting information and interfacing with the user
- content interface service: for interfacing with specific message hosts
  - some require the client side headless browser service to interface with, whenever the client is open
- server side headless browser service: for servicing the client-side headless browser service
  - client-side headless browser service: for interfacing with message hosts that don't have an API or webhooks
- information storage service: for storing information, indexing and retreiving it, and preventing other people from accessing unauthorized information
- event-triggered service: for triggering events based on user preferences and pre-defined event flows
  - also handles timers
- agent service: for generating responses to events based on the event content, any retreival content, and the user's prompt (if a message)

Andwe actually need to separate the contentInterfacers into
- client-side content-specific interfaces
- server-side content-specific interfaces
  - true server-side interfaces
  - wrappers for client-side interfaces