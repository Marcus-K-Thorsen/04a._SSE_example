import express from 'express';

const app = express();

// Serve static files from the 'public' directory
app.use(express.static('public'));

// SSE endpoint to send jokes to the client
app.get("/jokes", (req, res) => {
    res.writeHead(200, {
        // Set headers to keep the connection open and specify the content type as SSE
        "Connection": "keep-alive", // Keeps the connection open for continuous event streaming
        "Content-Type": "text/event-stream", // IMPORTANT: Ensures the browser treats the response as an event stream
        "Cache-Control": "no-cache" // Prevents caching to ensure real-time updates
    });

    // Send a joke to the client every 10 seconds
    // This interval function will repeatedly call sendJokeToClient to push updates to the client
    setInterval(() => sendJokeToClient(res), 10000);
});

// Function to send a random joke to the client
function sendJokeToClient(res) {
    const jokes = [
        "Why don't scientists trust atoms? Because they make up everything!",
        "Why did the scarecrow win an award? Because he was outstanding in his field!",
        "Why don't skeletons fight each other? They don't have the guts.",
        "What do you call fake spaghetti? An impasta!",
        "Why did the bicycle fall over? Because it was two-tired!"
    ];
    const randomJoke = jokes[Math.floor(Math.random() * jokes.length)];
    // Send the joke as an SSE event
    // The 'data:' prefix and '\n\n' suffix are required for SSE format
    res.write(`data: ${randomJoke} \n\n`);
}

const PORT = Number(process.env.PORT) || 8080;

// Start the server and listen on the specified port
app.listen(PORT, () => {
  console.log("Server is running on port", PORT);
});
