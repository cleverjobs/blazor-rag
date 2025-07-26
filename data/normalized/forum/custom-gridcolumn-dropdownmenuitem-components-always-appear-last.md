# Custom GridColumn/DropDownMenuItem components always appear last

## Question

**Kyl** asked on 18 Feb 2025

I've created a custom GridColumn component with special formatting like so: <GridColumn Field="@Field" Title="@Title" Width="@Width"> <Template Context="context"> @FormatValue(context) </Template> </GridColumn> When I place this within a <GridColumns> element (within a <TelerikGrid>) it always appears last. I'm pretty sure it's related to this issue but I don't quite follow the solution. The first one says to put the custom component directly in the grid tag. As in directly under <TelerikGrid> rather than within <GridColumns> (where I have it now)? I having the same issue with a custom <DropDownMenuItem> component in that it always appears last no matter where I place it within the <DropDownButtonItems> in a <TelerikDropDownButton>. This isn't quite as critical because all of my button items are custom components so I can arrange them properly. But the GridColumn is mixed with other normal GridColumn components and I'd rather not have to create custom components for all of them. Any thoughts? This is .NET 9 with Telerik UI for Blazor 7.1

## Answer

**Dimo** answered on 19 Feb 2025

Hello Kyle, The first solution in the KB is: Avoid nesting components and put the grid columns directly under the grid tag. This means to put the <GridColumn> instances as direct children of <GridColumn s> in the Grid, rather than in separate components. Another possible option is to move all Grid columns to custom components and not just one. The end result in both cases is that all Grid columns will be the same level deep in the app component hierarchy. In this way, the Grid will find out about them in the correct order. A related article on the topic is: Show Grid Command Column Always Last Regards, Dimo Progress Telerik

### Response

**Kyle** commented on 19 Feb 2025

Hi Dimo, Thanks for clarifying. To my knowledge, I'm not nesting the custom column. This is how I have it in my grid: <TelerikGrid Data="@MyData" Width="100%" FilterMode="@GridFilterMode.None" Sortable="false" SelectionMode="@GridSelectionMode.None" ScrollMode="@GridScrollMode.Scrollable" Pageable="false" ShowColumnMenu="false" Resizable="false"> <GridColumns> <GridColumn Field="Subject" Title="Subject" /> <<MyGridColumn Field="Creation" Title="Date/Time" /> </GridColumns> <NoDataTemplate> <div class="no-data"> No memos found </div> </NoDataTemplate> </TelerikGrid> Does the fact that my custom component includes a <GridColumn> at the root mean it's nested? If so, how would you define a custom GridColumn component?

### Response

**Dimo** commented on 19 Feb 2025

This is nesting: <GridColumns> <GridColumn Field="Subject" Title="Subject" /> <MyGridColumn Field="Creation" Title="Date/Time" /> </GridColumns> As far as I understand, you have a <GridColumn> inside <MyGridColumn>, right? Due to the way Blazor works, the Grid will find out about the <GridColumn> inside <MyGridColumn> after all <GridColumn> s that are direct children of <GridColumns>. So, either nest all columns, or nest none.

### Response

**Kyle** commented on 19 Feb 2025

Is there no way to define a custom column that can be used in conjunction with standard GridColumn components?

### Response

**Dimo** commented on 19 Feb 2025

If " in conjunction " means what you showed, then I am afraid not. This is how Blazor works. I shared one other possible option - make all columns "custom" by wrapping them in your own Razor component.

### Response

**Kyle** commented on 19 Feb 2025

Okay thanks for the explanation, that was very helpful. I had creating custom columns for everything as a backup option but not sure it's practical if there are only one or two custom components. Might explore the second option as well but seems like overkill for my purposes: Use the Grid State, its methods ( GetState, SetStateAsync ) and events ( OnStateInit, OnStateChanged ) to get the collection of column states and change the Order of the instances you want to rearrange.

### Response

**Kyle** commented on 05 Mar 2025

Dragging this up again because I'm having a similar issue with DropDownMenuItem. I've gone down the path of using custom menu items for everything because the alternative would be a rather large component which I'd like to avoid. My issue is that even embedding one or more custom menu items within an <AuthorizeView> component causes them to be placed at the bottom. In essence, the following doesn't show the menu items in the order presented: <DropDownButtonItems> <DropDownButtonItem> Moo 1 </DropDownButtonItem> <AuthorizeView Policy="@Policies.MY_POLICY"> <DropDownButtonItem> Master 1 </DropDownButtonItem> <DropDownButtonItem> Master 2 </DropDownButtonItem> </AuthorizeView> <DropDownButtonItem> Moo 2 </DropDownButtonItem> <DropDownButtonItem> Moo 3 </DropDownButtonItem> </DropDownButtonItems> What does everyone else do to get around this? I'd like to leverage the built-in Blazor components and what I think is a good practice of using custom components where possible but I feel like I'm fighting the framework a bit here. Or not understanding the methodology.

### Response

**Dimo** commented on 06 Mar 2025

@Kyle - an easy option is to place all <DropDownButtonItem>s inside the <AuthorizeView> component. All items will be in <Authorized> and some items will be in <NotAuthorized>. In other words, you will need to define the regular items twice.

### Response

**Kyle** commented on 06 Mar 2025

@Dimo That makes sense. Thanks
