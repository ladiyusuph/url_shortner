# URL Shortening Service

An API that takes in users' URLs and shortens them.

## About

This project provides a simple API for shortening URLs. Users can input a long URL, and the service will generate a shorter, more manageable URL. When the shortened URL is accessed, it redirects the user to the original long URL.

## Endpoints

- **POST /shorten/**: Takes a long URL and returns a shortened URL.
  - Request Body:
    ```json
    {
      "url": "http://example.com"
    }
    ```
  - Response Body:
    ```json
    {
      "Long URL": "http://example.com",
      "Shortened URL": "http://short.url/abc123"
    }
    ```
- **GET /<slug>**: Redirects the shortened URL to the main URL.

## App Logic

1. The user enters a URL address.
2. The URL is saved to the database.
3. A shortened URL (slug) is generated for each input URL.
4. Clicking on the shortened URL will redirect the user to the long URL.
