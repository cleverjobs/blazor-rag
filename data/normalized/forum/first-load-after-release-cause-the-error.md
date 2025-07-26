# first load after release cause the error

## Question

**Ale** asked on 23 Nov 2020

After release the fist load cause the error (same for each component on the page), reload the page helps to get rid of, Marin what information do you need to investigate? Microsoft.AspNetCore.Components.WebAssembly.Rendering.WebAssemblyRenderer[100] Unhandled exception rendering component: Could not find 'TelerikBlazor.initMenuItem' ('TelerikBlazor' was undefined). Error: Could not find 'TelerikBlazor.initMenuItem' ('TelerikBlazor' was undefined). at [https://..../crm-b/_framework/blazor.webassembly.js:1:1287](https://..../crm-b/_framework/blazor.webassembly.js:1:1287) at Array.forEach (<anonymous>) at e.findFunction ( [https://.../crm-b/_framework/blazor.webassembly.js:1:1247)](https://.../crm-b/_framework/blazor.webassembly.js:1:1247)) at b ( [https://.../crm-b/_framework/blazor.webassembly.js:1:2989)](https://.../crm-b/_framework/blazor.webassembly.js:1:2989)) at [https://.../crm-b/_framework/blazor.webassembly.js:1:3935](https://.../crm-b/_framework/blazor.webassembly.js:1:3935) at new Promise (<anonymous>) at Object.beginInvokeJSFromDotNet ( [https://.../crm-b/_framework/blazor.webassembly.js:1:3908)](https://.../crm-b/_framework/blazor.webassembly.js:1:3908)) at Object.w [as invokeJSFromDotNet] ( [https://.../crm-b/_framework/blazor.webassembly.js:1:64006)](https://.../crm-b/_framework/blazor.webassembly.js:1:64006)) at _mono_wasm_invoke_js_blazor ( [https://.../crm-b/_framework/dotnet.5.0.0.js:1:190800)](https://.../crm-b/_framework/dotnet.5.0.0.js:1:190800)) at do_icall (<anonymous>:wasm-function[10595]:0x194e46) Microsoft.JSInterop.JSException: Could not find 'TelerikBlazor.initMenuItem' ('TelerikBlazor' was undefined). Error: Could not find 'TelerikBlazor.initMenuItem' ('TelerikBlazor' was undefined). at [https://.../crm-b/_framework/blazor.webassembly.js:1:1287](https://.../crm-b/_framework/blazor.webassembly.js:1:1287) at Array.forEach (<anonymous>) at e.findFunction ( [https://.../crm-b/_framework/blazor.webassembly.js:1:1247)](https://.../crm-b/_framework/blazor.webassembly.js:1:1247)) at b ( [https://.../crm-b/_framework/blazor.webassembly.js:1:2989)](https://.../crm-b/_framework/blazor.webassembly.js:1:2989)) at [https://.../crm-b/_framework/blazor.webassembly.js:1:3935](https://.../crm-b/_framework/blazor.webassembly.js:1:3935) at new Promise (<anonymous>) at Object.beginInvokeJSFromDotNet ( [https://.../crm-b/_framework/blazor.webassembly.js:1:3908)](https://.../crm-b/_framework/blazor.webassembly.js:1:3908)) at Object.w [as invokeJSFromDotNet] ( [https://.../crm-b/_framework/blazor.webassembly.js:1:64006)](https://.../crm-b/_framework/blazor.webassembly.js:1:64006)) at _mono_wasm_invoke_js_blazor ( [https://.../crm-b/_framework/dotnet.5.0.0.js:1:190800)](https://.../crm-b/_framework/dotnet.5.0.0.js:1:190800)) at do_icall (<anonymous>:wasm-function[10595]:0x194e46) at Microsoft.JSInterop.JSRuntime.<InvokeAsync>d__15`1[[System.Object, System.Private.CoreLib, Version=5.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e]].MoveNext() at Telerik.Blazor.Components.Menu.MenuItem`1.<OnAfterRenderAsync>d__80[[CRM.Client.Model.MenuItem, CRM.Client, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]].MoveNext() at Microsoft.AspNetCore.Components.RenderTree.Renderer.GetErrorHandledTask(Task taskToHandle)

## Answer

**Aleksandr** answered on 23 Nov 2020

seems solved by adding autostart=true <script src="_framework/blazor.webassembly.js" autostart="true"></script>

### Response

**Aleksandr** answered on 23 Nov 2020

did not help, got error once again

### Response

**Marin Bratanov** answered on 24 Nov 2020

Hello Aleksandr, We have this article which offers some explanations and suggestions: [https://docs.telerik.com/blazor-ui/troubleshooting/js-errors.](https://docs.telerik.com/blazor-ui/troubleshooting/js-errors.) Most likely, the culprit in this case is either the defer attribute, or cache that does not work well in dev servers. Regards, Marin Bratanov

### Response

**Aleksandr** answered on 24 Nov 2020

Marin, this is not the dev server (it is but same as we have in prod), Marin i would appreciate for direct link to defer doc, the wiriness is that the reload helps & that the issue occur the first load after release Thx Alex

### Response

**Marin Bratanov** answered on 24 Nov 2020

Hi, The defer attribute is described in the article I linked from (screenshot attached), here's the anchor to its section directly [https://docs.telerik.com/blazor-ui/troubleshooting/js-errors#defer-attribute](https://docs.telerik.com/blazor-ui/troubleshooting/js-errors#defer-attribute) The fact that clearing the cache solves the error indicates that this is a caching problem and you should look into the server settings - what content it returns and with what caching policy. Regards, Marin Bratanov

### Response

**Aleksandr** answered on 24 Nov 2020

maybe, but nothing was changed in kendo to raise the error, where this object is located "TelerikBlazor." seems control initializes before some core code was loaded. the caching policy is default to publish command, later today i will add build number to the telerik js reference, will see if it helps Thx Alex

### Response

**Marin Bratanov** answered on 24 Nov 2020

Hello Aleksandr, The described behavior sounds like wrong content being returns or it being delayed. The fact that it works the second time indicates that the code itself is OK and fetching it does not work well until the cache updates. Regards, Marin Bratanov

### Response

**Aleksandr** answered on 24 Nov 2020

Marin, this is the web.config from the server, it was generated by publish command, i just added environment variable to have appsettings.json "transform" <? xml version="1.0" encoding="UTF-8"?> <configuration> <system.webServer> <staticContent> <remove fileExtension=".blat" /> <remove fileExtension=".dat" /> <remove fileExtension=".dll" /> <remove fileExtension=".json" /> <remove fileExtension=".wasm" /> <remove fileExtension=".woff" /> <remove fileExtension=".woff2" /> <mimeMap fileExtension=".blat" mimeType="application/octet-stream" /> <mimeMap fileExtension=".dll" mimeType="application/octet-stream" /> <mimeMap fileExtension=".dat" mimeType="application/octet-stream" /> <mimeMap fileExtension=".json" mimeType="application/json" /> <mimeMap fileExtension=".wasm" mimeType="application/wasm" /> <mimeMap fileExtension=".woff" mimeType="application/font-woff" /> <mimeMap fileExtension=".woff2" mimeType="application/font-woff" /> </staticContent> <httpCompression> <dynamicTypes> <add mimeType="application/octet-stream" enabled="true" /> <add mimeType="application/wasm" enabled="true" /> </dynamicTypes> </httpCompression> <httpProtocol> <customHeaders> <add name="blazor-environment" value="AWS" /> </customHeaders> </httpProtocol> <rewrite> <rules> <rule name="Serve subdir"> <match url=".*" /> <action type="Rewrite" url="wwwroot\{R:0}" /> </rule> <rule name="SPA fallback routing" stopProcessing="true"> <match url=".*" /> <conditions logicalGrouping="MatchAll"> <add input="{REQUEST_FILENAME}" matchType="IsFile" negate="true" /> </conditions> <action type="Rewrite" url="wwwroot\" /> </rule> </rules> </rewrite> </system.webServer> </configuration>

### Response

**Marin Bratanov** answered on 24 Nov 2020

Hi Aleksandr, if the "AWS" environment is amazon web services, and this is hosted through S3 and CloudFront, it is important to keep in mind that their caching is, to say the least, strange. Often times the first request will still hit cache, but subsequent requests will go once to the actual origin, update the edge caches in cloudfront and then start serving proper content. I highly recommend you review that behavior, as the web.config does not indicate caching policies in and of its own, servers should usually use the modified date on the files, but that does not always happen. Regards, Marin Bratanov

### Response

**Aleksandr** answered on 24 Nov 2020

Marin, yes, AWS is the virtual machine in Amazon cloud, i will try to add build number to the ref to the files & see whether it help or not Thx Alex

### Response

**Aleksandr** answered on 24 Nov 2020

removed defer, observing

### Response

**Aleksandr** answered on 25 Nov 2020

seems helped

### Response

**Hartwin** commented on 06 May 2025

helped for me, too. I had the same error: Could not find 'TelerikBlazor.initMenuItem' ('TelerikBlazor' was undefined). It happened on my developer computer, usually when starting the application, after some reloading it worked for the rest of the session. Seldom occurence of this error in staging or productive environment (in the azure cloud). after removing "defer" from the line <script src="_content/Telerik.UI.for.Blazor/js/telerik-blazor.js" defer></script> in the file _Host.cshtml the error disappeared.
