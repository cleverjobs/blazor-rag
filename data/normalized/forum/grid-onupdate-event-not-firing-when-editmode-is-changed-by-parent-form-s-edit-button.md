# Grid OnUpdate event not firing when EditMode is changed by parent form's Edit button

## Question

**Sha** asked on 19 Mar 2024

I have a form with an edit button and a grid. The EditMode property of the grid is set to a reference variable named @GridEditModeValue which has an initial value on page load of GridEditMode.None. When I press the Edit button of the Form, in the OnClick handler I set @GridEditModeValue=GridEditMode.Incell. This allows me to click into the cells of the grid and make changes to their values, however when i click out of the cell to another part of the form or to click the Submit button of the form, the OnUpdate event doesn't seem to fire and the changes are lost. If I click into a different cell of the grid, the event does fire and the event handler is executed correctly. Is there any way to have this event fire when the cell loses focus in this case?

## Answer

**Dimo** answered on 21 Mar 2024

Hello Shawn, I think the Grid is not fully capable of changing its EditMode on the fly like this. I will consult the team and probably log a bug. In the meantime, please use another approach: Enable Grid editing unconditionally. Cancel the OnAdd and OnEdit events when the Grid is in "read-only" mode. Another option is to hide and show the Grid when you toggle its EditMode parameter. This will recreate the component with the correct settings, but the user may see a flicker. Regards, Dimo Progress Telerik
