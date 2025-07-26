# Bug with sorting columns in grid with detail template

## Question

**Iva** asked on 22 Sep 2020

1. Replace MainLayout with TelerikDrawer [https://github.com/telerik/blazor-ui/tree/master/drawer/template](https://github.com/telerik/blazor-ui/tree/master/drawer/template) 2. Place simple Grid with detail template [https://docs.telerik.com/blazor-ui/components/grid/hierarchy](https://docs.telerik.com/blazor-ui/components/grid/hierarchy) 3. Bug - Latest column from parent grid becomes disabled for sorting. <TelerikGrid Data="salesTeamMembers" @ref="Grid" Sortable="true" FilterMode=@GridFilterMode.FilterMenu Height="780px"> <DetailTemplate> <span>Any template</span> </DetailTemplate> <GridColumns> <GridColumn Field="Id"></GridColumn> <GridColumn Field="Name"></GridColumn> <GridColumn Field="Order"></GridColumn> </GridColumns> </TelerikGrid> If remove detail tempate, all columns becomes availavle for sorting as expected

## Answer

**Marin Bratanov** answered on 23 Sep 2020

Hi Ivan, Thank you for your report. I made this page where you can Follow the status of this fix: [https://feedback.telerik.com/blazor/1485924-cannot-sort-the-last-grid-column-when-in-a-drawer-content-when-the-grid-has-a-detailtemplate](https://feedback.telerik.com/blazor/1485924-cannot-sort-the-last-grid-column-when-in-a-drawer-content-when-the-grid-has-a-detailtemplate) Regards, Marin Bratanov

### Response

**Ivan** answered on 08 Oct 2020

Dear developers, this is actually a very unpleasant defect in the control. If you have a nested template, it becomes impossible to customize the column sorting and you have to disable sorting for the entire grid. The reason for the error is simple - the source code apparently forgot to take into account that if there is a nested template, the first column of the grid is not a data column. Most likely an error in column indexing.

### Response

**Marin Bratanov** answered on 08 Oct 2020

Hi Ivan, I have raised the priority of this as much as possible, yet it also has to follow procedures, and determining its priority in the backlog need to take into account many other factors such as other tasks with higher priority, impact and urgency, and the popularity of this issue - so far this is the only time it has been hit in about half a year since we have the drawer component. A workaround I can suggest is that you consider using a button in a grid column to show additional details in a Window component instead of the DetailTemplate, in a fashion similar to this custom popup editing example. Regards, Marin Bratanov
