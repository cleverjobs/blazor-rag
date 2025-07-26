# Telerik Blazor for TelerikTabStrip is throwing Index was out of range error while closing tabs

## Question

**Vin** asked on 27 Jun 2022

Hi Team, I am using Telerik Blazor with 3.4.0 version with same base code as [https://docs.telerik.com/blazor-ui/knowledge-base/tabstrip-remove-tab.](https://docs.telerik.com/blazor-ui/knowledge-base/tabstrip-remove-tab.) I am seeing below error while closing tabs. could you please assist for same. Note (i don't see this error when i use 3.2.0) System.ArgumentOutOfRangeException: Index was out of range. Must be non-negative and less than the size of the collection. (Parameter 'index') at Telerik.Blazor.Components.TelerikTabStrip.FocusActiveTab() at Telerik.Blazor.Components.TelerikTabStrip.set_CurrentActiveTabIndex(Int32 value) at Microsoft.AspNetCore.Components.EventCallbackWorkItem.InvokeAsync[T](MulticastDelegate delegate, T arg) at Microsoft.AspNetCore.Components.ComponentBase.Microsoft.AspNetCore.Components.IHandleEvent.HandleEventAsync(EventCallbackWorkItem callback, Object arg) at Microsoft.AspNetCore.Components.RenderTree.Renderer.DispatchEventAsync(UInt64 eventHandlerId, EventFieldInfo fieldInfo, EventArgs eventArgs)

### Response

**Tom** commented on 24 Aug 2022

I'm experiencing a very similar issue. If I simply hide the first tab via the Visible property, the same ArgumentOutOfRangeException is thrown immediately when the component is rendered. <TelerikTabStrip> <TabStripTab Title="Tab A" Visible="false"> </TabStripTab> <TabStripTab Title="Tab B" Visible="true"> </TabStripTab> <TabStripTab Title="Tab C" Visible="true"> </TabStripTab> </TelerikTabStrip> It sounds like the solution/workaround is to define an activeIndex in the parent component and then micromanage it. I'm wondering if there is going to be a way to safely hide tabs in the future without having to explicitly manage the active index? EDIT: I've tried the simple example above using 3.3.0, 3.4.0, and 3.5.0. It fails for all three versions.

## Answer

**Svetoslav Dimitrov** answered on 30 Jun 2022

Hello Vinod, As part of our 3.3.0 release, we fixed a bug where a wrong tab is focused if there is an invisible tab. This is the reason why the example in the Knowledge-based article fails. I have updated the example in the article and you can see it from our public GitHub repository since the live documentation is not yet updated. Let me know if the updated example helps you move forward. Regards, Svetoslav Dimitrov

### Response

**Greg** commented on 03 Aug 2022

Same problem. The following code worked prior to release 3.3 but no longer works on 3.4 and throws the out of rangfe exception: public void OnActiveTabIndexChanged(int newIndex) { if (Tabs==null || Tabs.Count==0 || newIndex <0) { return; } if (newIndex <0) { return; } else { ActiveTabIndex=newIndex; } } void RemoveTab(string primaryGuid) { int currentTabIndex=ActiveTabIndex; int tabToCloseIndex; TabDescriptor tabToClose=null; foreach (TabDescriptor item in Tabs) { if (item.BusinessObjectPrimaryGuid==primaryGuid) { tabToClose=item; } } if (tabToClose !=null) { tabToCloseIndex=Tabs.IndexOf(tabToClose); if (tabToCloseIndex !=-1) { if (tabToCloseIndex==ActiveTabIndex) { NewTabIndex=Math.Max(ActiveTabIndex - 1, 0); } if (tabToCloseIndex> ActiveTabIndex) { NewTabIndex=ActiveTabIndex; // No change as we're closing a tab to the right not affecting the selected tab's index } if (tabToCloseIndex <ActiveTabIndex) { NewTabIndex=Math.Max(ActiveTabIndex - 1, 0); ; // Closing a tab to the left, so need to decrement the current index by one to keep current tab selected } ActiveTabIndex=NewTabIndex; Tabs.Remove(tabToClose); StateHasChanged(); } } OnActiveTabIndexChanged(NewTabIndex); return; }

### Response

**Svetoslav Dimitrov** answered on 29 Aug 2022

Hello Tom and Greg, Can you try the updated approach from the How to Remove a Tab knowledge-based article and get back to me if it helped you resolve the issue? On a side note, the TabStrip is not a data-bound component so removing the tabs is not supposed to happen by the design of the component. Manually managing ActiveTabIndex is the best way to achieve the behavior. Regards, Svetoslav Dimitrov

### Response

**Besir** commented on 02 Dec 2022

Hello I got a similar issue and when I use the ActiveTabIndexChanged handler, it gets called with -1 as the new index. I think this should be treated as a Bug and handled properly on the internal SetActiveTab method. Not being able to generate the Tabs dynamically makes this component basically useless in many business scenarios. Thanks & BR Besir

### Response

**Svetoslav Dimitrov** commented on 07 Dec 2022

Hello Besir, Can you send me a runnable code snippet where I can see the issue? The removal of tabs is not a built-in feature of the TabStrip as the component is not data bound. The component is meant to be a simple Navigation component that shows some content to the users. As this is not an official feature we would not be able to treat it as a bug.

### Response

**Besir** commented on 23 Dec 2022

Hi Svetoslav The issue dissappeared after updaing to the latest blazor Version. Maybe it was a Bug in some of the previous versions. Thanks & BR Besir

### Response

**Besir** answered on 14 Mar 2023

Hello Svetoslav After making a custom TabStrip component from the Source Code I found out the bug is really there, and it is happening in the FocusActiveTab method (see the highlighted red line, Tabs[ActiveTabIndex] gives an error if ActiveTabIndex=-1 ): In TelerikTabStrip.razor.cs private void FocusActiveTab() { var visibleTabs=Tabs.Where(item=> item.Visible).ToList(); // Had to add these lines to avoid the error if (Tabs.Count==0 || visibleTabs.Count==0) return; // TabItems probably not (re)rendered yet if (ActiveTabIndex==-1) { if (Tabs.Count> 0) ActiveTabIndex=Tabs.Count - 1; // Make the last tab active else return; } var focusedIndex=visibleTabs.IndexOf(Tabs[ActiveTabIndex]); // ERROR if TabStrip is rerendering and ActiveTabIndex=-1 _=InvokeVoidAsync(CustomJsInteropFunctions.InvokeComponentMethod, FocusTabFunction, DataId, focusedIndex); }

### Response

**Svetoslav Dimitrov** answered on 16 Mar 2023

Hello everyone, On our feedback portal, we have a new feature request for the Closeable tabs as a built-in feature. You can Vote for this item and click the Follow button to receive email notifications on status updates. Regards, Svetoslav Dimitrov Progress Telerik
