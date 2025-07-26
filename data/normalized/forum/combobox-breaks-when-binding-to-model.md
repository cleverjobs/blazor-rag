# ComboBox breaks when binding to model

## Question

**Sim** asked on 27 Mar 2020

Finally updated to the telerik blazor 2.9.0 release, but now the combobox does not bind to the model correctly. The best error is "WASM:
Microsoft.JSInterop.JSException: Failed to execute 'observe' on
'IntersectionObserver': parameter 1 is not of type 'Element'." The markup from the razor form: <TelerikComboBox Data="@SelectableClaims" TItem="ClaimModel" TValue="int" ValueField="Number" Placeholder="Claim #" ClearButton="true" Width="150px" TextField="Name" ValueChanged="@((int num)=> SelectClaim(claim, num))"></TelerikComboBox> However, I tried the telerik code in the documentation, it produces the same error. The full error is reproduced below. blazor.webassembly.js:1 WASM: ﻿Unhandled exception rendering
component: p.printErr @blazor.webassembly.js:1 blazor.webassembly.js:1 WASM:
Microsoft.JSInterop.JSException: Failed to execute 'observe' on
'IntersectionObserver': parameter 1 is not of type 'Element'. p.printErr @blazor.webassembly.js:1 blazor.webassembly.js:1 WASM: TypeError: Failed to execute
'observe' on 'IntersectionObserver': parameter 1 is not of type 'Element'. p.printErr @blazor.webassembly.js:1 blazor.webassembly.js:1 WASM: at e.value
([https://kendo.cdn.telerik.com/blazor/2.8.0/telerik-blazor.min.js:38:23963)](https://kendo.cdn.telerik.com/blazor/2.8.0/telerik-blazor.min.js:38:23963)) p.printErr @blazor.webassembly.js:1 blazor.webassembly.js:1 WASM: at new e
([https://kendo.cdn.telerik.com/blazor/2.8.0/telerik-blazor.min.js:38:20476)](https://kendo.cdn.telerik.com/blazor/2.8.0/telerik-blazor.min.js:38:20476)) p.printErr @blazor.webassembly.js:1 blazor.webassembly.js:1 WASM: at r
([https://kendo.cdn.telerik.com/blazor/2.8.0/telerik-blazor.min.js:1:6519)](https://kendo.cdn.telerik.com/blazor/2.8.0/telerik-blazor.min.js:1:6519)) p.printErr @blazor.webassembly.js:1 blazor.webassembly.js:1 WASM: at Object.r
([https://kendo.cdn.telerik.com/blazor/2.8.0/telerik-blazor.min.js:38:18001)](https://kendo.cdn.telerik.com/blazor/2.8.0/telerik-blazor.min.js:38:18001)) p.printErr @blazor.webassembly.js:1 blazor.webassembly.js:1 WASM: at [https://localhost:5001/_framework/blazor.webassembly.js:1:9740](https://localhost:5001/_framework/blazor.webassembly.js:1:9740) p.printErr @blazor.webassembly.js:1 blazor.webassembly.js:1 WASM: at new Promise (<anonymous>) p.printErr @blazor.webassembly.js:1 blazor.webassembly.js:1 WASM: at Object.beginInvokeJSFromDotNet
([https://localhost:5001/_framework/blazor.webassembly.js:1:9709)](https://localhost:5001/_framework/blazor.webassembly.js:1:9709)) p.printErr @blazor.webassembly.js:1 blazor.webassembly.js:1 WASM: at _mono_wasm_invoke_js_marshalled
([https://localhost:5001/_framework/wasm/dotnet.3.2.0-preview2.20159.2.js:1:162942)](https://localhost:5001/_framework/wasm/dotnet.3.2.0-preview2.20159.2.js:1:162942)) p.printErr @blazor.webassembly.js:1 blazor.webassembly.js:1 WASM: at do_icall (wasm-function[6008]:0x10e0aa) p.printErr @blazor.webassembly.js:1 blazor.webassembly.js:1 WASM: at do_icall_wrapper
(wasm-function[1886]:0x51cc2) p.printErr @blazor.webassembly.js:1 blazor.webassembly.js:1 WASM: at
System.Threading.Tasks.ValueTask`1[TResult].get_Result () <0x3031c70 +
0x0002c> in <filename unknown>:0 p.printErr @blazor.webassembly.js:1 blazor.webassembly.js:1 WASM: at Telerik.Blazor.Components.Popup.TelerikPopupBase.OnAfterRenderAsync
(System.Boolean firstRender) <0x3716860 + 0x00124> in <filename
unknown>:0 p.printErr @blazor.webassembly.js:1 blazor.webassembly.js:1 WASM: at
Microsoft.AspNetCore.Components.RenderTree.Renderer.GetErrorHandledTask
(System.Threading.Tasks.Task taskToHandle) <0x2f484a8 + 0x000c2> in
<filename unknown>:0

## Answer

**Simon** answered on 27 Mar 2020

Fixed it. It was pulling the wrong version of the telerik-blazor.min.js file from the CDN.
