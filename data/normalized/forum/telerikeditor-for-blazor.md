# TelerikEditor for Blazor

## Question

**Pay** asked on 08 Apr 2024

We are using Azure SignalR for our server side Websocket connection. When I try to update the Value of the TelerekEditor component, either via data binding or directly setting the Value property, the TelerikEditor is never updated in the browser. Is using Azure SignalR a supported scenario for the Telerik Blazor components, other components such as TelerikDropDownList are working fine.

## Answer

**Svetoslav Dimitrov** answered on 11 Apr 2024

Hello Payton, My best guess is that the Message Size of the Azure SignalR is not high enough. Sometimes, the content of the Editor can be large and the message size needs to be increased. Regards, Svetoslav Dimitrov Progress Telerik
