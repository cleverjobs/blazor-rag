# TabStrip not removing k-state-active on ActiveTabIndexChanged event

## Question

**Nat** asked on 30 Mar 2022

Hello, I am trying to use the TabStrip component but am running into issues. I have tried every combination of demos that are in the documentation, and none seem to function. I have tried it by just using @ref, I've tried just using ActiveTabIndex, and I've tried the below, and none seem to function the same as in the demos. With each way I tried, the previous active tab keeps it's .k-state-active class, and the newly selected tab receives a .k-state-active class. The previously selected tab does not get reset to .k-state-default. I have also tried this not nested within a TelerikGridLayout and it did not make a difference. Any input would be greatly appreciated <TelerikGridLayout>
<GridLayoutColumns>
<GridLayoutColumn Width="100%"></GridLayoutColumn>
</GridLayoutColumns>
<GridLayoutRows>
<GridLayoutRow Height="10vh"></GridLayoutRow>
<GridLayoutRow Height="90vh"></GridLayoutRow>
</GridLayoutRows>
<GridLayoutItems>
<GridLayoutItem Column="1" Row="1" Class="m-auto">
<img src="Images/logo.png" />
</GridLayoutItem>
<GridLayoutItem Column="1" Row="2">
<TelerikTabStrip TabPosition="Telerik.Blazor.TabPosition.Top" @ref="BaseDashboardTabStrip" ActiveTabIndex="@currentTab" ActiveTabIndexChanged="@TabChangedHandler">
<TabStripTab Title="Tab 1">
</TabStripTab>
<TabStripTab Title="Tab 2">
</TabStripTab>
<TabStripTab Title="Tab 3">
</TabStripTab>
<TabStripTab Title="Tab 4">
</TabStripTab>
<TabStripTab Title="Tab 5">
</TabStripTab>
<TabStripTab Title="Tab 6">
</TabStripTab>
</TelerikTabStrip>
</GridLayoutItem>
</GridLayoutItems>
</TelerikGridLayout>
@code {
TelerikTabStrip BaseDashboardTabStrip; int currentTab { get; set; }=0; void TabChangedHandler ( int newIndex ) {
currentTab=newIndex;
StateHasChanged();
}
}

## Answer

**Nathan** answered on 30 Mar 2022

Well I figured the issue out shortly after posting this. The tabs do not receive a correct tabIndex in the HTML if there is no content in the TabStripTab body. I don't know if that is the correct behavior or not, but content being present within the tab should not affect the functionality of the tabIndex and the TabStrip's ability to change state. Hopefully this is just a bug.

### Response

**Dimo** commented on 01 Apr 2022

Nathan, your observation is correct - the behavior is related to the empty tabs, but the Blazor framework also plays a role here. I think I have seen such a setup only once before. Can you describe what is the real-world scenario, which requires such implementation? On a side note, any invisible content inside the tabs will prevent the issue.

### Response

**Nathan** commented on 01 Apr 2022

The primary reason I was experiencing this behavior is because I was still in the process of getting content onto the page, and was testing the tab functionality before I had any content within the tabs. However, a potential real-world example where this could pose a problem is generating the content dynamically, and not displaying anything if there is no content to be generated. If the tab with no content is clicked, it would break the TabStrip, regardless of whether there is content in the other tabs or not.

### Response

**Dimo** commented on 01 Apr 2022

Thanks for the follow-up, Nathan.
