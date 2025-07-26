# Treelist blazor cannot resolve context

## Question

**ITG** asked on 05 Jul 2021

I have a problem when I tried to add a control on the TreeListCommandButton the context is not resolved Telerik version: 2.17.0 <TreeListCommandColumn Width="220px"> @{ var modelHierarchyInfo=(ModelHierarchyInfo)context; if (modelHierarchyInfo.DepthLevel <2) { <TreeListCommandButton Command="Add" Icon="add"></TreeListCommandButton> } } <TreeListCommandButton Command="Edit" Icon="edit"></TreeListCommandButton> <TreeListCommandButton Command="Delete" Icon="delete"></TreeListCommandButton> <TreeListCommandButton Command="Save" Icon="save" ShowInEdit="true"></TreeListCommandButton> <TreeListCommandButton Command="Cancel" Icon="cancel" ShowInEdit="true"></TreeListCommandButton> </TreeListCommandColumn>

## Answer

**Dimo** answered on 07 Jul 2021

Hello, The context for the Command column was introduced in version 2.25. Here are the relevant release notes: [https://www.telerik.com/support/whats-new/blazor-ui/release-history/ui-for-blazor-2-25-0](https://www.telerik.com/support/whats-new/blazor-ui/release-history/ui-for-blazor-2-25-0) Regards, Dimo Progress Telerik
