# Version 2.9 problem

## Question

**Pav** asked on 24 Mar 2020

Hi, I upgraded my project to Blazor WebAssembly 3.2.0 Preview 2 blazor.webassembly.js:1 WASM: TypeError: Failed to execute 'observe' on 'IntersectionObserver': parameter 1 is not of type 'Element'. at e.value (/_content/telerik.ui.for.blazor/js/telerik-blazor.js:38:23963) at new e (/_content/telerik.ui.for.blazor/js/telerik-blazor.js:38:20476) at r (/_content/telerik.ui.for.blazor/js/telerik-blazor.js:1:6519) at Object.r (/_content/telerik.ui.for.blazor/js/telerik-blazor.js:38:18001) at /_framework/blazor.webassembly.js:1:9740 at new Promise (<anonymous>) at Object.beginInvokeJSFromDotNet (/_framework/blazor.webassembly.js:1:9709) at _mono_wasm_invoke_js_marshalled (/_framework/wasm/dotnet.3.2.0-preview2.20159.2.js:1:162942)

## Answer

**Marin Bratanov** answered on 24 Mar 2020

Hi Pavel, What browser are you using? Can you confirm it is one of the supported browsers: [https://docs.telerik.com/blazor-ui/browser-support?](https://docs.telerik.com/blazor-ui/browser-support?) The error indicates that it comes from the IntersectionObserver API which is not supported under IE, and IE is not a browser we support. Regards, Marin Bratanov

### Response

**Pavel** answered on 24 Mar 2020

It is from Chrome. Same problem on Edge and mobile Chrome

### Response

**Pavel** answered on 24 Mar 2020

Another problem in version 2.9 - bad select items position in combobox. You can see it in screenshort.

### Response

**Marin Bratanov** answered on 24 Mar 2020

Hi Pavel, Our demos and my local tests seem to work fine and not throw such errors. A lot of things seem to be wrong here, and this is the first such report we get. My best guess is that something went wrong fundamentally with the upgrade - maybe old cached assets are used, maybe there is some invalid HTML even. I'd suggest going through the articles below and if the information from them does not help, to isolate these problems into a small runnable project I can run, debug and inspect, and send it to me in a private ticket. [https://docs.telerik.com/blazor-ui/upgrade/overview](https://docs.telerik.com/blazor-ui/upgrade/overview) [https://docs.telerik.com/blazor-ui/troubleshooting/general-issues](https://docs.telerik.com/blazor-ui/troubleshooting/general-issues) [https://docs.telerik.com/blazor-ui/troubleshooting/js-errors](https://docs.telerik.com/blazor-ui/troubleshooting/js-errors) Regards, Marin Bratanov

### Response

**Pavel** answered on 24 Mar 2020

Problem is cached javascript file when I use <script src="[https://kendo.cdn.telerik.com/blazor/2.9.0/telerik-blazor.min.js"](https://kendo.cdn.telerik.com/blazor/2.9.0/telerik-blazor.min.js") defer></script> instead of local all works fine.
