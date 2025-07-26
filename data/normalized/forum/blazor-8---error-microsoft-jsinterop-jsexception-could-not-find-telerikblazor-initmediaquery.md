# Blazor 8 - Error: Microsoft.JSInterop.JSException: Could not find 'TelerikBlazor.initMediaQuery'

## Question

**Geo** asked on 12 Apr 2024

Hello, I have followed the Blazor 8 Getting started instructions but am getting the error Error: Microsoft.JSInterop.JSException: Could not find 'TelerikBlazor.initMediaQuery'. I have double checked that the <script src="_content/Telerik.UI.for.Blazor/js/telerik-blazor.js"></script> is in the <head> of the app.razor i have double checked that the builder.Services.AddTelerikBlazor(); is in the program.cs and I have the <TelerikRootComponent> @Body </TelerikRootComponent> in the root layout component MainLayout.razor. This error causes my stylesheets not to load. Occasionally the page will load with the stylesheets, but if a clear the cache or do a CTRL-SHIFT-R, I will get the error and my styles will unload. HALP!

### Response

**James** commented on 13 Jun 2024

I am starting to get this error intermittently on several existing Telerik Blazor Server apps. It happens on load, but doesn't happen every time. I haven't tracked down the issue yet. Error: Microsoft.JSInterop.JSException: Could not find 'TelerikBlazor.initMediaQuery' ('TelerikBlazor' was undefined).

### Response

**James** commented on 13 Jun 2024

My issue was probably due to network congestion and the telerik-blazor.js file not getting loaded in time to be referenced. I think I have resolved my issue by delaying Blazor.Start() until the telerik-blazor.js file is loaded per the instructions here -> [https://docs.telerik.com/blazor-ui/troubleshooting/js-errors](https://docs.telerik.com/blazor-ui/troubleshooting/js-errors) [https://docs.telerik.com/blazor-ui/getting-started/what-you-need#javascript-file](https://docs.telerik.com/blazor-ui/getting-started/what-you-need#javascript-file)
