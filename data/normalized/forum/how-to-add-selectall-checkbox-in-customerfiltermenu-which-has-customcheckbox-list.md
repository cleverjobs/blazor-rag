# How to add SelectAll Checkbox in CustomerFilterMenu which has customcheckbox list

## Question

**Nit** asked on 10 Jun 2022

Hi, I am following below demo for adding custom filter menu with checboxes. [https://demos.telerik.com/blazor-ui/grid/custom-filter-menu](https://demos.telerik.com/blazor-ui/grid/custom-filter-menu) But it doesn't come with SelectAll checkbox option, please let me know how can add that option. regards, nitesh

### Response

**Benjamin** commented on 10 Jun 2022

Hi Nitesh, if you haven't selected any checkbox, it's actually equal to a "SelectAll". The downside of using custom templates instead of using the default "out-of-the-box" functionality comes with a lot of manual effort (I feel your pain ;)) As far as I understand your question: <FilterMenuTemplate>
@{
<div class="filter-values-container"> <TelerikCheckBox Value="@SelectedAll" ValueChanged="@((bool value)=> ToggleSelectAll(value))" Id="selectAll">
</TelerikCheckBox> @foreach ( var name in Names)
{
<div>
<TelerikCheckBox Value="@(GetFilterValues(context.FilterDescriptor).Contains(name))" ValueChanged="@((bool value)=> ColumnValueChanged(value, name, nameof(EmployeeDto.FirstName), context.FilterDescriptor))" Id="@($" name_{name} ")">
</TelerikCheckBox>
<label for="@($" name_{name} ")">
@name
</label>
</div>
}
</div>
}
</FilterMenuTemplate> Add the variable bool SelectedAll + the method ToggleSelectAll(bool value) where you process the filter state.

### Response

**Nitesh** commented on 10 Jun 2022

Hi Benjamin, thank you for sharing your thoughts on this. Although where do you set or unset SelectedAll. And when i check on Select All, where do i set all my checkboxes option to Checked state. regards, nitesh

## Answer

**Timothy J** answered on 10 Jun 2022

See this instead Blazor Grid - Filtering CheckBoxList | Telerik UI for Blazor

### Response

**Nitesh** commented on 13 Jun 2022

Hi Timothy, This is inbuilt checkbox with selectALL feature, since i need another filter criteria along with checkbox just similar to WPF filter one i need to build custom filter menu. Now i am feeling the customization is really painful for the filter atleast. regards, nitesh
