# One Popover for page, serving multiple anchors

## Question

**Kei** asked on 28 Oct 2024

I have a page with a collection of cards of client data. I want to invoke a TelerikPopover when a particular status field is clicked in a given card, but the popover would be populated with the unique status string for that client card. This almost works. However, even though I populate the string with the unique status for the current card, I get multiple popovers, on top of one another, containing values from other cards that I've clicked on previously. The Popover is defined like this : <TelerikPopover @ref="@PopoverRef" AnimationType="@AnimationType.Fade" AnchorSelector=".client-card-abar" ShowOn="PopoverShowOn.Click" Collision="@PopoverCollision.Flip" Position="@PopoverPosition.Bottom"> <PopoverHeader> Alerts </PopoverHeader> <PopoverContent> <div> @((MarkupString)statusText) </div> </PopoverContent> </TelerikPopover> And the value of statusText is being correctly set prior to displaying the popup, thusly: private void BeforeOpenPopover(int pid) { var txt=AlertText[pid]; statusText=txt + "<br />"; PopoverRef.Refresh(); } Is there a fundamental reason that using one TelerikPopover for the page will not work? I don't really want the "weight" of a seperate Popover control for every card if possible. Thanks.

## Answer

**Dimo** answered on 31 Oct 2024

Hi Keith, Here is a possible approach that you can use currently: [https://blazorrepl.telerik.com/cylORPYN24OduqpI16](https://blazorrepl.telerik.com/cylORPYN24OduqpI16) Due to an existing bug, the Popover cannot handle runtime AnchorSelector changes properly. This brings the need to recreate the component and show it programmatically. If there is no need to open a new Popover while the old one is still visible, the code can be simplified: [https://blazorrepl.telerik.com/cIbOHPuX351Luukm51](https://blazorrepl.telerik.com/cIbOHPuX351Luukm51) Regards, Dimo Progress Telerik
