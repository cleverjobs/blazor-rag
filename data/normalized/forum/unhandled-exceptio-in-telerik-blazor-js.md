# Unhandled exceptio in telerik-blazor.js

## Question

**Ali** asked on 10 Apr 2025

I have a Blazor server application that has worked well for a long time. Recently my computer crashed and I have to reinstall Windows, Visual Studio and so on. After that, as I want to imporve my application, I encounter an unhandled exception in telerik-blazor.js randomly, regardless of which component is called or what is the user's behavior. The exception is as follows in attached image I Used Telerik.UI.for.Blazor 5.1.1 in this project as DLLs ans staticwebassets instead of nuget packages. I tried to reinstall nuget packages but that did not help me. Can somone please help me with this or have an Idea?

## Answer

**Dimo** answered on 10 Apr 2025

Hi Alireza, This error occurs in the Telerik Blazor Tooltip and it was fixed in Telerik UI for Blazor version 8.0.0. Please consider upgrading. Regards, Dimo

### Response

**Alireza** answered on 10 Apr 2025

Hi Dimo, Thanks a lot for your replay. Before I try to update my Telerik version, I'm interested in why I haven't experienced a problem like this in a long time. I've attached another test screenshot, which is slightly different from the last one. It might help to find out if the problem is actually related to the tooltip error. From your point of view, is it also based on the same problem? Thanks again. Best regards, Alireza

### Response

**Alireza** commented on 10 Apr 2025

Hier is the detail info related to the last test: Nachricht=Quelle=Stapelüberwachung: at HTMLHtmlElement.onMouseEnter ([https://localhost:44393/_content/Telerik.UI.for.Blazor/js/telerik-blazor.js:50:1397719)](https://localhost:44393/_content/Telerik.UI.for.Blazor/js/telerik-blazor.js:50:1397719))

### Response

**Dimo** commented on 11 Apr 2025

>> why I haven't experienced a problem like this in a long time. The error does not always occur and depends on: Visual Studio must run the app in debug mode. The user must move the mouse during page load before the Tooltip is initialized completely.
