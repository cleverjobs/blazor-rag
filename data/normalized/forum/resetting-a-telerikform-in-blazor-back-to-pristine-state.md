# Resetting A TelerikForm in Blazor back to Pristine State

## Question

**bil** asked on 15 Nov 2021

I have a need to reset the form and it's validation back to a pristine state (blank form with validation) either when the form is complete and successful response is returned or by user initiated click event. I don't see anywhere in the documentation to do so. I have set it equal to a new instance of the FormModel, and that indeed clears the form, BUT it does not reset the form validation or any of those behaviors. How can I reinitialize the form the same way that the form initializes on route activation?

## Answer

**Marin Bratanov** answered on 16 Nov 2021

Hello Billy, Creating a new EditContext should clear the validation message store as well. You can find an example of this in our documentation: [https://docs.telerik.com/blazor-ui/components/form/formitems/buttons#how-to-add-a-reset-clear-button-to-the-form.](https://docs.telerik.com/blazor-ui/components/form/formitems/buttons#how-to-add-a-reset-clear-button-to-the-form.) Regards, Marin Bratanov Progress Telerik
