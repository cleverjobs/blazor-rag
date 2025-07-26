# NuGet API key invalidation

## Question

**Raf** asked on 10 Dec 2023

Hello, I'm trying to figure out how does the NuGet API Key works for Telerik feed when it comes to security. I created an API Key on my account for the NuGet feed. I used it in Visual Studio via NuGet.config file method. Everything was working fine. Then I deleted the API Key from my account. I made the test again and everything seems to still work in Visual Studio. I was under the impression that the key should be invalidated and stop working after I deleted it. How does it work exactly so I can make sure I can use it in a safe way? Does the key still work after deletion until it's expiration date?

## Answer

**Rafał** answered on 10 Dec 2023

It seems that after I waited a bit longer the key go invalidated as Visual Studio asked me for credentials. I'm not sure where is this delay coming from, but I guess it works as intended.

### Response

**Dimo** commented on 11 Dec 2023

Rafał - our credentials caching is relatively short (10 minutes), but there are two places where our packages reside and there may not be а need to make a remote request immediately - the bin folder in the app the NuGet cache folder on the machine

### Response

**Rafał** commented on 11 Dec 2023

Thanks for the information. I was already aware about NuGet package caching so I was getting different packages during testing. It seems the delay was just the credentials caching you mentioned that I wasn't aware about. Everything is working fine.
