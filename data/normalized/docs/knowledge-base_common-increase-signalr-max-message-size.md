
## Environment

<table>
<tbody>
<tr>
<td>Product</td>
<td>
Editor for Blazor, <br />
FileManager for Blazor, <br />
FileSelect for Blazor, <br />
PdfViewer for Blazor, <br />
Signature for Blazor
</td>
</tr>
</tbody>
</table>

## Description

This article applies only to Blazor **Server** apps. Blazor **WebAssembly** apps do not use SignalR between then browser and the .NET runtime.

How to increase the SignalR `MaximumReceiveMessageSize` in `HubOptions` of a Blazor Server application?

How to increase the maximum amount of characters supported by the **Editor** control?

How to increase the file size limit for **FileManager** download?

How to upload large files with the Telerik Blazor **FileSelect**?

How to display large PDF documents in the Blazor **PDFViewer** component?

Blazor Server apps use a **SignalR WebSocket** to communicate between the client (browser) and server. The SignalR WebSocket has a default maximum message size of **32 KB**. A large Editor `Value`, FileSelect file size, or a PDFViewer `Data` can exceed the maximum SignalR message size, which will close the connection and abort the current application task.

## Solution

Increase the `MaximumReceiveMessageSize` via `HubOptions`. The syntax and code placement can vary, depending on the .NET version or when the application was created. Here are a few possible alternatives.

>caption Use `Configure<HubOptions>` in Program.cs

<div class="skip-repl"></div>

````CS
using Microsoft.AspNetCore.SignalR;

var builder = WebApplication.CreateBuilder(args);

builder.Services.AddServerSideBlazor();

builder.Services.Configure<HubOptions>(options =>
{
    options.MaximumReceiveMessageSize = 1024 * 1024; // 1MB or use null
});
````

>caption Use `AddHubOptions` in Program.cs

<div class="skip-repl"></div>

````CS
builder.Services.AddServerSideBlazor().AddHubOptions(options => {
    options.MaximumReceiveMessageSize = null; // no limit or use a number
});
````

Also see these Microsoft articles:

* [ASP.NET Core SignalR configuration](https://learn.microsoft.com/en-us/aspnet/core/signalr/configuration)
* [SignalR Buffer management](https://learn.microsoft.com/en-us/aspnet/core/signalr/security?view=aspnetcore-7.0#buffer-management).

## Notes

Make sure that `AddServerSideBlazor()` is called **only once**. All configuration settings in `AddHubOptions` and `AddCircuitOptions` must go together with this single statement.

## See Also

* [Connection Closed Error in Blazor Server Apps](slug:common-kb-connection-closed)
* [ASP.NET Core SignalR configuration](https://learn.microsoft.com/en-us/aspnet/core/signalr/configuration)
* [SignalR Buffer management](https://learn.microsoft.com/en-us/aspnet/core/signalr/security?view=aspnetcore-7.0#buffer-management)
