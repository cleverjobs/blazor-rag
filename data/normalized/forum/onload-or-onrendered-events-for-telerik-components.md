# OnLoad or OnRendered events for Telerik Components?

## Question

**Joh** asked on 26 Nov 2023

I'm in need for an OnRendered event (or similar) for a TelerikWindow component. Actually, it would be nice to have for all Telerik blazor components. I this particular case I need to know when a specific <div> is avaible to the browser DOM so that I can call some javascript interop on it. In this case I need to show I leaflet map in the modal window. I solved it for now, using a javascript timeout of 0.1 second, but that is bad coding.

## Answer

**Dimo** answered on 28 Nov 2023

Hello Johan, Blazor doesn't provide such events natively and our components don't know when they have rendered either (except for the components with client-side rendering such as the Charts). So if we should expose such events, we need to do the same bad coding in the product itself. The coding may even be worse, because we will aim for more reliability and universal applicability. When I have a similar task, my usual approach is: Raise a boolean flag in the Razor component, for example where you are showing the Window. Check and reset the flag value in OnAfterRenderAsync, execute a short Task.Delay() and then call the JavaScript. Depending on the exact situation, I may use setTimeout in the JavaScript as well. Here is a REPL example. Regards, Dimo Progress Telerik
