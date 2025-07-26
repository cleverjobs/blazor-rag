# Optional Column Header Template

## Question

**Mar** asked on 10 Aug 2022

Is there a way to have the column header template be optional? Depending upon some values in my data, I might need to use a header template for a specific column, otherwise, I would like the have the default behavior. I tried placing an if statement inside the <GridColumn/> element like this: <GridColumn Field="" FieldType=""> @if (_useHeaderTemplate)
{ <HeaderTemplate> </HeaderTemplate> } </GridColumn> This results in a compile error of "Unrecognized child content inside component ...." I then tried <GridColumn Field="" FieldType=""> <HeaderTemplate> @if (_useHeaderTemplate)
{ <div>Custom Header </div> } </HeaderTemplate> </GridColumn> This results in no text being rendered for the column header. I'm trying to avoid (a) duplicating the <GridColumn/> configuration for both the true and false evaluations of the if statement; (b) I don't want to take over the complete rendering and management of the grid column header. I still want the framework to handle that. Thanks -marc

## Answer

**Dimo** answered on 11 Aug 2022

Hello Marc, The GridColumn component does not have a ChildContent property of type RenderFragment. That's why you can't place arbitrary content inside it (such as conditional statements or anything other than predefined <...Template> tags). On the other hand, you are not taking over the whole rendering if you have the conditional statement inside the <HeaderTemplate>. The following two columns will render identical header cell content: <TelerikGrid Data="@GridData" TItem="@Product" Pageable="true" Sortable="true" FilterMode="GridFilterMode.FilterMenu"> <GridColumns> <GridColumn Field="@nameof(Product.Name)" Title="Product Name" /> <GridColumn Field="@nameof(Product.Name)"> <HeaderTemplate> Product Name </HeaderTemplate> </GridColumn> </GridColumns> </TelerikGrid> @code {
List<Product> GridData { get; set; } protected override void OnInitialized ( ) {
GridData=new List<Product>(); var rnd=new Random(); for (int i=1; i <=7; i++)
{
GridData.Add( new Product ( ) {
Id=i,
Name="Product " + i,
Price=(decimal)rnd.Next( 1, 100 ),
ReleaseDate=DateTime.Now.AddDays(-rnd.Next( 60, 1000 )),
Active=i % 3==0 });
}
} public class Product { public int Id { get; set; } public string Name { get; set; } public decimal Price { get; set; } public DateTime ReleaseDate { get; set; } public bool Active { get; set; }
}
} Regards, Dimo
