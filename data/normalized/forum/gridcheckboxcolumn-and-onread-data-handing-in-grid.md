# GridCheckBoxColumn and OnRead data handing in Grid

## Question

**RobRob** asked on 21 Nov 2022

Hi, I'm having trouble getting a GridCheckBoxColumn to remember what was checked on page 1 of a grid, if I switch to page 2 and then back to page 1. I can't tell from the documentation if this is expected behavior or not. Does anyone else know if I need to write custom code here? Rob

### Response

**Rob** commented on 22 Nov 2022

Additional. I can go to this documentation page [https://docs.telerik.com/blazor-ui/components/grid/manual-operations](https://docs.telerik.com/blazor-ui/components/grid/manual-operations) and edit the REPL I can then add this column. <GridCheckboxColumn SelectAll="false" Width="70px" ShowColumnMenu="@false" /> Selected rows on page one do not remain selected when you swap to page 2 and back. :(

## Answer

**Dimo** answered on 24 Nov 2022

Hello Rob, I assume that the Grid is data bound via OnRead event? This may cause the data item instances to be different when you return to a previously visited page, even if the values are the same. As a result, the default Equals comparison of the model class returns false and the selection cannot be persisted. To resolve this behavior, override the Equals method of the model class and compare data items by their ID. Note that the SelectAllMode behavior is different when using Data parameter and OnRead event. With OnRead, users always select_all rows from the current page only. Regards, Dimo

### Response

**Rob** commented on 24 Nov 2022

Thank you so much for this suggestion, it explains a lot of what I was missing and works really well.
