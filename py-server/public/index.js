function initializeJokesSSE() {
    console.log("Initializing jokes SSE");
    // Get references to the joke div
    const serverSentJokeDiv = document.getElementById("server-sent_joke");

    // Create a new EventSource to connect to the /jokes endpoint
    const anotherEventSource = new EventSource("/jokes");

    // Listen for the connection open event
    anotherEventSource.addEventListener("open", (event) => {
        // Update the joke div to show that the connection is open
        serverSentJokeDiv.textContent = "Connected to /jokes endpoint\n";
    });

    // Listen for messages from the /anotherendpoint endpoint
    anotherEventSource.addEventListener("message", (event) => {
        // Update the message div with the received message
        serverSentJokeDiv.textContent += event.data;
    });


    // Listen for errors in the SSE connection
    anotherEventSource.addEventListener("error", (event) => {
        if (event.target.readyState === EventSource.CLOSED) {
            // Update the jokes div to show that the connection was closed
            serverSentJokeDiv.textContent = 'Connection to /jokes endpoint was closed';
        } else if (event.target.readyState === EventSource.CONNECTING) {
            // Update the status div to show that the client is trying to reconnect
            serverSentJokeDiv.textContent = 'Connecting to /jokes endpoint...';
        } else {
            // Update the status div to show that there was an error
            serverSentJokeDiv.textContent = 'Error with /jokes endpoint';
        }
    });
};


// Ensure the function is available globally
window.initializeJokesSSE = initializeJokesSSE;
