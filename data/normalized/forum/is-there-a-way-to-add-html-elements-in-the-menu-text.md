# Is there a way to add html elements in the menu text?

## Question

**SLSL** asked on 31 Mar 2020

I was hoping to put some icons in the Text section of the menu component. On regular nav link I can do this. <NavLink class="dropdown-item" href="settings/accountcategories"> <span class="oi oi-command" aria-hidden="true"></span> Account Categories </NavLink> Thanks.

## Answer

**Marin Bratanov** answered on 31 Mar 2020

Hi, You can, through templates: [https://docs.telerik.com/blazor-ui/components/menu/templates.](https://docs.telerik.com/blazor-ui/components/menu/templates.) By default, theitems have only text that is a string, so it can't render anything but text (it is not a MarkupString). We also offer a collection of icons you can use: [https://docs.telerik.com/blazor-ui/common-features/font-icons](https://docs.telerik.com/blazor-ui/common-features/font-icons) If you would expect built-in functionality, how would you imagine it to be exposed? Perhaps the same Icon/IconClass/IconUrl parameters on the menu item that render internally the TelerikIcon at the beginning of the text? Regards, Marin Bratanov

### Response

**SL** answered on 31 Mar 2020

Hi Marin, Thanks for pointing out the template. I was able to use the Open Iconic classes by adding an IconHtmlClass on each of the MenuItem: <TelerikMenu Data="@MenuItems"> <ItemTemplate Context="item"> @{ <NavLink href="@item.Url" target="@(IsInternalPage(item.Url) ? "" : "_blank")" class="k-nav k-link k-menu-link" ActiveClass="k-state-active" Match="@(item.Url=="/" ? NavLinkMatch.All : NavLinkMatch.Prefix)"> <span class="@item.IconHtmlClass" style="padding-right:.5em;font-weight:bold" aria-hidden="true"></span>@item.Text </NavLink> } </ItemTemplate> </TelerikMenu>
