# Toggle Scheduler Grouping

## Question

**Chr** asked on 21 Oct 2024

I want to toggle grouping for a given scheduler resource and took the following approach in the SelectedChanged hander for a ToggleButton. Are there pitfalls to this approach? Are built-in group toggles on the roadmap? <ToolBarToggleButton Title="@(Grouped ? " Ungroup ": " Group ")" Icon="@(Grouped ? SvgIcon.Ungroup : SvgIcon.Group)" SelectedChanged="@GroupedSelectedChanged"> @Grouped </ToolBarToggleButton> public bool Grouped { get; set; }=false;
...

List <string> GroupingResources=["Rooms"];

...

void GroupedSelectedChanged(bool newGrouped)
{
if (newGrouped)
{
SchedulerRef.GroupSettings=new SchedulerGroupSettings
{
Resources=GroupingResources,
Orientation=SchedulerGroupOrientation.Vertical
};
}
else
{
SchedulerRef.GroupSettings=null;
}

SchedulerRef.Rebind();

Grouped=newGrouped;
}

## Answer

**Nadezhda Tacheva** answered on 24 Oct 2024

Hi Christopher, Currently, there are no plans for exposing a built-in option to toggle the grouping. If the listed approach delivers the desired approach, you may use that. I would generally recommend a different option - managing the collection of the grouping resorces. To disable the grouping you may simply clear the collection and then populate it again to group the Scheduler. Here is a basic sample: [https://blazorrepl.telerik.com/QIbuwIbv00TnkDbO31.](https://blazorrepl.telerik.com/QIbuwIbv00TnkDbO31.) In our upcoming release in November, we will expose a Toolbar Template - you can use that to place the Toggle button in the Scheduler Toolbar. Regards, Nadezhda Tacheva Progress Telerik

### Response

**Christopher** commented on 29 Oct 2024

Thanks. This was helpful. For anyone who comes across this in the future, here are the relevant pieces. Toggle (to be moved to a scheduler toolbar template): <TelerikToolBar> <ToolBarToggleButton Title="@(Grouped ? " Ungroup ": " Group ")" Icon="@(Grouped ? SvgIcon.Ungroup : SvgIcon.Group)" Selected="@Grouped" SelectedChanged="@GroupedSelectedChanged"> @(Grouped ? "Ungroup" : "Group") </ToolBarToggleButton> </TelerikToolBar> Scheduler Resources: <SchedulerResources> <SchedulerResource Field="RoomId" Title="Room" Data="@RoomResources" /> </SchedulerResources> Properties: bool Grouped { get; set; }=false;
List <string> GroupingResources=[]; Toggle handler: private void GroupedSelectedChanged(bool newGrouped)
{
Grouped=newGrouped;
GroupingResources=Grouped ? ["RoomId"] : [];
}
