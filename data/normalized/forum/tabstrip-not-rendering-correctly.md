# Tabstrip not rendering correctly

## Question

**Ste** asked on 09 Mar 2023

I am using Blazor UI. Tabstrip was working, but suddenly now they are stacked on top of each other. Attached is what the tabstrip looks like. There are 3 tabs (TOP/HORIZONTAL). The UI still responds but isn't desirable. What is causing this issue? Is this related to licensing?

## Answer

**Yanislav** answered on 13 Mar 2023

Hello Steve, What I can suggest is to check the imported CSS files and look for any custom CSS that may be overriding the default styles. This can often cause issues with the layout and appearance of the components. Please ensure that you have not made any changes to the default theme file that could be causing the issue. Also, if you are using CDN to import the theme file check its version. Its version should match the version of the Telerik UI for Blazor package. <link rel="stylesheet" href="[https://blazor.cdn.telerik.com/blazor/](https://blazor.cdn.telerik.com/blazor/) 4.0.1/ kendo-theme-default/all.css" /> Another possible reason if the application type is Blazor WASM is caching the theme file. In this case, you have to hard reload the page to clear the cache (CTRL + F5). If you are still unable to find the cause of the problem, may I ask you to reproduce the problem in a sample application and send it to us for review? Thus we will be able to investigate the problem and further troubleshoot it. Regards, Yanislav
