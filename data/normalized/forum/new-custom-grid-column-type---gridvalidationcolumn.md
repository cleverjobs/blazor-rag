# New custom grid column type - GridValidationColumn

## Question

**Vas** asked on 28 Mar 2021

Is it possible to create a custom column type (eg GridValidationColumn) for TelerikGrid? I found the following example to validate a TelerikGrid cell (EditMode=GridEditMode.Incell). [https://feedback.telerik.com/blazor/1447439-is-there-a-way-to-implement-custom-validation-in-a-blazor-telerik-grid-when-pressing-save-update-command-](https://feedback.telerik.com/blazor/1447439-is-there-a-way-to-implement-custom-validation-in-a-blazor-telerik-grid-when-pressing-save-update-command-) button-if-not-is-there-plans-on-providing-custom-validation-as-a-feature-in-the-near-future Starting from this example, in order not to repeat the validation code for each column, GridValidationColumn will need to have a default EditorTemplate that contains all the logic in the example. With the option to customize only the cell editor.

## Answer

**Marin Bratanov** answered on 29 Mar 2021

Hi Vasile, With this enhancement, the grid will support data annotation validation in the InCell and Inline edit modes, just like it does for the Popup mode. The feature will be live in our next 2.23.0 release that should be live within a week. So, I'd encourage you to wait for the 2.23.0 release a little and try it out. For more detailed customizations, you would still use the editor template, the added benefit is that now you would have an EditContext as a cascading parameter. Regards, Marin Bratanov Progress Telerik

### Response

**Vasile** answered on 29 Mar 2021

Hi Marin, You give me great news. Vasile Lacatus Advanced Software Solutions

### Response

**Vasile** answered on 01 Apr 2021

Grid Incell edit validation also works with FluentValidation. Vasile Lacatus Advanced Software Solutions

### Response

**Vasile** answered on 01 Apr 2021

Sorry, it was a mistake on my part in the previous post. It does not work with Fluent Validation.

### Response

**Marin Bratanov** answered on 01 Apr 2021

Hello, I am afraid that such a built-in integration is not possible because it would mean us bringing in a third party dependency to all our customers. You can, however, build a custom edit form (examples here and here ) that can integrate with any validator you want. For example, our Form component can take any validator that is compatible with the standard EditContext. Regards, Marin Bratanov Progress Telerik
