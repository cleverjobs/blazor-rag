# IE support

## Question

**Ric** asked on 12 Jul 2019

I know Blazor is suppose to support IE 11 through some behind the scenes magic, what is the plan for Telerik for this? We don't really care too much in our department as we are recommending all internal users to stop using IE and if the app doesn't work then the app doesn't work, use a modern browser. However I am curious on if the plan will be there to support it as I do some things outside of our company that might be trickier to convince people to just not use IE on?

## Answer

**Marin Bratanov** answered on 15 Jul 2019

Hi Rick, The short answers is - we don't plan to support IE11 in Telerik UI for Blazor. We are aiming at modern and supported browsers like Chrome, Firefox, Edge, Safari. Client-side Blazor apps (that is, those relying on WebAssembly), are not not supported under IE, because it does not support WebAssembly. Server-side Blazor apps (that is, constant WebSockets connections to the server), while not requiring WebAssembly, are likely to cause issues too. The problem then arises mostly from the JS Interop code that is needed. IE 11 is not a modern browser and does not implement the current JS standards and so errors will be thrown. We do not intend to add polifylls for it. Regards, Marin Bratanov

### Response

**Rick** answered on 15 Jul 2019

Thanks Marin, I know there are some steps that can be used to have IE fallback so figured I would check. I am not a fan of IE but I do have to keep it in mind as it's not that easy to just tell users you have to switch browsers to use my site, they will simply just not use my site. Intranet obviously this isn't a problem.

### Response

**Marin Bratanov** answered on 16 Jul 2019

Absolutely agree with you, Rick. There are a few other considerations for leaving IE out of the loop: On MSDN, IE is listed as incompatible with client-side Blazor. In the future, the server-side and client-side model will likely become interchangeable through a flag, so that can break compatibility of apps in an unpleasant manner. On MSDN, IE is listed as requiring polyfills even for server-side Blazor. This means it is not fully supported by the framework itself. On top of that, we are trying to build things from the ground up, to follow best practices and to be native. Thus, including or requiring polyfills can lead to complexity, hacks and even conflicts with third-party code, and we don't feel it is a good road to go down to. IE is to be made obsolete in favor of Edge in the foreseeable future, and Edge is a supported browser. Moreover, Edge will be migrated to Chromium. IE has a very low market share, and, as you noted, in an Intranet you can control browsers, and an Intranet is the most common habitat of the IE browser. Regards, Marin Bratanov
