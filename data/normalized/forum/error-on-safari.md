# Error on Safari

## Question

**Jos** asked on 13 Apr 2021

When using the new MediaQuery, I am receiving an error on the iPad (Safari) but works fine with desktop and Android. Safari does not have support for addEventListener. warn: Microsoft.AspNetCore.Components.Server.Circuits.RemoteRenderer[100] Unhandled exception rendering component: this.mediaQueryList.addEventListener is not a function. (In 'th is.mediaQueryList.addEventListener("change",this.onMediaChange)', 'this.mediaQueryList.addEventListener' is un defined) value@[https://localhost:5001/_content/Telerik.UI.for.Blazor/js/telerik-blazor.js:59:14905](https://localhost:5001/_content/Telerik.UI.for.Blazor/js/telerik-blazor.js:59:14905) e@[https://localhost:5001/_content/Telerik.UI.for.Blazor/js/telerik-blazor.js:59:14611](https://localhost:5001/_content/Telerik.UI.for.Blazor/js/telerik-blazor.js:59:14611) r@[https://localhost:5001/_content/Telerik.UI.for.Blazor/js/telerik-blazor.js:1:13840](https://localhost:5001/_content/Telerik.UI.for.Blazor/js/telerik-blazor.js:1:13840) r@[https://localhost:5001/_content/Telerik.UI.for.Blazor/js/telerik-blazor.js:59:12983](https://localhost:5001/_content/Telerik.UI.for.Blazor/js/telerik-blazor.js:59:12983) ------------------------------------------------------- I've implemented a rather ugly workaround for now but this should be resolved within Telerik itself. Add this above <script src="_content/Telerik.UI.for.Blazor/js/telerik-blazor.js" defer></script>: <script> var mediaObj=window.matchMedia(""); if (typeof mediaObj.addEventListener !="function") { mediaObj.__proto__.addEventListener=function(event, listener) { mediaObj.addListener(listener); } } </script>

## Answer

**Svetoslav Dimitrov** answered on 16 Apr 2021

Hello Joshua, Thank you for reporting that to us. As a small token of appreciation, I have updated your Telerik Points. I have opened a new Bug Report on your behalf regarding the behavior you are experiencing. I have added your Vote for it and you are automatically subscribed for email notifications on status updates. Regards, Svetoslav Dimitrov
