# Could not find 'TelerikBlazor' in 'window'

## Question

**Cra** asked on 14 Oct 2019

Tried this both from creating a new Telerik Blazor project and adding Telerik UI for Blazor to an existing project. Server-Side Blazor projects. Both produce the same results. Version 2.1.1 when hitting the page with the Telerik Blazor Grid, the Output window fills with errors the first of which is: Microsoft.AspNetCore.Components.Server.Circuits.RemoteRenderer: Warning: Unhandled exception rendering component: Could not find 'TelerikBlazor' in 'window'. Error: Could not find 'TelerikBlazor' in 'window'. at Anonymous function ( [https://localhost:44365/_framework/blazor.server.js:8:28059)](https://localhost:44365/_framework/blazor.server.js:8:28059)) at Array.prototype.forEach (native code) at p ( [https://localhost:44365/_framework/blazor.server.js:8:28010)](https://localhost:44365/_framework/blazor.server.js:8:28010)) at Anonymous function ( [https://localhost:44365/_framework/blazor.server.js:8:28731)](https://localhost:44365/_framework/blazor.server.js:8:28731)) at Promise (native code) at e.jsCallDispatcher.beginInvokeJSFromDotNet ( [https://localhost:44365/_framework/blazor.server.js:8:28701)](https://localhost:44365/_framework/blazor.server.js:8:28701)) at Anonymous function ( [https://localhost:44365/_framework/blazor.server.js:1:19139)](https://localhost:44365/_framework/blazor.server.js:1:19139)) at Array.prototype.forEach (native code) at e.prototype.invokeClientMethod ( [https://localhost:44365/_framework/blazor.server.js:1:19117)](https://localhost:44365/_framework/blazor.server.js:1:19117)) at e.prototype.processIncomingData ( [https://localhost:44365/_framework/blazor.server.js:1:17160)](https://localhost:44365/_framework/blazor.server.js:1:17160))

## Answer

**Alan** answered on 01 Jul 2020

If this helps anyone, i did an upgrade to the latest Telerik Blazor. I had to do 2 things: 1) fix the reference in the _hosts.cshtml in the Pages, 2) Clean and rebuild. This is an app I haven't touched in months but it must have had the existing files cached in the obj/bin. Hope it helps someone.

### Response

**Jay** commented on 14 Jan 2022

I had this precise issue when updating telerik blazor from trial to full version. Thanks for the updated comment.

### Response

**Marin Bratanov** answered on 14 Oct 2019

Hello Craig, Please try the information from the following article that treats such exceptions: [https://docs.telerik.com/blazor-ui/troubleshooting/js-errors.](https://docs.telerik.com/blazor-ui/troubleshooting/js-errors.) If this does not help, please let me know what you tried and what the results were (for example, whether all network requests return successfully). Regards, Marin Bratanov

### Response

**Eduardo** commented on 15 Apr 2020

Not related to the grid component specifically but to the exception : "Could not find 'TelerikBlazor' in 'window'". I found that his happens when you refresh a page with a route like this: @page "/page/subpage". The first time the "subpage" is loaded, all blazor components render properly. The exception is thrown when you refresh the "subpage"

### Response

**Marin Bratanov** commented on 16 Apr 2020

Hi Eduardo, Could you try removing the "defer" attribute from the Telerik script tag to see if this helps? This behavior sounds like a timing problem in the browser, and the defer attribute may be causing it. Regards, Marin Bratanov

### Response

**Eduardo** commented on 17 Apr 2020

Hi Martin, I tried removing the defer attribute from the script tag, but I'm still getting the same error when reloading a page with a route like @page "/telerik/test". Something I should mention is that I'm developing a blazor app using a server hosting model, so I placed the telerik script tag in the _Host.html in the head section. Another interesting fact, is that if I navigate to the page by typing the url directly in the web browser, I get the same exception right off the bat. If I navigate through a NavLink with href="telerik/test", it loads correctly the first time, and the error is thrown after refreshing the page.

### Response

**Marin Bratanov** commented on 18 Apr 2020

Hi Eduardo, This indicates that the script is loaded very late, or not at all. Could you check the Network tab of your browser to see what the timeline of the requests is and whether this request is always successful? Does it load fast enough? Does moving it earlier in the DOM help? If not, could you open a ticket and send me a simple runnable project that reproduces this issue so I can have a look? Regards, Marin Bratanov

### Response

**DR** commented on 11 May 2020

I get the same error with the latest version of the blazor-dashboard demo: [https://github.com/telerik/blazor-dashboard](https://github.com/telerik/blazor-dashboard)

### Response

**Marin Bratanov** commented on 12 May 2020

Hello, Do you get it locally or from our site? If it is only on our live app, latency is the likely issue, because this is a server-side Blazor app which is not really suitable for an Internet scenario, but for Intranet. If you get problems when adapting it to your local use case and your own app, just remove the defer attribute from the script - see the Defer Attribute section near the end of this article: [https://docs.telerik.com/blazor-ui/troubleshooting/js-errors](https://docs.telerik.com/blazor-ui/troubleshooting/js-errors) Regards, Marin Bratanov
