## Authentication
This API uses Token-Based Authentication.

**How to authenticate:**
1. Send a POST request to `/api-token-auth/` with your `username` and `password`.
2. Copy the `token` string from the response.
3. Include the token in the `Authorization` header of all future requests:
   `Authorization: Token <your_token>`

## Permissions
* **Posts:** Public to read, but only the original author can edit or delete them.