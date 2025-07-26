# Editor - How to put the "Alignment" buttons into a dropdownlist in the toolbar

## Question

**Pau** asked on 11 Apr 2024

I'd like to move all of the Alignment buttons (along with indent and outdent) into a dropdownlist in the toolbar, so they won't take up as much space. I've tried adding my own custom dropdownlist, but the items I put in it did nothing. Is there a way to accomplish this?

## Answer

**Dimo** answered on 12 Apr 2024

Hi Paul, You can programmatically execute Editor commands that correspond to built-in ailgnment tools. Do this in the ValueChanged or OnChange events of the DropDownList. However, with this approach users won't see the current alignment in the DropDownList when they navigate across the Editor content. They will either see the last selected alignment, or nothing (depending on how you implement the DropDownList event). Regards, Dimo Progress Telerik
