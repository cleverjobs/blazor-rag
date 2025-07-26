# 2.23 WASM Dialog crash

## Question

**RobRob** asked on 30 Mar 2021

After installing 2.23 into my Blazor WASM project, there's a js crash with the following stacktrace: crit: Microsoft.AspNetCore.Components.WebAssembly.Rendering.WebAssemblyRenderer[100] Unhandled exception rendering component: Could not find 'TelerikBlazor.getLocationHost' ('getLocationHost' was undefined). Error: Could not find 'TelerikBlazor.getLocationHost' ('getLocationHost' was undefined). at [https://localhost:44320/_framework/blazor.webassembly.js:1:1287](https://localhost:44320/_framework/blazor.webassembly.js:1:1287) at Array.forEach (<anonymous>) at e.findFunction ([https://localhost:44320/_framework/blazor.webassembly.js:1:1247)](https://localhost:44320/_framework/blazor.webassembly.js:1:1247)) at b ([https://localhost:44320/_framework/blazor.webassembly.js:1:2989)](https://localhost:44320/_framework/blazor.webassembly.js:1:2989)) at [https://localhost:44320/_framework/blazor.webassembly.js:1:3935](https://localhost:44320/_framework/blazor.webassembly.js:1:3935) at new Promise (<anonymous>) at Object.beginInvokeJSFromDotNet ([https://localhost:44320/_framework/blazor.webassembly.js:1:3908)](https://localhost:44320/_framework/blazor.webassembly.js:1:3908)) at Object.w [as invokeJSFromDotNet] ([https://localhost:44320/_framework/blazor.webassembly.js:1:64232)](https://localhost:44320/_framework/blazor.webassembly.js:1:64232)) at _mono_wasm_invoke_js_blazor ([https://localhost:44320/_framework/dotnet.5.0.4.js:1:190800)](https://localhost:44320/_framework/dotnet.5.0.4.js:1:190800)) at do_icall (<anonymous>:wasm-function[10596]:0x194e4e) Microsoft.JSInterop.JSException: Could not find 'TelerikBlazor.getLocationHost' ('getLocationHost' was undefined). Error: Could not find 'TelerikBlazor.getLocationHost' ('getLocationHost' was undefined). at [https://localhost:44320/_framework/blazor.webassembly.js:1:1287](https://localhost:44320/_framework/blazor.webassembly.js:1:1287) at Array.forEach (<anonymous>) at e.findFunction ([https://localhost:44320/_framework/blazor.webassembly.js:1:1247)](https://localhost:44320/_framework/blazor.webassembly.js:1:1247)) at b ([https://localhost:44320/_framework/blazor.webassembly.js:1:2989)](https://localhost:44320/_framework/blazor.webassembly.js:1:2989)) at [https://localhost:44320/_framework/blazor.webassembly.js:1:3935](https://localhost:44320/_framework/blazor.webassembly.js:1:3935) at new Promise (<anonymous>) at Object.beginInvokeJSFromDotNet ([https://localhost:44320/_framework/blazor.webassembly.js:1:3908)](https://localhost:44320/_framework/blazor.webassembly.js:1:3908)) at Object.w [as invokeJSFromDotNet] ([https://localhost:44320/_framework/blazor.webassembly.js:1:64232)](https://localhost:44320/_framework/blazor.webassembly.js:1:64232)) at _mono_wasm_invoke_js_blazor ([https://localhost:44320/_framework/dotnet.5.0.4.js:1:190800)](https://localhost:44320/_framework/dotnet.5.0.4.js:1:190800)) at do_icall (<anonymous>:wasm-function[10596]:0x194e4e) at Microsoft.JSInterop.JSRuntime.<InvokeAsync>d__15`1[[System.String, System.Private.CoreLib, Version=5.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e]].MoveNext() at Telerik.Blazor.Components.Dialog.DialogBuilder.OnAfterRenderAsync(Boolean firstRender) at Microsoft.AspNetCore.Components.RenderTree.Renderer.GetErrorHandledTask(Task taskToHandle)

## Answer

**Marin Bratanov** answered on 30 Mar 2021

Hello Rob, Could you try the troubleshooting ideas here and let me know if they helped: [https://docs.telerik.com/blazor-ui/troubleshooting/js-errors?](https://docs.telerik.com/blazor-ui/troubleshooting/js-errors?) Regards, Marin Bratanov Progress Telerik

### Response

**Rob** answered on 30 Mar 2021

Thanks Marin, Cleaning the solution solved the issue. Best, Rob

### Response

**Marin Bratanov** answered on 30 Mar 2021

Happy to see you moving forward, Rob! --Marin

### Response

**Jeff** answered on 30 Mar 2021

Marin, I'm hitting the same crash stack with 2.23. I've cleared the NUGET package cache (and deleted the bin/obj folders). I've cleaned the solution. I even made sure I updated my node_modules to pull down the latest kendo-theme-bootstrap v4.35. Still hitting this on app launch. It's a .net 5 WASM project which was working clean with 2.22. crit: Microsoft.AspNetCore.Components.WebAssembly.Rendering.WebAssemblyRenderer[100] Unhandled exception rendering component: Could not find 'TelerikBlazor.getLocationHost' ('getLocationHost' was undefined). Error: Could not find 'TelerikBlazor.getLocationHost' ('getLocationHost' was undefined). at [https://localhost:5001/_framework/blazor.webassembly.js:1:1287](https://localhost:5001/_framework/blazor.webassembly.js:1:1287) at Array.forEach (<anonymous>) at e.findFunction ([https://localhost:5001/_framework/blazor.webassembly.js:1:1247)](https://localhost:5001/_framework/blazor.webassembly.js:1:1247)) at b ([https://localhost:5001/_framework/blazor.webassembly.js:1:2989)](https://localhost:5001/_framework/blazor.webassembly.js:1:2989)) at [https://localhost:5001/_framework/blazor.webassembly.js:1:3935](https://localhost:5001/_framework/blazor.webassembly.js:1:3935) at new Promise (<anonymous>) at Object.beginInvokeJSFromDotNet ([https://localhost:5001/_framework/blazor.webassembly.js:1:3908)](https://localhost:5001/_framework/blazor.webassembly.js:1:3908)) at Object.w [as invokeJSFromDotNet] ([https://localhost:5001/_framework/blazor.webassembly.js:1:64232)](https://localhost:5001/_framework/blazor.webassembly.js:1:64232)) at _mono_wasm_invoke_js_blazor ([https://localhost:5001/_framework/dotnet.5.0.4.js:1:190800)](https://localhost:5001/_framework/dotnet.5.0.4.js:1:190800))

### Response

**Jeff** answered on 30 Mar 2021

Cancel red alert. Lower shields. Clearing the browser cache removed the error. Kruft in the cache. :)

### Response

**Marin Bratanov** answered on 31 Mar 2021

It is good to see you have fixed this, Jeff. --Marin
