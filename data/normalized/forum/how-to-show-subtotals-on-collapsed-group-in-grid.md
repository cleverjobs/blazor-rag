# How to show subtotals on collapsed group in grid

## Question

**JimJim** asked on 16 Jul 2021

Hi, I'm relatively new to Blazor and Telerik UI for Blazor. I have a TelerikDataGrid on a page and it is defined to group data up to 6 levels. The grouping works great where the details inside the group are correct. When I collapse the group, I'd like to sum up the columns in the group and show those subtotals on the line with the collapsed group. For example, currently the grouping looks like this: What I'd like to do is something like this : Has anyone done this before? Any suggestions on how to make this happen? Thanks, Jim

## Answer

**Matthias** answered on 16 Jul 2021

Hi Jim, I think that I implemented it in a similar way. Here is a shortened Code-Snippet for my scenario: razor: <TelerikGrid @ref="@Grid" Pageable="false" PageSize="10" Class="GebGrid" OnDelete="@DeleteKarton" Data="@KartonModels" @bind-SelectedItems="@SelectedItems" SelectionMode="@GridSelectionMode.Single"> <GridColumns> <GridColumn Field="@nameof(KartonModel.ID)" Title="Nr" Width="60px"></GridColumn> <GridColumn Field="@nameof(KartonModel.KartonBezeichnung)" Title="Karton"></GridColumn> <GridColumn Field="@nameof(KartonModel.Menge)" Title="Menge" Width="70px"></GridColumn> -> more GridColumn <GridCommandColumn Locked="true" Width="40px"> <GridCommandButton Command="Delete" Icon="delete" Class="cmdBtn">&nbsp;</GridCommandButton> </GridCommandColumn> </GridColumns> <DetailTemplate> <TelerikGrid Data="@Karton.KartonPositionens" ShowColumnMenu="false" Pageable="true" Class="@DetailClass" Sortable="false" RowHeight="20" Resizable="true" EditMode="@GridEditMode.Inline" PageSize="7" OnUpdate=@UpdatePosItem OnDelete=@DeletePosItem> <GridColumns> <GridColumn Field=@nameof(KartonPosition.Einzelpreis) Title="Preis" Editable="false" Width="50px"/> <GridColumn Field=@nameof(KartonPosition.EinzelpreisSumme) Title="Summe" Editable="false" Width="50px"/> -> more GridColumn <GridCommandColumn Locked="true" Width="70px" Context="order"> <GridCommandButton Command="Edit" Icon="edit" Class="cmdBtn"/> <GridCommandButton Command="Delete" Icon="delete" Class="cmdBtn"/> <GridCommandButton Command="Save" Icon="save" ShowInEdit="true" Class="cmdBtn"/> <GridCommandButton Command="Cancel" Icon="cancel" ShowInEdit="true" Class="cmdBtn"/> </GridCommandColumn> </GridColumns> </TelerikGrid> </DetailTemplate> </TelerikGrid> The sum of the groups are calculated in a class like this: public decimal BetragSumme { get { return Convert.ToDecimal(KartonPositionens.Sum((_=> _.EinzelpreisSumme))); } } write if you have any questions about it! Greetings from Berlin Matthias

### Response

**Marin Bratanov** answered on 17 Jul 2021

Hi, You can also use the GroupHeader template to add the aggregation info for the group: [https://docs.telerik.com/blazor-ui/components/grid/templates/group-header.](https://docs.telerik.com/blazor-ui/components/grid/templates/group-header.) You may also find this feature request interesting and useful: [https://feedback.telerik.com/blazor/1456063-group-header-templates-should-expose-aggregates-for-all-the-fields-and-allow-you-to-align-them-with-the-columns.](https://feedback.telerik.com/blazor/1456063-group-header-templates-should-expose-aggregates-for-all-the-fields-and-allow-you-to-align-them-with-the-columns.) If so, Vote for it and Follow it. Regards, Marin Bratanov Progress Telerik
