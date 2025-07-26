# Row Details

## Question

**Ste** asked on 21 Nov 2020

Hello, coming from WPF, I was wondering if there was any way to implement RowDetails and RowDetail templates as in the radGridView [https://docs.telerik.com/devtools/wpf/controls/radgridview/row-details/overview](https://docs.telerik.com/devtools/wpf/controls/radgridview/row-details/overview) many thanks regards

## Answer

**Marin Bratanov** answered on 22 Nov 2020

Hello Stephane, The Blazor grid has the DetailTemplate which serves the same purpose: [https://docs.telerik.com/blazor-ui/components/grid/hierarchy.](https://docs.telerik.com/blazor-ui/components/grid/hierarchy.) It even provides extremely easy load on demand: [https://github.com/telerik/blazor-ui/tree/master/grid/load-on-demand-hierarchy.](https://github.com/telerik/blazor-ui/tree/master/grid/load-on-demand-hierarchy.) Alternatively, the RowClick or the item selection can let you respond to clicks on the row to do something else outside the grid: [https://docs.telerik.com/blazor-ui/components/grid/events#onrowclick](https://docs.telerik.com/blazor-ui/components/grid/events#onrowclick) [https://docs.telerik.com/blazor-ui/components/grid/selection/single](https://docs.telerik.com/blazor-ui/components/grid/selection/single) Regards, Marin Bratanov

### Response

**Stephane** answered on 27 Nov 2020

Thank you very much, I've downloaded the repo, very useful. A related question if I may: I have 3 levels of hierarchy. The second is loaded on demand. The third from code because not all rows at that level have a detail and I want to expand it automatically when it exists. So I would like to get rid of the expand/collapse button at that level. Any way I could achieve that?

### Response

**Marin Bratanov** answered on 27 Nov 2020

Hi Stephane, You can Follow the implementation of such a feature here: [https://feedback.telerik.com/blazor/1430980-conditionally-hide-hierarchical-grid-expand-button.](https://feedback.telerik.com/blazor/1430980-conditionally-hide-hierarchical-grid-expand-button.) You may also want to Follow this one in case an option different than the state becomes available: [https://feedback.telerik.com/blazor/1442162-expand-open-collapse-hierarchy-programmatically.](https://feedback.telerik.com/blazor/1442162-expand-open-collapse-hierarchy-programmatically.) Regards, Marin Bratanov

### Response

**Stephane** answered on 27 Nov 2020

thank you so much the swift reply!
