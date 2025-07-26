# On expand node throws exception in Lazy Loading Mode

## Question

**And** asked on 29 Jul 2019

Yesterday I download in database real business data for performance testing. And I found that TreeView works (moving between nodes) very slowly. It's absolutely expectable becase TreeView has more than 10 thousands nodes. OK. I switched TreeView in Lazy Loading Mode. All works fine, but I have some exceptions in console. Exception occured when I click for expand node. I see than OnExpand event sub works normally, but after my OnExpand sub I see exception messages from Telerik TreeView. Please, see my screenshot.

## Answer

**Marin Bratanov** answered on 29 Jul 2019

Hello Andriy, I tested the code from our documentation ( link ) in a sample client blazor app. It works fine for me. Thus, I will need you to post the code that leads to the problem, so I can investigate. You could use my sample as base. You can find it attached below. In the meantime, I need you to make sure that you have the correct JS Interop file referenced - either as a local asset, or that the CDN link you use points to the 1.4.0 version. Regards, Marin Bratanov

### Response

**Andriy** answered on 29 Jul 2019

It's very simple to reproduce. May be I was not absolutelly correct in my previous post. Exception thrown not when you expand node first time, but when you collapse node after first expanding. And then exception throws always when you expand or collapse this node.

### Response

**Andriy** answered on 29 Jul 2019

And one's more thing. In your project I was delete Telerik.UI.for.Blazor.Trial and reinstall it from [https://nuget.telerik.com/nuget](https://nuget.telerik.com/nuget) because I get error during build project ErrorNU1101Unable to find package Telerik.UI.for.Blazor. No packages exist with this id in source(s): [https://dotnet.myget.org/F/aspnetcore-dev/api/v3/index.json,](https://dotnet.myget.org/F/aspnetcore-dev/api/v3/index.json,) [https://dotnet.myget.org/F/blazor-dev/api/v3/index.json,](https://dotnet.myget.org/F/blazor-dev/api/v3/index.json,) Microsoft Visual Studio Offline Packages, nuget.org, telerik, Telerik Local Blazor UI FeedTestBlazorClientCoreHostedApp.ClientD:\ExampleProjects\TestBlazorClientCoreHostedApp\TestBlazorClientCoreHostedApp.Client\TestBlazorClientCoreHostedApp.Client.csproj1

### Response

**Marin Bratanov** answered on 29 Jul 2019

Hi Andriy, I tried collapsing the node and expanding it many times but it still works as expected for me and does not throw errors. Could you record a short video of the steps you take to get the error in my project? On the reference - sorry about that, I forgot the change the licensed reference to a trial one, but you are right in replacing it to get this running. Regards, Marin Bratanov

### Response

**Andriy** answered on 29 Jul 2019

Hi Matin I can not to send my video to your forum directly by 2MB limitation. This link to video from our site [https://andriy.co/download/products/2019-07-29%2018-46-52.mp4](https://andriy.co/download/products/2019-07-29%2018-46-52.mp4)

### Response

**Marin Bratanov** answered on 29 Jul 2019

Hello Andriy, You can attach archives and larger files in a private ticket. That said, the actual error is that our JS object is not found, which indicates that our JS Interop file is not loaded. What is the index file that you are using? Is this my sample project? Can you compare it with this and ensure all assets are loaded: <!DOCTYPE html> <html> <head> <meta charset="utf-8" /> <meta name="viewport" content="width=device-width" /> <title>TestBlazorClientCoreHostedApp</title> <base href="/" /> <link href="css/bootstrap/bootstrap.min.css" rel="stylesheet" /> <link href="css/site.css" rel="stylesheet" /> <link rel="stylesheet" href=" [https://unpkg.com/](https://unpkg.com/) @progress/kendo-theme-material@latest/dist/all.css" /> <!--<script src=" [https://kendo.cdn.telerik.com/blazor/1.4.0/telerik-blazor.min.js](https://kendo.cdn.telerik.com/blazor/1.4.0/telerik-blazor.min.js) " defer></script>--> <script src="_content/telerik.ui.for.blazor/js/telerik-blazor.js" defer></script> </head> <body> <app>Loading...</app> <script src="_framework/blazor.webassembly.js"></script> </body> </html> You can examine the network requests in the Network tab of the browser dev tools to ensure everything is 200 OK. If the file does not load, then the reason is that the machine does not have the .NET Core 3 Preview 7 installed, which fixes the static assets for client-side project types. In such a case, remove the highlighted line and uncomment the one above it. Regards, Marin Bratanov

### Response

**Andriy** answered on 29 Jul 2019

Hi, Marin "What is the index file that you are using? Is this my sample project?" Yes, Marin, this is your project without any changes, excluding replace link in NuGet, about that I wrote earlier. I like clear experiments. First, what I thik - may be problem in routing of my provider? Ок, I change provider to other (mobile). And I have absolutelly same result. I don't understand how works this link that you marked by green. I'm attached screenshot where link looks like [http://localhost:57429/_content/telerik.ui.for.blazor/js/telerik-blazor.js](http://localhost:57429/_content/telerik.ui.for.blazor/js/telerik-blazor.js) Why this link look at my machine I don't understand absolutelly. And also browser can't to find resource by this link. And I checked my .net core version, this is preview 7 I'm very hope for your help. Thank you.

### Response

**Andriy** answered on 29 Jul 2019

Marin, I found some thing. This link marked as green direct to nowere. I commented this link and restored link in previous row and all works fine. Tell me please, what correct link to telerik-blazor.js?

### Response

**Andriy** answered on 29 Jul 2019

Hi, Marin I found solution This index.html tag need to use for licenced version <script src="_content/telerik.ui.for.blazor/js/telerik-blazor.js" defer></script> But I have trial version and I need to use another link <script src="_content/telerik.ui.for.blazor.trial/js/telerik-blazor.js" defer></script> From here [https://docs.telerik.com/blazor-ui/getting-started/client-blazor](https://docs.telerik.com/blazor-ui/getting-started/client-blazor) Thank you very much
