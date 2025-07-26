# Is there a way to programmatically trigger form validation on a grid pop-up edit form?

## Question

**Joh** asked on 25 Jun 2024

I have a need to trigger the form validation process when certain actions are performed on the Grid popup add/edit form. What would be the best way to trigger the validation from code? private async Task GetNameHandler () { var companyName=await AgentServices.GetAgentCompName(editedAgent.AgentNumber); if (! string.IsNullOrEmpty(companyName))
{
editedAgent.Name=await myServices.GetCompanyName(editedAgent.AgentNumber);
} else {
editedAgent.Name=null; // Trigger form validation here }
} Submitting the form triggers the validation I want but I would like to make it trigger on a field OnBlur event that calls GetNameHandler()

### Response

**Hristian Stefanov** commented on 28 Jun 2024

Hi John, I confirm that the built-in validation in the Grid is designed to activate with each change to the currently focused input. For reference, you can see the example in our popup editing documentation. If you clear the "Name" input; a validation message will appear immediately, which is before you click outside the input. As a next step, could you provide more details about your goal? This will help me better understand your scenario and use case. Kind Regards, Hristian
