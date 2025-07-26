# Only one filter option in FilterMenu in Grid

## Question

**WimWim** asked on 27 Jan 2022

Hello We have only one filter option in our Grid in a FilterMenu. The previous css is not working anymore after the update to version 3.0.0.. k - filter - menu - container. k - dropdown,. k - filter - menu - container. k - state - empty: nth - of - type ( 2n ),. k - filter - menu - container. k - textbox: nth - of - type ( 2n ),. k - filter - menu - container. k - datepicker: nth - of - type ( 2n + 1 ),. k - filter - menu - container. k - numerictextbox: nth - of - type ( 2n ) { display: none; }. k - filter - menu - container. k - dropdown: first - of - type { display: block; } We have changed it to:.k-filter-menu-container .k-dropdownlist, .k-filter-menu-container .k-state-empty:nth-of-type(2n), .k-filter-menu-container .k-textbox:nth-of-type(2n), .k-filter-menu-container .k-datepicker:nth-of-type(2n+1), .k-filter-menu-container .k-numerictextbox:nth-of-type(2n) { display: none; } .k-filter-menu-container .k-dropdownlist:first-of-type { display: inline-flex; } But that shows the wrong dropdownlist. How can we fix that?

## Answer

**Dimo** answered on 31 Jan 2022

Hello Wim, UI for Blazor 3.0 uses consistent HTML rendering for all input components. Before, some components used <div>s and some used <span>s. Now all use <span>s. This requires changes in the CSS rule, because the tag indexing is no longer the same. Actually, the nth-of-type selector can be tricky to apply and troubleshoot, because it works with elements, not CSS classes. That's why it will be easier to use the:nth-child selector instead. This will make the custom CSS code a lot simpler too: /* UI for Blazor 3.0+ */.k-filter-menu-container> span:nth-child(n+3) { display: none;
} /* UI for Blazor 2.30- */.k-filter-menu-container> div>:nth-child(n+3) { display: none;
} I just updated the live KB article: Remove the secondary filter options in the Grid FilterMenu Regards, Dimo

### Response

**Wim** commented on 31 Jan 2022

Thank you Dimo, that works perfect.
