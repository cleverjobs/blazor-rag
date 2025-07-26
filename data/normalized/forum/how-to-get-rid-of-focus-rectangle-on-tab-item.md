# How to get rid of focus rectangle on tab item

## Question

**Mar** asked on 02 Apr 2024

Afternoon, I've attached a picture for it describes the problem best. After clicking on a tab item (Blazor UI) there is a "focus rectangle" around the tab. How can I make sure that this rectangle never shows, that is, clicking on the tab should simply select the tab and not paint the rectangle. To my surprise the following didn't work: ::deep .k-active:active{ outline: none!important;
}
::deep .k-active:focus{ outline: none!important;
}

## Answer

**Hristian Stefanov** answered on 03 Apr 2024

Hi Marcin, To change the current tab style and remove the border, override the " box-shadow " of the CSS rule. I have prepared an example for you: <style>.k-tabstrip-item.k-item:focus { box-shadow: none;
} </style> <TelerikTabStrip TabPosition="Telerik.Blazor.TabPosition.Left"> <TabStripTab Title="First"> First tab content. </TabStripTab> <TabStripTab Title="Second"> Second tab content. This tab is disabled and you cannot select it. </TabStripTab> <TabStripTab Title="Third"> Third tab content. </TabStripTab> </TelerikTabStrip> I hope this helps. Let me know if you are still facing difficulties. Regards, Hristian Stefanov Progress Telerik

### Response

**Marcin** commented on 03 Apr 2024

It worked perfectly, much thanks Hristian.
