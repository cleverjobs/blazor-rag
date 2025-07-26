# StateHasChanged throwing error "The render handle is not yet assigned." on tabstrip.

## Question

**Law** asked on 01 Jun 2021

I am trying to either disable or hide TabStripTab(s) based on boolean values in the component that contains the tabstrip. In another component I set the value(s) i need to set on the tabstrip component but it doesn't rerender and attempts to do so using StateHasChanged() throws the error above. I've looked at the dynamic tabs example but don't see a solution for me there. Is there some other way to force the component to redraw or is there a way to use a reference for it? My attempts to use a reference are either null or it still doesn't cause a re-rendering/update of whether the tabs are disabled or not. Clicking the the tab(s) does force a re-render and subsequent disabling but of course that isn't workable. Thank you, Lawrence.

### Response

**Dimo** commented on 02 Jun 2021

A "render handle is not yet assigned" error suggests that the problem may not be in StateHasChanged or the TabStrip, but in the app architecture. For example, recently I came across an implementation where a service inherited from a component and called component methods directly, instead of emitting events that the component consumes. This scenario resulted in the same error, because there was no render context. Still, if the error looks related to the TabStrip, please send us a runnable example and we will readily review it.

### Response

**Lawrence** commented on 03 Jun 2021

In the end it turns out that the tabstrip (contained in a layout) wouldn't re-render even after data updates because it didn't detect any changes. I had to modify the "layout" containing the above-mentioned tabstrip into a "component" and provide a parameter that changed causing a re-render when the parameter changed value. A lousy/phony solution really but one related to blazor and not the tabstrip itself in any way. Ideally MS needs to allow layouts to have parameters that can be modified to force a state change in the layout.

### Response

**Dimo** commented on 03 Jun 2021

Thanks for the follow-up and information, Lawrence!
