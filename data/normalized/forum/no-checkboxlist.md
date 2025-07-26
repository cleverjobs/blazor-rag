# No checkboxlist ?

## Question

**Bit** asked on 17 Jun 2020

Any plans to implement a checkboxlist component? Like in the aspnet-ajax library? Would come in handy with several projects im working on [https://docs.telerik.com/devtools/aspnet-ajax/controls/checkboxlist/overview](https://docs.telerik.com/devtools/aspnet-ajax/controls/checkboxlist/overview)

## Answer

**Marin Bratanov** answered on 18 Jun 2020

Hello, This is the first time we receive such a question and in Blazor you can very easily do a loop over the data source you have to render several checkboxes, so the need for a list component decreases dramatically. You an find a very similar example in the second snippet here: [https://docs.telerik.com/blazor-ui/components/checkbox/indeterminate-state](https://docs.telerik.com/blazor-ui/components/checkbox/indeterminate-state) - it uses a loop over a collection called Deliveries. You could, of course, use two-way binding instead, this example showscases the Indeterminate state. Would such a setup work for you? Would you expect a checkboxlist component to provide anything else? Regards, Marin Bratanov

### Response

**BitShift** answered on 18 Jun 2020

Yes, thats more or less what I ended up doing. Still kinda new but im getting the hang of it. Liking this library so far, especially the grid.
