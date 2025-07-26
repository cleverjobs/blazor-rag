# NET MAUI Blazor Hybrid App on Android < v32 in .net 8

## Question

**Mat** asked on 24 Feb 2024

As long as I use an API version> 31, everything works. But older versions won't start. Any ideas? Once I use <TelerikRootComponent> in the layout, the application stops working. Could not find TelerikBlazor.getLocationHost
('TelerikBlazor' was undefined). Error: Could not find
'TelerikBlazor.getLocationHost' ('TelerikBlazor' was
undefined). at
[https://0.0.0.0/_framework/blazor.webview.js:1:540...](https://0.0.0.0/_framework/blazor.webview.js:1:540...)

## Answer

**Svetoslav Dimitrov** answered on 27 Feb 2024

Hello Matthias, Telerik UI for Blazor supports only the latest version of all browsers. An old Android emulator most likely means an old version of the WebView which is a "browser that does not look like one". I would suggest that you update the WebView of your emulator which should solve the issue. Regards, Svetoslav Dimitrov Progress Telerik

### Response

**Matthias** commented on 01 Mar 2024

Thank you!
