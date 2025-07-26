# Wizard form validate method only works when viewing the form

## Question

**JonJon** asked on 27 Mar 2024

We have a need to enable non-linear access to our wizard. However, at the final confirmation page, we need to validate the user has completed the forms. There appears to be a bug that we cannot check if each form is valid on the final page. I've put together an example that shows 3 pages. When clicking next, I'm calling validate on each form then displaying the boolean value from each form in a dialog box. You can see that when a form is not visible to the user, the validate method always returns true. Is there a workaround we can implement until this is fixed by Telerik? [https://blazorrepl.telerik.com/myEnGhbz35WxeVpM30](https://blazorrepl.telerik.com/myEnGhbz35WxeVpM30)

### Response

**alex** commented on 27 Nov 2024

This is disappointing this is the first thing the business asked for. The form loads data from a previous version of an item. They only want to change info on page 6 and then submit. This prevents this from being possible

## Answer

**Svetoslav Dimitrov** answered on 01 Apr 2024

Hello Jon, Let me briefly overview how the Wizard component works to segue into the specific question's answer. The Wizard renders content in Steps in sequential order. The idea of this component is to make the user perform separate steps one at a time. When the Next button is clicked the content of the previous step is removed from the DOM. This means that the content of the step is no longer reachable. Validating all of the steps in one go contradicts the UX and how the Wizard operates (the technical aspects) and I am sorry to report that we cannot implement this request. Regards, Svetoslav Dimitrov Progress Telerik

### Response

**Jon** answered on 01 Apr 2024

I understand Telerik designed the control to render content in steps in sequential order. However, Telerik provides a setting to allow users to non-linearly navigate the wizard. This provides the opportunity for the user to enter the Wizard on step 1, then skip ahead to the final step and attempt to complete the entire form with missing required data. We need a way to detect the user has not completed all steps of the Wizard. For now, we've put together a work around by validating each model we're binding to each form. Telerik should consider that its control does enable this user behavior, and its own validation results are misleading by returning true for steps that were never accessed.

### Response

**Svetoslav Dimitrov** commented on 04 Apr 2024

Hello Jon, If you have integrated a form in the Wizard step, if the Form is not valid the Wizard must not proceed to the next step. You can observe that from the Wizard Overview online demo, if you click the Next button without filling all fields, the wizard will not proceed to the next step.

### Response

**Jon** commented on 04 Apr 2024

If you check out the example I provided here, [https://blazorrepl.telerik.com/myEnGhbz35WxeVpM30,](https://blazorrepl.telerik.com/myEnGhbz35WxeVpM30,) you will see that you can click on the wizard steps without clicking the next button. This doesn't trigger validation on the form. When using the non-linear setting of the wizard, a user doesn't need to navigate to each step. In the example I provided, the user can skip from the Registration step to the Confirmation step, without ever entering the Shipping Address step. This is the behavior we're looking for, however the user shouldn't be able to click "Done" on the confirmation step due to not all steps being completed. Validation isn't happening for the Shipping Address step. I understand from your first response why it's doing this, however I believe this is a bug in the behavior. If Telerik is going to offer the ability to enable a non-linear wizard, the non-linear wizard should still be able to confirm all steps are valid before a user completes the entire wizard.

### Response

**Svetoslav Dimitrov** commented on 09 Apr 2024

Hello Jon, The OnChange event is cancellable. If a condition is not met you can cancel the event and the wizard step will not be changed. Here is a modified version of the snippe t so that the Step is not changed and the form validates as expected. I suggest that you take a look at the Form Integration demo and documentation to see how to validate only the correct form that is on the current step.
