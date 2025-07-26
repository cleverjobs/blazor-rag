# Room for Animation Container

## Question

**Joe** asked on 27 Jun 2025

Can you tell me how to force the GridLayout to allow space for my TelerikAnimationContainer? It gets chopped off when the 3rd row is "short". I don't want the scroll bar to accommodate the height. I want to see the entire filter. Fully opened (When data extends the Grid): Short Closed: Short Open <TelerikGridLayout Class="grid-layout"> <GridLayoutRows> <GridLayoutRow Height="28px" /> <GridLayoutRow /> <GridLayoutRow /> </GridLayoutRows> <GridLayoutItems> <GridLayoutItem Row="1"> @if (Groups?.Count> 0)
{ <TelerikButton OnClick="@OnCreate" Class="gsi-width-100pct gsi-padding-0"> Create New </TelerikButton> } </GridLayoutItem> <GridLayoutItem Row="2"> <div> <div class="gsi-background-color-light" style="height: 41px; display:flex;justify-content:space-between;"> <div class="align-self-center gsi-font-kendo gsi-margin-0"> Patient Filters </div> <TelerikButton FillMode="Clear" Class="gsi-border-width-0 gsi-border-color-white gsi-padding-8" Icon="@(Telerik.SvgIcons.SvgIcon.Filter)" OnClick="@GridFilterExpandCollapse" /> </div> <TelerikAnimationContainer @ref="@FilterContainer" Class="gsi-background-color-light gsi-margin-5 k-rounded-0" Width="100%" Height="100vm"> <TelerikStackLayout Spacing="1px" Class="gsi-margin-5"> <TelerikCard Width="33vh"> <CardBody> @if (SessionOption1Items?.Count> 0)
{ <div class="form-group-short gsi-max-width-250"> <label class="col-form-label"> @SessionOption1Template.Name </label> <br /> <TelerikDropDownList Data="@SessionOption1Items" @bind-Value="@SessionOptionIndex1" TextField="Name" ValueField="Id" /> </div> @if (SessionOption2Items?.Count> 0)
{ <div class="form-group-short gsi-max-width-250"> <label class="col-form-label"> @SessionOption2Template.Name </label> <br /> <TelerikDropDownList Data="@SessionOption2Items" @bind-Value="@SessionOptionIndex2" TextField="Name" ValueField="Id" /> </div> }
}
else
{ <small> No Defined Filter </small> } </CardBody> </TelerikCard> <TelerikCard Width="33vh"> <CardBody> <div class="form-group-short gsi-max-width-250"> <label class="col-form-label"> Date Range </label> <br /> <TelerikDropDownList Data="@DateRangeOptions" @bind-Value="@DateRangeIndex" TextField="Name" ValueField="Id" /> </div> <div class="form-group-short gsi-max-width-250"> <label class="col-form-label"> Group Behavior </label> <br /> <TelerikDropDownList Data="@GroupFilterOptions" @bind-Value="@GroupFilterIndex" TextField="Name" ValueField="Id" /> </div> </CardBody> </TelerikCard> <TelerikCard Width="34vh"> <CardBody> <div class="form-group-short gsi-max-width-250"> <label class="col-form-label"> Status </label> <br /> <TelerikDropDownList Data="@IsActiveFilterOptions" @bind-Value="@IsActiveIndex" TextField="Name" ValueField="Id" /> </div> <div class="form-group-short align-bottom"> <label class="col-form-label gsi-color-white"> Apply Filter </label> <br /> <TelerikButton OnClick="OnFilterChanged" Class="gsi-background-color gsi-color-white gsi-width-100pct"> Apply Filter </TelerikButton> </div> </CardBody> </TelerikCard> </TelerikStackLayout> </TelerikAnimationContainer> </div> </GridLayoutItem> <GridLayoutItem Row="3"> <TelerikGrid Data=@Sessions...

### Response

**Joel** commented on 27 Jun 2025

Here is the entire UI hierarchy... thought you might need a little more context: <TelerikSplitter Orientation="SplitterOrientation.Horizontal"> <SplitterPanes> <SplitterPane Size="40%" Min="30%" Max="70%" Collapsible="false" Class="k-scrollable"> <TelerikGridLayout Class="grid-layout"> <GridLayoutRows> <GridLayoutRow Height="28px" /> <GridLayoutRow /> </GridLayoutRows> <GridLayoutItems> @if (Groups?.Count> 0)
{ <GridLayoutItem Row="1"> <TelerikButton OnClick="@(()=> SetTreeListExpandedItems())" Class="gsi-width-100pct gsi-padding-0"> Expand/Collapse Groups </TelerikButton> </GridLayoutItem> } <GridLayoutItem Row="2"> <TelerikTreeList @ref=@TreeListRef Data="@Groups" SelectedItems="@SelectedGroups" IdField="@nameof(Gsi.Customer.Models.Group.Id)" ParentIdField="@nameof(Gsi.Customer.Models.Group.ParentId)" OnStateInit="((TreeListStateEventArgs<Gsi.Customer.Models.Group> args)=> OnStateInitHandler(args))" Pageable="true" PageSize="10" Sortable="false" SelectionMode="TreeListSelectionMode.Single" FilterMode="@TreeListFilterMode.FilterMenu" SelectedItemsChanged="@((IEnumerable<Gsi.Customer.Models.Group> m)=> OnGroupSelected(m))"> <TreeListColumns> <TreeListColumn Field="Name" Title="Group Filter" Expandable="true"> <Template> @{
var item=context as Gsi.Customer.Models.Group; <img height="32" width="32" src="@item.ImageUrl" /> @item.Name
} </Template> </TreeListColumn> </TreeListColumns> </TelerikTreeList> </GridLayoutItem> </GridLayoutItems> </TelerikGridLayout> </SplitterPane> <SplitterPane Collapsible="false" Min="30%" Max="70%" Class="k-scrollable"> <TelerikGridLayout Class="grid-layout"> <GridLayoutRows> <GridLayoutRow Height="28px" /> <GridLayoutRow /> <GridLayoutRow /> </GridLayoutRows> <GridLayoutItems> <GridLayoutItem Row="1"> @if (Groups?.Count> 0)
{ <TelerikButton OnClick="@OnCreate" Class="gsi-width-100pct gsi-padding-0"> Create New </TelerikButton> } </GridLayoutItem>...

### Response

**Joel** commented on 27 Jun 2025

Also, if you can show me how to right-align this control to the right so it stays visually attached to the Filter Icon... that'd be awesome.

## Answer

**Dimo** answered on 30 Jun 2025

Hello Joel, The AnimationContainer is not designed to be used in such scenarios. It renders in-place, so it will be clipped by scrollable container boundaries. Use the Telerik Popup component instead. It provides quite a lot of positioning and alignment settings. Also see Comparison between Telerik popup components Regards, Dimo Progress Telerik
