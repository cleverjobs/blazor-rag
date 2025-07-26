# Text and CopyNPaste functionality issue

## Question

**Dea** asked on 20 Oct 2022

I have a text box user can type or paste a value into. A hidden button should appear once a value is in the box. The thing that's happening is after the value is pasted in, no button. user has to press a button in the textbox for the button to appear. Now the really strange thing is I put the pages code in your [https://blazorrepl.telerik.com/](https://blazorrepl.telerik.com/) tool and it appears to work. Just not in my main project or a test project using just the sample project app code that gets made when you create a blazor server project. I have include the code I have stuck in your tool, in the txt file, and my sample project in the zip file. The page in the project is: CopyNPasteTest. Would love to know whats going on. Thanks. Deasun.

## Answer

**Nadezhda Tacheva** answered on 25 Oct 2022

Hi Deasun, Thank you for sharing a runnable sample! I was able to successfully build the application. However, it does not reproduce the described issue on my end. The search button is accordingly shown when typing in the TextBox. Here is the result I am getting: [https://www.screencast.com/t/gA2jQRGycaB.](https://www.screencast.com/t/gA2jQRGycaB.) Having this in mind, I would say that the application and component configuration seem to be correct and deliver the desired result. So, the issue on your side is most likely caused by another reason. Please let me know if I am missing something or if there are any other specific steps to reproduce the issue you are facing. Other than that, I would recommend checking the browser console if any possible errors are thrown. If so, please send us the exact error, so we can provide some more insights on the matter. Side note: instead of wrapping the TextBox in a div and handling its @onkeypress and @onkeydown, you may simply handle the ValueChanged event of the TextBox to show the button. Regards, Nadezhda Tacheva Progress Telerik
