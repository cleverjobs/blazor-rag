# ForeignKey column?

## Question

**Ran** asked on 26 Oct 2019

Does anybody have an example of how to do this in the blazor grid? If not, does anybody have an example of a dropdownlist column template that show the text in the grid but stores the id in the list of items for the grid? Thanks ... Ed

## Answer

**Marin Bratanov** answered on 28 Oct 2019

Hi Ed, At the moment, a built-in feature for foreign keys does not exist. I am not completely sure it makes sense for Blazor because templates here are super powerful, and this can easily be solved through a template: [https://docs.telerik.com/blazor-ui/components/grid/templates.](https://docs.telerik.com/blazor-ui/components/grid/templates.) For example, the editor template example is pretty close to what you described. You can also define a method that returns the desired item from the secondary collection based on the ID coming in from the main one and use that to display data. Or, you could define a view model that contains that data in the first place so you don't need foreign keys at all. Nevertheless, if you would like to see some built-in feature about this, I'd encourage you to post it in the

### Response

**Randy Hompesch** answered on 28 Oct 2019

Yeah, after posting that I later figured out how to use the templates and was on my way. I didn't have a way of going back and deleting the posting. Hopefully, it'll help someone else. Once again... thanks!

### Response

**Rajesh** answered on 05 Dec 2020

Hi Marin, I used Template for foreign key-column into Telerik Blazor grid. But while doing group by and filter its showing Id, instead of name. Can you suggest how can show name instead of id in group by and filter. Here is coloum code:- <GridColumn Field=@nameof(ItemSubCategoryMaster.Category_Id) Editable="true" Title="Category" Width="100%"> <EditorTemplate> @{ currentItem=context as ItemSubCategoryMaster; <TelerikComboBox AllowCustom="false" @bind-Value="@currentItem.Category_Id" Data="@ItemCategoryMasterList" Placeholder="Select Category" TextField="@nameof(ItemCategoryMaster.Category_Description)" ValueField="@nameof(ItemCategoryMaster.Category_Id)" Filterable="true" Id="Category_Id" Width="100%" /> } </EditorTemplate> <Template> @{ int CategoryId=(context as ItemSubCategoryMaster).Category_Id; string Category=ItemCategoryMasterList.Where(x=> x.Category_Id==CategoryId).Select(x=> x.Category_Description).FirstOrDefault(); <text>@Category</text> } </Template> </GridColumn>

### Response

**Marin Bratanov** answered on 07 Dec 2020

Hello Rajesh, The approach is the same - you should use the grid templates to alter what the grid will render. You can find more examples and information in the following KnowledgeBase article: [https://docs.telerik.com/blazor-ui/knowledge-base/grids-foreign-key.](https://docs.telerik.com/blazor-ui/knowledge-base/grids-foreign-key.) Regards, Marin Bratanov

### Response

**Rajesh** answered on 07 Dec 2020

hi Marin , Thanks for feedback. But it's increase too much work for developer. Is it possible to get built-in option for foreign key-column?. It will really help us.

### Response

**Marin Bratanov** answered on 08 Dec 2020

Hello Rajesh, You do not have to implement all the templates, you should implement only the ones you need per your use case. Using the templates will provide full flexibility as opposed to a built-in feature that will still require that you provide the foreign key data and synchronous access to it, but it will be complex to configure, while rather limited in what it could do. How would you expect to expose all those capabilities I've showcased in the KB through some built-in feature? Regards, Marin Bratanov
