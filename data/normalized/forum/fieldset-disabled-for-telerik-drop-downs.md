# fieldset disabled for Telerik drop downs

## Question

**Dou** asked on 07 Nov 2024

I have a requirement to conditionally disable all controls in a TelerikForm. There a multiple ways to do that but what seems like the easiest to me is to wrap the form as such: <fieldset disabled> <TelerikForm>... </fieldset> I have buttons, text boxes, date pickers and drop down lists in my form. All of the controls get disabled except for the drop downs. Is there a simple way to do this so the drop downs will get included? I know I could do this through javascript or whatever but it just struck me as weird that most of the Telerik controls are disabled except for the drop downs. Thanks.

## Answer

**Nansi** answered on 12 Nov 2024

Hi Doug, I confirm that the whole Form doesn't expose a parameter that is related to disabling all fields. The approach that you have chosen is one of the possible ways. Indeed, with this approach the DropDownList does not respond to the disabled attribute on a fieldset by default. As a solution, you can explicitly set the FormItem Enabled parameter for the item, where you have included a DropDownList. Regards, Nansi Progress Telerik
