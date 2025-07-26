# command buttons disappear

## Question

**Ric** asked on 21 Jun 2019

Clicking a command button on my grid and running the code the handler contains causes all command buttons in that row to disappear. Refreshing the page makes them reappear. Perhaps I am not using it correctly. <TelerikGridCommandButton Command="Edit" OnClick="@OpenRequestEditWindow" Icon="edit">Edit</TelerikGridCommandButton> <TelerikGridCommandButton Command="Delete" OnClick="@DeleteRequestItem" Icon="delete">Delete</TelerikGridCommandButton> Clicking the "Edit" button opens a window with controls on it. User edits the values in the controls and has a save button <TelerikButton Icon="save" OnClick="@UpdateRequest">Save Purchase Request</TelerikButton><br /><br /> This event simply writes to the database and then rebinds the grid data. var grid=await service.GetRequests(); RequestAddGrid=grid.ToList();

## Answer

**Rick** answered on 21 Jun 2019

It looks like this was because of what i was naming the command, "Edit". Changed the command name and it's fine.

### Response

**Marin Bratanov** answered on 24 Jun 2019

Hi Rick, If you have those buttons in a command column, then firing the Edit or Delete commands have definitive meaning of their own in the grid, and you must, indeed, use different names for custom commands. Regards, Marin Bratanov

### Response

**Rob** commented on 30 Jan 2025

Hi Marin, I'm having a similar issue, all my GridCommandColum with GridCommandButton and the buttons will disappear as soon as I enter into cell edit (InCell). I tried renaming the Command="someotheredit" and the problems persists, all buttons disappear as soon as I enter into cell edit on the grid. Rob.

### Response

**Dimo** commented on 30 Jan 2025

@Rob - command buttons are visible either in display mode, or in edit mode, but not in both cases. This depends on the ShowInEdit parameter. If you need a command to be always usable, then you will need two command buttons.
