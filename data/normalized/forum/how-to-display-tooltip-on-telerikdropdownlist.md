# How to display tooltip on TelerikDropDownList

## Question

**Mar** asked on 09 Aug 2024

Hi, I have the need to display a tooltip when my TelerikDropDownList is in error mode (css class='change-local-dropdown error'). However the tooltip does not show anything and when inspecting the TelerikDropDownList, no html element in the TelerikDropDownList tree has a 'title' property set. This despite me explicitly setting the Title property, as can be seen in the code below. Here's my code <TelerikTooltip TargetSelector=".change-local-dropdown.error" /> <TelerikDropDownList Data="@Zones" AdaptiveMode="@AdaptiveMode.Auto" Class="@(string.IsNullOrEmpty(_zoneError) ? " change-local-dropdown ": " change-local-dropdown error ")"
@bind-Value="@SelectedZoneGuid" TextField="@nameof(Zone.Name)" ValueField="@nameof(Zone.Guid)" Title="My tooltip that I want to display, but it isn't showing up" Width="100%"> </TelerikDropDownList> Any help is greatly appreciated...

## Answer

**Dimo** answered on 12 Aug 2024

Hi Marcin, The DropDownList Title parameter has a different purpose. In your case, you need a Template to define the Tooltip content. Regards, Dimo
