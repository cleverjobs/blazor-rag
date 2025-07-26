# Breadcrumbs on the menu items

## Question

**SLSL** asked on 31 Mar 2020

Posting it here since it is related to the menu items. Is there a way to show bread crumbs on the menu items? Thanks.

## Answer

**Marin Bratanov** answered on 31 Mar 2020

Hello, How would you imagine a menu showing a breadcrumb, considering that the items have full links and it cannot be guaranteed that the parent item will point to the parent part of the URL segment? I am asking this because the way we've handled this elsewhere is by a dedicated component such as this one: [https://demos.telerik.com/kendo-ui/breadcrumb/index.](https://demos.telerik.com/kendo-ui/breadcrumb/index.) Would such a separate component be useful for you? Regards, Marin Bratanov

### Response

**SL** answered on 31 Mar 2020

Ah yes, the [https://demos.telerik.com/kendo-ui/breadcrumb/index](https://demos.telerik.com/kendo-ui/breadcrumb/index) would work. My requirement is to use the same menu items for the breadcrumb.

### Response

**Marin Bratanov** answered on 01 Apr 2020

Hello, I'm thinking that you want the navigation and bind-to-location features of the breadcrumb widget: [https://docs.telerik.com/kendo-ui/controls/navigation/breadcrumb/navigation.](https://docs.telerik.com/kendo-ui/controls/navigation/breadcrumb/navigation.) The menu items cannot be guaranteed to actually have appropriate URLs and segments to act as a breadcrumb. WIth the feature above, however, you would not even have to provide any items to the component, it would parse the URL, extract the "/" segments from it and generate items from them. It could even hook to the NavigationManager's LocationChanged event to re-parse the current URL after it changes (e.g., for cases when it is not part of the updated/navigated component, but part of the layout. If such a separate component would not work for your case, I would ask you to add some ideas on how would such a thing work in a menu component. Regards, Marin Bratanov

### Response

**SL** answered on 02 Apr 2020

Hi Marin, The kendo-ui style would work for me. Thanks.

### Response

**Marin Bratanov** answered on 02 Apr 2020

I made the following page in our
