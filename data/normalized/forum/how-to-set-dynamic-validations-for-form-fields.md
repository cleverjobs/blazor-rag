# How to set dynamic validations for Form fields ?

## Question

**Shu** asked on 04 Apr 2022

I am working on flow, where based on users selection in dropdown, I want to update the validations of TextBox field. Is there any way to do that ? Becz at start we are creating model and specifying all specific validations, but now how we can apply validations based on users selection.

## Answer

**Dimo** answered on 06 Apr 2022

Hi Shubham, It looks like you need custom conditional validation. We support any validator that is compatible with the Blazor EditForm and EditContext. You can either use a third-party validator that allows conditional validation or otherwise, implement your own. The GitHub project above demonstrates remote server validation, but you can change the implementation and perform custom validation in the Form's OnSubmit event. You can also use FormItem Templates for some special fields. Subscribe to the change handlers of the editors to execute custom logic, show notifications, etc. Finally, a simple Google search reveals an interesting alternative - implement your own conditional DataAnnotation attribute. To see an inline error message next to the field editor, you need to use the ValidationResult overload that passes a field name. In this way the form validator will know which field has failed validation. return new ValidationResult( this.FormatErrorMessage(validationContext.DisplayName), new List<string> { validationContext.MemberName }); Regards, Dimo Progress Telerik
