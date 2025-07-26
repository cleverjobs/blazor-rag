# Grid Custom Filter Row

## Question

**Mic** asked on 05 Aug 2020

Hi everyone, I've been testing the new features of the Telerik Grid and i've encountered a behavior that i can't quite understand. My Custom Filter Row is applied but to the previous column as it shows in the attached screenshot. Here is the entire code of my Grid : <TelerikGrid Data="@listDemandes" PageSize="10" Pageable="true" Sortable="true" Groupable="false" Reorderable="false" Resizable="true" FilterMode="Telerik.Blazor.GridFilterMode.FilterRow" OnUpdate="@UpdateHandler" OnEdit="@EditHandler" OnDelete="@DeleteHandler" OnCreate="@CreateHandler"> <DetailTemplate Context="ctxDemande"> @{ var demande=ctxDemande as WillyDemande; <TelerikGrid Data="demande.WillyMachines" Pageable="false"> <DetailTemplate Context="ctxMachine"> @{ var machine=ctxMachine as WillyMachine; <TelerikGrid Data="machine.WillyResults" Pageable="false"> <GridColumns> <GridColumn Field=@nameof(WillyResult.Type) Title="Type" Filterable="true" Editable="false" /> <GridColumn Field=@nameof(WillyResult.Description) Title="Description" Filterable="true" Editable="false" /> </GridColumns> </TelerikGrid> } </DetailTemplate> <GridColumns> <GridColumn Field=@nameof(WillyMachine.DocumentType) Title="Type" Filterable="true" Editable="false" /> <GridColumn Field=@nameof(WillyMachine.Statut) Title="Statut" Filterable="true" Editable="false" /> <GridColumn Field=@nameof(WillyMachine.DateDebut) Title="Debut" Filterable="true" Editable="false" /> <GridColumn Field=@nameof(WillyMachine.DateFin) Title="Fin" Filterable="true" Editable="false" /> <GridColumn Field=@nameof(WillyMachine.Performance) Title="Performance" Filterable="true" Editable="false" /> </GridColumns> </TelerikGrid> } </DetailTemplate> <GridColumns> <GridColumn Field=@nameof(WillyDemande.DessinCommande) Title="Commande" Editable="false"> <Template> @{ var ctx=context as WillyDemande; <input type="checkbox" disabled @bind="ctx.DessinCommande" /> } </Template> </GridColumn> <GridColumn Field=@nameof(WillyDemande.Username) Title="Usager" Editable="false"> <FilterCellTemplate> @*<TelerikComboBox Data="@CurrentUsernames" Value="@UserName" Filterable="true" ValueChanged="@(async (string val)=> { UserName=val; var filter=context.FilterDescriptor.FilterDescriptors[0] as FilterDescriptor; filter.Value=UserName; if (string.IsNullOrEmpty(UserName)) { await context.ClearFilterAsync(); } else { await context.FilterAsync(); } })"> </TelerikComboBox>*@</FilterCellTemplate> </GridColumn> <GridColumn Field=@nameof(WillyDemande.SendingComputer) Title="Poste" Editable="false"> <FilterCellTemplate> <TelerikComboBox Data="@CurrentSendingComputers" Value="@SendingComputer" Filterable="true" ValueChanged="@(async (string val)=> { SendingComputer=val; var filter=context.FilterDescriptor.FilterDescriptors[0] as FilterDescriptor; filter.Value=SendingComputer; if (string.IsNullOrEmpty(SendingComputer)) { await context.ClearFilterAsync(); } else { await context.FilterAsync(); } })"> </TelerikComboBox> </FilterCellTemplate> </GridColumn> <GridColumn Field="IdPartNavigation.Name" Title="Configuration" Editable="false" /> <GridColumn Field="IdPartNavigation.Revision" Title="Révision" Editable="false" /> <GridColumn Field=@nameof(WillyDemande.Eco) Title="ECO" Editable="false"> <FilterCellTemplate> <TelerikComboBox Data="@CurrentECOs" Value="@ECO" Filterable="true" ValueChanged="@(async (string val)=> { ECO=val; var filter=context.FilterDescriptor.FilterDescriptors[0] as FilterDescriptor; filter.Value=ECO; if (string.IsNullOrEmpty(ECO)) { await context.ClearFilterAsync(); } else { await context.FilterAsync(); } })"> </TelerikComboBox> </FilterCellTemplate> </GridColumn> <GridColumn Field=@nameof(WillyDemande.ProjectName) Title="Projet" Editable="false" /> <GridColumn Field=@nameof(WillyDemande.WilmaRbre) Title="RBRE" Editable="false"> <Template> @{ var ctx=context as WillyDemande; <input type="checkbox" disabled @bind="ctx.WilmaRbre" /> } </Template> </GridColumn> <GridColumn Field=@nameof(WillyDemande.WilmaRbtk) Title="RBTK" Editable="false"> <Template> @{ var ctx=context as WillyDemande; <input type="checkbox" disabled @bind="ctx.WilmaRbtk" /> } </Template> </GridColumn> <GridColumn Field=@nameof(WillyDemande.WilmaTls) Title="RBLK" Editable="false"> <Template> @{ var ctx=context as WillyDemande; <input type="checkbox" disabled @bind="ctx.WilmaTls" /> } </Template> </GridColumn> <GridColumn Field=@nameof(WillyDemande.WilmaTq) Title="TQUE" Editable="false"> <Template> @{ var ctx=context as WillyDemande; <input type="checkbox" disabled @bind="ctx.WilmaTq" /> } </Template> </GridColumn> <GridColumn Field=@nameof(WillyDemande.WilmaTc) Title="TCON" Editable="false"> <Template> @{ var ctx=context as WillyDemande; <input type="checkbox" disabled @bind="ctx.WilmaTc" /> } </Template> </GridColumn> <GridColumn Field=@nameof(WillyDemande.PdfOnly) Title="PDF Only" Editable="false"> <Template> @{ var ctx=context as WillyDemande; <input type="checkbox" disabled @bind="ctx.PdfOnly" /> } </Template> </GridColumn> <GridColumn Field=@nameof(WillyDemande.DateProduite) Title="Produite" Editable="false" /> <GridColumn Field=@nameof(WillyDemande.Priority) Title="Priorité" Editable="false"> <FilterCellTemplate> <TelerikComboBox Data="@CurrentPriorities" Value="@Priority" Filterable="true" ValueChanged="@(async (string val)=> { Priority=val; var filter=context.FilterDescriptor.FilterDescriptors[0] as FilterDescriptor; filter.Value=Priority; if (string.IsNullOrEmpty(Priority)) { await context.ClearFilterAsync(); } else { await context.FilterAsync(); } })"> </TelerikComboBox> </FilterCellTemplate> </GridColumn> <GridColumn Field=@nameof(WillyDemande.Statut) Title="Statut" Editable="false"> <FilterCellTemplate> <TelerikComboBox Data="@CurrentStatuts" Value="@Statut" Filterable="true" ValueChanged="@(async (string val)=> { Statut=val; var filter=context.FilterDescriptor.FilterDescriptors[0] as FilterDescriptor; filter.Value=Statut; if (string.IsNullOrEmpty(Statut)) { await context.ClearFilterAsync(); } else { await context.FilterAsync(); } })"> </TelerikComboBox> </FilterCellTemplate> </GridColumn> <GridColumn Field=@nameof(WillyDemande.StatutSyteline) Title="Importé" Editable="false"> <Template> @{ var ctx=context as WillyDemande; <input type="checkbox" disabled @bind="ctx.StatutSyteline" /> } </Template> </GridColumn> <GridColumn Field=@nameof(WillyDemande.DateSyteline) Title="Importation" Editable="false" /> <GridColumn Field=@nameof(WillyDemande.ServerName) Title="Serveur" Editable="false"> <FilterCellTemplate> <TelerikComboBox Data="@CurrentServerNames" Value="@ServerName" Filterable="true" ValueChanged="@(async (string val)=> { ServerName=val; var filter=context.FilterDescriptor.FilterDescriptors[0] as FilterDescriptor; filter.Value=ServerName; if (string.IsNullOrEmpty(ServerName)) { await context.ClearFilterAsync(); } else { await context.FilterAsync(); } })"> </TelerikComboBox> </FilterCellTemplate> </GridColumn> <GridColumn Field=@nameof(WillyDemande.DateDebut) Title="Début" Editable="false" /> <GridColumn Field=@nameof(WillyDemande.DateFin) Title="Fin" Editable="false" /> <GridColumn Field=@nameof(WillyDemande.Performance) Title="Performance" Editable="false" /> <GridColumn Field=@nameof(WillyDemande.PathModel) Title="Emplacement" Editable="false" /> <GridColumn Field=@nameof(WillyDemande.MailAddress) Title="Courriel" Editable="false" /> <GridCommandColumn> <GridCommandButton Command="Save" Icon="save" ShowInEdit="true">Mettre à jour</GridCommandButton> <GridCommandButton Command="Delete" Icon="delete">Supprimer</GridCommandButton> <GridCommandButton Command="Cancel" Icon="cancel" ShowInEdit="true">Cancel</GridCommandButton> </GridCommandColumn> </GridColumns> </TelerikGrid>

