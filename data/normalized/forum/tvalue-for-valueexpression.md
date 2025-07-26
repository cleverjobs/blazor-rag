# TValue for ValueExpression

## Question

**Rih** asked on 11 May 2020

Hello, I'm currently using a TextBox in one of my forms. The problem is that the "Value" of the text box is made from a combinaison of different variables, with "ToString()", I cannot bind it to a specific string value. The [Required] attribute is on a class, which does not contain a string value. The purpose would be to be able to link "ValueExpression" to any variable like you can do with the validation message " <ValidationMessage For="@AnyTypeRequiredValue"/>". Like this we will be able to have the field colored in red when the class is not filled and when it's not necesseraly a string. Hope you understood my problem. Have a nice day

## Answer

**Marin Bratanov** answered on 11 May 2020

Hello, The Blazor validation uses DataAnnotation attributes on the corresponding model fields - if the certain field does not have an attribute, it won't show error messages or block form submission. If you can't have an appropriate field, you should create a view model that does. For example, its getter can perform the necessary calculations, or you could perform them elsewhere in the view-model and set its value as desired. The TelerikTextbox requires a string field to bind to, like the standard <InputText /> - once you have the desired setup working with the InputText, it should work with the Telerik textbox. Regards, Marin Bratanov
