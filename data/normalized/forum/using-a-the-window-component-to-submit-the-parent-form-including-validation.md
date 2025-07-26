# Using a the Window component to submit the parent form including validation.

## Question

**Jst** asked on 24 Jun 2021

I have a form that I would like to use the Window component on to gather additional information before submitting the parent form. Is there a way to trigger submit of the parent form and the associated Validations from the Window component? Or is there a different component that should be used?

## Answer

**Marin Bratanov** answered on 26 Jun 2021

Hi, If you have an EditContext object for the form and you pass it to the window cotnents, you will be able to use its .Validate() method as required by your logic. That said, I recommend you take a look at the following three articles that explain similar situations and common issues with similar setups that you may want to keep in mind: [https://docs.telerik.com/blazor-ui/knowledge-base/window-does-not-update-parent](https://docs.telerik.com/blazor-ui/knowledge-base/window-does-not-update-parent) [https://docs.telerik.com/blazor-ui/knowledge-base/window-cascading-parameter-null](https://docs.telerik.com/blazor-ui/knowledge-base/window-cascading-parameter-null) [https://docs.telerik.com/blazor-ui/knowledge-base/window-in-form-edit-context](https://docs.telerik.com/blazor-ui/knowledge-base/window-in-form-edit-context) Regards, Marin Bratanov
