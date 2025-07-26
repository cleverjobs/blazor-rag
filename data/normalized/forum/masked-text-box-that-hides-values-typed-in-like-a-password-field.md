# Masked text box that hides values typed in like a password field?

## Question

**Dav** asked on 26 May 2021

I love the Masked TextBox control. We are using it for a a social security field with a mask of xxx-xx-xxxx. But we also need to have the value shown as ***-**-**** so that ssns are not reveled. Is this possible? I know we can use the standard TextBox and set it to password which hides the input, but we need to mask it somehow to be an ssn. Any Ideas on this?

## Answer

**Dimo** answered on 27 May 2021

Hi David, Generally, a textbox value can be "hidden" with asterisks if there is another <input /> element or a variable that will hold the actual value. Our masked textbox component renders only one textbox and works with the actual value only. This means that the desired behavior requires custom coding. For example, you can experiment with two separate textboxes, toggle their visibility with CSS and switch focus programmatically. For the programmatic focusing of the MaskedTextBox, you will need to use JavaScript, as shown at: [https://feedback.telerik.com/blazor/1497943-add-a-focus-method-for-all-applicable-component-references](https://feedback.telerik.com/blazor/1497943-add-a-focus-method-for-all-applicable-component-references) Regards, Dimo Progress Telerik
