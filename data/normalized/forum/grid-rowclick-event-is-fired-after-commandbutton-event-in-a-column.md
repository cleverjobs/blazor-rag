# Grid RowClick event is fired AFTER CommandButton event in a column?

## Question

**RobRob** asked on 01 Feb 2025

Grid EditMode=InCell. Grid SelectionMode="GridSelectionMode.Single" SelectedItems="mySelectedItems" I have a command button in one of my Grid columns. I have OnRowClick handler for the Grid. I have GridCommandColum with GridCommandButton and a OnClick command handler. The grid populates with data, no row currently selected. User clicks on the GridCommandButton and that event gets fired BEFORE the OnRowClick event. Logically this is not correct as the button is contained within the parent which is the Grid, so the OnRowClick should fire first before the OnClick for command button ... I have no way to work around this issue? UPDATE: correction, the OnRowClick event doesn't fire at all if I click on a GridCommandButton.

## Answer

**Dimo** answered on 03 Feb 2025

Hi Rob, The observed behavior is by design and documented: Grid OnRowClick documentation. If you need to execute the OnRowClick logic on command button click, please do that in the OnClick handler. The command button's OnClick handler should provide enough information to do so. Regards, Dimo Progress Telerik

### Response

**Rob** commented on 03 Feb 2025

Hi Dimo, Thanks, for some reason I didn't include the event args in the handler, add args ... all good. Sorry. Rob.
