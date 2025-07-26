# Can't get this to work on server

## Question

**Ric** asked on 18 Jun 2019

The date picker works fine on my machine debugging in VS but moving it out to a server I get an error. It fails when I click a date. From fiddler: DELETE [http://app2/purchaserequests/_blazor?id=FHxqj9eUdV72Ogv7Nz_OEg](http://app2/purchaserequests/_blazor?id=FHxqj9eUdV72Ogv7Nz_OEg) HTTP/1.1 Origin: [http://app2](http://app2) Referer: [http://app2/purchaserequests](http://app2/purchaserequests) User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763 Cache-Control: max-age=0 Accept: */* Accept-Language: en-US,en;q=0.5 Content-Type: text/plain;charset=UTF-8 X-Requested-With: XMLHttpRequest Accept-Encoding: gzip, deflate Content-Length: 0 Host: app2 Connection: Keep-Alive Pragma: no-cache Authorization: Negotiate YIIGqwYGKwYBBQUCoIIGnzCCBpugMDAuBgkqhkiC9xIBAgIGCSqGSIb3EgECAgYKKwYBBAGCNwICHgYKKwYBBAGCNwICCqKCBmUEggZhYIIGXQYJKoZIhvcSAQICAQBuggZMMIIGSKADAgEFoQMCAQ6iBwMFACAAAACjggSaYYIEljCCBJKgAwIBBaEQGw5OUkdTWVNURU1TLklOQ6IXMBWgAwIBAqEOMAwbBEhUVFAbBGFwcDKjggReMIIEWqADAgESoQMCATKiggRMBIIESDaAgCIPU5pwlAqbtuKJi6cKIYQi6RENH0nqdRQKfHkqZt ************************************************************************************************************************************************************************************** The response: HTTP/1.1 404 Not Found Transfer-Encoding: chunked Content-Type: text/plain Server: Microsoft-IIS/8.5 Persistent-Auth: true X-Powered-By: ASP.NET WWW-Authenticate: Negotiate oYG2MIGzoAMKAQChCwYJKoZIgvcSAQICooGeBIGbYIGYBgkqhkiG9xIBAgICAG+BiDCBhaADAgEFoQMCAQ+ieTB3oAMCARKicARuwTmW8q4q9F/fdoaK2/PDruGCkdkI7pOEjkefMGWNE36IZgNAIO+ECmKhZPsMUdi4SedW9NPcpRcyWbO/IKn52HOhDPYUkcCGmxVbMPW006UvpzDPa2/HKJJxO7JDuw0+b8Yi6bIibjNVbxvL/AM=Date: Tue, 18 Jun 2019 01:19:11 GMT 1a No Connection with that ID 0

## Answer

**Marin Bratanov** answered on 18 Jun 2019

Hello Rick, This looks like a problem with the SignalR connection between the host and the client. Are there any errors thrown? There was an issue in the picker where it caused errors in a server-side Blazor app that was fixed in 1.1.1, can you confirm this is the version you are using? If the same code works as expected on your machine, but not on another, I recommend that you compare them and ensure they have the same tooling installed. Also, our components are, at the moment, compatible with .NET Core Preview 5 only. Preview 6 went out last week and brought a lot of breaking changes, and we are working on a release that will adapt to them. We are expecting it will be out by the end of the week. On that note - if the server is having a different version than Preview 5, this can also cause various issues. You would then need to upgrade to Preview 6 when you get the 1.2.0 release we will shortly ship. Regards, Marin Bratanov

### Response

**Rick** answered on 18 Jun 2019

Looks like the issue was I missed enabling websockets.

### Response

**Marin Bratanov** answered on 19 Jun 2019

Hi Rick, It's good to hear you solved this. If you don't mind, would you share where was the setting that caused this problem, because it does not seem like a default behavior to me, and this information may be useful for someone else in the future. Regards, Marin Bratanov

### Response

**Rick** answered on 19 Jun 2019

Open server manager Add roles and features Chose server go to server roles Expand web server (IIS) Expand web server Expand Application Development Ensure that web socket protocol is checked

### Response

**Marin Bratanov** answered on 20 Jun 2019

Thanks for sharing, Rick. I marked both your posts as answers to this thread for anyone else encountering this in the future. --Marin
