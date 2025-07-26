# TreeView with checkboxes: Initial value for parent nodes

## Question

**Ray** asked on 18 Jul 2024

Hi, I have a TreeView where the initial values are set programmatically. When all the child nodes are checked the parent node should be checked as well. But it isn't: [https://blazorrepl.telerik.com/GIOLlWks03IKIiiZ31](https://blazorrepl.telerik.com/GIOLlWks03IKIiiZ31) Is there any solution for that? Best regards, Rayko

## Answer

**Dimo** answered on 19 Jul 2024

Hello Rayko, CheckParents="@true" and CheckChildren="@true" define how the TreeView reacts to user behavior. When checking and unchecking items programmatically, you need to handle all parents and children explicitly. Regards, Dimo

### Response

**Rayko** commented on 19 Jul 2024

Hi Dimo, but why is the parent set to intermediate state once one ore more children are not checked? There it is set automatically. So I thought it should be also handled for the other states as well. Best regards, Rayko

### Response

**Dimo** commented on 19 Jul 2024

The indeterminate state is only a visual indication for the user. Indeterminate items are not present in @bind-CheckedItems="@SelectedItems". There are two reasons why we don't check and uncheck items automatically during programmatic operations: In this way we give full control and more flexibility to the app and the developer. If we managed the checked items automatically in this case, this may be limiting to you. It is a general best practice for UI components not to interfere or override programmatic operations on them.
