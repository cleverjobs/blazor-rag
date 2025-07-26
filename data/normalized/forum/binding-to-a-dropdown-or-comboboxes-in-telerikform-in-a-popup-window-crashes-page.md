# Binding to a DropDown or Comboboxes in TelerikForm in a Popup Window Crashes Page

## Question

**Zac** asked on 05 Jul 2023

I've got an app where the user selects an issue from a grid and it pops up a window where they can edit the issue in a form. When I attempt this, the page freezes/crashes. Here is a reproduction of the issue. [https://blazorrepl.telerik.com/mHOLaTlG32jhfT7v19](https://blazorrepl.telerik.com/mHOLaTlG32jhfT7v19) If you comment out the form and uncomment the fields below it you'll see it works outside of the TelerikForm. It also works inside an EditForm. It appears to be stuck in an infinite loop. What's causing this? Is there no workaround besides using an EditForm?

## Answer

**Hristian Stefanov** answered on 06 Jul 2023

Hi Zachary, Thank you for providing such comprehensive information about the scenario and sharing a runnable reproduction. After careful analysis, I confirm that the frozen page issue is a result of the Form utilizing both the "Model" and "EditContext" simultaneously. It is important to note that the Form can operate with either the "Model" or the "EditContext" as they are alternative approaches. To address the current issue, I recommend removing either the "Model" or the "EditContext" from your implementation. I have made the necessary change in the provided sample, and it now appears to be functioning as expected. To access the updated sample, follow this REPL link. Please run and test it to verify if the result you get is the same. I remain at your disposal if you encounter any difficulties during the testing phase. Regards, Hristian Stefanov
