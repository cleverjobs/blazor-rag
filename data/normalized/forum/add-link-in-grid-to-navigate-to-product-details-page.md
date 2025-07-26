# Add Link in Grid to Navigate to Product Details Page

## Question

**Rog** asked on 16 Aug 2021

Hi: I'm new to Telerik for Blazor and was hoping to create a column of links in a Products Grid that would bring the user to the Product Details page for the particular link. In particular, I want to go the the @page "/productdetails/{ProductId}" I'm assuming the best method is with a template? Here's what I have so far: <GridColumns> <GridColumn Field="ProductId" Title="Id" /> <GridColumn Field="Product" Title="User" /> <GridColumn> <Template> @{ <div> <a href="#" @onclick=""> Product Details </a> </div> //onclick go to product details page and pass parameter
} </Template> </GridColumn> </GridColumns> @page "/productdetails/{ProductId}" Any help greatly appreciated.

## Answer

**Matthias** answered on 17 Aug 2021

Hi Roger, I also use a template for this. However, in this case I use NavigationManager. <GridColumn Field="@(nameof(customer.CustZip))"> <Template> <span class="span-nav" @onclick="@(()=> _navigationManager.NavigateTo($" CustZipPage /{( context as customer ).CustZip }"))"> @((context as customer).CustZip) </span> </Template> </GridColumn> In the example, only CustZip must be replaced by Id. href is ultimately also used by the NavigationManager. It calls a JavaScript of type "location.href". In this point you can also use your solution. I find NavigationManager in Blazor a bit more consistent. Regards Matthias

### Response

**Roger** commented on 18 Aug 2021

Perfect - thanks Matthias! Regards, Roger
