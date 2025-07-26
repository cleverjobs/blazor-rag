# Telerik Blazor Application Template JavaScript Error in Edge

## Question

**TimTim** asked on 14 Nov 2020

I created a new project as follows: Telerik C# Blazor Application, Hosting Model Type: Web Assembly, Target Framework .NET 5.0, CRUD, Form, Chart Before making any changes, I tried to run it. It works in Chrome, but in Edge the page only shows: Loading... In the browser's Developer Tools I see: Syntax error in blazor.webassembly.js I'm using Visual Studio Community 2019 version 16.9.0 Preview 1.0. Any idea how to resolve this? Thanks, Tim

## Answer

**Marin Bratanov** answered on 14 Nov 2020

Hi Tim, Does the standard WebAssembly template work for you under .NET 5? The error seems to stem from the syntax of the framework script, which indicates a problem between Edge and the Blazor Framework, not in our components. At this point my best guess is that one or more of the following is happening: the browser has a cached version of the framework script, so clearing its cache (or just pressing Ctrl+F5) might help there was an issue with the build - for example, .NET 5 is not properly installer, or is still the RC version, or something else went wrong there is something wrong with the Edge instance itself - for example, it's still the very old edge and/or is perhaps trying to emulate IE (that was a feature in previous Edge versions) Another thing that may be going wrong is that the Telerik Blazor VS Extensions you have are not yet updated - it was only a couple of days ago that we released the new version that supports .NET 5 and that' when the extensions were updated in the VS marketplace, so there is a chance they are still the old version on your machine. Last but not least, its important to make sure you're running our 2.19.0 version as that's the first version to support. NET 5 (more on the supported frameworks here ). Regards, Marin Bratanov

### Response

**Tim** answered on 14 Nov 2020

The standard WebAssembly template gives the same error with .NET 5, but not CORE 3.1. Ctrl+F5 did not help. So it seems to be a .NET 5/Edge issue. The version of Edge that I have is old (44.18362.449.0) but I'm not able to update it. I have Telerk UI for Blazor Extensions version 2020.3.1111.1 (not sure if it's the latest. and Telerik Blazor 2.19.0. Thanks for your reply, Tim

### Response

**Marin Bratanov** answered on 16 Nov 2020

Hello Tim, This does sound like a problem coming from this old Edge version, it probably does not support the modern JavaScript APIs that the Blazor framework now uses. At the moment, Edge is at v86 and both Microsoft and we don't support these old versions either, only the current latest which is on based on the Chromium engine ( Telerik docs link, and MSDN link ). What I can suggest until you can update your Edge is that you use Chrome or Firefox for .NET 5 Blazor apps. Regards, Marin Bratanov
