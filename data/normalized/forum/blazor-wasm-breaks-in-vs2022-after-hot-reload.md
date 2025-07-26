# Blazor WASM breaks in VS2022 after Hot Reload

## Question

**Ste** asked on 02 Jul 2024

Working on a Blazor WASM app (.NET 8) and seeing the error below in the browser's console after successful Hot Reload from VS2022 and clicking on any button in the app. Same button works fine before the Hot Reload. The issue is not limited only to buttons. I believe this started with the latest VS update (17.10.3). The Telerik version we're using is old, 4.3.0, however we never had that particular issue before. Anybody having the same issues? Is this VS issue? Thank you, Stefan <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<Microsoft.JSInterop.JSException: Cannot read properties of null (reading 'addEventListener') TypeError: Cannot read properties of null (reading 'addEventListener') at gD.bindEvents ([http://localhost:5137/_content/Telerik.UI.for.Blazor/js/telerik-blazor.js:50:1844171)](http://localhost:5137/_content/Telerik.UI.for.Blazor/js/telerik-blazor.js:50:1844171)) at gD.onAfterShow ([http://localhost:5137/_content/Telerik.UI.for.Blazor/js/telerik-blazor.js:50:1844381)](http://localhost:5137/_content/Telerik.UI.for.Blazor/js/telerik-blazor.js:50:1844381)) at Module.fe ([http://localhost:5137/_content/Telerik.UI.for.Blazor/js/telerik-blazor.js:50:1044593)](http://localhost:5137/_content/Telerik.UI.for.Blazor/js/telerik-blazor.js:50:1044593)) at [http://localhost:5137/_framework/blazor.webassembly.js:1:2878](http://localhost:5137/_framework/blazor.webassembly.js:1:2878) at new Promise (<anonymous>) at b.beginInvokeJSFromDotNet ([http://localhost:5137/_framework/blazor.webassembly.js:1:2835)](http://localhost:5137/_framework/blazor.webassembly.js:1:2835)) at Object.vn [as invokeJSJson] ([http://localhost:5137/_framework/blazor.webassembly.js:1:58849)](http://localhost:5137/_framework/blazor.webassembly.js:1:58849)) at [http://localhost:5137/_framework/dotnet.runtime.8.0.5.gongq8hbow.js:3:178364](http://localhost:5137/_framework/dotnet.runtime.8.0.5.gongq8hbow.js:3:178364) at Tl ([http://localhost:5137/_framework/dotnet.runtime.8.0.5.gongq8hbow.js:3:179198)](http://localhost:5137/_framework/dotnet.runtime.8.0.5.gongq8hbow.js:3:179198)) at wasm://wasm/00b2193a:wasm-function[349]:0x1fab4 at Microsoft.JSInterop.JSRuntime.<InvokeAsync>d__16`1[[Microsoft.JSInterop.Infrastructure.IJSVoidResult, Microsoft.JSInterop, Version=8.0.0.0, Culture=neutral, PublicKeyToken=adb9793829ddae60]].MoveNext() at Microsoft.JSInterop.JSRuntimeExtensions.InvokeVoidAsync(IJSRuntime jsRuntime, String identifier, Object[] args) at Telerik.Blazor.Components.Dialog.DialogBase.InvokeOnAfterShowAsync() at Telerik.Blazor.Components.Dialog.DialogBuilder.OnAfterRenderAsync(Boolean firstRender) at Microsoft.AspNetCore.Components.RenderTree.Renderer.GetErrorHandledTask(Task taskToHandle, ComponentState owningComponentState)>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

### Response

**Stefan** commented on 03 Jul 2024

Additional info. The issue is caused by Dialogs.AlertAsync. Steps to reproduce. Start with the default Blazor WASM project template. Add the Telerik to it. Then change the Counter.razor as shown below. Start debugging. Everything works fine. Change the button text from 'Click me' to 'Click me 2'. Hot Reload. On the button click the 5 seconds delay works fine but the error shows as soon as Alert Async is called. Calling the method in more async fashion @onclick="@(async Task()=> await IncrementCount())" doesn't help. Making the method synchronous doesn't help either.>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <h1>Counter</h1> <p role="status">Current count: @currentCount</p> <button class="btn btn-primary" @onclick="IncrementCount">Click me</button> @code { [CascadingParameter] public required DialogFactory Dialogs { get; set; } private int currentCount=0; private async Task IncrementCount() { currentCount++; Console.WriteLine("Delay for 5sec."); await Task.Delay(5000); Console.WriteLine("Show alert."); await Dialogs.AlertAsync($"Clicked"); } }

## Answer

**Paul** answered on 08 Jul 2024

We experiencing a similar problem with version 6.0 of the Telerik Blazor component set. In a blazor web server project with .NET 8.0. Dialogs.AlertAsync is called within a synchronous method. It's not occuring all the time. Seems to be random and/or a timing issue. ERROR: blazor.web.js:1 [2024-06-20T10:14:25.876Z] Error: Microsoft.JSInterop.JSException: Cannot read properties of null (reading 'addEventListener') TypeError: Cannot read properties of null (reading 'addEventListener') at o.bindEvents (*********/_content/Telerik.UI.for.Blazor/js/telerik-blazor.js:50:1179113) at o.onAfterShow ( ********* /_content/Telerik.UI.for.Blazor/js/telerik-blazor.js:50:1179346) at e.invokeComponentMethod ( ********* /_content/Telerik.UI.for.Blazor/js/telerik-blazor.js:50:1112740) at ********* /_framework/blazor.web.js:1:3244 at new Promise (<anonymous>) at y.beginInvokeJSFromDotNet ( ********* /_framework/blazor.web.js:1:3201) at gn._invokeClientMethod ( ********* /_framework/blazor.web.js:1:62841) at gn._processIncomingData ( ********* /_framework/blazor.web.js:1:60316) at connection.onreceive ( ********* /_framework/blazor.web.js:1:53957) at i.onmessage ( ********* /_framework/blazor.web.js:1:82102) at Microsoft.JSInterop.JSRuntime.InvokeAsync[TValue](Int64 targetInstanceId, String identifier, Object[] args) at Microsoft.JSInterop.JSRuntimeExtensions.InvokeVoidAsync(IJSRuntime jsRuntime, String identifier, Object[] args) at Telerik.Blazor.Components.Dialog.DialogBase.InvokeOnAfterShowAsync() at Telerik.Blazor.Components.Dialog.DialogBuilder.OnAfterRenderAsync(Boolean firstRender) at Microsoft.AspNetCore.Components.RenderTree.Renderer.GetErrorHandledTask(Task taskToHandle,

### Response

**Nadezhda Tacheva** answered on 10 Jul 2024

Hi Stefan and Paul, I managed to reproduce the error on my end but I suspect it is not specifically related to the Telerik component. I will perform some additional testing to validate if I can hit that without using our components. I will share the result here afterwards. Regards, Nadezhda Tacheva Progress Telerik

### Response

**Nadezhda Tacheva** answered on 17 Jul 2024

Hi Stefan and Paul, I've revised the scenairo with our development team and we've confirmed that there is a bug with the predefined dialogs. I've logged the following item, so you can track the progress of the fix: Predefined dialogs throw when hot reload updates are applied. Regards, Nadezhda Tacheva Progress Telerik

### Response

**Saurabh** commented on 23 Aug 2024

Hi @Nadezhda Tacheva I am facing similar issue in .net 8.0. What would be solution or alternative for DialogFactory.AlertAsync

### Response

**Nadezhda Tacheva** commented on 27 Aug 2024

Hi Saurabh, The issue has been fixed in UI for Blazor 6.1.0. You can upgrade to resolve it on your end.
