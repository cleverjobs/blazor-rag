# 1.4.0 Can't open dropdown part

## Question

**And** asked on 27 Jul 2019

In new version I have this (see picture)

## Answer

**Marin Bratanov** answered on 29 Jul 2019

Hello Andriy, Please post a relevant code snippet that shows how to reproduce this. Usually a few lines of markup + a few simple variables for binding would suffice to showcase a bug in our components. Doing that can help us get to the bottom of issues you are facing in a much more efficient manner. In the meantime, please make sure that: You have the TelerikRootComponent in your main layout. That the JS Interop file link has been updated to point to 1.4.0 (the CDN URL must be updated with each Telerik update). Also, since you are using a client-side app, make sure that the CDN is used as static assets may not work with it yet. All projects have been updated to Preview 7. I'd also suggest you compare it with our demos which seem to work fine for me. Regards, Marin Bratanov
