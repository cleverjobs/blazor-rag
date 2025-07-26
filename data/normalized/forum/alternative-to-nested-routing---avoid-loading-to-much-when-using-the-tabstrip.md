# Alternative to nested routing - Avoid loading to much when using the TabStrip

## Question

**Mar** asked on 05 Nov 2021

Blazor has no concept of nested routing which I don't understand Any way I need to find a way to avoid loading a lot of component in a tabstrip. If this was Angular I would define sub routes and clicking on a tab would navigate to that page. What patterns are you using when having a lot of tab items?

### Response

**Marin Bratanov** commented on 06 Nov 2021

The Telerik TabStrip "loads" only the current tab in the sense that it does not initialize the others. You can also control which tab is selected through the ActiveTabIndex parameter (which can be -1 for no selection) so you can capture the routing/url/information that you have incoming, and set the tab index as desired. Then, that tab can have its own components whose events can be used for further async data loading (such as AfterRenderAsync and/or ParametersSetAsync).
