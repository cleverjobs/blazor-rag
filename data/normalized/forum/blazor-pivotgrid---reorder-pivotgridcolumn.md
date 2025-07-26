# Blazor PivotGrid - reorder PivotGridColumn?

## Question

**Mik** asked on 23 Jul 2024

Hi, I have a PivotGridColumn: <PivotGridColumns> <PivotGridColumn Name="@nameof(PivotIpEncounterDetail.Year)"> </PivotGridColumn> </PivotGridColumns> And I have the data loaded in for the pivot grid in reverse year order (example 2022, 2021, 2020), but when I go to test the grid the columns are reordered in ascending order. By design, I'm not allowed to add extra complexity of the configurator, as our users will only be shown one specific view with an optional aggregation. What can I leverage to get the columns in the correct order? Edited to add details: Using a Local DataProviderType, 2 PivotGridRows, 1 PivotGridMeasure (Sum). All the internal guts of the grid itself are fine (numbers are where they should be, etc.), Just can't seem to reorder the year columns programatically.

## Answer

**Nansi** answered on 26 Jul 2024

Hi Mike, When the field is of a type int, the order is ascending. This is the expected and current ordering behavior. It will be possible to programmatically control the order once the PivotGrid exposes a state management functionality. I have added your vote for this feature request. You can click the Follow button to receive email notifications on status updates. Currently, the Configurator allows the user to order the columns, but you said that this is not desired in your scenario. Regards, Nansi
