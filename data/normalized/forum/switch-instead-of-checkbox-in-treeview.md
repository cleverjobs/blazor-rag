# Switch instead of checkbox in TreeView

## Question

**Jus** asked on 31 Dec 2024

Is there a way to use a Switch control instead of checkbox in a TreeView? I am able to use ItemTemplate to insert a switch next to the checkbox but I need to replace the checkbox and have the switch use CheckChildren and CheckParents. Any ideas? Thanks! <TelerikTreeView OnItemRender="@OnItemRender" CheckBoxMode="TreeViewCheckBoxMode.Multiple" CheckChildren="true" CheckParents="true" Data="@FlatData" @bind-ExpandedItems="@ExpandedItems"> <TreeViewBindings> <TreeViewBinding TextField="Text" IdField="Id" ParentIdField="ParentId" ItemsField="Text" HasChildrenField="HasChildren" IconField="Icon"> <ItemTemplate> @{var treeItem=(TreeItem)context; } <div class="treeview-item"> <TelerikSwitch @bind-Value="treeItem.IsChecked" /> <span> @treeItem.Text </span> </div> </ItemTemplate> </TreeViewBinding> </TreeViewBindings> </TelerikTreeView>

## Answer

**Dimo** answered on 02 Jan 2025

Hello Justin, When using checkboxes or a similar component inside the TreeView ItemTemplate, the CheckParents and CheckChildren logic must be implemented manually. You will need a ValueChanged or OnChange event for the Switch. A possible workaround that will make your job easier is to render the built-in checkboxes and hide them with CSS. On Switch toggle, click the corresponding checkbox with JavaScript, which will execute the built-in check parents/children logic. One downside of using Switches instead of TreeView checkboxes is the lack of indeterminate state. On a side note, please ask the license holder at your company to assign you a license, so that your account complies with our license agreement. Regards, Dimo Progress Telerik
