# Why is the listview not showing anything?

## Question

**Dav** asked on 07 Feb 2022

I have confirmed that there are items in _ownersWithStatus. But my list is blank. What am I doing wrong? <TelerikListView Data="@_ownersWithStatus" Width="500px">
<HeaderTemplate>
<ListViewCommandButton Command="Add"><i class="fas fa-user-plus"></i></ListViewCommandButton>
</HeaderTemplate>
<Template>
<h4>@context.Name</h4>
@if (context.Enabled)
{
<h5 class="k-text-success">Enabled</h5>
} else {
<h5 class="k-text-error">Disabled</h5>
}
<ListViewCommandButton Command="Delete" Class="mb-sm">Delete</ListViewCommandButton>
</Template>
<EditTemplate>
</EditTemplate>
</TelerikListView>

@code {
[ Parameter ] public string Mailbox { get; set; }="";

[ CascadingParameter ] private Task<AuthenticationState> authenticationStateTask { get; set; }

MailboxOwnerDto _owners { get; set; }=new MailboxOwnerDto(); string _error { get; set; }
List<OwnerWithStatus> _ownersWithStatus { get; set; } protected override async Task OnInitializedAsync ( ) {
_owners=await _adService.GetMailboxOwners(Mailbox); try { var authState=await authenticationStateTask; var user=authState.User; if ( string.IsNullOrEmpty(_owners.Owners)) return; else { var ownerList=_owners.Owners.Split( ',' ).ToList(); var oun=user.Identity.Name.Split( '\\' )[ 1 ]; foreach ( var owner in ownerList)
{ var ownerEnabled=( await _service.GetIdentity(owner)).Active; var ownerwithstatus=new OwnerWithStatus();
ownerwithstatus.Enabled=ownerEnabled;
ownerwithstatus.Name=owner;
_ownersWithStatus.Add(ownerwithstatus);
}
}
}
catch
{
_error="Error determining if this user is an owner.";
}
} public class OwnerWithStatus { public string Name { get; set; } public bool Enabled { get; set; }
}
}

### Response

**David** commented on 07 Feb 2022

I've determined that if I initialize my list with a collection of test items they do show up. So it seems like the Listview component isn't refreshing when items are added to its bound data source. Do I need to use a different collection type other than list?

## Answer

**David** answered on 07 Feb 2022

If I used ObservableCollection instead of List it works.
