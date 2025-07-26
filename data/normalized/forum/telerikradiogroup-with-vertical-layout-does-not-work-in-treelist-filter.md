# TelerikRadioGroup with Vertical layout does not work in TreeList filter

## Question

**Tua** asked on 23 Feb 2022

Hi all, I am using TelerikTreeList with custom filter menu. In the filter menu template I am using TelerikRadioGroup with Vertical layout but it is always display as Horizontal. I try to add css to a div outside with display:inline but it still does not work. It is only display as Vertical when I inspect element and then remove class k-filter-menu. The problem is I have many items in the radioGroup so display Horizontal does not look good. Is there any workaround solution for this? The code is look like this (I already removed some other columns) <TelerikTreeList Data="@Tasks" IdField="Id" Class="taskTreeView" ParentIdField="ParentId" Resizable="true" EditMode="TreeListEditMode.Inline" FilterMode="@TreeListFilterMode.FilterMenu" OnRowRender="@OnRowRenderHandler"> <TreeListToolBar> <TreeListCommandButton Command="Add" Icon="add"> New Task </TreeListCommandButton> </TreeListToolBar> <TreeListColumns> <TreeListColumn Field=@nameof(TaskItem.DueDate) Title="Due Date" Width="100px" FieldType="@typeof(string)"> <Template> @{
var item=context as TaskItem; <div> @(item.DueDate.ToString("MMM d")) </div> } </Template> <FilterMenuTemplate> @{
HireDateFilterMenuTemplateContext=context;
ExtendHireDateFilterDescriptor();
} <div class="filter-radio"> <TelerikRadioGroup Data="@DateOptions" Value="@SelectedDueDateRadioSelector" ValueChanged="@((int value)=>
OnChangeHandler(value) )" Layout="RadioGroupLayout.Vertical" ValueField="@nameof(RadioOptionsModel.IdField)" TextField="@nameof(RadioOptionsModel.DisplayField)"> </TelerikRadioGroup> </div> </FilterMenuTemplate> </TreeListColumn> </TelerikTreeList> The UI looks like this

### Response

**Dimo** commented on 28 Feb 2022

Can you provide a runnable example? Your code seems to work as expected. You can also inspect the radio group styles when the component is inside and outside a TreeList.
