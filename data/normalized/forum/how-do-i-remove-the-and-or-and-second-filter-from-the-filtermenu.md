# How do I remove the And/Or and second filter from the FilterMenu?

## Question

**Tim** asked on 05 Jun 2021

I tried this.... But I end up with nothing.... <GridColumn Width="7%" Field="@nameof(VehiclePartModel.YearId)"> <FilterMenuTemplate> @{ if (context is FilterMenuTemplateContext filterMenuTemplateContext) { filterMenuTemplateContext.FilterDescriptor.FilterDescriptors.Clear(); filterMenuTemplateContext.FilterDescriptor.FilterDescriptors.Add(new FilterDescriptor(nameof(VehiclePartModel.YearId), FilterOperator.IsEqualTo, string.Empty)); } } </FilterMenuTemplate> </GridColumn>

## Answer

**Svetoslav Dimitrov** answered on 09 Jun 2021

Hello Timothy, We have a knowledge-based article that shows how to remove the second filter from the FilterMenu. Can you give the solution in this article a go and get back to me if you achieved the desired result? Regards, Svetoslav Dimitrov Progress Telerik
