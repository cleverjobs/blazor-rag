# Clear FilterCellTemplate TelerikComboBox value on Button click

## Question

**BenBen** asked on 23 Apr 2021

I have a Blazor Telerik Grid with FilterCellTemplate and a TelerikComboBox inside it, I would like to clear the selected value inside the ComboBox on button click I am trying to create functionality to clear all the filters for a Telerik Grid on a button click event. TelerikGrid has GridColumn that has FilterCellTemplate which is contains a TelerikComboBox.

## Answer

**Marin Bratanov** answered on 23 Apr 2021

Hi Ben, The easiest way to reset a grid is to call its .SetState(null) method. You can read more about the grid state in its dedicated article, it opens up a lot of possibilities for your app: [https://docs.telerik.com/blazor-ui/components/grid/state.](https://docs.telerik.com/blazor-ui/components/grid/state.) The combo box itself (or any element in the filter template) will usually have its Value bound to a field in the view-model. If that is not tied directly to the filter descriptors the grid gives you, resetting the state will not reset the input. In such a case, you will need to reset that field in the view-model with your own code, like you would clear any other input that is not in a template. Regards, Marin Bratanov

### Response

**Ben** answered on 23 Apr 2021

The Combobox is not bound to a view model, I am using the ValueChanged event to update the grids content when the user select the value from the ComboBox. I was able to reset the grid , but the value inside the combobox does not clear. I am adding a button to the grid toolbar "Clear Filters" , that should clear all the applied filters and clear all the filter values. Here it the definition of the column <GridColumn Field="@(nameof(SearchResult.StateName))" Title="State" Filterable="true" Width="100px"> <FilterCellTemplate> <TelerikComboBox Data="@Filter.StateFilters" Filterable="true" FilterOperator="@StringFilterOperator.Contains" Width="100%" AllowCustom="false" ValueChanged="@(async (string val)=> { var filter=context.FilterDescriptor.FilterDescriptors[0] as FilterDescriptor; filter.Value=val; if (string.IsNullOrEmpty(val)) { await context.ClearFilterAsync(); } else { await context.FilterAsync(); } })"> </TelerikComboBox> </FilterCellTemplate> <Template> @{ var sr=context as SearchResult; <div class="align-content-center" title="@sr.StateName"> <img class="rounded" width="20" height="20" src="@($"~/../../images/{sr.StateName}.png")" /> </div> } </Template> </GridColumn>

### Response

**Marin Bratanov** answered on 23 Apr 2021

Hi Ben, If you want to control the Value of the combobox programmatically, you must use that parameter and point it to a field in your view-model, so you can change that field and affect the component. This is the way such things are done in Blazor. Regards, Marin Bratanov

### Response

**Ben** answered on 23 Apr 2021

Thanks for the quick reply, So I would now have to apply the filters from code , and I would have to do this for other columns as well that have regular filters ? is there an example for it that I can refer to ?

### Response

**Marin Bratanov** answered on 23 Apr 2021

Hello Ben, All you need to do is to use the Value parameter of the combobox, see the third example in the docs of the ValueChanged event: [https://docs.telerik.com/blazor-ui/components/combobox/events#valuechanged.](https://docs.telerik.com/blazor-ui/components/combobox/events#valuechanged.) You only need such "extra" code where you want to control the filters through templates, columns that us the built-in filters already have their Value bound to their corresponding filter descriptor in our code so you don't have to do this anywhere else but in places where you want to control the Value. Regards, Marin Bratanov Progress Telerik

### Response

**Ben** answered on 23 Apr 2021

So this is the solution I got. I added a new property string StateFilter {get;set} The Modified the combobox to Value="@StateFilter" and then update theValueChanged Method I have to set the StateFilter to val ValueChanged="@(async (string val)=> { var filter=context.FilterDescriptor.FilterDescriptors[0] as FilterDescriptor; filter.Value=val; StateFilter=val; if (string.IsNullOrEmpty(val)) { await context.ClearFilterAsync(); } else { await context.FilterAsync(); } })" and then in my code I update the StateFilter=String.Empty; to clear the value in combo box. Thank you
