# Error after upgrading to v3.7

## Question

**Dou** asked on 14 Nov 2022

My app worked on v3.6.1 but when I upgraded to v3.7 I'm getting the error below. It has something to do with the TelerikDatePicker. If I remove the date picker it I don't get the error. Any way I can get around this? fail: Microsoft.AspNetCore.Components.Web.ErrorBoundary[0] Microsoft.JSInterop.JSException: Cannot read properties of null (reading 'addEventListener') TypeError: Cannot read properties of null (reading 'addEventListener') at QM.bindEvents ([https://localhost:7116/_content/Telerik.UI.for.Blazor/js/telerik-blazor.js:50:1755270)](https://localhost:7116/_content/Telerik.UI.for.Blazor/js/telerik-blazor.js:50:1755270)) at new QM ([https://localhost:7116/_content/Telerik.UI.for.Blazor/js/telerik-blazor.js:50:1756185)](https://localhost:7116/_content/Telerik.UI.for.Blazor/js/telerik-blazor.js:50:1756185)) at Zt ([https://localhost:7116/_content/Telerik.UI.for.Blazor/js/telerik-blazor.js:50:1029936)](https://localhost:7116/_content/Telerik.UI.for.Blazor/js/telerik-blazor.js:50:1029936)) at Module.tE ([https://localhost:7116/_content/Telerik.UI.for.Blazor/js/telerik-blazor.js:50:1756262)](https://localhost:7116/_content/Telerik.UI.for.Blazor/js/telerik-blazor.js:50:1756262)) at [https://localhost:7116/_framework/blazor.webassembly.js:1:3332](https://localhost:7116/_framework/blazor.webassembly.js:1:3332) at new Promise (<anonymous>) at Object.beginInvokeJSFromDotNet ([https://localhost:7116/_framework/blazor.webassembly.js:1:3306)](https://localhost:7116/_framework/blazor.webassembly.js:1:3306)) at Object.St [as invokeJSFromDotNet] ([https://localhost:7116/_framework/blazor.webassembly.js:1:59938)](https://localhost:7116/_framework/blazor.webassembly.js:1:59938)) at _mono_wasm_invoke_js_blazor ([https://localhost:7116/_framework/dotnet..oafyft2lng.js:9073:37)](https://localhost:7116/_framework/dotnet..oafyft2lng.js:9073:37)) at do_icall (wasm://wasm/031ebc56:wasm-function[3582]:0xc1359) at Microsoft.JSInterop.JSRuntime.<InvokeAsync>d__16`1[[Microsoft.JSInterop.Infrastructure.IJSVoidResult, Microsoft.JSInterop, Version=6.0.0.0, Culture=neutral, PublicKeyToken=adb9793829ddae60]].MoveNext() at Microsoft.JSInterop.JSRuntimeExtensions.InvokeVoidAsync(IJSRuntime jsRuntime, String identifier, Object[] args) at Telerik.Blazor.Components.Common.Pickers.TelerikPickerBase`1.<InitPicker>d__119[[System.DateTime, System.Private.CoreLib, Version=6.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e]].MoveNext() at Telerik.Blazor.Components.Common.Pickers.TelerikPickerBase`1.<OnAfterRenderAsync>d__115[[System.DateTime, System.Private.CoreLib, Version=6.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e]].MoveNext() at Microsoft.AspNetCore.Components.RenderTree.Renderer.GetErrorHandledTask(Task taskToHandle, ComponentState owningComponentState)

## Answer

**Doug** answered on 16 Nov 2022

The other day I upgraded to v3.7 and got errors, created the forum entry above and then downgraded to v3.6.1. I have since been working on unrelated things and just now when I went back to do a little more testing with this issue I upgraded back to v3.7 and it seems to be working now. So I have no idea what happened there but I guess it's good.

### Response

**Dimo** answered on 17 Nov 2022

Hello Doug, Probably a caching issue. Regards, Dimo Progress Telerik

### Response

**Saurabh** commented on 23 Aug 2024

Hello Doug, I am facing similar issue after upgrading UI for Blazor to 6.0.2 from 4.4.0. Any other solution? Note- I am also switching from .net core 6.0 to net core 8.0

### Response

**Dimo** commented on 26 Aug 2024

@Saurabh - if the information in the addEventListener KB article does not help you and the error persists even after you have cleared the browser cache and rebuilt the app, please send a stripped (but runnable) version of your app for inspection.
