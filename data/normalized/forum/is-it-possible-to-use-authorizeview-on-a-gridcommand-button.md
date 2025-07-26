# Is it possible to use AuthorizeView on a GridCommand Button

## Question

**Fab** asked on 14 Feb 2022

I'm currently trying to use AuthorizeView to inherit the Policy restrictions to programmatically show/hide the GridCommandButton Something like this: <AuthorizeView Policy="@Policies.ManageAllUsersPolicy"> <Authorized> <GridCommandColumn Width="190px"> <GridCommandButton Command="Edit" Icon="edit"> Edit </GridCommandButton> </GridCommandColumn> </Authorized> </AuthorizeView> But I get an Error: Severity Error Code RZ9999 Description The child content element 'ChildContent' of component 'GridCommandColumn'
uses the same parameter name ('context') as enclosing child content element
'Authorized' of component 'AuthorizeView'. Specify the parameter name like:
'<ChildContent Context="another_name"> to resolve the
ambiguity I'm fairly new to the Kendo UI so I simply tried to name the Context directly on the AuthorizeView/Authorized component and GridCommandColumn (there's no Context property on GridCommanButton) But without success. Is it possible to use AUthorizeView, or should I move toward a solution where I manually check to the fulfillment of the policy and use a boolean to show/hide the button?

### Response

**Fabrizio** commented on 14 Feb 2022

My Bad! I had another grid with the same configuration in another component that was still giving the error Adding Context on AuthorizeView/Authorized component and GridCommandColumn works.
