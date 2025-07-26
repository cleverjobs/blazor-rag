# How to change order of events being called

## Question

**Fab** asked on 26 Mar 2025

Currently I am using a Telerikform which has a FormItem. This FormItem is a Dropdownlist using templates. The Form has an OnUpdate event I am listening to and the Dropdownlist has a ValueChanged event. If I select an Item in the Dropdownlist the OnUpdate of the Form get triggered befire the ValueChanged on the DropDownlist. Is this intended behaviour, if yes, how can I change the order?

## Answer

**Anislav** answered on 26 Mar 2025

Yes, this is the expected behavior, as documented on the following page: Telerik Form Events - OnUpdate: By default, OnUpdate will fire on each keystroke for auto-generated form items and FormItem templates. To change this behavior, define a FormItem Template and set ValidateOn to ValidationEvent.Change for the field editor component. In this case, OnUpdate will fire when the user blurs the field editor or hits Enter while the editor is focused. However, the ValidateOn property is only available for simple input components, meaning this approach is not applicable to the DropDownList. Regards, Anislav Atanasov
