# Blazor UI v6.0.0 gives error after upgrade

## Question

**JKa** asked on 17 May 2024

If i revert to 2024 Q1 the error disappears... 2024-05-16 19:54:03,530 [ERROR] Unhandled exception in circuit 'S77usknbj_EFjppCUa4yC1LlVuSlrA3J5HkaJib6jRs'. Microsoft.JSInterop.JSException: Could not find 'TelerikBlazor.initListView' ('initListView' was undefined). Error: Could not find 'TelerikBlazor.initListView' ('initListView' was undefined). at [http://localhost:5242/_framework/blazor.server.js:1:734](http://localhost:5242/_framework/blazor.server.js:1:734) at Array.forEach (<anonymous>) at l.findFunction ([http://localhost:5242/_framework/blazor.server.js:1:702)](http://localhost:5242/_framework/blazor.server.js:1:702)) at _ ([http://localhost:5242/_framework/blazor.server.js:1:5445)](http://localhost:5242/_framework/blazor.server.js:1:5445)) at [http://localhost:5242/_framework/blazor.server.js:1:3238](http://localhost:5242/_framework/blazor.server.js:1:3238) at new Promise (<anonymous>) at y.beginInvokeJSFromDotNet ([http://localhost:5242/_framework/blazor.server.js:1:3201)](http://localhost:5242/_framework/blazor.server.js:1:3201)) at Xt._invokeClientMethod ([http://localhost:5242/_framework/blazor.server.js:1:61001)](http://localhost:5242/_framework/blazor.server.js:1:61001)) at Xt._processIncomingData ([http://localhost:5242/_framework/blazor.server.js:1:58476)](http://localhost:5242/_framework/blazor.server.js:1:58476)) at Xt.connection.onreceive ([http://localhost:5242/_framework/blazor.server.js:1:52117)](http://localhost:5242/_framework/blazor.server.js:1:52117)) at Microsoft.JSInterop.JSRuntime.InvokeAsync[TValue](Int64 targetInstanceId, String identifier, Object[] args) at Microsoft.JSInterop.JSRuntimeExtensions.InvokeVoidAsync(IJSRuntime jsRuntime, String identifier, Object[] args) at Telerik.Blazor.Components.TelerikListView`1.InitListView() at Telerik.Blazor.Components.TelerikListView`1.OnAfterRenderAsync(Boolean firstRender) at Microsoft.AspNetCore.Components.RenderTree.Renderer.GetErrorHandledTask(Task taskToHandle, ComponentState owningComponentState) 2024-05-16 19:54:03,838 [WARN ] Unhandled exception rendering component: JavaScript interop calls cannot be issued at this time. This is because the circuit has disconnected and is being disposed. Microsoft.JSInterop.JSDisconnectedException: JavaScript interop calls cannot be issued at this time. This is because the circuit has disconnected and is being disposed. at Microsoft.AspNetCore.Components.Server.Circuits.RemoteJSRuntime.BeginInvokeJS(Int64 asyncHandle, String identifier, String argsJson, JSCallResultType resultType, Int64 targetInstanceId) at Microsoft.JSInterop.JSRuntime.InvokeAsync[TValue](Int64 targetInstanceId, String identifier, CancellationToken cancellationToken, Object[] args) at Microsoft.JSInterop.JSRuntime.InvokeAsync[TValue](Int64 targetInstanceId, String identifier, Object[] args) at Microsoft.JSInterop.JSRuntimeExtensions.InvokeVoidAsync(IJSRuntime jsRuntime, String identifier, Object[] args) at Telerik.Blazor.Components.TelerikTextArea.SetJsValueAsync() at Telerik.Blazor.Components.Common.TextBoxBase.OnAfterRenderInternalAsync(Boolean firstRender) at Telerik.Blazor.Components.Common.TextBoxBase.OnAfterRenderAsync(Boolean firstRender) at Telerik.Blazor.Components.TelerikTextArea.OnAfterRenderAsync(Boolean firstRender) at Microsoft.AspNetCore.Components.RenderTree.Renderer.GetErrorHandledTask(Task taskToHandle, ComponentState owningComponentState)

## Answer

**Tsvetomir** answered on 21 May 2024

Hi John, I'm ready to help you as quickly as possible resolve the error below. From the provided information, it seems the error stems from missing the JavaScript of the ListView component. Such an error means that the telerik-blazor.js script file version does not match the NuGet package version. As a result, the script does not include all components, features, or correct method names. From here, I recommend you refer to our troubleshooting article section about init[Component] was undefined, which suggests a few possible reasons and solutions for the same type of issues. The most likely case is that an old script is referenced and/or is cached. I hope the provided information helps to resolve the matter. Regards, Tsvetomir Progress Telerik

### Response

**JKattestaart** commented on 21 May 2024

Thx for the update I upgraded via Nuget, so it must be something with the browser cache

### Response

**JKattestaart** commented on 21 May 2024

Tried again and seems te work now!
