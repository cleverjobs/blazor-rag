# Keeping tabstrip when navigating to "edit" pages from a grid in content?

## Question

**Jst** asked on 18 Mar 2023

The content area of my tabs have grid controls on them. I have them configured to go to a detail page when a row is double clicked. When the detail page comes up I lose the tab strip. Is there a strategy or technique for keeping the tabstrip at the top even when navigating from grid to a detail page?

### Response

**Jstemper** commented on 18 Mar 2023

The tabstrip is contained in a component file that I'v created.

## Answer

**Nadezhda Tacheva** answered on 22 Mar 2023

Hi John, As I understand the current scenario, once the user double clicks a Grid row, you are navigating them to another page in the application that contains the item details. Is that correct? If this is the case, the expected framework behavior is to dispose the content of the current page and initialize the content of the new page. This applies to all Blazor components and not just the Telerik ones. If you want to keep the TabStrip, I can suggest displaying the Grid item details in a Window component instead of navigating to a separate page. The Window can be maximized to fill the entire screen for better visibility if needed but the user will still be on the same page. Thus, the TabStrip will not be disposed. An example of a similar configuration is available in the following article: [https://docs.telerik.com/blazor-ui/knowledge-base/grid-rows-text-ellipsis.](https://docs.telerik.com/blazor-ui/knowledge-base/grid-rows-text-ellipsis.) A Window with item details is displayed on a double click of a Grid row. I hope you will find this useful. Please let us know if any further questions arise. Regards, Nadezhda Tacheva Progress Telerik
