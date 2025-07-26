# How can I add a placeholder on the Blazor TextBox?

## Question

**SLSL** asked on 07 Jan 2020

You can do this with the standard input element: <input type="text" class="form-control" id="counterAccountCode" placeholder="999-999-999-999-999-999, NONE if not applicable" bind="@Item.CounterAccountCode" /> Is there a way to do this with the Blazor TextBox or is this something that is still in the works? Thanks.

## Answer

**Marin Bratanov** answered on 08 Jan 2020

Hi, The Label parameter does this, you can see it in action in the demos: [https://demos.telerik.com/blazor-ui/textbox/overview.](https://demos.telerik.com/blazor-ui/textbox/overview.) Regards, Marin Bratanov

### Response

**SL** answered on 08 Jan 2020

Thank you Marin.

### Response

**Hao** answered on 11 Nov 2022

hi Marin Bratanov, Can we have placeholder template like this? I may need to customize search box from Textbox because the buit-in search box in the Grid does not have click, how to get search text... If possible, please give me some advices. Thanks

### Response

**Dimo** commented on 15 Nov 2022

Hao, see the KB article Add icon to textbox.
