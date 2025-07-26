# GridColumn definition with condition mixes column order / Dynamic Grid columns

## Question

**Chr** asked on 17 Feb 2022

I have defined a Combobox where the user can choose between various templates. After changing the Template (value in Combobox) a TelerikGrid will change the number/order of columns in the grid. Depending on the defined column name (Name=="Spacer" via a conditional if) I will create one column differently. This will end up as an unexpected order of the columns. See order of columns in method CreateTemplates. This is only a simple example, but I have more complex conditions for creating GridColumns depending on the data which I want to display. What is wrong? My expectation is the TelerikGrid should display the column as defined in IList<Template> Templates Razor Selection: <div class="row"> <div class="column"> <label> Template: <select class="form-control col-12" @onchange="@OnSelectTemplate"> @foreach (var template in Templates)
{
if (template.Name==_selectedTemplate.Name)
{ <option value="@template.Name" selected> @template.Name </option> }
else
{ <option value="@template.Name"> @template.Name </option> }
} </select> </label> </div> </div> Razor Grid: <TelerikGrid Data="@Data" Pageable="false" Resizable="true" Sortable="false" EditMode="@GridEditMode.Incell" Width="1200px" Height="600px" OnUpdate="@UpdateHandler" SelectionMode="@GridSelectionMode.Single"> <GridColumns> @{
// Data is provided
if (Data !=null && Data.Any())
{
// ....Fill Grid
}
else
{
// No Data provided
foreach (var column in ColumnList)
{
if (column.Name=="Spacer")
{ <GridColumn Field="" Title="XXX" Width="20px" Resizable="false" Editable="false" Id="Spacer" /> }
else
{ <GridColumn Id="@column.Name" Field="@column.Name" Title="@column.Caption" Width="@(column.Width + $" px ")" Resizable="true" FieldType="@typeof(string)" /> }
}
}
} </GridColumns> </TelerikGrid> Class Template: public class Template { public string Name { get; set; } public IEnumerable<TemplateColumn> Columns { get; set; } public static IList<Template> CreateTemplates ( ) { var result=new List<Template>()
{ new Template()
{
Name="Template 1",
Columns=new List<TemplateColumn>()
{ new TemplateColumn()
{
Name="ID",
Caption="ID",
IsReadOnly=true,
Width=80 }, new TemplateColumn()
{
Name="Desc_EN",
Caption="Description",
IsReadOnly=false,
Width=250 }, new TemplateColumn()
{
Name="Spacer",
Caption="XXX",
IsReadOnly=true,
Width=20 }, new TemplateColumn()
{
Name="Desc_DE",
Caption="Description german",
IsReadOnly=false,
Width=250 },
}
}, new Template()
{
Name="Template 2",
Columns=new List<TemplateColumn>()
{ new TemplateColumn()
{
Name="ID",
Caption="ID",
IsReadOnly=true,
Width=80 }, new TemplateColumn()
{
Name="Spacer",
Caption="XXX",
IsReadOnly=true,
Width=20 }, new TemplateColumn()
{
Name="Desc_DE",
Caption="Description german",
IsReadOnly=false,
Width=250 }, new TemplateColumn()
{
Name="Desc_EN",
Caption="Description",
IsReadOnly=false,
Width=250 },
}
}
}; return result;
}
} Class TemplateColumn: public class TemplateColumn { public string Name { get; set; } public string Caption { get; set; } public int Width { get; set; } public bool IsReadOnly { get; set; }
} Additional Razor Code: @code { private List <BomItemDto> Data { get; set; }=new List<BomItemDto>(); private IList <Template> Templates { get; set; }=new List<Template>(); private Template _selectedTemplate; public IList <TemplateColumn> ColumnList { get; set; }=new List<TemplateColumn>(); protected override async Task OnInitializedAsync ( ) { var bomTemplates=Template.CreateTemplates();

Templates=bomTemplates.ToList();
_selectedTemplate=bomTemplates.FirstOrDefault();

ColumnList=_selectedTemplate.Columns.ToList();
} private async Task OnSelectTemplate ( ChangeEventArgs e ) { var selectedTemplateName=e.Value.ToString();
_selectedTemplate=Templates.FirstOrDefault(p=> p.Name==selectedTemplateName); var columnList=_selectedTemplate.Columns.ToList();

ColumnList.Clear();
ColumnList=columnList;
} private async Task UpdateHandler ( GridCommandEventArgs args ) {
}


}

## Answer

**Marin Bratanov** answered on 17 Feb 2022

Hello, If you use the Visible parameter of the columns to choose whether they render or not (set it to false to hide them), their order will be preserved when you toggle it to true. Regards, Marin Bratanov

### Response

**Chris1108** commented on 18 Feb 2022

Thanks Martin for your answer, but due to my dynamic changing the grid columns this will not help to toggle only the visible parameter. Lets add more complexity to the creation process of my grid columns: Render columns differently depending on the column prefix name: if (column.Name.StartsWith( "ABC_" ))
{
var colEditable=!column.IsReadOnly; <GridColumn Field="@column.Name" Title="@column.Caption" Width="@(column.Width + $" px ")" Resizable="true" Editable="@colEditable" OnCellRender=" OnABCDataCellRender " /> }

if (column.Name.StartsWith( "DEF_" ))
{ <GridColumn Field="@column.Name" Title="@column.Caption" Width="@(column.Width + $" px ")" Resizable="true" Editable="false" OnCellRender=" OnDEFDataCellRender " /> } Expand each entry of a Dictionary property as an additional column: public class TemplateColumn {
... public IDictionary<string, string> Quantities { get; set; }
} @if (Data !=null && Data.Any())
{
var firstItem=Data.First();
var dictionaryItem=firstItem.Quantities;

foreach (var column in TreeColumnList)
{
...
if (column.Name=="Quantity"))
{
foreach (var item in dictionaryItem)
{ <GridColumn Title="@item.Key" Width="@(column.Width + $" px ")" Resizable="true" OnCellRender="OnDataCellRender" Editable="false"> <Template> @((context as DataItem).Quantities[item.Key]) </Template> </GridColumn> }

...
}
...
}

... This will also leed into a mixing of columns ordering when changing the value from my select box
