# Grid single selection mode is set, but certain rows when clicked will add the "k-selected" class to other rows. Has anyone else experienced this?

## Question

**Wil** asked on 14 May 2025

There is a known issue where the previously selected row will stay selected. That's not what I'm seeing. My issue is seemingly random but consistent. Clicking certain rows will always apply "K-selected" to the same extra rows, and selecting any one of the highlighted rows will also highlight the same set of rows. There doesn't seem to be any connection in the data between the rows, and the "selected items" object is correctly holding the proper selected item and no others. Has anyone else seen anything similar? Thank you! It would be difficult to provide you with working code, but the attached video shows my issue.

## Answer

**Dimo** answered on 15 May 2025

Hello Will, The observed behavior suggests a possible problem with: data item instances (object references) (e.g. Equals () override) custom business logic (e.g. in SelectedItemsChanged ) incorrect usage of two-way parameter binding in a parent-child component scenario We will need an isolated runnable example to troubleshoot further. Regards, Dimo Progress Telerik

### Response

**Will** commented on 15 May 2025

Dimo, Thank you so much! It was in fact an Equals() override that I had completely forgotten about. I don't know if I ever would have figured that one out. Seriously thank you!
