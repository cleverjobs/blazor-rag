# Custom Filter along with Default filter

## Question

**Dav** asked on 18 Jul 2025

I’m trying to build a custom filter for a column in the Telerik Grid. I’d like to have both the custom filter and the default filter available in the column's filter menu. I’ve managed to get the custom filter displaying and working correctly, but the default filter is not appearing in the filter menu for that column. I’ve attached the code — could you please help me figure out what’s missing or incorrect? Many Thanks <GridColumn Field="@nameof(StockVehicleRowDTO.PerformanceGrading)" Title="Grade" Lockable="true" TextAlign="@ColumnTextAlign.Center" Locked="true" Width="120px" Filterable="true"> <FilterMenuTemplate Context="context"> <div class="p-2"> <!-- Default Telerik Filter Menu --> <TelerikGridFilterMenu Context="context" /> <hr /> <!-- Custom Checkbox Filter --> <div> <strong>Quick Grade Filter:</strong> @foreach (var grade in GradeFilterOptions) { <div> <TelerikCheckBox Value="@(IsGradeChecked(context.FilterDescriptor, grade))" ValueChanged="@((bool value)=> OnGradeFilterChanged(value, grade, context.FilterDescriptor))" Id="@($"grade_{grade}")"> </TelerikCheckBox> <label for="@($"grade_{grade}")">@grade</label> </div> } </div> </div> </FilterMenuTemplate> <Template> @{ var vehicleRow=(context as DDD.Application.Vehicles.ViewModels.StockVehicleRowDTO); var grade=vehicleRow?.PerformanceGrading; } <GradeChip Grade="@grade" /> </Template> </GridColumn> Backend code.. // Grade filter options for the filter menu (dynamic from data) public List<string> GradeFilterOptions=> StockPageVehicles?.ActiveVehicles .Select(v=> v.PerformanceGrading) .Distinct() .OrderBy(g=> g) .Select(g=> g.ToString()) .ToList() ?? new List<string>(); // Helper to check if a grade is selected in the filter descriptor public bool IsGradeChecked(CompositeFilterDescriptor filterDescriptor, string grade) { return filterDescriptor.FilterDescriptors.Any(f=> (f as FilterDescriptor)?.Value?.ToString()==grade); } // Handler for checkbox changes in the Grade filter menu public void OnGradeFilterChanged(bool value, string grade, CompositeFilterDescriptor filterDescriptor) { var filter=filterDescriptor.FilterDescriptors.FirstOrDefault(f=> (f as FilterDescriptor)?.Value?.ToString()==grade); filterDescriptor.LogicalOperator=FilterCompositionLogicalOperator.Or; int gradeInt; if (!int.TryParse(grade, out gradeInt)) return; if (value && filter==null) { filterDescriptor.FilterDescriptors.Add(new FilterDescriptor(nameof(StockVehicleRowDTO.PerformanceGrading), FilterOperator.IsEqualTo, gradeInt)); } else if (!value && filter !=null) { filterDescriptor.FilterDescriptors.Remove(filter); } }

## Answer

**Ivan Danchev** answered on 22 Jul 2025

Hello, This was resolved in a support ticket, but I'll post more details here as well, in case someone from the community stumbles upon a similar scenario. There is currently no built-in way to use FilterMenuTemplate and have
the default filter options (inputs, operators, etc.) automatically
rendered for you in Telerik UI for Blazor. When you set
FilterMenuTemplate, you fully override the filter menu UI for that
column, and the default filter controls are not available as a reusable
component or tag. As a workaround, you may consider creating the inputs and dropdowns manually in the filter menu template and adding your custom filter after them, as demonstrated in this example, which shows a custom filter (in this case a custom checkbox filter) added after
the filter inputs and dropdowns: [https://blazorrepl.telerik.com/wfYhwFEZ57I9AdXK16](https://blazorrepl.telerik.com/wfYhwFEZ57I9AdXK16) Regards, Ivan Danchev Progress Telerik
