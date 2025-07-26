# How to reference components inside a Grid DetailTemplate

## Question

**Twa** asked on 20 Oct 2022

Hello. I would like to know how is the best way to reference the components that are inside a grid detail template from the code behind. To exemplify the situation I leave the following code: <TelerikGrid TItem="@MyModel" @ref="_myMainGridReference" OnRead="@OnReadHandler" OnRowDoubleClick="@OnGridDoubleClickHandler">
<GridColumns>
- Main grid columns here -
</GridColumns>
<DetailTemplate>
@{ /* Child component inside detailtemplate=> how can I reference from the code behind? */ var ctex=context as JobViewModel;
<TelerikGrid @ref="??????" Data="@ctex.data" SelectionMode="@GridSelectionMode.Multiple">
<GridColumns>
- Detail grid columns here -
</GridColumns>
</TelerikGrid>
}
</DetailTemplate>
</TelerikGrid> I have some ideas on how to achieve this but I don't know if they are the most appropriate. For that reason I would like to know what your approach would be to solve it. Best regards,

## Answer

**Hristian Stefanov** answered on 25 Oct 2022

Hi Marcos, Here are the two easiest options to use: 1) One reference is responsible for every inner instance <TelerikGrid @ref="Grid" Data="salesTeamMembers"> <DetailTemplate> @{
var employee=context as MainModel; <TelerikGrid @ref="InnerGrid" Data="employee.Orders" Pageable="true" PageSize="5"> <GridColumns> <GridColumn Field="OrderId"> </GridColumn> <GridColumn Field="DealSize"> </GridColumn> </GridColumns> </TelerikGrid> } </DetailTemplate> <GridColumns> <GridColumn Field="Id"> </GridColumn> <GridColumn Field="Name"> </GridColumn> </GridColumns> </TelerikGrid> @code {
public TelerikGrid <MainModel> Grid { get; set; } public TelerikGrid <DetailsModel> InnerGrid { get; set; } List <MainModel> salesTeamMembers { get; set; }

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
mdl.Orders=Enumerable.Range(1, 15).Select(x=> new DetailsModel { OrderId=x, DealSize=x^i }).ToList();
data.Add(mdl);
}
return data;
}

public class MainModel
{
public int Id { get; set; }
public string Name { get;set; }
public List <DetailsModel> Orders { get; set; }
}

public class DetailsModel
{
public int OrderId { get; set; }
public double DealSize { get; set; }
}
} 2) Different references for the different instances <TelerikGrid @ref="Grid" Data="salesTeamMembers"> <DetailTemplate> @{
var employee=context as MainModel; <TelerikGrid @ref="employee.InnerGrid" Data="employee.Orders" Pageable="true" PageSize="5"> <GridColumns> <GridColumn Field="OrderId"> </GridColumn> <GridColumn Field="DealSize"> </GridColumn> </GridColumns> </TelerikGrid> } </DetailTemplate> <GridColumns> <GridColumn Field="Id"> </GridColumn> <GridColumn Field="Name"> </GridColumn> </GridColumns> </TelerikGrid> @code {
public TelerikGrid <MainModel> Grid { get; set; }
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
MainModel mdl=new MainModel { Id=i, Name=$"Name {i}", InnerGrid=new TelerikGrid <DetailsModel> () };
mdl.Orders=Enumerable.Range(1, 15).Select(x=> new DetailsModel { OrderId=x, DealSize=x^i }).ToList();
data.Add(mdl);
}
return data;
}

public class MainModel
{
public int Id { get; set; }
public string Name { get;set; }
public List <DetailsModel> Orders { get; set; } public TelerikGrid <DetailsModel> InnerGrid { get; set; } }

public class DetailsModel
{
public int OrderId { get; set; }
public double DealSize { get; set; }
}
} Choose based on the scenario needs. Additionally, make sure to always check for " null " when operating with the reference because when the parent is collapsed, there is no child rendered. Let me know if we can help with anything else. Regards, Hristian Stefanov Progress Telerik

### Response

**Twain** answered on 23 Dec 2022

Hi Hristian. Thank you for pointing me in the right direction. The second approach fits my needs. Sorry for the late reply. I have been away for the last two months. Regards. Marcos.
