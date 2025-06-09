# HTTP and HTTPS
<br>

## :bulb: The differences Between HTTP and HTTPS
<br>

| Feature |    HTTP    | HTTPS |
|---------|---------|-------|
|Encryption  | No | Yes (uses SSL/TLS)|
| security| Data is readable by third parties | Data is encrypted and secure |
| Port Number | 80 | 443 |
| Use Cases | Blogs, news sites, public pages | Login pages, e-commerce, banking |
| URL Format |``` http://```| ```https://```|
<br>

## :books:  The structure of an HTTP request and response
- **HTTP Request Example**
```
GET / HTTP/1.1              ← *Method - Path - HTTP version*
Host: developer.mozilla.org   ← *Header*
Accept-Language: fr           ← *Header*
```
An HTTP request typically includes the following components:<br <br>>
**Method**: Defines the action (e.g., GET, POST, OPTIONS, HEAD)<br>
**Path**: The specific resource being requested, without protocol, domain, or port.<br>
**HTTP Version**: Indicates the protocol version used.<br>
**Headers (optional)**: Provide additional information to the server.
**Body (optional)**: Used with methods like POST to send data to the server.



- **HTTP Response Example**
```
HTTP/1.1 200 OK　　　　　　　← HTTP version - Status Code - Status Message
Date: Sat, 09 Oct 2010 14:28:02 GMT          ---------
Server: Apache                                        |
Last-Modified: Tue, 01 Dec 2009 20:18:22 GMT          |
ETag: "51142bc1-7449-479b075b2891b"                 Headers
Accept-Ranges: bytes                                  |
Content-Length: 29769                                 |
Content-Type: text/html                     __________|

<!doctype html>… <br>                           ←　Body
(here come the 29769 bytes of the requested web page)
```
An HTTP response typically includes the following components:<br><br>
**HTTP Version**: Indicates the protocol version used.<br>
**Status Code**: Shows whether the request was successful and why.<br>
**Status Message**: A brief description of the status code.<br>
**Headers**: Provide additional information, similar to request headers.<br>
**Body (optional)**: Contains the requested resource or data.




## :page_with_curl: Common HTTP methods and status codes 
All HTTP response status codes are separated into five classes or categories.<br>
The first digit of the status code defines the class of response, while the last two digits do not have any classifying or categorization role. <br>
There are five classes defined by the standard:

1xx : Informational – Request received, continuing process<br>
2xx : Success – Request completed successfully<br>
3xx : Redirection – Further action needed to complete request<br>
4xx : Client Error – Problem with the request from the client<br>
5xx : Server Error – Server failed to fulfill a valid request<br>

:pencil2: **Example**
|Status Code |status message | Description |  Use cases
|--------|--------|--------|----|
|100 | continue| Keep sending the request|Large POST request in progress|
|200 | OK | Request succeeded| Page loaded successfully|
|301| Moved Permanently | Resource moved to new URL |Redirect to new website|
|403 | Forbidden | Access not allowed | Unauthorized admin access|
|404 | Not Found | Resource not found | URL does not exist |
|500 | Internal Server Error | Server had a problem | Server had a problem |
