# validation for dynamically rendered components

## Question

**Ste** asked on 14 Jan 2022

Hello

I have a question related to Validation. In our application we use forms that are dynamically rendered (without using a model). Therefor we are not able to use the TelerikFrom and its edit context.
I was wondering if it is possible to do Validation on a single Property/field and show a validation message (with the Validation built by Telerik)?
As far as I can see, you seem to only support validation for components wrapped in the TelerikForm/EditForm.

Thanks in advance

## Answer

**Marin Bratanov** answered on 15 Jan 2022

Hi Stefan, The Validation tools offered by Telerik step on the framework and typically require a model field, just like the built-in ValidationMessage. We don't implement the actual validation, however, we use the EditContext that comes with the EditForm. The TelerikForm component also does that, but simplifies the generation of forms based on the model. For heavy customizations, the standard components are to be preferred as that's not the goal of the Telerik Form component - its goal is to simplify the common case. Anyway, if you have an EditForm that can validate as expected you can point the validation message or tooltip component to the desired field. If that scenario works with the standard ValidationMessage, I see no reason at this point why it would not work with the Telerik validation message, tooltip or summary. As for enforcing validation - the .Validate() method should let you call that on demand, but that also comes from the framework, not from Telerik. Regards, Marin Bratanov
