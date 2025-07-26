# How can I add the 'x' Close icon to my Predefined Dialogs?

## Question

**Joh** asked on 01 Oct 2024

Hello there, I am using the Telerik Predefined Dialogs for several different uses, and I want to add the x Close icon in the upper right corner. I know it's redundant, but it's a project requirement and it also seems to be best practice for UI/UX. if (DisclosureReportSelections.ActivitySelection==-1)
{
await Dialogs.AlertAsync("Activity must be reported for this period.", "Report Information Required");
return false;
} I like the Predefined Dialogs because they provide 'await' for the user's response, which is handy and efficient in code. I do not want the hassle of customizing a standard Dialog while managing it's visible state. Attached image for reference.

## Answer

**Hristian Stefanov** answered on 02 Oct 2024

Hi John, Thank you for providing a detailed description along with a screenshot of what you're looking for. However, our predefined dialogs are designed to resemble standard browser alerts, which also lack the "x" button. You're also correct in noting that adding the "x" would be redundant, as it would perform the same action as the existing button. For this type of customization, we recommend using our standalone Dialog component, which includes a header tag where you can easily add such a button. Regards, Hristian Stefanov Progress Telerik
