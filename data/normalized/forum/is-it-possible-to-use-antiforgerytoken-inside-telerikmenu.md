# Is it possible to use AntiforgeryToken inside TelerikMenu?

## Question

**Mar** asked on 16 Jan 2024

Hi We have been using a form action to logout within our TelerikMenu: <TelerikMenu Data="@MenuItems"> <ItemTemplate Context="item"> @{
if (item.IsForm)
{ <form method="post" action="@item. Action"> <AntiforgeryToken /> <input type="hidden" name="ReturnUrl" value="/" /> <input type="submit" value="@item. Text" /> </form> }
else
{ <NavLink href="@item.Url"> <span> @item.Text </span> </NavLink> }
} </ItemTemplate> </TelerikMenu> But we are now struggling with the new `<AntiforgeryToken />`. It does not seem to be able to render itself. I don't know if it has anything to do with the way it constructs itself: private void RenderField ( RenderTreeBuilder builder ) {
builder.OpenElement( 0, "input" );
builder.AddAttribute( 1, "type", "hidden" );
builder.AddAttribute( 2, "name", _requestToken!.FormFieldName);
builder.AddAttribute( 3, "value", _requestToken.Value);
builder.CloseElement();
} We have managed to create a work around by basically copying the AntiforgeryToken logic into our own component i.e.: @inject AntiforgeryStateProvider antiforgeryStateProvider

<input type="hidden" name="@_requestToken!.FormFieldName" value="@_requestToken.Value" />

@code { private AntiforgeryRequestToken? _requestToken;

??? (){
_requestToken=antiforgeryStateProvider?.GetAntiforgeryToken();
}
} But this means that we would have to maintain that extra code and take on the responsibility of the security it provides. Is TelerikMenu the wrong component for this or is there any better way to get this working? Thanks, Mark

## Answer

**Dimo** answered on 19 Jan 2024

Hi Mark, Based on my testing, I think there is a race condition. It looks like the <AntiforgeryToken /> needs some time to be generated and the Menu popup renders too quickly. Once the popup is visible, it can't be updated. My suggestion is to render one more <AntiforgeryToken /> tag outside the Menu, so that the time-consuming process completes before the Menu popup shows. On a side note, I confirm that putting a <form> inside a Menu is not recommended, because leads to invalid HTML markup. The Menu items are wrapped in <span> which accepts inline elements as children. Regards, Dimo Progress Telerik

### Response

**Mark** commented on 19 Jan 2024

Thank you for your answer, Dimo. Would it be prudent for Telerik to add that that putting a <form> inside a Menu is not recommended to the documentation. Perhaps in the article detailing navigation with Menu? It's a bit disappointing that the menu can not be used this fashion. Especially when the official ASP.NET Blazor template projects redirect to logout using a form in this fashion. <div class="nav-item px-3"> <form action="Account/Logout" method="post"> <AntiforgeryToken /> <input type="hidden" name="ReturnUrl" value="@currentUrl" /> <button type="submit" class="nav-link"> <span class="bi bi-arrow-bar-left-nav-menu" aria-hidden="true"> </span> Logout </button> </form> </div> From your response, am I to understand that there is no alternative component that would be recommended for this behaviour & that we must instead implement, yet another, Telerik work-around. Thanks, Mark

### Response

**Dimo** commented on 19 Jan 2024

The coming release 5.1.0 will include Popup and PopOver components, which can be used in a similar way to the Menu - as animated dropdowns that appear on mouseover or click. They can accommodate any child content. We avoid documenting what *not* to do, unless we see that a lot of developers do it and it has negative side effects (neither is true in this case). By the way, the Account section in .NET 8 project templates is non-interactive, so it can't contain our components.

### Response

**Mark** commented on 19 Jan 2024

I thought documentation was supposed to be helpful. By the way, I did try to be clear but it seems I fell short. The official * Microsoft* ASP.NET Blazor template projects.
