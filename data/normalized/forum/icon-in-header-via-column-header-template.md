# Icon in header (via Column Header Template)

## Question

**Den** asked on 30 Oct 2023

I have been trying to show an icon in a grids header. Therefore I have copied the code from [https://docs.telerik.com/blazor-ui/components/grid/templates/column-header](https://docs.telerik.com/blazor-ui/components/grid/templates/column-header) Sadly, I dont get an icon. The preview of your example doesn't show one either :-( Is there something that has been changed? How can I use the template to show an icon in the header? with kind regards, Dennis de Vries

## Answer

**Hristian Stefanov** answered on 31 Oct 2023

Hi Dennis, The example from the documentation that you have linked uses a Font icon. As of the 4.6 version, the Font Icons were detached from the themes distribution. That means, to make the font icons work, you need to add a dedicated Telerik UI for Blazor CDN link in the " _Host.cshtml " or " index.html " (based on the hosting model) file in your application: <link href="[https://blazor.cdn.telerik.com/blazor/4.6.0/kendo-font-icons/font-icons.css"](https://blazor.cdn.telerik.com/blazor/4.6.0/kendo-font-icons/font-icons.css") rel="stylesheet" type="text/css" /> For more detailed information, here is a knowledge base article we have: Font Icons do not Render in Telerik UI for Blazor 4.6.0. Another option is to use an SVG icon without the need for an additional CDN link: @using Telerik.SvgIcons <TelerikGrid Data="@MyData" Height="300px" Pageable="true" Sortable="true" FilterMode="@GridFilterMode.FilterMenu"> <GridColumns> <GridColumn Field="@(nameof(SampleData.Id))" Title="This title will not be rendered" /> <GridColumn Field="@(nameof(SampleData.Name))" /> <GridColumn Field="HireDate" Width="350px" /> <GridColumn> <HeaderTemplate> <span> <TelerikSvgIcon Icon="@SvgIcon.TableBody" /> Column with Icon </span> </HeaderTemplate> </GridColumn> </GridColumns> </TelerikGrid> @code {
public class SampleData
{
public int Id { get; set; }
public string Name { get; set; }
public DateTime HireDate { get; set; }
}

public IEnumerable <SampleData> MyData=Enumerable.Range(1, 50).Select(x=> new SampleData
{
Id=x,
Name="name " + x,
HireDate=DateTime.Now.AddDays(-x)
});
} Regards, Hristian Stefanov Progress Telerik
