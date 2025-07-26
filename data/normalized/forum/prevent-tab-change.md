# Prevent tab change

## Question

**Geo** asked on 05 Nov 2020

How can I programmatically prevent the active tab page changing? I'm really looking for something like ActiveTabIndexChanging, where the change can be cancelled based on some logic. Is there a workaround for this?

## Answer

**Marin Bratanov** answered on 05 Nov 2020

Hello George, That event already exists: [https://docs.telerik.com/blazor-ui/components/tabstrip/events](https://docs.telerik.com/blazor-ui/components/tabstrip/events) If you don't update your view-model and the tab strip binds to an tab index field, you will effectively cancel the event, as is the typical behavior of two-way binding. Here's an example I made for you: <TelerikTabStrip ActiveTabIndex="@ActiveTabIndex" ActiveTabIndexChanged="@TabChangedHandler">
<TabStripTab Title="First">
First tab content. Click through the tabs.
</TabStripTab>
<TabStripTab Title="Second">
Second tab content.
</TabStripTab>
<TabStripTab Title="Third">
Third tab content.
</TabStripTab>
</TelerikTabStrip>

@code { int ActiveTabIndex { get; set; } void TabChangedHandler ( int newIndex ) { // this will update the view-model for all items but the third, // effectively cancelling the event for the third tab if (newIndex !=2 )
{
ActiveTabIndex=newIndex;
}
}
} Regards, Marin Bratanov

### Response

**Dustin** commented on 02 Aug 2023

Is there a way to prevent the tab change event from happenning at all. When I use this method and I have a Razor Component in my tab contenxt, it rerenders the component causing it to load all of my data again in the OnInitializedAsync() call. I'd like to stop that from happening if certain conditions are met.

### Response

**Dimo** commented on 04 Aug 2023

@Dustin - currently it's not possible to prevent tab change at all, but there is a feature request about cancellable TabStrip navigation.

### Response

**Dustin** commented on 04 Aug 2023

Awesome, thanks for the info! I gave that item a vote.

### Response

**George** answered on 05 Nov 2020

I was looking for ActiveTabIndexChang ing rather than ActiveTabIndexChang ed. I didn't have ActiveTabIndex bound to anything, so even with a return in the event handler the tab changed. Binding ActiveTabIndex works for me though. Thanks :)
