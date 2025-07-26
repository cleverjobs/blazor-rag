# Treeview with checkboxes, problems with CheckParents=@true CheckChildren=@true

## Question

**mic** asked on 27 Jun 2024

We are updating the data bound to the treeview dynamically which has CheckParents and CheckChildren set to true . Issue is it appears the binding is ignoring these flags. screenshot show it ignoring CheckParents. This REPL shows it ignoring CheckChildren [https://blazorrepl.telerik.com/GyuKmVPY13f8gREi18](https://blazorrepl.telerik.com/GyuKmVPY13f8gREi18) <TelerikTreeView Data="@PermissionTreeData" @bind-CheckedItems="@CheckedItems" CheckBoxMode=@TreeViewCheckBoxMode.Multiple CheckParents=@true CheckChildren=@true>

## Answer

**Stamo Gochev** answered on 01 Jul 2024

Hi Michael, I have already answered the original support ticket (Ticket ID: 1656889) on the same topic and I am pasting the answer here for reference purposes: If you have a follow-up, please post it in the original thread, so I can suggest further actions. Here is the answer to the ticket: "The code for manually checking TreeView items: <TelerikButton OnClick="@(()=> { var precheckedItem=FlatData.Where(x=> x.Id==3); checkedItems=new List<object>(precheckedItem); })"> Load </TelerikButton> can be updated to include the full hierarchy of the items and not just the parent item (in this case with Id=3). As the handler might contain complex logic for checking and unchecking parent and child items, the developer is expected to provide the whole list of selected items and not just the parents. Note that this differs from interacting with the UI (clicking the checkbox by hand) as this is done through API and not user interaction. Here is an updated Telerik Blazor REPL example that sets the full selection: [https://blazorrepl.telerik.com/wIuVulOj39Vl1F3S32](https://blazorrepl.telerik.com/wIuVulOj39Vl1F3S32) Regards, Stamo Gochev Progress Telerik
