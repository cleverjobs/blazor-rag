# Hierarchical Grid expand/collapse icon

## Question

**Val** asked on 19 Apr 2021

Hello, The Hierarchical Grid allows us to expand its rows by clicking on a + icon. (k-plus / k-minus) How can i change the icon? ( k-i-expand / k-i-collapse) Regards.

## Answer

**Hristian Stefanov** answered on 22 Apr 2021

Hello Valeriy, The easiest way to do that is by overriding the built-in icons with other icons using custom CSS rules. This way, you can change the icons in the Hierarchical Grid however you want. In addition, you can use the Class parameter of the Grid to add custom CSS Class and modify a specific instance of the Grid, instead of all instances in the application. The attached code sample demonstrates how to achieve that. It showcases the general concept of changing the built-in icons in the Hierarchical Grid by adding custom CSS rules. Also, after your question, I have created this knowledge base article for changing built-in icons in the Hierarchical Grid, where anyone interested can see more details related to this case. Regards, Hristian Stefanov Progress Telerik

### Response

**Valeriy** answered on 07 Jun 2023

Hello Hristian, Since the update to version 4.3.0, this solution no longer works. How can I now change built-in SVG icons in the Hierarchical Grid? Regards

### Response

**Hristian Stefanov** commented on 11 Jun 2023

Hi Valeriy, Thank you for notifying us about the need for an update on this article. Indeed, as of version 4.3, the Grid uses SVG icons, and you need to change the path of the <svg> element. To get the desired icons, you can use your browser dev tools to inspect the rendered icon and copy its path value. Here is the updated sample for version 4.3 from the knowledge base article: <style>.custom-icons.k-hierarchy-cell.k-svg-i-plus svg path {
d: path ( 'M352 256 160 384V128l192 128z' );
}.custom-icons.k-hierarchy-cell.k-svg-i-minus svg path {
d: path ( 'M256 352 128 160h256L256 352z' );
} </style> <TelerikGrid Class="custom-icons" Data="salesTeamMembers" @ref="Grid" OnStateInit="@( (GridStateEventArgs<MainModel> args)=> OnStateInit(args))"> <DetailTemplate> @{
var employee=context as MainModel; <TelerikGrid Data="employee.Orders"> <GridColumns> <GridColumn Field="OrderId"> </GridColumn> <GridColumn Field="DealSize"> </GridColumn> </GridColumns> </TelerikGrid> } </DetailTemplate> <GridColumns> <GridColumn Field="Id"> </GridColumn> <GridColumn Field="Name"> </GridColumn> </GridColumns> </TelerikGrid> @code {
public TelerikGrid <MainModel> Grid { get; set; }

async Task OnStateInit(GridStateEventArgs <MainModel> args)
{
//expand first row
args.GridState.ExpandedItems=new List <MainModel> { salesTeamMembers.FirstOrDefault() };
}

List <MainModel> salesTeamMembers { get; set; }

protected override void OnInitialized()
{
salesTeamMembers=GenerateData();
}

private List <MainModel> GenerateData()
{
List <MainModel> data=new List <MainModel> ();
for (int i=0; i <5; i++)
{
MainModel mdl=new MainModel { Id=i, Name=$"Name {i}" };
mdl.Orders=Enumerable.Range(1, 3).Select(x=> new DetailsModel { OrderId=x, DealSize=x ^ i }).ToList();
data.Add(mdl);
}
return data;
}

public class MainModel
{
public int Id { get; set; }
public string Name { get; set; }
public List <DetailsModel> Orders { get; set; }
}

public class DetailsModel
{
public int OrderId { get; set; }
public double DealSize { get; set; }
}
} Please run and test it to see the result. The article will be updated with the above sample very soon. If there are further difficulties with the SVG icons, I remain at your disposal. Kind Regards, Hristian
