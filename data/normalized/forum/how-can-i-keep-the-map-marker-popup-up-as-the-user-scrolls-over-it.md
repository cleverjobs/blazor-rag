# How can I keep the Map Marker popup up as the user scrolls over it

## Question

**Dav** asked on 24 Feb 2024

Hi all; This is on Blazor server side (running on .Net 8, but using the old ver 6 server side). First off, is this the right approach? I have a map marker up and it has a `MapLayerMarkerSettingsTooltip` that has some information - including a link and a clickable razor component. But if I move the mouse to the tooltip, when it leaves the marker it goes away. 1. Is this the right approach? Or should the tooltip be static text and they have to click the marker, and on the click I popup an overlay dialog? 2. If this is the right approach, how do I get the tooltip to stay up? thanks- dave ps - This was incredibly easy to get running. Kudos to the dev team that created this and the documentationt eam that wrote it up.

## Answer

**Nadezhda Tacheva** answered on 26 Feb 2024

Hi David, Thank you for your input! I am glad that you were able to easily set up the Map component. As I understand, you want to allow the user to interact with the marker tooltip - you've mentioned that you have included a link and a clickable razor component in it. In this case, I would recommend a different approach. The current behavior is expected considering the component design. By default, the tooltip is shown upon hovering the markers. Thus, as soon as the mouse leaves the tooltip target (the marker), the tooltip is hidden. While this is expected behavior, in this scenario, the user will never be able to interact with the content of the tooltip. A potential solution would be to show the tooltip on click of the marker instead of on hover. This is currently not supported but I opened a feature request for it on your behalf: Show marker tooltip on click instead of on hover. I added your vote there and as a creator, you are automatically subscribed to get status updates. Regards, Nadezhda Tacheva Progress Telerik
