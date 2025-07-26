# Problem with grid in tab

## Question

**Pat** asked on 20 May 2020

Hello, I have a display that contains a tab control with two tabs and each tab containing a grid. The problem is that, when I switch tab, the sorting and filtering of the grid is lost.

## Answer

**Marin Bratanov** answered on 20 May 2020

Hello Patrick, The tab strip renders only the currently active tab. This means that all other tabs are disposed - this is the true blazor way and it improves performance. This also means that if you want to maintain the state of components in those tabs, you should keep that state somewhere (e.g., in the component thathosts the tab strip). The grid offers a state feature that can let you do that easily through a simple in-memory variable in the parent component: [https://docs.telerik.com/blazor-ui/components/grid/state.](https://docs.telerik.com/blazor-ui/components/grid/state.) You may also find interesting this feature request and if so - add your Vote for it and Follow it: [https://feedback.telerik.com/blazor/1431932-tabs-can-hide-with-css-only-to-avoid-re-initializing](https://feedback.telerik.com/blazor/1431932-tabs-can-hide-with-css-only-to-avoid-re-initializing) Regards, Marin Bratanov
