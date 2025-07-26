# Dropdown in Command Column with Row Select

## Question

**Kel** asked on 22 Mar 2020

I would like to have a dropdown in the CommandColumn (or a column that is editable), but still be able to select the row from one of the other non-editable columns. This is for an action like setting the state of the record (completed, in-work, etc.), placing it in-line edit, or even deleting. It seems that you can have one or the other; in-cell editing, or row select. Am I missing something here? Maybe Templates in a CommandColumn would be the solution?

## Answer

**Marin Bratanov** answered on 23 Mar 2020

Hello Kelly, With InCell editing, the click action would be ambigious - either a cell should be opened, or the row selected. This is why in this mode a checkbox column is to be used: [https://docs.telerik.com/blazor-ui/components/grid/selection/overview#notes](https://docs.telerik.com/blazor-ui/components/grid/selection/overview#notes) As for a dropdown for editing - you can use an editor template: [https://docs.telerik.com/blazor-ui/components/grid/templates#edit-template](https://docs.telerik.com/blazor-ui/components/grid/templates#edit-template) Regards, Marin Bratanov
