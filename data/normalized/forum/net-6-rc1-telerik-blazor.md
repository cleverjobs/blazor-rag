# .NET 6 RC1 Telerik Blazor

## Question

**Dal** asked on 14 Sep 2021

I know the focus is .NET 5 right now and rightfully so. Currently the latest version Telerik DOES work with .NET 6 but there are a few issues like exceptions being throw after navigating away from a page with Telerik controls... usually resulting in a ton of exceptions being thrown. Microsoft.JSInterop.JSDisconnectedException: JavaScript interop calls cannot be issued at this time. This is because the circuit has disconnected and is being disposed. I'm wondering if we will see a preview release or beta of Telerik available to possibly test with before the final release of .NET 6 in November? I remember last year .NET 5 support was added on the last preview build they released.

### Response

**Peter** commented on 15 Sep 2021

They just released an update

## Answer

**Dimo** answered on 17 Sep 2021

Hi Dale, We keep an eye on all .NET 6 preview releases and check our source code for compatibility. Our usual approach is to release a compatible UI for Blazor version as soon as possible after the official .NET release. It takes a few days to do this. Regards, Dimo Progress Telerik

### Response

**Adam** commented on 03 Oct 2021

I have just updated our .Net 6 RC1 app to use the latest Telerik 2.27.0 and am still seeing lots of these errors. Is that to be expected? Microsoft.JSInterop.JSDisconnectedException: JavaScript interop calls cannot be issued at this time. This is because the circuit has disconnected and is being disposed. at Microsoft.AspNetCore.Components.Server.Circuits.RemoteJSRuntime.BeginInvokeJS(Int64 asyncHandle, String identifier, String argsJson, JSCallResultType resultType, Int64 targetInstanceId) at Microsoft.JSInterop.JSRuntime.InvokeAsync[TValue](Int64 targetInstanceId, String identifier, CancellationToken cancellationToken, Object[] args) at Microsoft.JSInterop.JSRuntime.InvokeAsync[TValue](Int64 targetInstanceId, String identifier, Object[] args) at Microsoft.JSInterop.JSRuntimeExtensions.InvokeVoidAsync(IJSRuntime jsRuntime, String identifier, Object[] args) at Telerik.Blazor.Components.TelerikCheckBox`1.DestroyJsComponentAsync() at Telerik.Blazor.Components.TelerikCheckBox`1.Dispose() at Microsoft.AspNetCore.Components.Rendering.RendererSynchronizationContext.ExecuteSynchronously(TaskCompletionSource`1 completion, SendOrPostCallback d, Object state) at System.Threading.ExecutionContext.RunInternal(ExecutionContext executionContext, ContextCallback callback, Object state)

### Response

**Dimo** commented on 06 Oct 2021

@Adam - are you testing a scenario that has worked with .NET 5? If yes, can you provide a runnable test page, so that we check it?

### Response

**Adam** commented on 11 Oct 2021

@Dimo - it doesn't stop the app from working and just generates the exceptions when you navigate away from a page so might be some lifecycle issue. I'll wait for the next .net 6 RC and see if we still see the issue and if we are we will work out if we can provide a test page.

### Response

**Dimo** commented on 11 Oct 2021

OK, let me know how it goes when you have more insights.

### Response

**Dan** commented on 01 Dec 2021

I am experiencing this problem currently with .NET 6 and Telerik.UI.for.Blazor v2.29.0. Here is the exception I'm getting: Microsoft.AspNetCore.Components.Server.Circuits.CircuitHost[111]
Unhandled exception in circuit 'Af3awsoTLmv2bbcjQftZY9cygTnEdfbKl8nQB2VpCCY'.
Microsoft.JSInterop.JSDisconnectedException: JavaScript interop calls cannot be issued at this time. This is because the circuit has disconnected and is being disposed.
at Microsoft.AspNetCore.Components.Server.Circuits.RemoteJSRuntime.BeginInvokeJS(Int64 asyncHandle, String identifier, String argsJson, JSCallResultType resultType, Int64 targetInstanceId)
at Microsoft.JSInterop.JSRuntime.InvokeAsync[TValue](Int64 targetInstanceId, String identifier, CancellationToken cancellationToken, Object[] args)
at Microsoft.JSInterop.JSRuntime.InvokeAsync[TValue](Int64 targetInstanceId, String identifier, Object[] args)
at Microsoft.JSInterop.JSRuntimeExtensions.InvokeVoidAsync(IJSRuntime jsRuntime, String identifier, Object[] args)
at Telerik.Blazor.Components.TelerikMultiSelect`2.Dispose()
at System.Threading.Tasks.Task. <> c. <ThrowAsync> b__127_0(Object state)
at Microsoft.AspNetCore.Components.Rendering.RendererSynchronizationContext.ExecuteSynchronously(TaskCompletionSource`1 completion, SendOrPostCallback d, Object state)
at Microsoft.AspNetCore.Components.Rendering.RendererSynchronizationContext. <> c.<.cctor>b__23_0(Object state)
at System.Threading.ExecutionContext.RunInternal(ExecutionContext executionContext, ContextCallback callback, Object state)
--- End of stack trace from previous location ---
at Microsoft.AspNetCore.Components.Rendering.RendererSynchronizationContext.ExecuteBackground(WorkItem item)

### Response

**Dimo** commented on 02 Dec 2021

Hi Dan, We fixed a similar issue specifically in UI for Blazor 2.29. If you are certain that you are using this version, please send us a runnable project for inspection, as we are no longer able to reproduce the problem.

### Response

**Dan** commented on 02 Dec 2021

Hi Dimo, Thanks for a quick response. Attached is a simple project to reproduce the issue. I created a default .NET 6 Blazor Server project and made the following changes: Added a web.config file to mimic our setup closer (we have multiple apps running at the same root URL, but with different paths - micro-frontend architecture) Updated launchSettings.json to run in IIS Added a TelerikRootComponent to the MainLayout.razor Added a telerik-blazor.js script tag in _Layout.cshtml In _Host.cshtml, changed the render-mode to "Server" Added a TelerikMultiSelect to the Index.razor page To reproduce the issue, just run the app. It happens as soon as the page is loaded. Thanks. -Dan UPDATE: Actually, in the case of the attached solution it's my mistake - the "defer" attribute is inside the quotes instead of outside, messing with the telerik-blazor.js path. I will continue to work on a repro solution and post it here once I have it. Thanks, -Dan

### Response

**Dan** commented on 02 Dec 2021

Ok, sorry for the back-and-forth. Attached is a demo solution that reproduces the problem. There are 2 applications - HomeApp (served at [http://localhost:9747](http://localhost:9747) ) and MultiSelectApp (served at [http://localhost:9747/multi](http://localhost:9747/multi) ). The MultiSelectApp is set up as described in my previous comment. For the HomeApp: I created a default .NET 5 Blazor Server project Added a web.config file Updated launchSettings.json to run in IIS Added a TelerikRootComponent to the MainLayout.razor Added a telerik-blazor.js script tag in _Host.cshtml In _Host.cshtml, changed the render-mode to "Server" To reproduce the problem: Set both projects as Start Up projects Run the app(s) - you'll end up in the HomeApp first Click the "Go to Multi" link which takes you to the MultiSelectApp - it contains an empty TelerikMultiSelect on the target page Click "Go Home" Observe the exception in the output of the MultiSelectApp - in my real-world case this exception crashes the circuit. I think it started happening once I added the TelerikRootComponent to the HomeApp. If you need more information, please let me know. Thanks. -Dan

### Response

**Dan** commented on 02 Dec 2021

P.S. The example I provided is missing builder.Services.AddTelerikBlazor() in both apps, but adding it did not change the outcome.

### Response

**Dimo** commented on 06 Dec 2021

Hi Dan, Thanks the provided project and follow-ups. It turns out I provided misleading information to you. We fixed the "JavaScript interop calls cannot be issued at this time" error in 2.29, but not for all components. The MultiSelect component is one of those that will get a fix in 2.30, which is due in a week or so. Please excuse me for this misunderstanding and possible loss of time. I can send you an internal 2.30 build to test and verify that the error disappears on your side. Please ask the license holder at your company to assign you a license. Then, submit a private ticket and refer to this forum thread.

### Response

**Dan** commented on 06 Dec 2021

No problem, thank you, I will submit a ticket. I'll update this thread once I have the results.

### Response

**Daniel** commented on 14 Dec 2021

Installing build 2.30 fixed this issue. Thanks, -Dan
