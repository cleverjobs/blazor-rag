# Grid custom column ordering problems

## Question

**Jer** asked on 04 Aug 2023

Hi, our team is using - [https://docs.telerik.com/blazor-ui/components/grid/overview](https://docs.telerik.com/blazor-ui/components/grid/overview) We are trying to extend the 'GridColumn' control to have show/hide depending on if our user is authenticated, with some role-based things as well. Where I've gotten to is something like this... //AuthorizedGridColumn.razor @typeparam TItem

@if (IsAuthorized)
{
<GridColumn Field="@Field" Title="@Title">
<Template Context="item">
@ChildContent((TItem)item)
</Template>
</GridColumn>
}

@code {

[ Inject ] private AuthenticationStateProvider AuthenticationStateProvider { get; set; }=null!;
[ Parameter ] public string Field { get; set; }

[ Parameter ] public string Title { get; set; }

[ Parameter ] public RenderFragment<TItem> ChildContent { get; set; }

[ Parameter ] public string PolicyName { get; set; } private bool IsAuthorized { get; set; } protected override async Task OnInitializedAsync () { var authState=await AuthenticationStateProvider.GetAuthenticationStateAsync(); var user=authState.User; if (user.Identity==null )
{
IsAuthorized=false;
} else {
IsAuthorized=user.Identity.IsAuthenticated && user.IsInRole( "Admin" );
} await base.OnInitializedAsync();
}
} With usage that looks like... <AuthorizedGridColumn TItem="OurClass" Field="@nameof(OurClass.OurProperty)" Title="Something">
<ChildContent Context="binding">
@{
<p>Only Admins!</p>
}
</ChildContent>
</AuthorizedGridColumn> Which does work, but the ordering of the columns is incorrect. Instead of displaying in order e.g. I would expect <AuthorizedGridColumn TItem="OurClass" Field="@nameof(OurClass.OurProperty)" Title="Something"> <ChildContent Context="binding"> @{ <p> Only Admins! </p> } </ChildContent> </AuthorizedGridColumn> <GridColumn> </GridColumn> <GridColumn> </GridColumn> To produce something like |AuthorizedColumn|Regular Column|Regular Column| | content| content| content| Instead it renders |Regular Column|Regular Column|Authorized Column| Fwiw the same behavior also seems to be a problem when you do this without the custom control <AuthorizeView Roles="Admin"> <GridColumn> </GridColumn> </AuthorizeView> <GridColumn> </GridColumn> <GridColumn> </GridColumn> Any help is greatly appreciated!

## Answer

**Dimo** answered on 08 Aug 2023

Hi Jeremy, This is how Blazor works - components are initialized and added to the component tree in hierarchy. As a result, the Grid finds out about the authorized column after the other columns, because the authorized columns are one level deeper. To arrange the Grid columns in the expected way, the <GridColumn> tags must be at the same hierarchy level in your app. So, you have two options: Implement a <NonAuthorizedGridColumn> component and put the regular columns inside it. Remove the <AuthorizedColumn> component and move the IsAuthorized check inside <GridColumns>. There is a third option, but it may be the most complex one to implement - reorder the Grid columns via the Grid state in OnStateInit. Regards, Dimo Progress Telerik
