# Google Ad Block

## Question

**Ric** asked on 01 Jul 2019

We have a few people doing testing and have discovered that when using Chrome and using various ad blocking extensions that it causes the windows not to open. Have you experienced this and have a work around?

## Answer

**Rick** answered on 01 Jul 2019

Actually when the blocking is happening, no button works on the page. Only way to get it to work is removing the ad blocker from chrome, not even disabling or adding a whitelist works. This does not seem to be all ad blockers, some work fine. One of the ones that do not work is [https://chrome.google.com/webstore/detail/adguard-adblocker/bgnkhhnnamicmpeenaelnjfhikgbkllg?hl=en](https://chrome.google.com/webstore/detail/adguard-adblocker/bgnkhhnnamicmpeenaelnjfhikgbkllg?hl=en) Is there anything I need to know or should be doing when it comes to dealing with the blockers?

### Response

**Rick** answered on 01 Jul 2019

Upon further review, this is only when windows authentication is enabled.

### Response

**Rick** answered on 01 Jul 2019

Ok, further research is showing this works fine IF running fiddler at the same time. What is fiddler doing that is allowing it to go through? It appears that it is blocking web sockets while using windows credentials but not when fiddler is up.

### Response

**Marin Bratanov** answered on 02 Jul 2019

Hello Rick, My best guess is that there is something off in the networking setup in your office, also considering your previous thread. I suspect that something breaks network requests in your case, which breaks server-side blazor apps pretty insidiously, because web sockets are hard to monitor. Fiddlers adds a proxy to your connection so it can capture https traffic, and perhaps routing the signalr requests through that lets them pass instead of get blocked by the original network config that is in effect. Regards, Marin Bratanov

### Response

**Rick** answered on 02 Jul 2019

It seems like switching to basic authentication instead of windows authentication in IIS makes it work. Since this is only over our company intranet that will be fine as a fall back. This is also only certain ad blockers, not all ad blockers do this. We will advice people to just use a different ad blocker and if it seems to be a big issue company wide we will switch the app to basic authentication and just have it prompt for credentials instead of auto login.

### Response

**Marin Bratanov** answered on 03 Jul 2019

Hi Rick, It's good to hear you have a viable path forward. Could you share some of the extensions that cause a problem in your case here, so other people can see that list in case they stumble on a similar problem? Thanks, Marin Bratanov
