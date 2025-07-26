# Validation in Grid pop-up

## Question

**Mar** asked on 15 Apr 2021

First a salute to the Telerik team. The Grid is awesome, thanks for making me look like a rock star. I am using the build in Blazor FileUpload component, not Telerik and would like to show validations errors in the pop-up form for not supported file types. How can I show errors in a component like the Validation Summary?

## Answer

**Martin** answered on 15 Apr 2021

Unable to edit my post, so I add some more content here. Is there a way to add content to the Validation Summary control? Can I access it in code?

### Response

**Marin Bratanov** answered on 16 Apr 2021

Thank you, Martin! I'm happy to see our components put to good use! On the file validation - this post will send you down a rabbit hole because you will have to delve deep into the way validation works in Blazor. Since there is none built-in validation for files in the framework, one has to roll out their own, and that's not super easy. You can start from the following sample to see one way you could implement validation for files: [https://github.com/telerik/blazor-ui/tree/master/upload/form-validation](https://github.com/telerik/blazor-ui/tree/master/upload/form-validation) If you can't put all the necessary code in an editor template, I would suggest you create a custom edit form: [https://github.com/telerik/blazor-ui/tree/master/grid/custom-popup-form](https://github.com/telerik/blazor-ui/tree/master/grid/custom-popup-form) Programmatic access to components isn't really a thing in Blazor, at least for the purpose of modifying data, to affect the validation one usually goes through the edit context and its validation message store. You can read more about these things in the MSDN documentation, there is quite a lot to unpack: [https://docs.microsoft.com/en-us/aspnet/core/blazor/forms-validation?view=aspnetcore-5.0.](https://docs.microsoft.com/en-us/aspnet/core/blazor/forms-validation?view=aspnetcore-5.0.) Regards, Marin Bratanov
