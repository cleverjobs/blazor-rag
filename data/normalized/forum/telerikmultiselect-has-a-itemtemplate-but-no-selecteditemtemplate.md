# TelerikMultiSelect has a <ItemTemplate> but no <SelectedItemTemplate>

## Question

**Rol** asked on 12 Jan 2022

I can give the items in the dropdown a color, but once these items are selected i have no influence over the formatting. The selected items are always a <span> item name </span> even if the corresponding item in the dropdown has its own style with a red color. Is there a workaround so I can format selected items as well?

## Answer

**Marin Bratanov** answered on 15 Jan 2022

Hello Roland, The ItemTemplate is applied for selected items too - the styling comes from an element higher in the DOM where we add the k-state-selected class which alters CSS styling. Thus, you can use it to add your own cascade with heavier selectors to get the desired appearance. You may also find useful the PopupClass of the component to make this specific for concrete component instances, not all dropdowns. Regards, Marin Bratanov

### Response

**Roland** commented on 15 Jan 2022

I don't follow. With <ItemTemplate> i can give one particular item a style or give it class that i can use to style the item. Neither this style nor this class is visible in the .k-multiselect .k-multiselect-wrap .k-reset li.k-button span hierarchy. Even if i give all items the same style or class, this is not reflected in the selected items.

### Response

**Marin Bratanov** commented on 15 Jan 2022

My answer was referring to the item template and how items render in the dropdown. I am getting the feeling that you want to customize the tags in the input, for that - Follow this request: [https://feedback.telerik.com/blazor/1528556-tagtemplate-for-multi-select.](https://feedback.telerik.com/blazor/1528556-tagtemplate-for-multi-select.) You can still use CSS to change some basics there but the HTML rendering cannot yet be changed like you can change the items in the dropdown through the ItemTemplate.

### Response

**Roland** commented on 15 Jan 2022

I solved my problem with a lot of JavaScript, but a <TagTemplate> would indeed make life a lot simpler
