# Grid Menu filter - copy paste not working

## Question

**WimWim** asked on 23 May 2022

The copy paste functionality is not working when I use the menu filter for a numeric value. This does also not work for the demo on [https://demos.telerik.com/blazor-ui/grid/filter-menu](https://demos.telerik.com/blazor-ui/grid/filter-menu)

## Answer

**Tsvetomir** answered on 25 May 2022

Hi Wim, Indeed, pasting a value from Excel is not correctly parsed and applied to the NumericTextBox. This is due to the fact that the value from the clipboard carries additional characters that make the value invalid for the component. The defect is already fixed and will be available with Telerik UI for Blazor 3.4.0 version expected in late June. [https://feedback.telerik.com/blazor/1565272-cannot-paste-number-from-excel-into-numerictextbox](https://feedback.telerik.com/blazor/1565272-cannot-paste-number-from-excel-into-numerictextbox) Let me know if there is anything else I can help with. Kind regards, Tsvetomir Progress Telerik
