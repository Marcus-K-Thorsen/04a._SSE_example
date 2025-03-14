# 04a [Individual] SSE Example

**Type**: Individual

Create or use an SSE example.

You can reuse one of the two we created in class or create a new one. The important thing is that you understand the example well. 

For this assignment, I **will** ask about implementation details of SSE during the exam.


## Understanding Server-Sent Events (SSE)

Server-Sent Events (SSE) is a standard allowing servers to push data to web clients over a single HTTP connection. It is commonly used for real-time updates, such as notifications, live feeds, or streaming data.

### How SSE Works

1. **Client Requests SSE Endpoint**: 
    - The client initiates a connection to the server by making an HTTP request to a specific endpoint designed to handle SSE.
    - This is typically done using the `EventSource` API in JavaScript, which creates a persistent connection to the server.

2. **Server Keeps Connection Open**: 
    - Upon receiving the request, the server responds by keeping the HTTP connection open.
    - The server sends updates to the client as events occur, using a specific format for the event data.
    - The connection remains open, allowing the server to push multiple updates over time without needing to re-establish the connection.

3. **Client Receives Updates**: 
    - The client listens for incoming events from the server.
    - When an event is received, the client processes the event data and updates the user interface or performs other actions as needed.
    - The `EventSource` API provides event listeners to handle different types of events, such as `message`, `open`, and `error`.

### Illustration

```plaintext
+---------+            +---------+
|  Client |            |  Server |
+---------+            +---------+
     |                      |
     |  Request SSE         |
     |--------------------->|
     |                      |
     |  Open Connection     |
     |<---------------------|
     |                      |
     |  Receive Event       |
     |<---------------------|
     |                      |
     |  Process Event       |
     |--------------------->|
     |                      |
     |  Receive Event       |
     |<---------------------|
     |                      |
     |  Process Event       |
     |--------------------->|
     |                      |
```

In this illustration:
- The client requests the SSE endpoint from the server.
- The server responds by keeping the connection open and sending events to the client.
- The client receives and processes the events as they arrive, updating the user interface or performing other actions as needed.


# Server-sent events (SSE)

Based on the same technique as long polling.

Unidirectional. Allows servers to update clients as long as the client has the appropriate code setup.

Most browsers today [support it](https://caniuse.com/eventsource). 
No libraries needed. Just declare:

```javascript
new EventSource("url");
```

And the server must respond with the following in its header:

```json
{
    "Connection": "keep-alive",
    "Content-Type": "text/event-stream",
    "Cache-Control": "no-cache"
}
```

---

# Required Headers and their meaning


| Key             | Value                | Reason why                                              |
|-----------------|----------------------|-------------------------------------------------------|
| `Connection`    | `keep-alive`         | Keeps the connection open for continuous event streaming. This is necessary because SSE relies on a persistent connection to push updates to the client without closing and reopening the connection. |
| `Content-Type`  | `text/event-stream`  | Ensures the browser treats the response as an event stream. This tells the browser to expect a stream of events and process them accordingly. |
| `Cache-Control` | `no-cache`           | Prevents caching to ensure real-time updates. This ensures that the browser does not cache the response and always receives the latest updates from the server. |


---

# SSE Sending data

The format to send data is:

```plaintext 
data: somedata \n\n
```

| Field   | Purpose                                                                |
|---------|------------------------------------------------------------------------|
| `event:` | Defines a custom event type (instead of the default `"message"`).     |
| `id:`    | Assigns a unique identifier to the event (used for reconnection).     |
| `retry:` | Suggests a reconnection delay (in milliseconds) if the connection is lost. |

To send a data event, the data sent must start with `data:`.

While `\n\n` signals the end of an event, `\n` signals a newline in the event to send multiple lines of data:

```plaintext
data: Line1
data: Line2
```
