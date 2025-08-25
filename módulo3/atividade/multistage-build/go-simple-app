package main

import (
    "fmt"
    "net/http"
    "os"
)

func main() {
    greeting := os.Getenv("MESSAGE")
    if greeting == "" {
        greeting = "Hello, World!"
    }

    http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
        fmt.Fprintf(w, "%s\n", greeting)
    })

    port := os.Getenv("PORT")
    if port == "" {
        port = "8080"
    }

    fmt.Printf("Listening on port %s...\n", port)
    http.ListenAndServe(":"+port, nil)
}
