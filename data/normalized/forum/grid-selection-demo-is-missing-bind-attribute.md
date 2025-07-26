# Grid Selection demo is missing bind attribute

## Question

**Rya** asked on 17 Oct 2019

The Grid Selection demo code is missing the @bind-SelectedItems attribute. The demo is on this page: [https://demos.telerik.com/blazor-ui/grid/selection.](https://demos.telerik.com/blazor-ui/grid/selection.) The TelerikGrid element should contain the attribute: @bind-SelectedItems="SelectedItems"

## Answer

**Marin Bratanov** answered on 17 Oct 2019

Hi Ryan, Thank you for noticing. If we do this binding on the demo, we will have to cater for handling those selected items when the selection mode gets changed, and that's not very likely to happen in a real app. Nevertheless, we will consider the idea. In the meantime, you can find examples of binding the collection and using the event in the documentation: for multiple selection: [https://docs.telerik.com/blazor-ui/components/grid/selection/multiple](https://docs.telerik.com/blazor-ui/components/grid/selection/multiple) for single selection: [https://docs.telerik.com/blazor-ui/components/grid/selection/single](https://docs.telerik.com/blazor-ui/components/grid/selection/single) Regards, Marin Bratanov

### Response

**Ryan** answered on 17 Oct 2019

Hi Marin, the demo code was a bit confusing because it declares and sets the SelectedItems variable but it does not get used. Instead of binding the variable, you could remove these lines: public IEnumerable<Product> SelectedItems { get; set; } SelectedItems=GridData.Where(item=> item.ProductId> 3 && item.ProductId <6).ToList();

### Response

**Marin Bratanov** answered on 17 Oct 2019

I agree with you completely, and at this point I think we will just use the two-way binding on the demo and combine the current two demos into one. That will happen for our next release, though. I am attaching the WIP version (it has not passed QA yet, and changing the selection mode at runtime is not a scenario we envision to be common). In the meantime, the documentation provides 6-7 other examples for selection. Regards, Marin Bratanov