## Answer

**Michael** answered on 05 Aug 2020

I'm fairly confident that this is caused by the Multi-level hierarchy. I seems that DetailTemplate doesn't take the "+" column in consideration.

### Response

**Marin Bratanov** answered on 05 Aug 2020

Hi Michael, Can you give the 2.16.0 version a try? it just went live a couple of hours ago. With it, the following seems to work fine for me, so perhaps what you are facing will be fixed too (I can't really run it to confirm). @using Telerik.DataSource

<TelerikGrid Data="salesTeamMembers" FilterMode="@GridFilterMode.FilterRow">
<DetailTemplate>
@{ var employee=context as MainModel;
<TelerikGrid Data="employee.Orders" Pageable="true" PageSize="5">
<GridColumns>
<GridColumn Field="OrderId"></GridColumn>
<GridColumn Field="DealSize"></GridColumn>
</GridColumns>
</TelerikGrid>
}
</DetailTemplate>
<GridColumns>
<GridColumn Field="Id"></GridColumn>
<GridColumn Field="Name"></GridColumn>
<GridColumn Field="Age">
<FilterCellTemplate>
@{ // we store a reference to the filter context to use in the business logic // you can also use it inline in the template, like with the Clear button below theFilterContext=context;
}

<label for="min">Min:&nbsp;</label>
<TelerikNumericTextBox Id="min" @bind-Value="@MinValue" OnChange="@SetupFilterRule">
</TelerikNumericTextBox>
<label for="min">Max:&nbsp;</label>
<TelerikNumericTextBox Id="max" @bind-Value="@MaxValue" OnChange="@SetupFilterRule">
</TelerikNumericTextBox>
<TelerikButton ButtonType="ButtonType.Button" Class="k-clear-button-visible ml-2" Icon="filter-clear" Enabled="@( MinValue !=null || MaxValue !=null )" OnClick="@(async ()=>
{
MinValue=MaxValue=null;

// clear filter through the method the context provides
await context.ClearFilterAsync();
})">
</TelerikButton>
</FilterCellTemplate>
</GridColumn>
</GridColumns>
</TelerikGrid>

