# 'None' option in Grid filter for empty values

## Question

**Ale** asked on 04 Jul 2023

I have a grid where 'Location' column may contain empty values. I have implemented the column in the following way: <GridColumn Title="Location" Width="100px" FilterMenuType="FilterMenuType.CheckBoxList" Field="@nameof(AreaViewModel.Location)"> <Template> @{
// If there is 'None' value specified for location - show just empty cell (hide actual data object property value).
// But filter will be able to work in this case filtering by value 'None' as if it is shown in the cell.
// Filter require that filter option text must match with the text in the bound data object property.
AreaViewModel item=context as AreaViewModel;
string cellValue=item.Location=="None" ? null : item.Location; <div> @cellValue </div> } </Template> <FilterMenuTemplate Context="context"> <TelerikCheckBoxListFilter Data="@FilterAreaLocations" Field="@(nameof(AreaLocationDto.Location))" @bind-FilterDescriptor="context.FilterDescriptor"> </TelerikCheckBoxListFilter> </FilterMenuTemplate> </GridColumn> It allows to filter rows with empty values when I select 'None' in the filter. But I must substitute nulls with text 'None' in Grid data to get to work (that is not desired). Sorting does not work as I need in this case. It places rows with empty 'Location' field in position of word 'None' (in alphabet order). But I need to sort it as if it has null (or empty string) value instead of 'None'. So questions are (I have not found answers in documentation): 1. Is it possible to implement custom sorting (some comparision function to implement or override for example) where I can handle 'None' values as nulls? 2. Is there some placeholder in filters for empty values that allows to assign some text for filter item with empty value (or some approach to implement it) ? I would be able to use actual nulls instead of text 'None' in grid data in this case. 3. Is there some other approach to implement such behaviour for Grid filter that allows filtering/sorting to work in desired way ?
