# Duplicate verification messages when switching between tabs

## Question

**Iva** asked on 23 Oct 2020

Hello! I have a tabstrip with many tabs. One of tabs contains validator like <ValidationMessage For="@(()=> crmView.Name)" /> If I switch between tabs, and return to the tab with validation, duplicate validation messages occur when switching between tabs. How to prevent that?

## Answer

**Marin Bratanov** answered on 23 Oct 2020

Hi Ivan, We don't control the validation message store, the edit forms and edit contexts control it, so you may need to Clear() it yourself. Perhaps this thread can help you get started with that [https://stackoverflow.com/questions/60917323/how-to-reset-custom-validation-errors-when-using-editform-in-blazor-razor-page,](https://stackoverflow.com/questions/60917323/how-to-reset-custom-validation-errors-when-using-editform-in-blazor-razor-page,) or this one [https://blazor-university.com/forms/writing-custom-validation/.](https://blazor-university.com/forms/writing-custom-validation/.) Or, maybe if the validation context is stored outside of the tab strip perhaps it should not be, or you could re-create it in the SelectedIndexChanged event. Regards, Marin Bratanov

### Response

**Ivan** answered on 23 Oct 2020

Thank you! The simplest way is create new editcontext in ActiveTabIndexChanged event