@code {
List<MainModel> salesTeamMembers { get; set; }

FilterCellTemplateContext theFilterContext { get; set; } public decimal? MinValue { get; set; } public decimal? MaxValue { get; set; } async Task SetupFilterRule ( ) { // set up min value filter - there is one default filter descriptor // that alredy has the field set up, so we use that for the MIN filter // and set up a value and operator var filter1=theFilterContext.FilterDescriptor.FilterDescriptors[ 0 ] as FilterDescriptor;
filter1.Value=MinValue==null? int.MinValue : MinValue;
filter1.Operator=FilterOperator.IsGreaterThan; // set up max value filter - we may have to crete a new filter descriptor // if there wasn't one already so we prepare it first and check whether we have the second filter var filter2Val=MaxValue==null? int.MaxValue : MaxValue; var filter2=new FilterDescriptor( "Age", FilterOperator.IsLessThan, filter2Val);
filter2.MemberType=typeof ( decimal ); if (theFilterContext.FilterDescriptor.FilterDescriptors.Count> 1 )
{
theFilterContext.FilterDescriptor.FilterDescriptors[ 1 ]=filter2;
} else {
theFilterContext.FilterDescriptor.FilterDescriptors.Add(filter2);
} // ensure logical operator between the two filters is AND (it is the default, but we showcase the option) theFilterContext.FilterDescriptor.LogicalOperator=FilterCompositionLogicalOperator.And; // invoke filtering through the method the context provides await theFilterContext.FilterAsync();
} protected override void OnInitialized ( ) {
salesTeamMembers=GenerateData();
} private List<MainModel> GenerateData ( ) {
List<MainModel> data=new List<MainModel>(); for ( int i=1; i <6; i++)
{
MainModel mdl=new MainModel { Id=i, Name=$"Name {i} ", Age=18 + i };
mdl.Orders=Enumerable.Range( 1, 15 ).Select(x=> new DetailsModel { OrderId=x, DealSize=x ^ i }).ToList();
data.Add(mdl);
} return data;
} public class MainModel { public int Id { get; set; } public string Name { get; set; } public int Age { get; set; } public List<DetailsModel> Orders { get; set; }
} public class DetailsModel { public int OrderId { get; set; } public double DealSize { get; set; }
}
} Regards, Marin Bratanov

### Response

**Michael** answered on 05 Aug 2020

Wow! It is indeed fixed! Funny fact, I looked up for an update right before posting this. Bad timing it was! Consider this one solved
