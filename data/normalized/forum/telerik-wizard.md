# Telerik Wizard

## Question

**Nid** asked on 23 Aug 2023

hi, I've been working on creating a form using the Telerik Wizard component, allowing users to fill out information across different steps. I've been using the same model for binding data in several WizardSteps. I referred to the example here: [https://demos.telerik.com/blazor-ui/wizard/overview.](https://demos.telerik.com/blazor-ui/wizard/overview.) However, I've removed the confirmation page since it's not necessary for my use case. In the model, I have a few required fields, but I don't want to prevent users from moving to the next page if the current page's input is invalid. Instead, I'd like to collect all the validation messages and display them in their entirety on the last step. To achieve this, I placed a <TelerikValidationSummary> component in the last step of the wizard. However, it seems that the validation messages aren't being displayed. I've attached a screenshot of my Razor page for your reference. It's a blazor webassembly app. If anyone could provide insights or guidance on how to make the validation summary work properly, I'd greatly appreciate it! Thanks in advance for your help!

### Response

**Hristian Stefanov** commented on 28 Aug 2023

Hi Nidhi, I am actively researching potential approaches that will fulfill your requirements. Rest assured that I will provide you with an update shortly once I have obtained any relevant results. Your patience is highly valued. Kind Regards, Hristian

### Response

**Hristian Stefanov** commented on 30 Aug 2023

Hi Nidhi, I'd like to once again express my gratitude for your patience throughout this process. Now I'm able to share more details as I managed to craft an example for you. Let me shed some light on the approach I've employed. Each step of the wizard corresponds to a distinct Form. Consequently, in order to aggregate and display all validation messages from these Form components during the final step, a manual process of collecting validation messages from each page via separate EditContext instances becomes needed. I'm sharing the sample that shows this concept via this REPL link. Please run and test it to see whether it meets your requirements. If needed, feel free to adjust the custom logic inside the OnChange handlers based on your business needs. Kind Regards, Hristian

### Response

**Nidhi** commented on 05 Sep 2023

Hi Hristian, Your assistance was greatly appreciated; thank you! I've attached an image representing the final step in the wizard. As previously mentioned, the goal is for the user to see a validation summary message when all the checkboxes are checked. I attempted to implement this scenario using the OnChange/OnFinish events of the wizard. Is it feasible to achieve this functionality with the Telerik wizard? Thank you

### Response

**Nidhi** commented on 06 Sep 2023

I could make it. Thanks

### Response

**Hristian Stefanov** commented on 07 Sep 2023

Hi Nidhi, Thank you for sharing an update on the outcome. I'm glad to see that you've found a suitable approach for your specific scenario. Kind Regards, Hristian
