# TreeList losing indicators

## Question

**EdEd** asked on 10 Jan 2022

Hi, I have defined a treelist as shown below. I followed the example in the demo. The only problem is that when I expand a row, all other rows that have an expand arrow next to them lose the arrow. The only way I can get them back is to refresh the page. I've attached a couple of screen shots. What am I missing? Thanks ... Ed protected async Task OnExpand(TreeListExpandEventArgs args)
{
var item=args.Item as ColorRMLotModel;

if (item.Lot.HasChildren && !tvData.Any(x=> x.Lot.ParentLotId==item.Lot.ColorRMLotId))
{
var items=GetKids(item.Lot.ColorRMLotId); ;
tvData.AddRange(items);
}
} SelectionMode="@TreeListSelectionMode.Single"
@ref="tlRef"
IdField="ColorRMLotId"
OnStateInit="((TreeListStateEventArgs <ColorRMLotModel> args)=> OnStateInitHandler(args))"

ColumnVirtualization="true"
ParentIdField="ParentLotId"
HasChildrenField="HasChildren"
Pageable="false"

Reorderable="true"
Sortable="true"
FilterMode="@TreeListFilterMode.FilterMenu"
OnEdit="@((TreeListCommandEventArgs args)=> OnEdit(args))"
OnExpand="@OnExpand"
Width="1250px"
Height="650px"
Resizable="true"> <TreeListToolBar>

## Answer

**Dimo** answered on 12 Jan 2022

Hello Ed, I have to admit that this is a known bug triggered by the combination of: loading child items on demand using a filter menu I hope you can change the filter mode as a workaround. I voted for the bug report on your behalf to bump its priority. Regards, Dimo
