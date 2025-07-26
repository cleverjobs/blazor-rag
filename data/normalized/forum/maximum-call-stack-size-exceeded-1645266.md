# Maximum call stack size exceeded

## Question

**Dan** asked on 18 Mar 2024

I am getting this error when hosting on our application. It does not appear to happen locally. We are using the new .Net 8 autorender functionality and this seems to happen only in a virtual environment. I can give more context if needed.

## Answer

**Nansi** answered on 21 Mar 2024

Hello Dane, Usually, the Maximum call stack size exceeded error occurs only when using an older component version: [https://www.telerik.com/forums/using-telerik-blazor-4-3-0-for-blazor-8](https://www.telerik.com/forums/using-telerik-blazor-4-3-0-for-blazor-8) [https://www.telerik.com/forums/error-with-blazor-server-net-8-and-telerik-ui-for-blazor-4-4](https://www.telerik.com/forums/error-with-blazor-server-net-8-and-telerik-ui-for-blazor-4-4) If your app is using Telerik UI for Blazor 5.1.1, then clear the browser cache, which will reload the telerik-blazor.js file and see if the error goes away. Also add a cache buster for your end users, which will have the same effect: <script src="_content/Telerik.UI.for.Blazor/js/telerik-blazor.js? version511 "> </script> If the error persists, please send me a stripped runnable version of the app, which reproduces the error. Regards, Nansi Progress Telerik
