# Disabling a TelerikgridCheckboxColumn on data load

## Question

**Afr** asked on 17 Apr 2023

Hi, I am using telerikgrid control to display the employees information. I have telerikgridcheckboxcolumn which is bind to a IEnumerable list of employee who are eligible for promotion. I am looking for a solution to disable this header checkbox when there is none of the employee is eligible for promotion. Please see below my code snippet for Grid and Checkbox: <TelerikGrid Data="ShipmentInfo" SelectionMode="GridSelectionMode.Multiple" SelectedItems="SelectedEmployees" Class="grid-no-scroll" Sortable="true" Size="Telerik.Blazor.ThemeConstants.Grid.Size.Medium" Resizable="true" Pageable="false" Height="55vh" ScrollMode="GridScrollMode.Scrollable" FilterMode="GridFilterMode.None" OnRowRender="@OnRowRenderHandler" SelectedItemsChanged="@((IEnumerable<EmployeeInfoDto> employeess)=> SelectedItemsChanged(employees))"> <GridCheckboxColumn Title="Allow Promotion" SelectAll="true" CheckBoxOnlySelection="true" HeaderClass="@GetHeaderCssClass()"></GridCheckboxColumn> private void SelectedItemsChanged(IEnumerable<EmployeeInfoDto> employees) { // Checkboxes are disabled for shipments that aren't allowed to be routed but we don't want the select all function to select unroutable shipments // so remove any unroutable shipments from the given collection and set that to the SelectedItems collection SelectedEmployees=employeess.Where(s=> s.EligibleForPromotion).ToList(); } Please can you help get my desired requirement. Thanks & regards, Afreen

## Answer

**Hristian Stefanov** answered on 20 Apr 2023

Hi Afreen, I have already provided information that gives a solution to this question in the following public post: Disabling the header level TelerikGridCheckboxColumn. If there are still difficulties or if I'm missing something, I'm at your disposal to keep the conversation there so it is all in one place. Regards, Hristian Stefanov Progress Telerik
