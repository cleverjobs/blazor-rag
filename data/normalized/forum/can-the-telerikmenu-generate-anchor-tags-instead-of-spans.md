# Can the TelerikMenu generate anchor tags instead of spans?

## Question

**Jev** asked on 27 Jun 2025

As of right now, the TelerikMenu generates a menu where each menu item is a span with an onclick handler that navigates to the page. It looks like this: <li data-id="..." tabindex="0" class="k-item k-menu-item k-first" role="menuitem" aria-live="polite"> <span class="k-link k-menu-link "> <span class="k-menu-link-text"> Page Title </span> </span> </li> However, because they are only spans, when right clicking on a menu item, there is no option to open the link in a new tab. In addition, middle clicking the menu item doesn't work either. Can these be changed to anchor tags so menu items can be opened in a new tab? I know there is an ItemContext that can be added to the TelerikMenu, but I would like to keep all the styling of the default TelerikMenu.

## Answer

**Dimo** answered on 30 Jun 2025

Hello Jevon, Yes, the Menu itself always renders <span> elements and uses the standard framework NavigationManager to navigate. You can use the Menu ItemTemplate to render <NavLink>'s or <a>'s Regards, Dimo Progress Telerik
