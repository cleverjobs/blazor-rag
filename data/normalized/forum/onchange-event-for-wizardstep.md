# Onchange event for wizardstep

## Question

**Chr** asked on 10 Sep 2021

Hello, is there a way to trigger the OnChange event within the wizard step only for the next action and not for the previous action. Currently I'm using the Wizard and wizard step to allow users to input data into a Telerik grid component. Since there is currently no validation for the grid I'm having to use my own validation which simple checks to see if there is at least 1 record in the grid before allowing the user to move on. However, since the OnChange event fires for both (next and previous) this makes the page not so user friendly. I would like to allow my validation to still work but only if the user wants to go to the next step in the Wizard but ignore my validation if they wish to go back. Below I have attached a code snippet of my OnChange parameter along with my validation.

## Answer

**Dimo** answered on 13 Sep 2021

Hi Christopher, The OnChange event fires before the Wizard step has changed, so there is an easy way to check if the user has navigated backwards. In the OnChange event handler, compare args.TargetIndex to the current Wizard Value. Regards, Dimo Progress Telerik

### Response

**Christopher** commented on 13 Sep 2021

Thanks I was able to get it working using target Index.
