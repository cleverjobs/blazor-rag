# FluentValidation and Custom Popup Edit & Other Questions

## Question

**Tim** asked on 28 Feb 2020

We are evaluation the blazor controls from telerik and would like to know few things. 1. Is it possible to implement fluent validation as part of the object validation as done here? [https://blog.stevensanderson.com/2019/09/04/blazor-fluentvalidation/](https://blog.stevensanderson.com/2019/09/04/blazor-fluentvalidation/) I tried doing this but it would not catch the validation <EditForm Model="@selectedBuildingModel" OnValidSubmit="@Save"> <FluentValidator TValidator="BuildingModelValidator" /> <div class="form-row"> <div class="col"> <TelerikTextBox @bind-Value="@selectedBuildingModel.Name" Label="First Name"></TelerikTextBox> <ValidationMessage For="@(()=> selectedBuildingModel.Name)" /> </div> </div> <div class="form-row"> <ValidationSummary /> <TelerikButton Icon="save" Primary="true" ButtonType="@ButtonType.Submit">Save</TelerikButton> <TelerikButton Icon="cancel" OnClick="@ClearSelection" ButtonType="@ButtonType.Button">Cancel</TelerikButton> </div> </EditForm> public class BuildingModelValidator : AbstractValidator<BuildingModel> { public BuildingModelValidator() { RuleFor(x=> x.Name).NotEmpty().MaximumLength(5); } } 2. When will the upload control be available (even if its insiders, we just wanna see how it works)? Thank you

## Answer

**Marin Bratanov** answered on 02 Mar 2020

Hi, We support and test only the standard data annotations validation as this is what comes with the framework. Generally, the fluent validation example should work, provided it is synchronous. We have one report that causes async validation to fail and to cater for that we will need to implement an event handler to update the UI. You can Follow the status of this task in this page (I have added your Vote for it to raise its priority): [https://feedback.telerik.com/blazor/1441550-async-validation-is-not-updating-after-a-delay](https://feedback.telerik.com/blazor/1441550-async-validation-is-not-updating-after-a-delay) On the upload component - we are working on it at this very moment and it is scheduled for our next release (2.9.0). You can Follow its status here: [https://feedback.telerik.com/blazor/1397642-upload-async.](https://feedback.telerik.com/blazor/1397642-upload-async.) Hopefully, i will be available around mid-March (the exact release date will depend somewhat on the next WASM Preview release). Regards, Marin Bratanov
