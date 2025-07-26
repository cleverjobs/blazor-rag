# Incell editing and OnRead event

## Question

**Gre** asked on 18 Jan 2022

Hello - I wish to implement both inline editing and server-side paging. My use case is: User searches for data and gets the first page of X records out of Y total. User makes a few changes to a few data rows. Toolbar detects the change and displays buttons to save or cancel. If user attempts to page - they are challenged / prevented from paging until the changes are saved or cancelled. My problem is that OnRead fires immediately after selecting a different field to edit. My OnRead handler fetches the requested next page of data - therefore wiping out the pending changes. How can I prevent the OnRead event from firing when I'm just poking around on a single page of records? Thanks! -Greg

### Response

**Gregory** commented on 18 Jan 2022

Not sure if there is any other preferable way to do this, but what I did to solve this was to: Save args values in a variable or object. Everytime OnRead fires off I then compare the args to what I previously stored. If the values are the same between OnRead events, I can assume that the user is still on the same page. If they are different, I can then fetch the requested page of data and then save the new args values.

## Answer

**Svetoslav Dimitrov** answered on 21 Jan 2022

Hello Gregory, I am happy to report that this might be indeed the most preferable way to achieve the desired functionality. The other possibilities would require usage of most of the Grid events and a lot more custom code. Regards, Svetoslav Dimitrov
