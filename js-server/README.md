# Server-Sent Events Example

This project demonstrates how to use Server-Sent Events (SSE) with an Express server to send real-time updates to the client.

# The initital setup
```bash
 $ cd <project_directory>
 $ cd js_server
 $ npm init -y
 $ npm i express
```
Add key-value pair `"type": "module"` in `package.json`.

Create `app.js`, a folder called `public` with a file `index.html`.

# Install
```bash
 $ cd <project_directory>
 $ cd js_server
 $ npm install
```

### Running the Server

You can set the port yourself when starting the server by using the `PORT` environment variable.
If you do not set the `PORT` environment variable, the server will default to port 8080.

# Usage
```bash
 $ cd <project_directory>
 $ cd js_server
 $ nodemon app.js
# or
 $ export PORT=3000 && nodemon app.js
```



## Understanding Server-Sent Events (SSE)

Server-Sent Events (SSE) is a standard allowing servers to push data to web clients over a single HTTP connection. It is commonly used for real-time updates, such as notifications, live feeds, or streaming data.

### How SSE Works in This Application

1. **Client Requests SSE Endpoint**: 
    - The client initiates a connection to the server by making an HTTP request to the `/jokes` endpoint, which is designed to handle SSE.
    - This is done using the `EventSource` API in JavaScript, which creates a persistent connection to the server. The `EventSource` object is created and connected to the `/jokes` endpoint.

2. **Server Keeps Connection Open**: 
    - Upon receiving the request, the server responds by keeping the HTTP connection open. This is achieved by setting the appropriate headers (`Connection: keep-alive`, `Content-Type: text/event-stream`, and `Cache-Control: no-cache`).
    - The server then periodically sends updates to the client. In this application, the `setInterval` function is used to call the `sendJokeToClient` function every 10 seconds, which sends a random joke to the client.

3. **Client Receives Updates**: 
    - The client listens for incoming events from the server. The `EventSource` object provides event listeners to handle different types of events, such as `message`, `open`, and `error`.
    - When a `message` event is received, the client processes the event data and updates the user interface. In this application, the received joke is displayed in the `server-sent_joke` div.
    - The `open` event listener updates the status to show that the connection is open, and the `error` event listener handles any errors or reconnection attempts.


### Example Flow

1. **Client Request**:
    - The client requests the SSE endpoint using `EventSource`.
    ```javascript
    const eventSource = new EventSource("/jokes");
    ```

2. **Server Response**:
    - The server responds with an open connection and sends events periodically.
    ```javascript
    res.write(`data: ${randomJoke} \n\n`);
    ```

3. **Client Receives Events**:
    - The client listens for events and updates the UI accordingly.
    ```javascript
    eventSource.addEventListener("message", (event) => {
        serverSentJokeDiv.textContent = event.data;
    });
    ```

