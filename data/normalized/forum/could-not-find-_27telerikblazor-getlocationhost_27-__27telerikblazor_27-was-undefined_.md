# Could not find 'TelerikBlazor.getLocationHost' ('TelerikBlazor' was undefined).

## Question

**Way** asked on 01 Apr 2021

Blazor WebAssembly on .Net 5 After updating Telerik.UI.For.Blazor to version 2.23.0 I often see an error in the Console "Could not find 'TelerikBlazor.getLocationHost' ('TelerikBlazor' was undefined)." after doing a build and refreshing the page. If I then refresh the page again the error will not reappear. I am only using the TelerikGrid. crit: Microsoft.AspNetCore.Components.WebAssembly.Rendering.WebAssemblyRenderer[100] Unhandled exception rendering component: Could not find 'TelerikBlazor.getLocationHost' ('TelerikBlazor' was undefined). Error: Could not find 'TelerikBlazor.getLocationHost' ('TelerikBlazor' was undefined). at [https://localhost:44359/_framework/blazor.webassembly.js:1:1287](https://localhost:44359/_framework/blazor.webassembly.js:1:1287) at Array.forEach (<anonymous>) at e.findFunction ([https://localhost:44359/_framework/blazor.webassembly.js:1:1247)](https://localhost:44359/_framework/blazor.webassembly.js:1:1247)) at b ([https://localhost:44359/_framework/blazor.webassembly.js:1:2989)](https://localhost:44359/_framework/blazor.webassembly.js:1:2989)) at [https://localhost:44359/_framework/blazor.webassembly.js:1:3935](https://localhost:44359/_framework/blazor.webassembly.js:1:3935) at new Promise (<anonymous>) at Object.beginInvokeJSFromDotNet ([https://localhost:44359/_framework/blazor.webassembly.js:1:3908)](https://localhost:44359/_framework/blazor.webassembly.js:1:3908)) at Object.w [as invokeJSFromDotNet] ([https://localhost:44359/_framework/blazor.webassembly.js:1:64232)](https://localhost:44359/_framework/blazor.webassembly.js:1:64232)) at _mono_wasm_invoke_js_blazor ([https://localhost:44359/_framework/dotnet.5.0.4.js:1:190800)](https://localhost:44359/_framework/dotnet.5.0.4.js:1:190800)) at do_icall (<anonymous>:wasm-function[10596]:0x194e4e) Microsoft.JSInterop.JSException: Could not find 'TelerikBlazor.getLocationHost' ('TelerikBlazor' was undefined). Error: Could not find 'TelerikBlazor.getLocationHost' ('TelerikBlazor' was undefined). at [https://localhost:44359/_framework/blazor.webassembly.js:1:1287](https://localhost:44359/_framework/blazor.webassembly.js:1:1287) at Array.forEach (<anonymous>) at e.findFunction ([https://localhost:44359/_framework/blazor.webassembly.js:1:1247)](https://localhost:44359/_framework/blazor.webassembly.js:1:1247)) at b ([https://localhost:44359/_framework/blazor.webassembly.js:1:2989)](https://localhost:44359/_framework/blazor.webassembly.js:1:2989)) at [https://localhost:44359/_framework/blazor.webassembly.js:1:3935](https://localhost:44359/_framework/blazor.webassembly.js:1:3935) at new Promise (<anonymous>) at Object.beginInvokeJSFromDotNet ([https://localhost:44359/_framework/blazor.webassembly.js:1:3908)](https://localhost:44359/_framework/blazor.webassembly.js:1:3908)) at Object.w [as invokeJSFromDotNet] ([https://localhost:44359/_framework/blazor.webassembly.js:1:64232)](https://localhost:44359/_framework/blazor.webassembly.js:1:64232)) at _mono_wasm_invoke_js_blazor ([https://localhost:44359/_framework/dotnet.5.0.4.js:1:190800)](https://localhost:44359/_framework/dotnet.5.0.4.js:1:190800)) at do_icall (<anonymous>:wasm-function[10596]:0x194e4e) at Microsoft.JSInterop.JSRuntime.<InvokeAsync>d__15`1[[System.String, System.Private.CoreLib, Version=5.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e]].MoveNext() at Telerik.Blazor.Components.Dialog.DialogBuilder.OnAfterRenderAsync(Boolean firstRender) at Microsoft.AspNetCore.Components.RenderTree.Renderer.GetErrorHandledTask(Task taskToHandle)

## Answer

**Marin Bratanov** answered on 01 Apr 2021

Hi Wayne, Please try the steps from this article: [https://docs.telerik.com/blazor-ui/troubleshooting/js-errors](https://docs.telerik.com/blazor-ui/troubleshooting/js-errors) Regards, Marin Bratanov Progress Telerik

### Response

**Giuseppe** commented on 19 Jul 2021

Hi Marin. We also ran into this issue. Is there something speaking against using <script src="/_content/Telerik.UI.for.Blazor/js/telerik-blazor.js" asp-append-version="true"></script> ?

### Response

**Dimo** commented on 22 Jul 2021

Hi Giuseppe, As long as the <script> declaration has no defer attribute, it should be a blocking script and force the browser to load the file before parsing the rest of the DOM. So, I don't expect the asp-append-version attribute to cause problems. Are you saying that you get a JavaScript error only when you have the asp-append-version="true" attribute to our JS file? Does the error occur only once after you clear the browser cache? Or does it always occur the first time the app is opened in the browser? Can you show us where exactly the JavaScript file is registered in the page markup? Also, what do you observe in the browser's Network tab when the error occurs - is the file not loaded at all, or is it loaded for too long?

### Response

**Giuseppe** commented on 22 Jul 2021

Hi Dimo. Acutally I had the defer attribute in it, so I removed it. I just wanted to ensure that with asp-append-version the browsers take the newest version we we release and not running into browser caching problems. (I asked because some scripts having troubles if there's ?xy=xx in the end of it.)

### Response

**Yoly** answered on 13 Apr 2021

I'm getting the same error after upgrading, also on .Net 5. The provided troubleshooting link didn't help. I downgraded back to 2.22 and the error is gone. Any info on how to solve this specific error? Unhandled exception rendering component: Could not find 'TelerikBlazor.getLocationHost' ('TelerikBlazor' was undefined). Thanks.

### Response

**Marin Bratanov** answered on 14 Apr 2021

Hi Yoly, This is definitely a wrong JS Interop file being used in the browser. Clearing the browser cache should help. If it is a build issue with the build caching old assets, deleting the bin and obj folders will help (then clear the browser cache too). If you are not using the static assets but the cdn, make sure to update its URL too to point to the new package version as well. If neither of this helps, please open a support ticket with the sample project that has the problem. Regards, Marin Bratanov

### Response

**Jeremy** commented on 14 May 2021

Browser cache fixed it, thanks!

### Response

**Yoly** answered on 14 Apr 2021

Hi Marin, It seems it was a browser cache issue. I had previously done clean/rebuild and it didn't help, clearing the browser cache as you suggested fixed the issue. Thanks for the help!

### Response

**Wayne Hiller** answered on 05 May 2021

I had removed the defer when loading the js file and it seemed to help a little but the issue still happens a lot. Seems like there is a timing issue, sometimes it loads in time, other times not.

### Response

**Marin Bratanov** commented on 05 May 2021

You can try moving the script earlier in the page, e.g., in the <head> to give the browser more time to parse it. Without the defer attribute, putting it above the framework script should let the browser parse all the Telerik code before the app has had the chance to really initialize and so it should not throw errors anymore.

### Response

**Wayne Hiller** commented on 05 May 2021

It is already the first script load in the head

### Response

**Marin Bratanov** commented on 06 May 2021

If you are using the CDN, try using the static assets, such errors are not expected if the versions match, and when the CDN is used its URL must match the version of the package in the project, and that's often overlooked when upgrading.

### Response

**Wayne Hiller** answered on 06 May 2021

<script src="_content/Telerik.UI.for.Blazor/js/telerik-blazor.js" defer></script> Well It ended up that I still had the defer, This project was copied from a base project and I forgot to remove it in this one (I have multiple projects using Telerik in Blazor). I will try it without the defer and see how it goes.

### Response

**Marin Bratanov** commented on 06 May 2021

I hope that helps

### Response

**Dorian** answered on 13 Aug 2022

For core 6.0, I was able to resolve this by adding the following lines to the program.cs file. This issue occurred for me locally after changing the environment variable [ASPNETCORE_ENVIRONMENT] from "Development" to "Release" as static web assets are enabled by default for the Development environment. var builder=WebApplication.CreateBuilder(args); builder.WebHost.UseStaticWebAssets(); // ----> added this line here var app=builder.Build(); app.UseStaticFiles(); // ---> Make sure this line exists

### Response

**Tony** answered on 22 Aug 2022

I got a similar error. In my case, I began using the Trial, then got a License, but did not change the JavaScript and CSS accordingly. So I changed from the Trial: <script src="_content/Telerik.UI.for.Blazor.Trial/js/telerik-blazor.js" defer> </script> <link rel="stylesheet" href="_content/Telerik.UI.for.Blazor.Trial/css/kendo-theme-default/all.css" /> To the Licensed version: <script src="_content/Telerik.UI.for.Blazor/js/telerik-blazor.js" defer> </script> <link rel="stylesheet" href="_content/Telerik.UI.for.Blazor/css/kendo-theme-default/all.css" /> Hope that helps someone who get this error.
