# Checkbox unchecks itself right after I check it

## Question

**Dav** asked on 22 Jan 2021

I am having an issue with my checkboxes unchecking as soon as I check them. Here is my model: class AppRegistration { public DateTime DateCreated { get; set; } public List<RoleRequest> RolesRequested { get; set; } public string Approver { get; set; } public string Status { get; set; } public string Description { get; set; } public int Id { get; set; } } enum Role { MFAAdmin, ListServerAdmin, SecretServerAdmin, IdentityAdmin } class RoleRequest { public Role Role { get; set; } public bool Requested { get; set; } } Here is my markup: <div class="col"> @{ _newAppReg=new AppRegistration(); _newAppReg.RolesRequested=new List<RoleRequest>(); foreach (var role in Enum.GetValues( typeof (Role))) { _newAppReg.RolesRequested.Add( new RoleRequest { Role=(Role)role }); } foreach (var r in _newAppReg.RolesRequested) { <div class="mt-sm"> <TelerikCheckBox @bind-Value="@r.Requested" Enabled="@true" Id="@r.Role.ToString()"> </TelerikCheckBox> <label for="@r.Role.ToString()">@r.Role.ToString()</label> </div> } } </div>

## Answer

**Marin Bratanov** answered on 23 Jan 2021

Hi David, In a simplistic case, this seems to work for me (I am attaching a short video) and I expect that the problem in your situation stems from the re-rendering of the parent component which causes the model instance to get new-ed up again, which probably resets the data (I added a Console.Writeline() to illustrate where I think this happens): @page "/" @{
_newAppReg=new AppRegistration();

Console.WriteLine( "model created anew, data can reset" );

_newAppReg.RolesRequested=new List<RoleRequest>(); foreach ( var role in Enum.GetValues( typeof (Role)))
{
_newAppReg.RolesRequested.Add( new RoleRequest
{
Role=(Role)role
});
} foreach (RoleRequest r in _newAppReg.RolesRequested)
{
<div class="mt-sm">
<TelerikCheckBox @bind-Value="@r.Requested" Enabled="@true" Id="@r.Role.ToString()">
</TelerikCheckBox>
<label for="@r.Role.ToString()">@r.Role.ToString()</label>
</div>
}
}

@code{
AppRegistration _newAppReg { get; set; } public class AppRegistration { public DateTime DateCreated { get; set; } public List<RoleRequest> RolesRequested { get; set; } public string Approver { get; set; } public string Status { get; set; } public string Description { get; set; } public int Id { get; set; }
} public enum Role
{
MFAAdmin,
ListServerAdmin,
SecretServerAdmin,
IdentityAdmin
} public class RoleRequest { public Role Role { get; set; } public bool Requested { get; set; }
}
} Thus, I'd suggest you consider preparing the data outside of the markup - in the component code. The OnInitialized is usually a good spot for such preparations on the view-model. Depending on your use case, perhaps the OnParametersSet or OnParametersSetAsync may be more suitable if you need to respond to changes to parameters coming from above. Here's an example with initializing the model only once instead of on every re-render (video attached): @foreach (RoleRequest r in _newAppReg.RolesRequested)
{
<div class="mt-sm">
<TelerikCheckBox @bind-Value="@r.Requested" Enabled="@true" Id="@r.Role.ToString()">
</TelerikCheckBox>
<label for="@r.Role.ToString()">@r.Role.ToString()</label>
</div>
}

@code{
AppRegistration _newAppReg { get; set; } protected override void OnInitialized () {
_newAppReg=new AppRegistration();

Console.WriteLine( "model created anew, data can reset" );

_newAppReg.RolesRequested=new List<RoleRequest>(); foreach ( var role in Enum.GetValues( typeof (Role)))
{
_newAppReg.RolesRequested.Add( new RoleRequest
{
Role=(Role)role
});
} base.OnInitialized();
} public class AppRegistration { public DateTime DateCreated { get; set; } public List<RoleRequest> RolesRequested { get; set; } public string Approver { get; set; } public string Status { get; set; } public string Description { get; set; } public int Id { get; set; }
} public enum Role
{
MFAAdmin,
ListServerAdmin,
SecretServerAdmin,
IdentityAdmin
} public class RoleRequest { public Role Role { get; set; } public bool Requested { get; set; }
}
} If the ideas and information above do not help you move forward, please modify my snippets to showcase the problem so I can have a look. If it needs something else, perhaps opening a support ticket where you could attach a project with the few extra bits would be easier (I only ask you keep it runnable - free of business logic, databases, layouts and complexity that are not related to the Telerik issue - this would let us run, debug and review it). Regards, Marin Bratanov

### Response

**David** answered on 26 Jan 2021

That was it. Thank you so much for such a detailed reply.
