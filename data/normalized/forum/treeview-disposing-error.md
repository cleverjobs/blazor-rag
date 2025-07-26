# TreeView Disposing/Error

## Question

**Ant** asked on 16 Feb 2024

In my blazor app I'm seeing the TelerikTreeView is erroring out during garbage collection or disposing when I switching between pages too quickly in my. Is there something I can do to suppress this error or add some nullcheck so this doesnt appear in my logs? Here is the error I'm getting: Microsoft.JSInterop.JSException: Cannot read properties of null (reading 'addEventListener') TypeError: Cannot read properties of null (reading 'addEventListener') at c.bindEvents ([https://0.0.0.0/_content/Telerik.UI.for.Blazor/js/telerik-blazor.js:50:1282242)](https://0.0.0.0/_content/Telerik.UI.for.Blazor/js/telerik-blazor.js:50:1282242)) at new c ([https://0.0.0.0/_content/Telerik.UI.for.Blazor/js/telerik-blazor.js:50:1282116)](https://0.0.0.0/_content/Telerik.UI.for.Blazor/js/telerik-blazor.js:50:1282116)) at e.initComponent ([https://0.0.0.0/_content/Telerik.UI.for.Blazor/js/telerik-blazor.js:50:1085487)](https://0.0.0.0/_content/Telerik.UI.for.Blazor/js/telerik-blazor.js:50:1085487)) at e.initTreeView ([https://0.0.0.0/_content/Telerik.UI.for.Blazor/js/telerik-blazor.js:50:1279920)](https://0.0.0.0/_content/Telerik.UI.for.Blazor/js/telerik-blazor.js:50:1279920)) at [https://0.0.0.0/_framework/blazor.webview.js:1:3337](https://0.0.0.0/_framework/blazor.webview.js:1:3337) at new Promise ( <anonymous> ) at beginInvokeJSFromDotNet ([https://0.0.0.0/_framework/blazor.webview.js:1:3311)](https://0.0.0.0/_framework/blazor.webview.js:1:3311)) at [https://0.0.0.0/_framework/blazor.webview.js:1:42795](https://0.0.0.0/_framework/blazor.webview.js:1:42795) at EventTarget. <anonymous> ( <anonymous>:7:62) at EmbeddedBrowserWebView. <anonymous> ( <anonymous>:1:40673)
at Microsoft.JSInterop.JSRuntime.InvokeAsync[TValue](Int64 targetInstanceId, String identifier, Object[] args)
at Microsoft.JSInterop.JSRuntimeExtensions.InvokeVoidAsync(IJSRuntime jsRuntime, String identifier, Object[] args)
at Telerik.Blazor.Components.TelerikTreeView.InitTreeView()
at Telerik.Blazor.Components.TelerikTreeView.OnAfterRenderAsync(Boolean firstRender)
at Microsoft.AspNetCore.Components.RenderTree.Renderer.GetErrorHandledTask(Task taskToHandle, ComponentState owningComponentState)
Microsoft.JSInterop.JSException: Cannot read properties of null (reading 'addEventListener') TypeError: Cannot read properties of null (reading 'addEventListener') at c.bindEvents ([https://0.0.0.0/_content/Telerik.UI.for.Blazor/js/telerik-blazor.js:50:1282242)](https://0.0.0.0/_content/Telerik.UI.for.Blazor/js/telerik-blazor.js:50:1282242)) at new c ([https://0.0.0.0/_content/Telerik.UI.for.Blazor/js/telerik-blazor.js:50:1282116)](https://0.0.0.0/_content/Telerik.UI.for.Blazor/js/telerik-blazor.js:50:1282116)) at e.initComponent ([https://0.0.0.0/_content/Telerik.UI.for.Blazor/js/telerik-blazor.js:50:1085487)](https://0.0.0.0/_content/Telerik.UI.for.Blazor/js/telerik-blazor.js:50:1085487)) at e.initTreeView ([https://0.0.0.0/_content/Telerik.UI.for.Blazor/js/telerik-blazor.js:50:1279920)](https://0.0.0.0/_content/Telerik.UI.for.Blazor/js/telerik-blazor.js:50:1279920)) at [https://0.0.0.0/_framework/blazor.webview.js:1:3337](https://0.0.0.0/_framework/blazor.webview.js:1:3337) at new Promise ( <anonymous> ) at beginInvokeJSFromDotNet ([https://0.0.0.0/_framework/blazor.webview.js:1:3311)](https://0.0.0.0/_framework/blazor.webview.js:1:3311)) at [https://0.0.0.0/_framework/blazor.webview.js:1:42795](https://0.0.0.0/_framework/blazor.webview.js:1:42795) at EventTarget. <anonymous> ( <anonymous>:7:62) at EmbeddedBrowserWebView. <anonymous> ( <anonymous>:1:40673)
at Microsoft.JSInterop.JSRuntime.InvokeAsync[TValue](Int64 targetInstanceId, String identifier, Object[] args)
at Microsoft.JSInterop.JSRuntimeExtensions.InvokeVoidAsync(IJSRuntime jsRuntime, String identifier, Object[] args)
at Telerik.Blazor.Components.TelerikTreeView.InitTreeView()
at Telerik.Blazor.Components.TelerikTreeView.OnAfterRenderAsync(Boolean firstRender)
at Microsoft.AspNetCore.Components.RenderTree.Renderer.GetErrorHandledTask(Task taskToHandle, ComponentState owningComponentState)

### Response

**Hristian Stefanov** commented on 21 Feb 2024

Hi Anthony, We have a knowledge base article regarding the error you are observing: Cannot read properties of null (reading addEventListener). Could you take a look at it if you haven't done it yet to see whether the information from there helps? If the issue persists, please send me a small runnable app for inspection. This will allow me to investigate further and provide possible fixes. I look forward to hearing an update from you. Kind Regards, Hristian

## Answer

**Alexey** answered on 15 Nov 2024

I have the same issue. I tried to fix it using envelope of my application and components in: <LogErrorBoundary> my problem Blazor Telerik components here </LogErrorBoundary> where LogErrorBoundary is: @inherits ErrorBoundary
@inject ILogger <LogErrorBoundary> Logger

@ChildContent
@if (ErrorContent is not null && CurrentException is null)
{
@ErrorContent(CurrentException)
}

@code {
protected override Task OnErrorAsync(Exception ex)
{
Logger.LogError(ex, "Unhandled exception in the application");
return Task.CompletedTask;
}
} and any JS calls from Blazor like: try
{
if (!string.IsNullOrWhiteSpace(MyJSMethod))
{
await JS.InvokeAsync <string> (MyJSMethod, new MyDto { MyData="Data" });
}
}
catch (JSException jsEx)
{
Logger.LogError(ex, "Unhandled js exception");
}
catch (Exception e)
{
Logger.LogError(e, "Unhandled exception");
} But i t does not help me and i still get errors like: WebApp.Shared.LogErrorBoundary[0] Unhandled exception in the application Microsoft.JSInterop.JSException: Cannot read properties of null (reading 'addEventListener') TypeError: Cannot read properties of null (reading 'addEventListener') at r.bindEvents ([http://127.0.0.1:8000/_content/Telerik.UI.for.Blazor/js/telerik-blazor.js:50:1303463)](http://127.0.0.1:8000/_content/Telerik.UI.for.Blazor/js/telerik-blazor.js:50:1303463)) at new r ([http://127.0.0.1:8000/_content/Telerik.UI.for.Blazor/js/telerik-blazor.js:50:1303389)](http://127.0.0.1:8000/_content/Telerik.UI.for.Blazor/js/telerik-blazor.js:50:1303389)) at e.initComponent ([http://127.0.0.1:8000/_content/Telerik.UI.for.Blazor/js/telerik-blazor.js:50:1112278)](http://127.0.0.1:8000/_content/Telerik.UI.for.Blazor/js/telerik-blazor.js:50:1112278)) at e.initTextBox ([http://127.0.0.1:8000/_content/Telerik.UI.for.Blazor/js/telerik-blazor.js:50:1303097)](http://127.0.0.1:8000/_content/Telerik.UI.for.Blazor/js/telerik-blazor.js:50:1303097)) at [http://127.0.0.1:8000/_framework/blazor.server.js:1:3244](http://127.0.0.1:8000/_framework/blazor.server.js:1:3244) at new Promise (<anonymous>) at y.beginInvokeJSFromDotNet ([http://127.0.0.1:8000/_framework/blazor.server.js:1:3201)](http://127.0.0.1:8000/_framework/blazor.server.js:1:3201)) at Xt._invokeClientMethod ([http://127.0.0.1:8000/_framework/blazor.server.js:1:61001)](http://127.0.0.1:8000/_framework/blazor.server.js:1:61001)) at Xt._processIncomingData ([http://127.0.0.1:8000/_framework/blazor.server.js:1:58476)](http://127.0.0.1:8000/_framework/blazor.server.js:1:58476)) at Xt.connection.onreceive ([http://127.0.0.1:8000/_framework/blazor.server.js:1:52117)](http://127.0.0.1:8000/_framework/blazor.server.js:1:52117)) at s.onmessage ([http://127.0.0.1:8000/_framework/blazor.server.js:1:80262)](http://127.0.0.1:8000/_framework/blazor.server.js:1:80262)) at Microsoft.JSInterop.JSRuntime.InvokeAsync[TValue](Int64 targetInstanceId, String identifier, Object[] args) at Telerik.Blazor.Components.Common.TextBoxBase.InitJsComponentAsync() at Telerik.Blazor.Components.Common.TextBoxBase.OnAfterRenderInternalAsync(Boolean firstRender) at Telerik.Blazor.Components.Common.TextBoxBase.OnAfterRenderAsync(Boolean firstRender) at Microsoft.AspNetCore.Components.RenderTree.Renderer.GetErrorHandledTask(Task taskToHandle, ComponentState owningComponentState)

### Response

**Hristian Stefanov** commented on 15 Nov 2024

Hi Alexey, Have you tried one specific solution - it is an approach that we use in our own demo website, where we haven't experienced such an error thus far. Here's a link for it with more details from the Microsoft documentation: Initialize Blazor when the document is ready. In summary, try the following steps: Open the file where you are loading the scripts, including our Telerik JavaScript. Depending on the project type, this file can be _Host.cshtml / _Layout.cshtml / App.razor. Insert the following line to ensure that the JavaScript is loaded on time: <script src="_framework/blazor.web.js" autostart="false"> </script> <script> document.addEventListener( "DOMContentLoaded", function ( ) {
Blazor.start();
}); </script> Let me know whether the above approach helps. If, despite following the steps mentioned above, the error persists, I remain at your disposal to assist further. Kind Regards, Hristian

### Response

**Alexey** commented on 19 Nov 2024

Your solution is not fit for my application. When we load "Blazor + Telerik" we have enough checks for detecting alive or died "Blazor + Telerik". We have issue with close aplication "Blazor + Telerik" where we have that Issue. We use "Blazor + Telerik" solution as part of other solution through the Web Components, like: var builder=WebApplication.CreateBuilder(args);
// some code here ...............

builder.Services.AddServerSideBlazor(
options=>
{
options.RootComponents.RegisterCustomElement <BlazorTelerikUsersErrorBoundary> ("blazor-telerik-users");
options.RootComponents.RegisterCustomElement <BlazorTelerikEditUserFormErrorBoundary> ("blazor-telerik-edit-user-form");
options.RootComponents.RegisterCustomElement <BlazorTelerikViewUserErrorBoundary> ("blazor-telerik-view-user");
options.DetailedErrors=true;
}); And then I use it as part of other application in Dialog which built using React. I use "Blazor + Telerik" as component like: <blazor-telerik-edit-user-form key={key} on-close="onClose" on-blazor-telerik-loaded="onBlazorTelerikLoaded" /> And if users work with application slowly we will not have any issue. But when users close application (Dialog where we use "Blazor + Telerik" as component ) we have issue which i posted above: WebApp.Shared.LogErrorBoundary[0]
Unhandled exception in the application
Microsoft.JSInterop.JSException: Cannot read properties of null (reading 'addEventListener')
TypeError: Cannot read properties of null (reading 'addEventListener')
at r.bindEvents ([http://127.0.0.1:8000/_content/Telerik.UI.for.Blazor/js/telerik-blazor.js:50:1303463)](http://127.0.0.1:8000/_content/Telerik.UI.for.Blazor/js/telerik-blazor.js:50:1303463))
at new r ([http://127.0.0.1:8000/_content/Telerik.UI.for.Blazor/js/telerik-blazor.js:50:1303389)](http://127.0.0.1:8000/_content/Telerik.UI.for.Blazor/js/telerik-blazor.js:50:1303389))
at e.initComponent ([http://127.0.0.1:8000/_content/Telerik.UI.for.Blazor/js/telerik-blazor.js:50:1112278)](http://127.0.0.1:8000/_content/Telerik.UI.for.Blazor/js/telerik-blazor.js:50:1112278))
at e.initTextBox ([http://127.0.0.1:8000/_content/Telerik.UI.for.Blazor/js/telerik-blazor.js:50:1303097)](http://127.0.0.1:8000/_content/Telerik.UI.for.Blazor/js/telerik-blazor.js:50:1303097))
at [http://127.0.0.1:8000/_framework/blazor.server.js:1:3244](http://127.0.0.1:8000/_framework/blazor.server.js:1:3244)
at new Promise ( <anonymous> )
at y.beginInvokeJSFromDotNet ([http://127.0.0.1:8000/_framework/blazor.server.js:1:3201)](http://127.0.0.1:8000/_framework/blazor.server.js:1:3201))
at Xt._invokeClientMethod ([http://127.0.0.1:8000/_framework/blazor.server.js:1:61001)](http://127.0.0.1:8000/_framework/blazor.server.js:1:61001))
at Xt._processIncomingData ([http://127.0.0.1:8000/_framework/blazor.server.js:1:58476)](http://127.0.0.1:8000/_framework/blazor.server.js:1:58476))
at Xt.connection.onreceive ([http://127.0.0.1:8000/_framework/blazor.server.js:1:52117)](http://127.0.0.1:8000/_framework/blazor.server.js:1:52117))
at s.onmessage ([http://127.0.0.1:8000/_framework/blazor.server.js:1:80262)](http://127.0.0.1:8000/_framework/blazor.server.js:1:80262))
at Microsoft.JSInterop.JSRuntime.InvokeAsync[TValue](Int64 targetInstanceId, String identifier, Object[] args)
at Telerik.Blazor.Components.Common.TextBoxBase.InitJsComponentAsync()
at Telerik.Blazor.Components.Common.TextBoxBase.OnAfterRenderInternalAsync(Boolean firstRender)
at Telerik.Blazor.Components.Common.TextBoxBase.OnAfterRenderAsync(Boolean firstRender)
at Microsoft.AspNetCore.Components.RenderTree.Renderer.GetErrorHandledTask(Task taskToHandle, ComponentState owningComponentState) After this error we no ability to alive your application "Blazor + Telerik". Each components die.

### Response

**Hristian Stefanov** commented on 21 Nov 2024

Hi Alexey, Thank you for keeping me updated on your situation. Just to confirm, have you had a chance to try the solution mentioned in the knowledge base article I shared in my initial response? If you’ve already tested it and the issue persists, could you create a small, runnable, and isolated example (not your entire application) and share it with me? This will allow me to investigate the matter further. Additionally, what is the Telerik version you are using? I look forward to your reply. Kind Regards, Hristian

### Response

**Alexey** commented on 16 Jul 2025

We resolve this issue. We have a lot of calls JS from our blazor application. we replace it: await JS. InvokeAsync <string>( "scrollToError", invalidFields); to it await JS. InvokeVoidAsync ( "scrollToError", invalidFields); and this approach help us.
