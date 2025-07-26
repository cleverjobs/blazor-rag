# Hiding markers from charts

## Question

**Emi** asked on 13 Dec 2022

Is there a way to hide/remove markers from chart, so they also dont appear on hover. When setting visible on ChartSeriesMarker to false, the marker is hidden but will still show up when hovering. Best Regards, Emil

## Answer

**Nadezhda Tacheva** answered on 16 Dec 2022

Hi Emil, You are correct, when the Visible parameter of the ChartSeriesMarkers is set to false, the markers will not be displayed. However, by design, when the user hovers the series, the markers are rendered, so there is still some indication for the value points. I can suggest a custom configuration of the markers, so they are not visible on hover. Here is a runnable sample demonstrating the approach: [https://blazorrepl.telerik.com/wmFQvAOj06sOjLCO42.](https://blazorrepl.telerik.com/wmFQvAOj06sOjLCO42.) I hope this will help you move forward with your application. Please let us know if any other questions appear. Regards, Nadezhda Tacheva Progress Telerik
