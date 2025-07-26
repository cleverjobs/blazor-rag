# DisplayContent doesn't work for GroupDescriptor

## Question

**Ale** asked on 27 Mar 2023

I use TelerikGrid, and in it I do grid grouping. new GroupDescriptor()
{
Member="workItemViewModel.WorkItemGroupId",
DisplayContent="Application",
MemberType=typeof(string)
} Grouping is working, but I need to see text " Application", but I see " workItemViewModel.WorkItemGroupId" instead. How to fix it?

## Answer

**Svetoslav Dimitrov** answered on 30 Mar 2023

Hello Alexandre, The DisplayContent affects the group indicator inside the Grid group panel, which is above the header cells. For example, this online demo renders a group panel. There are 3 ways to customize the column label in the group header: Set the Title of the GridColumn. Set a DisplayName DataAnnotations attribute in the Grid model class. Use a GroupHeaderTemplate. Regards, Svetoslav Dimitrov

### Response

**Alexandre** commented on 03 Apr 2023

thanks, fixed
