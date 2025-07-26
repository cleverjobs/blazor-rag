# Telerik Blazor Grid - TelerikCheckBoxListFilter use LogicalOperator = FilterCompositionLogicalOperator.Or

## Question

**Adr** asked on 26 May 2021

I have implemented a TelerikCheckBoxListFilter as shown in: [https://docs.telerik.com/blazor-ui/components/grid/filter/checkboxlist#custom-data](https://docs.telerik.com/blazor-ui/components/grid/filter/checkboxlist#custom-data) My code looks like this. <FilterMenuTemplate Context="context"> <TelerikCheckBoxListFilter Data="@ManufacturersList" Field="@(nameof(ManufacturerCodeFilterOption.Make))" @bind-FilterDescriptor="@context.FilterDescriptor"> </TelerikCheckBoxListFilter> </FilterMenuTemplate> The TelerikCheckBoxListFilter renders as expected but when I try to apply selected items to filter the data, it builds those individual selected items with an "AND" clause. Is it possible to change the LogicalOperator for the FilterDescriptor it uses to use "OR" clauses between the selected items?

## Answer

**Marin Bratanov** answered on 26 May 2021

Hello Adrian, You have three options: use the OnRead event to get the DataSourceRequest that describes the grid and alter it - either immediately, or only on the server backend just before shaping the data use the StateChanged event of the grid state to change the state to alter the desired filter operator (see the "Get and Override User Action That Changes The Grid" section for a similar example) implement a custom filter template where you will have full control over the UI, UX and the way you generate filter operator collections Regards, Marin Bratanov Progress Telerik

### Response

**Adrian** commented on 27 May 2021

As suggested above I have used option 3 and implemented my own FilterMenuTemplate. Is there a way I can convert this FilterMenuTemplate I have added to a single grid into a reusable RenderFragment/Component so that I can add it to X number of grids without the need to duplicate the same FilterMenuTemplate in each grid?

### Response

**Marin Bratanov** commented on 27 May 2021

You should be able to encapsulate the desired UI and code in a component to reuse - it could take the context of the template as a parameter and raise events to update it. If you make such a sample, you could open a Pull Request with it in this repo, we award such contributions with Telerik points. Just make sure to add a proper attribution to you and/or your company in the readme, credit should go where credit is due.
