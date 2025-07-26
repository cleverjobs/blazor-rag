# Boolean Columns

## Question

**Mic** asked on 04 Oct 2019

Is it possible to show something else than "True/False" for a Boolean Column? CheckBox, PNG of a checkmark, a light, etc...

## Answer

**Marin Bratanov** answered on 04 Oct 2019

Hello Michael, I am pasting here my response from your private ticket on the subject: You can do this by using templates - the <Template> for read mode, and the <EditorTemplate> for edit mode in case you want to alter the default checkbox. Here's more information about them: [https://docs.telerik.com/blazor-ui/components/grid/templates.](https://docs.telerik.com/blazor-ui/components/grid/templates.) Regards, Marin Bratanov

### Response

**Greg** answered on 08 Feb 2021

Please post a specific example of how to do this here.

### Response

**Eric R | Senior Technical Support Engineer** answered on 08 Feb 2021

Hi Greg, We like to make all demos included with the UI framework available publicly. In this case, the UI for Blazor demos are available at Blazor Components Demos and Examples - Telerik UI for Blazor and the Grid Template demo is available at Blazor DataGrid Demos - Templates | Telerik UI for Blazor. For specific example, see the following code and output section. Simple Boolean Template In the following sample, if the IsActive property is true it will display Is Active and if it is false it will display Not Active. Page Markup and Code @page "/"
@using GridTemplateBooleanColumn.Data
@inject ProductService ProductService <h1> Grid Template Column </h1> <TelerikGrid Data="Products"> <GridColumns> <GridColumn Field="@nameof(Product.ID)" Title="@nameof(Product.ID)" Editable="false"> </GridColumn> <GridColumn Field="@nameof(Product.Name)" Title="@nameof(Product.Name)"> </GridColumn> <GridColumn Field="@nameof(Product.IsActive)" Title="@nameof(Product.IsActive)"> <Template> @{
Product product=context as Product;
if (product.IsActive)
{ <span> Is Active </span> }
else
{ <span> Not Active </span> }
} </Template> </GridColumn> </GridColumns> </TelerikGrid> <br /> @code {
IEnumerable <Product> Products;

protected override void OnInitialized()
{
Products=ProductService.GetProducts();
}
} The Output Wrapping Up I hope the public demos and the previous example illustrates the possibilities with changing the output value of a Boolean Column with Templates. If it doesn't, I encourage opening a Support Ticket through your Telerik Account. This will give us the opportunity to address more specific questions. Please let me know if you need any additional information. Thank you for using the UI for Blazor Forums. Regards, Eric R | Senior Technical Support Engineer
