# Programmatically select other Tab

## Question

**Fra** asked on 14 Aug 2020

I am trying to use your example here: Forum Post I am rendering a dynamic list of Tabs but can't seem to programmatically select another Tab with the ActiveTabIndexChanged. The code in your example needs to be updated. Can you update us on doing this with both a dynamic Tab list + an ActiveTabIndex set ? Thank you.

## Answer

**Marin Bratanov** answered on 14 Aug 2020

Hello Francis, This example is very old and did not use the proper blazor way to handle things, so that was changed. Now instead of a method, there is a parameter that is the index of the tab you want selected. So, you have to set the ActiveTabIndex parameter to select a certain tab. I encourage you to review the documentation to make sure you are looking at details for the latest version: [https://docs.telerik.com/blazor-ui/components/tabstrip/overview](https://docs.telerik.com/blazor-ui/components/tabstrip/overview) This works when you create tabs programmatically too, you just have to keep track of which model index you are in. For example, combining the second and third examples from the current docs you can create tabs in a loop and activate on based on the desired index. Here's an example I made for you: @result

<TelerikTabStrip ActiveTabIndex="@activeTab" ActiveTabIndexChanged="@TabChangedHandler">
@{ foreach (MyTabModel item in tabs)
{
<TabStripTab Title="@item.Title" Disabled="@item.Disabled">
Content for tab @item.Title
</TabStripTab>
}
}
</TelerikTabStrip>

<TelerikButton OnClick="@( _=> activeTab=2 )"> Select third tab ( will not fire the ActiveTabIndexChanged event )</TelerikButton>

@code { int activeTab { get; set; }

MarkupString result { get; set; } void TabChangedHandler ( int newIndex ) { // when using events from two-way binding parameters, always update the parameter in the handler activeTab=newIndex; string tempResult=$"current tab {newIndex} selected on {DateTime.Now} ";
MyTabModel currTab=tabs[newIndex];
tempResult +=$"<br />the new tab has a title {currTab.Title} ";
result=new MarkupString(tempResult);
}

List<MyTabModel> tabs=new List<MyTabModel>()
{ new MyTabModel { Title="One" }, new MyTabModel { Title="Two", Disabled=true }, new MyTabModel { Title="Three" }
}; public class MyTabModel { public string Title { get; set; } public bool Disabled { get; set; }
}
} Regards, Marin Bratanov

### Response

**Francis** answered on 17 Aug 2020

Thank you. I had declared the same variable name as the activeindex which is why it was not working. All is good now and thank you for the code update.

### Response

**Bob** answered on 18 Sep 2020

I have followed this example in order to set my tab when the page loads, but it is not working. I am storing the tab selected in session storage and reading it in the OnAfterRenderAsync method, but the selected tab is not changing when I set the activeTabIndex. <TelerikTabStrip ActiveTabIndex="@activeTabIndex" ActiveTabIndexChanged="TabChangedHandler"> <TabStripTab Title="Open Tickets"> <TicketList MyTickets="false" UserId="@userId" ClosedTickets="false" TicketAreas="@ticketAreas" TicketPriorities="@ticketPriorities" TicketStatuses="@ticketStatuses" Staff="@staff"> </TicketList> </TabStripTab> <TabStripTab Title="My Tickets"> <TicketList MyTickets="true" UserId="@userId" ClosedTickets="false" TicketAreas="@ticketAreas" TicketPriorities="@ticketPriorities" TicketStatuses="@ticketStatuses" Staff="@staff"> </TicketList> </TabStripTab> <TabStripTab Title="Closed / Cancelled"> <TicketList MyTickets="false" UserId="@userId" ClosedTickets="true" TicketAreas="@ticketAreas" TicketPriorities="@ticketPriorities" TicketStatuses="@ticketStatuses" Staff="@staff"> </TicketList> </TabStripTab> <TabStripTab Title="Search"> <TicketSearch></TicketSearch> </TabStripTab> </TelerikTabStrip> protected override async Task OnAfterRenderAsync(bool firstRender) { if (firstRender) { activeTabIndex=await sessionStorage.GetItemAsync<int>("ticketTabSelected"); } } private async Task TabChangedHandler(int newIndex) { activeTabIndex=newIndex; await sessionStorage.SetItemAsync<int>("ticketTabSelected", newIndex); }

### Response

**Francis** answered on 18 Sep 2020

Are you sure your activeTabIndex has a value from your session storage and that your firstRender is True? Try to debug first by just putting activeTabIndex=0 to see if your first index gets selected.

### Response

**Bob** answered on 18 Sep 2020

Yes, I have break pointed the code and it is getting tab index 1 when I come back to the page.

### Response

**Marin Bratanov** answered on 18 Sep 2020

Hello Bob, Have you tried invoking StateeHasChanged after altering the field? That's needed in events like OnAfterRenderAsync. Regards, Marin Bratanov

### Response

**Bob** answered on 18 Sep 2020

That worked to change the tab but now it is blowing up after the tab changes. Each tab contains a grid and it appears that changing the tab is causing it to error when trying to load the data for the grid on the tab it is changing too, possibly because it is still trying to load the data from the initial tab. Is there a better way to do this? All I want to do is have it remember the tab they were on so that when they return to this screen from another, it starts on the last tab they were on? Storing it in the session is only way I can see to do that.

### Response

**Marin Bratanov** answered on 20 Sep 2020

Hi Bob, Storing the current index somewhere (session storage, local storage, database, ...) is the way I'd do this. Perhaps holding the data for the child components in the main component where the tab strip is will let you avoid errors related to disposing them, while also helping you have a state for them. You should check what the error is, what its stack trace is and that will probably let you see how to guard against it (maybe implementing IDisposable in the component in the tab and cleaning up things/cancelling requests in the Dispose method). There was also a bug in the grid that threw exceptions when being disposed while still initializing ( link ), and we fixed that in 2.17.0, so upgrading to it might help. If that bug is not the issue you're hitting, and the error come from Telerik components in the tab (the tab strip itself merely switches the rendered component like an if-else block), I suggest you open a support ticket and send us a simple runnable mockup of the problem so we can have a look and avoid guessing. Regards, Marin Bratanov
