# Grid sorting state lost when using tabs

## Question

**Dou** asked on 02 Dec 2020

I am using a telerik tab control with a grid in one tab. If you sort, filter, or page the grid; the state will be lost if you click into a tab and then back to the tab with the grid. What's the proper way to save this state? Thanks - Doug

## Answer

**Marin Bratanov** answered on 03 Dec 2020

Hi Doug, The following demo showcases how you can persist the grid state: [https://demos.telerik.com/blazor-ui/grid/persist-state.](https://demos.telerik.com/blazor-ui/grid/persist-state.) You can read more about it in the documentation to see more details on what you can do with the state: [https://docs.telerik.com/blazor-ui/components/grid/state.](https://docs.telerik.com/blazor-ui/components/grid/state.) For example, storing the state in OnStateChanged can let you restore it later easily. You may also want to Follow this feature request for a feature in the tab strip that would let you avoid re-initializing components inside: [https://feedback.telerik.com/blazor/1431932-tabs-can-hide-with-css-only-to-avoid-re-initializing.](https://feedback.telerik.com/blazor/1431932-tabs-can-hide-with-css-only-to-avoid-re-initializing.) I've added your Vote for it on your behalf to raise its priority, and you can click the Follow button for status update emails. Regards, Marin Bratanov

### Response

**Doug** answered on 03 Dec 2020

Thanks. That feature request is exactly what I am looking for. I use tabs for similarly, where the first tab is a grid of records. Subsequent tabs or detail of the records and their related records.
