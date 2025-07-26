# Missing low-level API on charts

## Question

**Hei** asked on 08 Feb 2023

I am just creating an application with Blazor using Telerik UI for Blazor. It seems that a few properties and methods from former ASP.NET Core version are missing, at least: SeriesDefaults no more "xxx.visual" "OnRender" event Especially the "visual" function and the "OnRender" event among other low-level API is sorely missed since I have to draw additional things on the charts. Can anyone give me a tip on how to do the same thing with Blazor? Thanks in advance! Heiko

## Answer

**Svetoslav Dimitrov** answered on 13 Feb 2023

Hello Heiko, I have added two feature requests to your behavior: Add the SeriesDefaults configuration Expose an OnRender event I have added your Vote for both of them and you are automatically subscribed to receive email notifications on status updates. The Chart Series Visuals are already an existing feature request - Custom rendering for series element - visual template. Your Vote is already in and you can click the Follow button to receive email notifications on status updates. Regards, Svetoslav Dimitrov

### Response

**Heiko** commented on 15 Feb 2023

Hello Svetoslav, thank you for adding these as feature requests, it is very much appreciated! Do you know a way to accomplish changes to a chart during or after render? I have to put a line with a small text on a stacked bar at a certain position. Regards Heiko

### Response

**Svetoslav Dimitrov** commented on 17 Feb 2023

Hello Heiko, Drawing Horizontal and vertical lines on the Chart is a planned feature request. In the public thread, you can see how to achieve the desired behavior until the official feature is implemented. I have added your Vote for the request and you can click the Follow button to receive email notifications on status updates.
