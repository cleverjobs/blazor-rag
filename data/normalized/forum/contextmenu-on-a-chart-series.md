# ContextMenu on a chart series

## Question

**Ada** asked on 04 Mar 2021

Hi I would like to bring up a ContextMenu component for a Chart OnSeriesClick event so e.g. the user can click on a chart series and be presented with options. I am able to do this by e.g. having a OnSeriesClick handler method that invokes ContextMenu.ShowAsync to show the ContextMenu - the problem is that ShowAsync requires the X/Y coordinates from the mouse click and the OnSeriesClickEventArgs class does not provide mouse coordinates so i cannot show the context menu in the right place. Any ideas how this could be accomplished? Thanks Adam

## Answer

**Stamo Gochev** answered on 05 Mar 2021

Hi, The built-in functionality of the ContextMenu can be used with the Chart directly by setting the "Selector" property: <TelerikChart Class="chart-selector"...> </TelerikChart> <TelerikContextMenu Selector=".chart-selector"...> </TelerikContextMenu> This will show the context menu without a need for managing its position manually (note it doesn't expose settings for configuring the position). On the other hand, if you need to display a popup menu with a click on the series, this can be achieved by wrapping the chart in an HTML element and handling "onclick" (or even "oncontextmenu") events: <div @onclick="@OnClick" @oncontextmenu="@OnContextMenu"> <TelerikChart...> </TelerikChart> </div> and use the position that is exposed in the "MouseEventArgs": public void OnClick ( MouseEventArgs args ) {
Console.WriteLine( args.ClientX);
} public void OnContextMenu ( MouseEventArgs args ) {
Console.WriteLine( args.ClientX );
} to get the coordinates and display information in a customized context menu. Regards, Stamo Gochev

### Response

**Adam** answered on 08 Mar 2021

Thanks Stamo, this has helped.
