# Close Modal window when user clicks off of it

## Question

**Chr** asked on 02 Aug 2021

Hello, I'm trying to figure out a way to trigger an event to close when the Modal window looses focus from the user for example when they click outside of the box. I've looked through the documentation for the window component and although their are keyboard shortcuts such as "ESC" to close the window I couldn't find any events for closing the window based on lose of focus. Any suggestions or assistance with this issue would be great.

### Response

**Blazorist** commented on 02 Aug 2021

Hi Christopher. There was a request about something like that... Here: [https://feedback.telerik.com/blazor/1451714-window-modal-click-on-overlay-to-close?_ga=2.268782450.2060060634.1627913753-1735856614.1611674562&_gac=1.48456338.1627913764.EAIaIQobChMIxZi4usb_8QIVmeyGCh0trwNwEAAYASAAEgK6cfD_BwE](https://feedback.telerik.com/blazor/1451714-window-modal-click-on-overlay-to-close?_ga=2.268782450.2060060634.1627913753-1735856614.1611674562&_gac=1.48456338.1627913764.EAIaIQobChMIxZi4usb_8QIVmeyGCh0trwNwEAAYASAAEgK6cfD_BwE) There is an example attached with a workaround to achieve what you need. Hope that help at least as inspiration. Blazorist.

## Answer

**Blazorist** answered on 02 Feb 2022

Hi Christopher. Since version 2.30.0 there is a configuration parameter "CloseOnOverlayClik". Set it to true and this will do exactly what you want. <TelerikWindow Modal="true" Width="35%" Height="40%" Visible="@IsVisible" CloseOnOverlayClick="true"> <WindowTitle> <!-- your window title --> </WindowTitle> <WindowContent> </WindowContent> <!-- your content here --> <WindowActions> <WindowAction Name="Close" OnClick="@(_=> Close())" /> </WindowActions> </TelerikWindow>
