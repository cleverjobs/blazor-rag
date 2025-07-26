# Problem with TelerikDateInput using version 1.2.0

## Question

**Ken** asked on 21 Jun 2019

I am getting the following exception when I load a page with the DateInput widget on it: Microsoft.AspNetCore.Components.Server.ComponentHub: Warning: Unhandled Server-Side exception Microsoft.JSInterop.JSException: this.element.addEventListener is not a function TypeError: this.element.addEventListener is not a function at t.value ([https://kendo.cdn.telerik.com/blazor/1.0.0/telerik-blazor.min.js:1:3367)](https://kendo.cdn.telerik.com/blazor/1.0.0/telerik-blazor.min.js:1:3367)) at new t ([https://kendo.cdn.telerik.com/blazor/1.0.0/telerik-blazor.min.js:1:2735)](https://kendo.cdn.telerik.com/blazor/1.0.0/telerik-blazor.min.js:1:2735)) at initialize ([https://kendo.cdn.telerik.com/blazor/1.0.0/telerik-blazor.min.js:1:2169)](https://kendo.cdn.telerik.com/blazor/1.0.0/telerik-blazor.min.js:1:2169)) at [https://localhost:44329/_framework/blazor.server.js:8:21434](https://localhost:44329/_framework/blazor.server.js:8:21434) at new Promise (<anonymous>) at e.beginInvokeJSFromDotNet ([https://localhost:44329/_framework/blazor.server.js:8:21403)](https://localhost:44329/_framework/blazor.server.js:8:21403)) at [https://localhost:44329/_framework/blazor.server.js:1:16653](https://localhost:44329/_framework/blazor.server.js:1:16653) at Array.forEach (<anonymous>) at e.invokeClientMethod ([https://localhost:44329/_framework/blazor.server.js:1:16624)](https://localhost:44329/_framework/blazor.server.js:1:16624)) at e.processIncomingData ([https://localhost:44329/_framework/blazor.server.js:1:14624)](https://localhost:44329/_framework/blazor.server.js:1:14624)) at Telerik.Blazor.Components.DateInput.TelerikDateInputBase`1.OnAfterRender() at System.Threading.Tasks.Task.<>c.<ThrowAsync>b__139_0(Object state) at Microsoft.AspNetCore.Components.Rendering.RendererSynchronizationContext.ExecuteSynchronously(TaskCompletionSource`1 completion, SendOrPostCallback d, Object state) at Microsoft.AspNetCore.Components.Rendering.RendererSynchronizationContext.<>c.<.cctor>b__23_0(Object state) at System.Threading.ExecutionContext.RunInternal(ExecutionContext executionContext, ContextCallback callback, Object state) --- End of stack trace from previous location where exception was thrown --- at System.Threading.ExecutionContext.RunInternal(ExecutionContext executionContext, ContextCallback callback, Object state) at System.Threading.ExecutionContext.Run(ExecutionContext executionContext, ContextCallback callback, Object state) at Microsoft.AspNetCore.Components.Rendering.RendererSynchronizationContext.ExecuteBackground(WorkItem item) Here is a simple example page taken and simplified from the demo source code that reproduces the problem: @page "/Tests" @using Telerik.Blazor.Components.DateInput <strong> Hire Date</strong> <TelerikDateInput @bind-Value="HireDate" Format="MMMM/dd/yyyy"></TelerikDateInput> @code { DateTime HireDate=new DateTime(2018, 5, 6); } I tried it with an ampersand in front of HireDate as it was in the demo code sample like so and got the same results: <TelerikDateInput @bind-Value="@HireDate" Format="MMMM/dd/yyyy"></TelerikDateInput> Thanks, Kenny

## Answer

**Kenny** answered on 21 Jun 2019

I forgot to mention, this "kills" the events on the page. No clicks or other JavaScript events work after this exception.

### Response

**Rick** answered on 22 Jun 2019

Did you remember to update the Telerik javascript reference to the latest version when you upgraded? In your host.cshtml file?

### Response

**Kenny** answered on 22 Jun 2019

Nope, I forgot that part. That was it! Thanks Rick.

### Response

**Marin Bratanov** answered on 24 Jun 2019

Hi guys, It's good to see you have resolved this, and thank you for helping out, Rick. I'd like to chime in with two bits of trivia that may be useful (for someone else too): If you are using a Server-side Blazor app (which you seem to be), you can use static assets as shown in the following article, so you don't have to update the CDN: [https://docs.telerik.com/blazor-ui/getting-started/what-you-need#static-assets.](https://docs.telerik.com/blazor-ui/getting-started/what-you-need#static-assets.) Hopefully, in the next framework releases this will start working for client-side apps too. You can easily review which version your app references in the stack trace, so you can make sure it is kept up to date: Microsoft.JSInterop.JSException: this.element.addEventListener is not a function TypeError: this.element.addEventListener is not a function at t.value ( [https://kendo.cdn.telerik.com/blazor](https://kendo.cdn.telerik.com/blazor) /1.0.0 /telerik-blazor.min.js:1:3367) at new t ( [https://kendo.cdn.telerik.com/blazor](https://kendo.cdn.telerik.com/blazor) /1.0.0/ telerik-blazor.min.js:1:2735) at initialize ( [https://kendo.cdn.telerik.com/blazor](https://kendo.cdn.telerik.com/blazor) /1.0.0 /telerik-blazor.min.js:1:2169) at [https://localhost:44329/_framework/blazor.server.js:8:21434](https://localhost:44329/_framework/blazor.server.js:8:21434) at new Promise (<anonymous>) Regards, Marin Bratanov
