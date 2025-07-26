# Is DockManager state saving completely broken?

## Question

**Vit** asked on 27 Mar 2025

Hello Telerik, Thank you for the recently released DockManager component. It really helps, However, I am trying to use the DockManager's persistent state (GetState(), SetState(), OnStateInit, OnStateChanged), and it seems that the DockManagerState object provided by GetState() and the events is simply wrong: Panel sizes are a mix of their current values, old values and the initial Size settings; When restoring a saved state, sizes are applied inconsistently; SetState(null) does literally nothing. My goal is to save the DockManager's layout in an external string, then restart the application and restore the DockManager's layout from that string. From a quick stepthrough, one of the problem places is DockManagerContentPane.SetUnpinned(). It forces a refresh on the same pane that is being configured from the saved state, and its size reverts to the default. Possibly, it happens more often for panes with a constant Id property. Update. If I remove Id properties from all content panes, then the layout has the right size, but all panes are empty. No content. If I put Id properties back, I get the content, but the pane size is lost. Can you please confirm that you are aware of the problem? To create a reproducible example app may be too hard.

## Answer

**Anislav** answered on 27 Mar 2025

Hi Vitaly, The DockManager is a new component, so I also tested its state-saving and restoring functionality, and it appears to work as expected. I created an example that demonstrates this, including a mock application restart: [https://blazorrepl.telerik.com/cJYHQBYZ451qWxq419.](https://blazorrepl.telerik.com/cJYHQBYZ451qWxq419.) Based on your comment, it seems that you might be setting the DockManager state too early. Please note the following from the documentation:> The GetState and SetState methods of the DockManager instance allow you to retrieve and apply the current DockManager state at any time after OnStateInit. It is recommended providing a handler for the OnStateInit event and setting the DockManager state there, if you are not already doing so. Regards, Anislav Atanasov

### Response

**Anislav** commented on 08 Apr 2025

Did you get it working?

### Response

**Vitaly** commented on 20 Apr 2025

Hello Anislav, Sorry about the delay in responding. Yes, thank you, the provided example (as an online sandbox) works as expected. The problem is, it does not exactly match my use scenario for the dock manager. I am attaching a demo project here. This is a Maui Blazor Hybrid application (VS 2022, .Net 8) based on the default project created by Visual Studio. My goal is to have a page with some panes in a dockmanager, where I can save pane sizes between calls to the application and to reset the layout to its "factory settings" with a button click. In the application, on the home page, you will find five "named" content panes arranged in some "unnamed" split container panes. There are also toolbar toggle buttons bound to the same properties as the Visible attributes of the content panes and the Reset button. 1. Hide some panes using their Close icons or the buttons on the toolbar. Click the Reset button. The hidden panes are restored - I take this as a proof that the page can save and restore its state. It works as expected. 2. Resize some panes/splitters. Click the Reset button. The pane sizes are _not_ restored. I take it as a fail. 3. Set a breakpoint in the Home.OnDockManagerStateChanged() method. Close a pane using its Close icon. The breakpoint gets hit, i.e. the OnStateChanged event is fired. Good. Now close a pane using the toggle button on the toolbar. The pane disappears, but the breakpoint is _not_ hit. This may be by-design, but it makes saving the layout a bit harder. 4. In the Home.OnResetLayoutButton() method, replace the call to DockManager.SetState(initialState) with a call to DockManager.SetState(null). This is supposed to work as "restore the initial layout". Hide or resize some panes and click Reset. Nothing happens - the call to SetState(null) does nothing at all. I hope you can point out for me what I am doing wrong, and how I can make the Reset button work correctly in this demo. Closing and reopening the whole page is not a good option. To reduce the demo project size, I have excluded the parts of the demo where I save and load the state from an external storage. It is very likely that, after I get the Reset button to work correctly, all my problems with the saved state will disappear as well.
